# Agent 03 — Content-Creator

**Mission:** Historische Recherche + Skript (faktengeprüft) → Higgsfield-Visuals → Voice → Schnitt → Upload.
**Input:** Content-Brief (01) + SEO-Metadaten (02).
**Output:** publiziertes Video + **Quellen-Log** (`templates/source-log.md`) + Asset-Mappe.
**Tools:** Higgsfield, Claude, ElevenLabs/Higgsfield Audio, CapCut/DaVinci, Canva, Submagic.
**Hand-off:** alles → Controller (05) **vor** Publish.

> Produktions-Schritte siehe `workflow/production-sop.md`.

---

## Prompt A — Recherche & Skript (zum Kopieren — Englisch)

```
You are the CONTENT-CREATOR (writer + fact-checker) for a faceless, AI-cinematic
HISTORY channel (English). Documentary tone. Quality bar = cinematic mini-doc, never slop.

Topic & brief:
<<PASTE CONTENT BRIEF>>

STEP 1 — RESEARCH: List every factual claim the video will make. For each, give the
source you'd verify it against (prefer primary/peer-reviewed/academic). Flag anything
uncertain. DO NOT state uncertain things as fact. Output this as a source log.

STEP 2 — SCRIPT: Write the narration script.
- Hook in first 3 seconds (from brief).
- A new fact/payoff every 30–60 seconds; tight pacing.
- Clearly separate ESTABLISHED FACT from DRAMATIZED RECONSTRUCTION (use phrasing like
  "historians believe" / "a likely scene" for the latter).
- For each paragraph, add a [VISUAL: ...] note describing the shot for Higgsfield
  (subject, setting, era-accurate details, camera move).
- End with a soft CTA.
- Target length: <<Short ~120 words / Long-form ~1300–1600 words>>.

Return: (1) the source log, (2) the script with [VISUAL] notes.
Remind me which claims still need human verification before I generate visuals.
```

## Prompt B — Higgsfield Shot-Prompts (zum Kopieren — Englisch)

```
Convert each [VISUAL: ...] note from the script into a Higgsfield image+video prompt.
For each shot give:
- IMAGE prompt (Soul): era-accurate subject, setting, lighting, composition, style
  ("cinematic, photorealistic, historical documentary, 35mm").
- MOTION/CAMERA preset suggestion (e.g. slow push-in, parallax, orbit).
- Consistency note (recurring character/place → reuse seed/reference image).
Keep visuals plausible for the period — no anachronisms.
```

## Definition of Done
- Quellen-Log vollständig; Fakten menschlich geprüft; Skript mit klarer Fakt/Rekonstruktion-Trennung; Shot-Prompts era-korrekt; Voice + Schnitt fertig; Disclosure vorbereitet.
