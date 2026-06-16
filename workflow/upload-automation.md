# Upload-Automatisierung (Semi-auto via YouTube Data API)

> **Empfohlener Weg fürs Experiment.** Ein lokales Python-Skript lädt das fertige Video
> **als privat (oder terminiert)** hoch und setzt die Metadaten. **Manuell** bleibt nur der
> letzte Klick in YouTube Studio: **KI-Disclosure-Label setzen + Controller-Go + veröffentlichen.**
> Das ist Absicht — genau dort sitzen die zwei Hard-Stops (Faktencheck, KI-Kennzeichnung).

**Warum Python statt n8n (jetzt):** null Hosting-Kosten, keine VPS, volle Kontrolle. n8n lohnt erst,
wenn du auf feste Cadence voll-automatisierst (dann VPS ~$5–7/Mo).

---

## Was automatisiert / was manuell

| Schritt | Wer |
|---|---|
| Video hochladen (privat/terminiert), Titel/Description/Tags/Chapters, Thumbnail | **Skript** |
| KI-Disclosure „altered/synthetic content"-Label | **Mensch** (Studio) — API stellt das nicht zuverlässig bereit |
| Controller-Gate (Faktencheck, Quellen) + finale Freigabe | **Mensch** |

---

## Einrichtung (einmalig, ~15–20 Min)

### 1. Google Cloud Projekt + API
1. [console.cloud.google.com](https://console.cloud.google.com/) → neues Projekt (z. B. `yt-channel-upload`).
2. **APIs & Dienste → Bibliothek →** „YouTube Data API v3" → **Aktivieren**.

### 2. OAuth-Zustimmungsbildschirm
3. **OAuth consent screen** → User Type **External** → App-Name/Mail eintragen.
4. Unter **Test users** deine YouTube-Google-Adresse hinzufügen (im Testmodus reicht das; kein Verifizierungs-Review nötig, solange nur du es nutzt).

### 3. OAuth-Client (Desktop)
5. **Anmeldedaten → Anmeldedaten erstellen → OAuth-Client-ID → Anwendungstyp „Desktop-App"**.
6. JSON herunterladen → als **`scripts/client_secret.json`** ablegen. **Niemals committen** (steht in `.gitignore`).

### 4. Python-Umgebung
```powershell
cd C:\dev\YT-Channel\scripts
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 5. Erststart (OAuth-Login)
```powershell
python upload_youtube.py "C:\pfad\zu\video.mp4" --meta video_metadata.json
```
Beim ersten Lauf öffnet sich der Browser → mit dem Kanal-Google-Account einloggen → Zugriff erlauben.
Danach liegt `token.json` vor und der Login wird gecacht.

---

## Metadaten pflegen

`video_metadata.example.json` → kopieren nach `video_metadata.json` und aus
`templates/seo-metadata.md` füllen. Felder:

| Feld | Bedeutung |
|---|---|
| `title` / `description` / `tags` | aus SEO-Metadaten; Description enthält Disclosure + „Sources:" |
| `categoryId` | `27` = Education (History/Edu), `22` = People & Blogs, `24` = Entertainment |
| `privacyStatus` | `private` (Default) / `unlisted` / `public` |
| `publishAt` | terminiert: ISO-8601-**UTC**, z. B. `2026-07-01T09:00:00Z` (erzwingt `private` bis dahin) |
| `madeForKids` | i. d. R. `false` |

---

## Wichtige Grenzen (ehrlich)

- **Private-until-audited:** Ohne bestandenes [YouTube-API-Audit](https://developers.google.com/youtube/v3/docs/videos/insert) kann die API **nur als privat** hochladen. Für *direktes* public-Auto-Upload müsste das API-Projekt den Audit durchlaufen. Für unseren semi-auto-Weg **nicht nötig** — du veröffentlichst manuell.
- **Quota:** `videos.insert` kostet **1.600 Units**; Standard-Tageskontingent 10.000 → **~6 Uploads/Tag**. Mehr → Quota-Erhöhung beantragen.
- **Custom-Thumbnail** (`--thumb`) braucht einen **verifizierten Kanal**.
- **KI-Disclosure** wird in **Studio** gesetzt (API-Feld nicht zuverlässig) — bewusst Teil des manuellen Gates.
- **Headless/Server:** `run_local_server` braucht einen Browser. Auf einem Server einmal lokal `token.json` erzeugen und mitnehmen.

---

## Später: Cadence automatisieren
- **Windows:** Aufgabenplanung (Task Scheduler) ruft das Skript zu festen Zeiten auf.
- **n8n:** YouTube-Node + „watch folder" (Drive) für vollere Automatisierung — Redaktion/Faktencheck bleiben manuell.

## Sicherheit
`client_secret.json` und `token.json` sind **Zugangsdaten** → nie teilen/committen (in `.gitignore`). Bei Verdacht: in der Google Cloud Console widerrufen und neu erzeugen.
