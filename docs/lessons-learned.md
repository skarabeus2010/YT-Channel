# Lessons Learned — Produktion der ersten Videos

> Praxiswissen aus der tatsächlichen Produktion (2026-06-16/17): Pyramids-Short + Pompeii-Long-form.
> Ergänzt die [production-sop](../workflow/production-sop.md) um das, was man erst beim Machen lernt.

## 0. Das größte Missverständnis
**Ein fertiges Video entsteht NICHT aus einem Klick.** KI-Tools (Kling etc.) liefern nur **kurze, stumme Clips (3–15 Sek.)** — die Bausteine. Das fertige Video wird **zusammengesetzt**: viele Clips/Standbilder **+ separate Erzählstimme + Captions + Musik**. Länge = **Erzählstimme**, nicht Clip-Anzahl.

## 1. Higgsfield-Tier & Kosten (Stand 06/2026)
- **Free-Plan = unbrauchbar für uns:** nur 10 Credits **und keine kommerziellen Rechte** → Output darf nicht auf einen monetarisierten Kanal. **Vor jeder Produktion ein Paid-Tier.**
- **„Starter $15" existiert nicht mehr** — günstigster Tier ist **PLUS (~€49/Mo, 1.000 Credits)**. (Entscheidungs-Log #3/#7 entsprechend überholt.)
- **Credit-Richtwerte (PLUS):**
  - Bild (GPT Image 2): ~0,5 Cr (high) / ~0,3 Cr (medium). **Medium reicht** für B-Roll, das mit Bewegung + Caption läuft.
  - Video (Kling 3.0, 5s, std, silent): **~7,5 Cr/Clip.**
  - **Ein 40-Sek-Short ≈ ~60 Credits.** Ein 8-Min-Long-form (Ken-Burns-Stills) ≈ ~40–90 Credits.
  - → PLUS reicht für **~12–18 fertige Videos/Monat**.
- **Concurrency-Limit PLUS = 8 gleichzeitige Jobs.** In **8er-Wellen** arbeiten, sonst „Rate limit reached".
- **Immer `sound: off`** bei Kling rendern (wir legen eigene VO drüber) → spart Credits.
- **`get_cost: true`** vor teuren Jobs zum Preflight nutzen.

## 2. Erzählstimme (TTS) — der Längen-Treiber
- Modell **Inworld TTS**, Stimme **„Theodore (en)"** (ruhiger Doku-Ton) = unsere Kanal-Stimme.
- **Sprechtempo ~2 Wörter/Sek.:** 125 Wörter ≈ 60s · ~730 Wörter ≈ 6 Min.
- ⚠️ **VO-Länge VOR der Bildproduktion aus der Wortzahl abschätzen!** Long-form braucht **≥8 Min für Mid-Roll-Ads** → das sind **~1.000–1.100 gesprochene Wörter**. (Wir hatten erst nur 5,9 Min und mussten das Skript erweitern.)
- Lange Skripte **kapitelweise** generieren (sauber fürs Timing von Bildern + Captions; umgeht TTS-Längenlimits).

## 3. Bild/Video-Generierung
- **GPT Image 2** liefert era-treue, cinematische Stills (sogar korrekte Latein-Schrift wie „PISTOR"). Prompt-Stil: „cinematic photorealistic, 35mm historical documentary, era-accurate <Jahr>".
- **Look + Bewegung erst an 1 Beispiel freigeben**, dann erst den ganzen Batch generieren (Credit-Disziplin).
- **nsfw-Filter:** Prompts mit „children + panic + dark/death" werden geflaggt. Entschärfen: „plaster cast", „archaeological", „dramatized reconstruction", keine Gewalt-Details.
- **Format:** Short = 9:16, Long-form = **16:9**.
- **Long-form füllt man mit Ken-Burns-Stills (~0,5 Cr), NICHT mit 100 Video-Clips** (8 Min reine Clips ≈ ~825 Cr = Wahnsinn). Faustregel: meist Stills + ~8 Hero-Clips für Schlüsselmomente.

## 4. Tooling-Setup (Windows)
- **Higgsfield-MCP** über `/mcp` (OAuth im Browser) ist der saubere Weg. **User-Scope** wählen, sonst taucht der Server nicht im `/mcp`-Panel auf.
- **Higgsfield-CLI (npm/curl) ist auf Windows kaputt:** GNU-`tar` interpretiert das `C:` im Pfad als Remote-Host. → MCP nutzen.
- **ffmpeg** ist nicht vorinstalliert: `winget install Gyan.FFmpeg`. PATH-Update braucht neue Shell → vollen `.exe`-Pfad verwenden (wir cachen ihn in `_renders/.ffmpeg_path.txt`).
- Frisch heruntergeladene `.exe` ist durch „Mark of the Web" blockiert (`Unblock-File`).

## 5. ffmpeg-Assemblierung (die teuer erkauften Fallstricke)
- **`zoompan` (Ken Burns) ist pathologisch langsam** (~30s/Segment) → **animierter Crop-Schwenk** stattdessen (`crop=...:x=(iw-ow)*t/DUR`): **~1,6s/Segment, ~30× schneller**, sieht ähnlich gut aus.
- **PowerShell-Quoting:** ffmpeg-Filter-Ausdrücke **NICHT in Single-Quotes** auf Windows (bricht den Parser) → unquoted: `zoompan=z=zoom+0.005:x=iw/2-(iw/zoom/2)...`.
- **Concat-Label-Bug:** `"[$_:a]"` ergibt leer → `"[$($_):a]"`.
- **Tempo:** 24 fps, kein unnötiges Hochskalieren, `-preset ultrafast` (Segmente) / `veryfast` (Final).
- **Captions:** SRT mit **wortproportionalem Timing pro Kapitel** bauen → gute Synchronität. Einbrennen mit `subtitles=`-Filter (ins Verzeichnis `cd`, relativer Pfad). **Impact-Font** für Thumbnails (`C:/Windows/Fonts/impact.ttf`).
- **Musik:** ~90s-Bett(en) generieren, mit `-stream_loop -1` auf die Länge loopen; **Stimmungswechsel** (ruhig→düster) wirkt stark. Lautstärke ~0,12 unter die VO mischen (`amix=...:normalize=0`).
- **Assembly als wiederverwendbares `.ps1`** schreiben (idempotent, `_work`-Ordner neu aufbauen), nicht inline.

## 6. Compliance & Monetarisierung (nicht verhandelbar)
- **Kommerzielle Rechte + Content-ID-sichere Musik** sind beide durch den **Paid-Tier** gelöst (KI-generierte Sonilo-Musik = sicher).
- **KI-Label** wird **manuell in Studio** gesetzt (API macht es nicht zuverlässig) — bewusst der menschliche Gate-Schritt.
- **Faktencheck (Mensch) + KI-Label = die zwei Hard-Stops.** Alles andere ist automatisierbar.
- Umstrittene Fakten **offen lassen** (z. B. Pompeji-Datum), Rekonstruktionen kennzeichnen, **kein KI-Bild als „Archivmaterial"**.
- **8-Min-Schwelle** = Voraussetzung für Mid-Roll-Ads. Echtes Ad-Geld erst nach **YPP** (1.000 Abos + 4.000 Std., realistisch 6–12+ Mon.). **Custom-Thumbnail braucht verifizierten Kanal.**

## 7. Bewährter Produktions-Ablauf (pro Long-form)
1. Skript schreiben → **Wortzahl auf ≥8 Min prüfen** (≥~1.000 Wörter) → ggf. erweitern (faktengeprüft!).
2. VO **kapitelweise** generieren, Gesamtlänge messen.
3. Stills (16:9) in 8er-Wellen generieren (Look an 1 Bild freigeben).
4. 2 Musik-Betten (ruhig/düster) generieren.
5. Captions-SRT (kapitel-proportional) bauen.
6. `assemble.ps1`: Crop-Schwenk-Segmente → Concat → VO + Musik-Mix + Caption-Burn.
7. Frames extrahieren zur Sicht-Prüfung → Faktenfreigabe → Upload → KI-Label → Publish.
