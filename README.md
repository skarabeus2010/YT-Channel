# YT-Channel — KI-Historien-Kanal (Replikation von @Zenn0009)

Operating-Kit zum Aufbau eines **englischsprachigen, faceless, KI-cinematischen Historien-Kanals** nach Vorbild von [@Zenn0009](https://www.youtube.com/@Zenn0009), produziert mit [Higgsfield.ai](https://higgsfield.ai/).

> **Strategie & Doku:** Vollständiger Plan + Recherche liegen in [`docs/`](docs/strategy-plan.md).
> Dieses Repo macht den Plan **ausführbar**. (Original-Planfile auch unter
> `~/.claude/plans/verwende-agenten-eine-youtube-experte-quirky-sky.md`.)

## Was das ist

Fünf „Experten" als kopierfertige Prompts + ein **Controller**, der jedes Video gegen feste Gates prüft (vor allem **historische Faktentreue** und **KI-Compliance** — die zwei Sperr-Risiken dieses Genres 2026).

## Dokumentation (in `docs/`)

| Datei | Inhalt |
|---|---|
| [strategy-plan.md](docs/strategy-plan.md) | Vollständiger Strategie-Plan (Single Source of Truth) |
| [research-findings.md](docs/research-findings.md) | Alle Recherche-Daten: Benchmarks, Preise, Policy, Higgsfield, Stack |
| [decisions-log.md](docs/decisions-log.md) | Entscheidungen + Begründungen + offene Punkte |
| [sources.md](docs/sources.md) | Quellenlinks (Stand Juni 2026) |
| [glossary.md](docs/glossary.md) | Begriffe kurz erklärt |

## Ordner-Map

```
YT-Channel/
├─ README.md                 ← du bist hier
├─ docs/                     ← Doku (Plan, Recherche, Entscheidungen, Quellen, Glossar)
│  ├─ strategy-plan.md
│  ├─ research-findings.md
│  ├─ decisions-log.md
│  ├─ sources.md
│  └─ glossary.md
├─ agents/                   ← die 5 Experten als Prompt-Vorlagen
│  ├─ 01-youtube-strategist.md
│  ├─ 02-seo-expert.md
│  ├─ 03-content-creator.md
│  ├─ 04-marketing-expert.md
│  └─ 05-controller.md
├─ templates/                ← pro Video kopieren
│  ├─ content-brief.md
│  ├─ source-log.md
│  ├─ seo-metadata.md
│  ├─ ai-disclosure.md
│  └─ controller-checklist.md
├─ workflow/
│  ├─ production-sop.md      ← Schritt-für-Schritt Higgsfield-Pipeline
│  └─ upload-automation.md   ← Semi-auto YouTube-Upload (Setup + Nutzung)
└─ scripts/                  ← Upload-Automatisierung (Python)
   ├─ upload_youtube.py
   ├─ requirements.txt
   └─ video_metadata.example.json
```

## So benutzt du das Kit (pro Video)

1. **YouTube-Stratege** (`agents/01`) → erzeugt einen **Content-Brief** (`templates/content-brief.md`).
2. **SEO-Experte** (`agents/02`) → Ziel-Keywords + Metadaten (`templates/seo-metadata.md`).
3. **Content-Creator** (`agents/03`) → Recherche + Skript + **Quellen-Log** (`templates/source-log.md`) → Higgsfield-Produktion (`workflow/production-sop.md`).
4. **Controller** (`agents/05`) → füllt `templates/controller-checklist.md` aus → **Go/No-Go**.
5. Nach Go: Upload via [`scripts/upload_youtube.py`](scripts/upload_youtube.py) (lädt **privat/terminiert**) → in Studio **KI-Disclosure** (`templates/ai-disclosure.md`) setzen + veröffentlichen. Setup: [`workflow/upload-automation.md`](workflow/upload-automation.md).
6. **Marketing-Experte** (`agents/04`) → Repurposing (Shorts→TikTok/Reels) + Community.
7. Nach 48 h / 7 Tagen: Controller-**Post-Publish-Audit**.

Jeder Agenten-Prompt ist so geschrieben, dass du ihn 1:1 an Claude (oder ein anderes LLM) geben kannst. Die eigentlichen Content-Prompts sind **englisch** (für englischen Output), die Erklärungen deutsch.

## Roadmap (abhaken)

- [ ] **Phase 0 – Setup (Woche 1):** Google Brand Account + 2FA · Branding-Assets · Higgsfield-Abo · Bootstrap-Tools · Checklisten als Vorlage
- [ ] **Phase 1 – Manueller Pilot (Woche 2–5):** 2–3 Long-form + 10–15 Shorts komplett manuell durch die 5-Rollen-Pipeline
- [ ] **Phase 2 – Iterieren (Woche 6–10):** A/B-Thumbnails · Hooks/Pacing nach Retention · Repurposing-Routine
- [ ] **Phase 3 – Teil-Automatisierung (ab Woche 10):** n8n für Mechanik (Redaktion bleibt manuell)
- [ ] **Go/No-Go:** Tag 30 (Prozess stabil, Policy sauber?) · Tag 90 (Trend Richtung YPP?)

## Budget-Schnellreferenz (Stand 2026, vor Buchung prüfen)

| Tier | Kern | ~ / Monat |
|---|---|---|
| Lern-Minimum | Higgsfield Starter $15 + Free-Tools | €30–40 |
| Produktiver Start | Higgsfield Plus $34 + ElevenLabs + Artlist | €60–75 |
| Semi-Pro | Higgsfield Ultra $84 + vidIQ + Submagic + … | €200–300 |

KI-Video-Credits sind der größte variable Block. Modell-Tipp: **Kling 3.0** (günstig) zum Start, **Veo 3.1** für Premium-Stücke. ⚠ Sora 2 wird Sept 2026 abgekündigt.

## Compliance — nicht verhandelbar (sonst Demonetarisierung/Sperre)

1. **KI-Disclosure** pro Video (YouTube „altered/synthetic content"-Label) + **C2PA-Metadaten**.
2. **Historische Faktenprüfung** mit Quellen-Log — keine KI-Halluzination als Fakt.
3. **Menschliche Redaktion** dokumentieren · Musik nur Content-ID-sicher.
4. EU AI Act KI-Kennzeichnung (ab Aug 2026) — als EU-Creator relevant.
