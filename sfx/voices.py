#!/usr/bin/env python3
"""Generate character voice lines with the ElevenLabs TTS API.
Usage: ELEVENLABS_API_KEY=sk_... python3 voices.py
"""
import json, os, sys, pathlib, urllib.request, urllib.error

KEY = os.environ.get("ELEVENLABS_API_KEY")
if not KEY:
    sys.exit("ELEVENLABS_API_KEY not set")

OUT = pathlib.Path(__file__).parent / "voice"
OUT.mkdir(exist_ok=True)

# premade ElevenLabs voices, cast per character
VOICES = {
    "sichar":  "N2lVS1w4EtoT3dr4eOWO",  # Callum — intense, brash
    "chram":   "TxGEqnHWrfWFTfGW9XjX",  # Josh — young, tense
    "gregory": "onwK4e9ZLuTAKqWW03F9",  # Daniel — authoritative, episcopal
    "judge":   "pNInz6obpgDQGcFmaJgB",  # Adam — deep, official
    "priest":  "JBFqnCBsd6RMkjVDRZzb",  # George — warm
    "servant": "iP95p4xoKVk53GoZ742B",  # Chris — casual young
    "austre":  "VR6AewLTigWG4xSOukaG",  # Arnold — crisp, hard
    "king":    "nPczCjzI2devNBz1zQrb",  # Brian — resonant, royal
}

LINES = [
    ("v_priest_invite",   "priest",  "Boy — go bid the men come drink at my house, for the feast!"),
    ("v_servant_invite",  "servant", "The priest invites you to drink, good sirs!"),
    ("v_sichar_challenge","sichar",  "Austregisel! Answer for the boy's blood!"),
    ("v_austre_silver",   "austre",  "The silver is mine now."),
    ("v_judge_verdict",   "judge",   "Austregisel: homicide. Let him bear the censure of the law!"),
    ("v_sichar_ride",     "sichar",  "My silver sits in Auno's hall. We ride tonight."),
    ("v_chram_father",    "chram",   "Father… no!"),
    ("v_gregory_peace",   "gregory", "Cease, O men! Blessed are the peacemakers — let the Church's silver pay, that no soul be lost!"),
    ("v_chram_refuse",    "chram",   "No silver weighs against my father's blood. I refuse."),
    ("v_sichar_dog",      "sichar",  "Work, dog!"),
    ("v_puer_blows",      "servant", "No more blows, master!"),
    ("v_chram_roof",      "chram",   "Sichar dead, and not by my hand? Then his roof will pay. Ride!"),
    ("v_judge_oaths",     "judge",   "He who burned houses forfeits half the price. The Church pays the rest. Swear the oaths!"),
    ("v_sichar_swear",    "sichar",  "I swear it."),
    ("v_chram_swear",     "chram",   "And I."),
    ("v_sichar_cup",      "sichar",  "Brother! Another cup!"),
    ("v_chram_friend",    "chram",   "For you, sweet friend — always."),
    ("v_sichar_boast",    "sichar",  "Thank me, sweet brother! I slew your kin — and the gold for it fills this very house!"),
    ("v_chram_heart",     "chram",   "Avenge them… or be called a weak woman."),
    ("v_chram_beg",       "chram",   "I beg my life, O glorious king! They slew my kin and stripped my house!"),
    ("v_king_gone",       "king",    "The queen held Sichar in her word. Get you gone — and prove your cause."),
]

ok = fail = skip = 0
for key, who, text in LINES:
    path = OUT / f"{key}.mp3"
    if path.exists() and path.stat().st_size > 1000:
        print(f"skip {key}"); skip += 1; continue
    body = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.75, "style": 0.35},
    }).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICES[who]}",
        data=body, method="POST",
        headers={"xi-api-key": KEY, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if data[:2] in (b"ID", b"\xff\xfb") or data[:3] == b"ID3" or len(data) > 4000:
            path.write_bytes(data)
            print(f"ok   {key} ({len(data)//1024} KB)"); ok += 1
        else:
            print(f"FAIL {key}: unexpected payload {data[:80]!r}"); fail += 1
    except urllib.error.HTTPError as e:
        print(f"FAIL {key}: HTTP {e.code} {e.read()[:200]!r}"); fail += 1

print(f"done: {ok} generated, {skip} skipped, {fail} failed")
sys.exit(1 if fail else 0)
