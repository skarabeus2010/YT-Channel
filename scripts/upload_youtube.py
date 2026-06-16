#!/usr/bin/env python3
"""
upload_youtube.py - Semi-automatischer YouTube-Upload (privat/terminiert).

Laedt ein Video als PRIVAT (oder terminiert via publishAt) hoch und setzt die
Metadaten aus einer JSON-Datei. Das KI-Disclosure-Label ("altered/synthetic
content") und das finale Veroeffentlichen erfolgen bewusst MANUELL in YouTube
Studio - das ist das Controller-Gate (Faktencheck + KI-Kennzeichnung).

Setup-Anleitung: ../workflow/upload-automation.md

Aufruf:
    python upload_youtube.py mein_video.mp4 --meta video_metadata.json --thumb thumb.png
"""

import argparse
import json
import os
import sys

import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Nur Upload-Scope - so wenig Rechte wie noetig.
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRET_FILE = os.environ.get("YT_CLIENT_SECRET", "client_secret.json")
TOKEN_FILE = os.environ.get("YT_TOKEN", "token.json")


def get_service():
    """OAuth-Token holen/erneuern (beim ersten Mal oeffnet sich der Browser)."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            if not os.path.exists(CLIENT_SECRET_FILE):
                sys.exit(
                    f"Fehlt: {CLIENT_SECRET_FILE}. Siehe workflow/upload-automation.md "
                    "(Google-Cloud-OAuth-Client herunterladen)."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w", encoding="utf-8") as fh:
            fh.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def upload(meta_path, video_path, thumb_path=None):
    if not os.path.exists(video_path):
        sys.exit(f"Videodatei nicht gefunden: {video_path}")
    with open(meta_path, encoding="utf-8") as fh:
        meta = json.load(fh)

    status = {
        "privacyStatus": meta.get("privacyStatus", "private"),
        "selfDeclaredMadeForKids": bool(meta.get("madeForKids", False)),
    }
    # Terminierte Veroeffentlichung: publishAt verlangt privacyStatus=private
    # und ISO-8601-UTC, z.B. "2026-07-01T09:00:00Z".
    if meta.get("publishAt"):
        status["privacyStatus"] = "private"
        status["publishAt"] = meta["publishAt"]

    body = {
        "snippet": {
            "title": meta["title"],
            "description": meta["description"],
            "tags": meta.get("tags", []),
            "categoryId": str(meta.get("categoryId", "27")),  # 27 = Education
            "defaultLanguage": meta.get("language", "en"),
            "defaultAudioLanguage": meta.get("language", "en"),
        },
        "status": status,
    }

    yt = get_service()
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    request = yt.videos().insert(part="snippet,status", body=body, media_body=media)

    print(f"Upload laeuft: {video_path}")
    response = None
    while response is None:
        progress, response = request.next_chunk()
        if progress:
            print(f"  {int(progress.progress() * 100)} %")
    video_id = response["id"]
    print(f"OK  video_id={video_id}  (Status: {body['status']['privacyStatus']})")

    if thumb_path:
        # Custom-Thumbnail braucht einen verifizierten Kanal.
        yt.thumbnails().set(
            videoId=video_id, media_body=MediaFileUpload(thumb_path)
        ).execute()
        print(f"Thumbnail gesetzt: {thumb_path}")

    print("\nNAECHSTER SCHRITT - manuell (Controller-Gate):")
    print(f"  https://studio.youtube.com/video/{video_id}/edit")
    print("  -> 'Altered/synthetic content' (KI-Disclosure) setzen,")
    print("     Quellen/Description pruefen, dann veroeffentlichen/terminieren.")
    return video_id


def main():
    parser = argparse.ArgumentParser(
        description="Semi-automatischer YouTube-Upload (privat/terminiert)."
    )
    parser.add_argument("video", help="Pfad zur Videodatei (z. B. video.mp4)")
    parser.add_argument("--meta", default="video_metadata.json", help="Metadaten-JSON")
    parser.add_argument("--thumb", help="Thumbnail-Datei (optional)")
    args = parser.parse_args()
    try:
        upload(args.meta, args.video, args.thumb)
    except HttpError as err:
        sys.exit(f"YouTube-API-Fehler: {err}")


if __name__ == "__main__":
    main()
