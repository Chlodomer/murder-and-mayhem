#!/bin/bash
# Generates the simulation's sound effects with the ElevenLabs sound-generation API.
# Usage: ELEVENLABS_API_KEY=sk_... bash sfx/generate.sh
cd "$(dirname "$0")"
gen() {
  local file="$1" dur="$2" prompt="$3"
  if [ -s "$file" ]; then echo "skip $file (exists)"; return; fi
  echo "generating $file ..."
  curl -sS -X POST "https://api.elevenlabs.io/v1/sound-generation" \
    -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
    -d "{\"text\": \"$prompt\", \"duration_seconds\": $dur, \"prompt_influence\": 0.4}" \
    -o "$file"
  # API errors come back as JSON, not mp3 — drop those
  if file "$file" | grep -qi 'json\|ascii'; then echo "  ERROR: $(cat "$file" | head -c 200)"; rm -f "$file"; fi
}
gen bell.mp3 3.5 "A single deep medieval church bell toll from an old bronze bell in a village stone tower, natural reverb tail, no music"
gen clang.mp3 1.2 "Short metallic sword clash, two steel blades striking once, medieval combat, dry, no music"
gen thud.mp3 1.0 "A heavy soft thud of a body collapsing onto packed earth, short, no music"
gen whoosh.mp3 0.8 "Quick short whoosh of a sheet of parchment paper being thrown, no music"
gen coin.mp3 1.2 "Brief jingle of silver coins dropped into a leather pouch, no music"
gen fire_loop.mp3 8 "Seamless loop of a large crackling wood fire burning a thatched roof house, steady crackle, no music"
gen wind_loop.mp3 10 "Seamless loop of soft cold winter wind blowing over open fields, gentle, no music"
gen rain_loop.mp3 10 "Seamless loop of steady rainfall falling on grass and wooden rooftops, no thunder, no music"
gen crickets_loop.mp3 10 "Seamless loop of quiet night crickets chirping in a rural meadow, sparse, no music"
gen birds_loop.mp3 10 "Seamless loop of sparse countryside songbirds chirping in distant trees, peaceful morning, no music"
gen gallop_loop.mp3 6 "Seamless loop of two horses galloping on a packed dirt road, rhythmic hoofbeats, no music"
echo "done"
