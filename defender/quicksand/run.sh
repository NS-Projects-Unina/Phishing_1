#!/usr/bin/env bash

# Usage: ./quicksand.sh /path/to/file.pdf

PDF="$1"
if [[ -z "$PDF" || ! -f "$PDF" ]]; then
  echo "Usage: $0 <path_to_pdf>"
  exit 1
fi

OUTPUT=$(quicksand -f json "$PDF") || {
  echo "Errore nell'esecuzione di quicksand"
  exit 1
}

# Estrai e mostra i campi chiave con jq
echo
echo "=== PDF Analysis Report ==="
echo "File: $PDF"
echo "MD5:    $(echo "$OUTPUT" | jq -r '.md5')"
echo "SHA1:   $(echo "$OUTPUT" | jq -r '.sha1')"
echo "SHA256: $(echo "$OUTPUT" | jq -r '.sha256')"
echo
echo "Risk level: $(echo "$OUTPUT" | jq -r '.risk')"
echo "Score:      $(echo "$OUTPUT" | jq -r '.score')"
echo "Warnings:   $(echo "$OUTPUT" | jq -r '.warning')"
echo "Exploits:   $(echo "$OUTPUT" | jq -r '.exploit')"
echo

echo "=== Dettagli delle regole scattate ==="
echo "$OUTPUT" \
  | jq -r '.results.root[] | "• \(.desc) (\(.rule))"'

echo
