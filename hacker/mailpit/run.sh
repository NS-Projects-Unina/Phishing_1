#!/usr/bin/env bash
set -euo pipefail

# Parametri
VERSION="v1.27.0" # latest al momento della creazione
BIN_DIR="/usr/local/bin"
MAILPIT_BIN="${BIN_DIR}/mailpit"
DOWNLOAD_URL="https://github.com/axllent/mailpit/releases/download/${VERSION}/mailpit-linux-amd64.tar.gz"
SMTP_PORT=":1025"
HTTP_PORT=":8025"
POP3_PORT=":1110"
# auth per accesso POP3
AUTH_FILE="./auth.txt"
AUTH_USER="antonio.rossi"
AUTH_PASS="pass123"

# 1) Scarica e installa Mailpit se non già presente
if ! command -v mailpit &>/dev/null || [[ ! -x "${MAILPIT_BIN}" ]]; then
  echo "📥 Scarico Mailpit ${VERSION}..."
  wget -qO mailpit.tar.gz "${DOWNLOAD_URL}"
  tar xzf mailpit.tar.gz
  sudo mv mailpit "${MAILPIT_BIN}"
  sudo chmod +x "${MAILPIT_BIN}"
  rm mailpit.tar.gz
  echo "Mailpit installato in ${MAILPIT_BIN}"
else
  echo "Mailpit già installato"
fi

# 2) Prepara il file di autenticazione POP3
cat > "${AUTH_FILE}" <<EOF
${AUTH_USER}:${AUTH_PASS}
EOF
echo "File di autenticazione creato in ${AUTH_FILE}"

# 3) Avvia Mailpit con SMTP, HTTP e POP3
echo "Avvio Mailpit:"
echo "   • SMTP  -> porta ${SMTP_PORT}"
echo "   • HTTP  -> porta ${HTTP_PORT}"
echo "   • POP3  -> porta ${POP3_PORT}"
exec "${MAILPIT_BIN}" \
  --smtp "${SMTP_PORT}" \
  --listen "${HTTP_PORT}" \
  --pop3 "${POP3_PORT}" \
  --pop3-auth-file "${AUTH_FILE}"
