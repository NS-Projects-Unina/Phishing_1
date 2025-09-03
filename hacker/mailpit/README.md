# Mailpit Automation Script
Script Bash per **installare, configurare e avviare rapidamente [Mailpit](https://github.com/axllent/mailpit)**, uno strumento open source per il testing e la cattura di email (mailcatcher) con supporto SMTP, interfaccia web e POP3.

## Descrizione
Lo script esegue in automatico:

1. **Download e installazione di Mailpit** nell’ultima versione stabile (personalizzabile tramite variabile).
2. **Preparazione dell’autenticazione POP3**, creando un file credenziali (`auth.txt`).
3. **Avvio di Mailpit** con:

   * server SMTP su `:1025`
   * interfaccia web su `:8025`
   * server POP3 su `:1110` (con autenticazione base)
   * parametri completamente personalizzabili all’inizio dello script

## Requisiti
* **Linux o macOS**
* **wget**
* **sudo** (per installare Mailpit in `/usr/local/bin`)

## Utilizzo
1. **Clona il repository o copia lo script in una directory.**

2. **Modifica i parametri** in testa allo script secondo necessità:

   * `VERSION`: versione di Mailpit da installare
   * `BIN_DIR`: directory in cui installare l’eseguibile
   * `SMTP_PORT`, `HTTP_PORT`, `POP3_PORT`: porte di ascolto
   * `AUTH_USER`, `AUTH_PASS`: credenziali per POP3

3. **Rendi lo script eseguibile:**

   ```bash
   chmod +x run.sh
   ```

4. **Esegui lo script:**

   ```bash
   ./run.sh
   ```

5. **Interfaccia Web:**
   Accedi a [http://localhost:8025](http://localhost:8025) per visualizzare e gestire le email ricevute via SMTP.

6. **Accesso POP3:**
   Collegati su `localhost:1110` usando le credenziali specificate (`auth.txt`).

## Esempio di Output

```bash
📥 Scarico Mailpit v1.27.0...
Mailpit installato in /usr/local/bin/mailpit
File di autenticazione creato in ./auth.txt
Avvio Mailpit:
   • SMTP  -> porta :1025
   • HTTP  -> porta :8025
   • POP3  -> porta :1110
```

## Disclaimer
Script fornito **solo a scopo didattico o di test**.
Non usare in ambienti di produzione senza opportuni controlli di sicurezza.
