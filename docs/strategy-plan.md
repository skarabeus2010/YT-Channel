# Strategie-Plan: @Zenn0009 replizieren (KI-cinematischer Historien-Kanal)

> Single Source of Truth im Repo. Freigegebene Fassung (2026-06-16). Spiegelt den Plan unter
> `~/.claude/plans/verwende-agenten-eine-youtube-experte-quirky-sky.md`.

## Kontext

Ziel: den YouTube-Kanal **[@Zenn0009](https://www.youtube.com/@Zenn0009)** replizieren — als **englischsprachiges Lern-Experiment mit minimalem Budget**. Fünf Experten-Rollen (YouTube-, SEO-, Marketing-Experte, Content-Creator, Controller). Gebraucht: Kanal-Analyse, Replikations-Vorschläge, Tools, Infrastruktur, ein Plan für die Experten, ein Verifikationsplan für den Controller.

**Was der Kanal ist:** KI-generierte, cinematische Historien-/„Ancient World"-Videos (z. B. *„What Did Ancient Humans Do at Night?"*) — faceless, hyperrealistisch, dokumentarisch vertont. Erstellt mit **[Higgsfield.ai](https://higgsfield.ai/)** (Modelle Sora 2 / Kling 3.0 / Veo 3.1; Cinema-Studio; 70+ Kamera-Presets; TTS „Higgsfield Audio").

**Strategisch wichtigste Tatsache:** Dieses Genre ist Hauptziel von YouTubes „AI-Slop"-Durchgriff 2026 (Jan 2026: 16 Kanäle / 4,7 Mrd. Views entfernt; Mai 2026: Auto-Labeling). Tragfähiger Weg = **dokumentarische Qualität + nachprüfbare historische Korrektheit + menschliche Redaktion + saubere KI-Kennzeichnung**. Korrekt deklarierte KI bleibt monetarisierbar. EU AI Act KI-Kennzeichnung ab Aug 2026 relevant (EU-Creator).

## TL;DR

| Entscheidung | Empfehlung |
|---|---|
| Nische | KI-cinematische Geschichte / „immersive ancient world" (wie @Zenn0009); cinematic-history Shorts nahezu unbesetzt |
| Sprache | Englisch (CPM ~$10 vs. ~$3,50 global) |
| Kern-Tool | Higgsfield.ai (Image→Video); Kling 3.0 günstig (~$5–8/Min), Veo 3.1 Premium (~$45/Min) |
| Format | Shorts-dominant (24–38 Sek.) + 1 Long-form (8–15 Min) |
| Output | 3–5 Shorts/Woche + 1 Long-form/Woche; dokumentarischer VO |
| Budget | Lern-Minimum ~€30–40 · Produktiver Start ~€60–75 · Semi-Pro ~€200–300 /Mo |
| Überlebens-Regel | KI-Disclosure + C2PA + historische Faktenprüfung mit Quellen + menschliche Voice/Redaktion |
| Arbeitsweise | erst manuell (lernen), dann Mechanik via n8n — nie die Redaktion |

## 1. Kanal-Analyse
KI-generierte cinematische Geschichte; faceless, voll KI-visualisiert via Higgsfield; Shorts als Discovery-Motor (im Segment fast konkurrenzlos) + längere Stücke; Neugier-Hook + cinematische Bildkraft. Qualitäts-Nordstern: MagnatesMedia / ColdFusion. **Benchmarks:** CTR ≥4 % (Ziel 7 %+) · Retention ≥40 %, erste 30–60 Sek. entscheidend · Returning Viewers >10 % · Shorts-Sweetspot 24–38 Sek. · ~100 Videos Durchhaltevermögen.

## 2. Das Experten-Team (5-Agenten-Betriebsmodell)

```
[YouTube-Experte] → [SEO-Experte] → [Content-Creator] → [Marketing-Experte]
        │                 │                  │                    │
        └─────────────────┴────► [CONTROLLER] ◄───────────────────┘
            prüft: Fakten · KI-Compliance · Qualität · SEO
            (Go/No-Go VOR Publish + Audit DANACH)
```

| Rolle | Output | Tools |
|---|---|---|
| YouTube-Experte | Content-Brief + Kalender | YouTube Studio, vidIQ/TubeBuddy |
| SEO-Experte | Keywords + Metadaten | vidIQ/TubeBuddy, Trends, Autocomplete |
| Content-Creator | Video + Quellen-Log + Assets | Higgsfield, Claude, ElevenLabs, CapCut/DaVinci, Canva |
| Marketing-Experte | Distributions-Plan + Community | OpusClip, Repurpose.io, Community-Tab, Discord |
| Controller | Prüfbericht + Audit | Faktencheck, YT-Policy-Checkliste, Analytics |

Die *Historiker-/Faktenchecker-Funktion* liegt produktionsseitig beim Content-Creator, prüfseitig beim Controller. Kein Video ohne Controller-„Go".
→ Ausführbare Prompts: [`agents/`](../agents/). Verifikationsdetails: §6.

## 3. Strategie & Produktions-Pipeline
Faceless, KI-visualisiert, AI-assistiert + menschliche Redaktion. Shorts (24–38 Sek.) Discovery; 1 Long-form (8–15 Min) Monetarisierungs-Watchtime.
Pipeline: Recherche & Skript (faktengeprüft, Quellen-Log) → Storyboard (Higgsfield Soul) → Image→Video (Kling/Veo + Presets) → Voice (Higgsfield Audio/ElevenLabs) → Assembly (CapCut→DaVinci, Content-ID-sichere Musik, Captions) → Packaging & Upload (KI-Label + C2PA + Quellen) → Controller-Gate → Publish → Repurposing.
Lern-vor-Automatisierung: Phase 1 manuell; später n8n nur für Mechanik. → Details: [`workflow/production-sop.md`](../workflow/production-sop.md).

## 4. Tools (nach Pipeline-Stufe)
Vollständige Tabelle mit Bootstrap- vs. Semi-Pro-Stack und Preisen: siehe [`docs/research-findings.md`](research-findings.md) §7.
Kern: **Higgsfield** (KI-Video) · Claude (Skript) · ElevenLabs/Higgsfield Audio (Voice) · Artlist/Epidemic (Content-ID-sichere Musik) · DaVinci/CapCut (Schnitt) · Canva (Thumbnails) · vidIQ/TubeBuddy (SEO) · OpusClip (Repurposing) · n8n (Automation, später).

## 5. Infrastruktur
Normaler Laptop reicht (cloud-basiert). Google Brand Account + 2FA; 2FA auf allen API-Keys. Branding-Assets (Logo 1080×1080, Banner 2560×1440, Beschreibung + Disclaimer). Compliance-Setup: YT-Label, C2PA, Disclosure-Baustein. Storage: Drive (versioniert) + Backblaze B2 (Backup) + Quellen-Logs. Optionaler n8n-VPS später ($5–7/Mo). Budgets siehe §3 TL;DR / research-findings §9.

## 6. Controller-Verifikationsplan
Vollständig als ausführbare Checkliste: [`templates/controller-checklist.md`](../templates/controller-checklist.md). Agent-Prompt: [`agents/05-controller.md`](../agents/05-controller.md).
- **6.1 Pre-Production:** Hook, Retention-Struktur, Suchnachfrage/Lücke, Titel+Keywords.
- **6.2 Historische Korrektheit ⚠ HARD-STOP:** alle Aussagen mit Quelle belegt; Fakt vs. Rekonstruktion getrennt; keine Halluzination als Fakt; keine erfundene „Archiv"-Aufnahme; Visuals epochen-plausibel.
- **6.3 KI-Compliance ⚠ HARD-STOP:** YT-„synthetic/altered"-Label; C2PA; Disclosure-Text; KI-Stimme offengelegt; EU-AI-Act.
- **6.4 Anti-Slop/Qualität:** eigener Winkel + Tiefe; menschliche Redaktion dokumentiert; Content-Mix; saubere AV; Musik Content-ID-sicher.
- **6.5 SEO/Packaging:** Titel+Thumbnail eine Einheit; Keyword im 1. Satz; Chapters; Hashtags; Captions; Thumbnail-A/B.
- **6.6 Go/No-Go:** alle Pass → Go. Fail in 6.2/6.3 → Hard-Stop. Sonst Revise.
- **6.7 Post-Publish-Audit (48 h/7/28 T.):** CTR ≥4 %, Retention ≥40 %, Halten >60 Sek. ≥45 %, Subs/View 0,5–2 %, Returning >10 %, Policy-Status grün.
- **6.8 Monatsreview:** Trajektorie Richtung YPP, Policy-Risiko, Modell-/Kostencheck.
- **6.9 Scoring (0–2 je Dimension, max 14):** ≥12/14 UND kein 0 bei Korrektheit/Compliance/Lizenzen = Go.

## 7. Risiken & Compliance
AI-Slop-Sperrwelle (höchstes Risiko) · EU AI Act (ab Aug 2026) · historische Fehlinformation · Kosten-/Modell-Volatilität (Sora 2 Abkündigung Sep 2026) · Erwartung: 6–12 Monate bis YPP, ~100 Videos Durchhaltevermögen.

## 8. Roadmap
- Phase 0 Setup (Wo 1) · Phase 1 Manueller Pilot (Wo 2–5) · Phase 2 Iterieren (Wo 6–10) · Phase 3 Teil-Automatisierung (ab Wo 10). Go/No-Go Tag 30 & Tag 90.

## 9. Verifikation des Gesamtplans
Pilot: Setup-Check → 1 Long-form durch alle 5 Rollen (Controller-Gates ausgefüllt, Quellen-Log) → Publish mit KI-Label + Audit → 3–5 Videos Scoring-Schnitt ≥12/14 → Tag-30/Tag-90-Entscheidung.

## Upload-Sicherstellung
Semi-auto via [`scripts/upload_youtube.py`](../scripts/upload_youtube.py) (privat/terminiert) + manuelles KI-Label/Publish in Studio (= Controller-Gate). Setup: [`workflow/upload-automation.md`](../workflow/upload-automation.md). Begründung im Entscheidungs-Log.
