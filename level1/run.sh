#!/bin/sh
set -eu

# Generate a random one-time flag where the server expects it
FLAG_PATH="${FLAG_PATH:-/home/ctf/flag.txt}"
if [ ! -f "$FLAG_PATH" ]; then
  RAND=$(python3 -c "import secrets;print(secrets.token_hex(16))")
  mkdir -p "$(dirname "$FLAG_PATH")"
  echo "flag{dhke_lvl1_${RAND}}" > "$FLAG_PATH"
  chmod 600 "$FLAG_PATH"
fi

exec python3 /app/server.py

