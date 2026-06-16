# Übergabe-Prompt für Claude Code

> Diesen Prompt in einer neuen Claude-Code-Session (im Ordner `C:\dev\YT-Channel`) einfügen,
> um die Arbeit nahtlos fortzusetzen. Alles Nötige liegt im Repo (`docs/`, `agents/`, `templates/`, `workflow/`, `scripts/`).

```text
Projekt-Übernahme: KI-cinematischer YouTube-Historien-Kanal (Replikation von @Zenn0009).

Arbeitsverzeichnis: C:\dev\YT-Channel  (Windows, PowerShell).
Sprache mit mir: Deutsch. Der Kanal-Content selbst ist Englisch.

Es existiert bereits ein vollständiges, dokumentiertes Operating-Kit. Bitte übernimm es
komplett – inklusive aller Skripte. Lies dich ZUERST in dieser Reihenfolge ein, um den
vollen Kontext zu haben, bevor du irgendetwas tust:
  1. README.md
  2. docs/strategy-plan.md      (die Gesamtstrategie, Single Source of Truth)
  3. docs/decisions-log.md      (was entschieden wurde + offene Punkte)
  4. docs/research-findings.md  (Benchmarks, Preise, Policy, Higgsfield, Tool-Stack)
  5. docs/channel-setup.md      (Kanal-Identität: Embered Ages)
  6. überfliege agents/, templates/, workflow/, scripts/

Worum es geht: faceless, KI-generierte cinematische Geschichts-Videos (immersive Antike),
produziert mit Higgsfield.ai, Englisch, als minimal-Budget-Lern-Experiment. Der Kanal heißt
"Embered Ages" (@EmberedAges), neuer Google-Brand-Account (Identität: docs/channel-setup.md).
5-Rollen-Modell (YouTube-Stratege, SEO, Content-Creator, Marketing, Controller) mit dem
Controller als Qualitäts-Gate.

NICHT VERHANDELBARE LEITPLANKEN (sonst YouTube-Sperre – das ist der Kern des Projekts):
  - Compliance Hard-Stops pro Video: KI-Disclosure-Label + C2PA-Metadaten +
    historische Faktenprüfung mit Quellen-Log + nachweisbare menschliche Redaktion.
  - Keine Vollautomatik der Redaktion. Korrekt deklarierte KI bleibt monetarisierbar.
  - Upload semi-auto: scripts/upload_youtube.py lädt PRIVAT/terminiert hoch; das finale
    KI-Label + Veröffentlichen passiert MANUELL in YouTube Studio (= Controller-Gate).
    Setup-Anleitung: workflow/upload-automation.md.

Was schon fertig ist: kompletter Plan + Doku (docs/), 5 ausführbare Experten-Prompts
(agents/), 5 Pro-Video-Templates (templates/), Higgsfield-Produktions-SOP + Upload-Anleitung
(workflow/), Python-Upload-Skript inkl. requirements + Beispiel-Metadaten (scripts/),
.gitignore. Das Skript wurde bereits mit py_compile auf Syntax geprüft.

Deine Aufgabe:
  1. Mach dich mit dem gesamten Kit und den Skripten vertraut und übernimm sie.
  2. Gib mir eine kurze Bestätigung (3–5 Sätze), dass du den Stand verstanden hast,
     plus eine Liste der offenen Punkte aus docs/decisions-log.md.
  3. Danach warte auf meine Richtung – oder schlage den nächsten konkreten Schritt vor.
     Naheliegend: (A) als YouTube-Stratege die ersten 5 Video-Konzepte erstellen
     (agents/01-youtube-strategist.md), oder (B) das Google-Cloud-/OAuth-Setup für den
     ersten Test-Upload durchgehen (workflow/upload-automation.md).

Optional: Wenn sinnvoll, schlage vor, das Repo mit `git init` zu versionieren
(.gitignore liegt bereit). Frag mich vorher.
```
