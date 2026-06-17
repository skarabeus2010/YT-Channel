# CLAUDE.md — Embered Ages (KI-Historien-YouTube-Kanal)

> Operating-Leitfaden für Claude. Wird jede Session geladen — knapp halten.
> Sprache mit Heiko: **Deutsch**. Kanal-Content: **Englisch**.

## Was das ist
Faceless, **KI-cinematischer Geschichts-Kanal „Embered Ages"** (immersive Antike/Historie), produziert mit **Higgsfield.ai**. Vorbild: @Zenn0009. **Ziel #1 = Geld verdienen** → **Long-form ≥8 Min priorisieren** (Mid-Roll-Ads), Shorts als Discovery-Funnel.

## ⚠️ Nicht verhandelbar — die 2 Hard-Stops (sonst YouTube-Sperre)
1. **Menschliche Faktenfreigabe (Heiko)** je Video — gegen den Quellen-Log. Claude recherchiert/belegt, aber Heiko gibt frei.
2. **KI-Label** „altered/synthetic content" beim Upload (manuell in YouTube Studio).
→ **Nichts wird ohne beides veröffentlicht.** Korrekt deklarierte KI bleibt voll monetarisierbar. Umstrittene Fakten offen lassen, Rekonstruktionen kennzeichnen, kein KI-Bild als „Archivmaterial".

## Das 5-Agenten-Modell (`agents/`)
1. **YouTube-Stratege** → Konzept/Brief, Packaging, Retention-Struktur.
2. **SEO-Experte** → Keywords, Metadaten (`content/seo-*.md`).
3. **Content-Creator** → Recherche + Skript + Quellen-Log (`content/script-*.md`) → Higgsfield-Produktion.
4. **Marketing-Experte** → Repurposing, Community.
5. **Controller** → Qualitäts-/Compliance-Gate (Go/No-Go + Post-Publish-Audit). Kein Video ohne Controller-„Go".

## „Interview Me"-Modus
Wenn Heiko ein **neues Video/Batch** startet (oder „interview me" sagt): **erst eine kurze, fokussierte Fragerunde** (Thema/Seed · Short oder Long-form · Winkel/Pflicht-Inhalte · Ton), **dann** produzieren. Nicht raten, wenn Inputs fehlen — aber bei „mach einfach"/Auto-Modus eigenständig sinnvolle Defaults wählen und durchziehen.

## Konventionen / Preferences
- **IMMER Titelvorschläge mitliefern:** 1 empfohlen (<60 Zeichen, Keyword + Curiosity-Gap) + 2 A/B-Alternativen. Nie warten, bis Heiko fragt.
- **Ordner:** `content/` = Text (`script-*`, `seo-*`, Kalender). `content/renders/` = Medien (`FINAL.mp4`, Thumbnails) — **gitignored** (zu groß).
- **Commits/Push** wenn Heiko es sagt oder ein Batch fertig ist.

## Produktions-Pipeline (Details: `docs/lessons-learned.md`, `workflow/production-sop.md`)
- Higgsfield über **MCP** (`/mcp`-Auth), **PLUS-Tier** (kommerzielle Rechte + Content-ID-sichere Musik). Max **8 parallele Jobs** → 8er-Wellen. ~150 Credits pro Batch (mehrere Videos).
- **Reihenfolge:** VO zuerst (bestimmt die Länge!) → Stills (GPT Image 2, medium) → Musik (Sonilo) → Captions-SRT → **ffmpeg-Assembly** (Crop-Schwenk statt zoompan; unquoted Filter-Expr) → Thumbnail (Impact-Font).
- **Long-form ≥8:00 Min** für Mid-Rolls = **~1.000+ gesprochene Wörter** (Theodore-Stimme ~2 Wörter/Sek). Länge VOR Bildproduktion prüfen.
- Voice „Theodore (en)"; Kling silent rendern; nsfw-Filter via vorsichtige Prompts umgehen.

## Status (2026-06-17)
- **Live:** Pyramids-Short, Pompeii-Long-form (KI-Label gesetzt).
- **Produziert, pending Upload:** Urine, Two-Sleeps, Rome-Smell, Gladiator (Faktenfreigabe erteilt; nur noch Upload + KI-Label).
- **In Skripten:** Batch 2 — 5 Shorts + 5 Long-forms → `content/batch-2-calendar.md`.
- **Audit-Routine:** `trig_01JbafvmNWbLV26TgDBFJxni` (Cloud, prüft die 2 Live-Videos).
