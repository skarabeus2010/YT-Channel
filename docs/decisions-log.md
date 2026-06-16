# Entscheidungs-Log

> Was wir entschieden haben und warum. Chronologisch ergänzen.

## 2026-06-16 — Projektstart & Kernentscheidungen

| # | Entscheidung | Begründung | Status |
|---|---|---|---|
| 1 | **Ziel-Kanal: @Zenn0009** | Vom Nutzer bestätigt (zunächst nur „zenn"-Suche, dann Handle nachgereicht) | fix |
| 2 | **Nische: KI-cinematische Geschichte** | Das ist das tatsächliche Format des Kanals (immersive Antike/Historie) | fix |
| 3 | **Kern-Tool: Higgsfield.ai** | Nutzer-Hinweis: Kanal damit produziert; Marktführer für cinematische KI-Videos | fix |
| 4 | **Sprache: Englisch** | CPM ~$10 vs. ~$3,50 global; größte Reichweite | fix |
| 5 | **Format: faceless, AI-assistiert + menschliche Redaktion** | Vollautomatik wird von YouTube gesperrt (AI-Slop-Purge); Redaktion = Überlebensbedingung | fix |
| 6 | **Budget: „Experiment" / minimal** | Vom Nutzer gewählt → Bootstrap-Stack, Manuell-zuerst | fix |
| 7 | **Modell-Start: Kling 3.0** (statt Veo 3.1) | ~$5–8/Min vs. ~$45/Min; für Lernphase günstiger; Veo für Hero-Stücke | empfohlen, anpassbar |
| 8 | **Cadence: Shorts-first + 1 Long-form/Woche** | Shorts = Discovery (fast konkurrenzlos im Genre), Long-form = Monetarisierungs-Watchtime | Default, anpassbar |
| 9 | **Compliance: Disclosure + C2PA + Quellen-Log Pflicht** | Genre ist Hauptziel der Sperrwelle; EU AI Act ab Aug 2026 | fix (Hard-Stop im Controller) |
| 10 | **Upload: semi-auto (Python + YouTube Data API)** | Kein YouTube-MCP-Connector verfügbar; „private-until-audited"-Limit → privat/terminiert hochladen, Mensch setzt KI-Label + veröffentlicht (= Controller-Gate). Python statt n8n: null Hosting-Kosten | fix |
| 11 | **n8n erst später** | Lohnt erst bei fester Cadence-Automatisierung (VPS-Kosten) | aufgeschoben |

## Offene Punkte
- **Shorts-first vs. Long-form-first** endgültig bestätigen (Default: Shorts-first).
- **Erste 5 Video-Konzepte** noch zu erstellen (Phase-1-Start).
- **Higgsfield-Abo-Tier** wählen (Starter zum Lernen vs. Plus produktiv).
- **YouTube-API-Audit** später, falls public-Voll-Automatik gewünscht.
- Preise/Policies bei Umsetzung tagesaktuell verifizieren.

## Verworfene Annahmen
- ~~Nische „Zen/Meditation/Stoizismus"~~ — basierte auf der mehrdeutigen „zenn"-Suche, bevor der echte Kanal bekannt war. Hinfällig seit Entscheidung #1/#2.
