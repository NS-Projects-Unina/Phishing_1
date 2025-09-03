# Metasploit PDF Automation Script
Script bash che automatizza la creazione di un file PDF malevolo sfruttando Metasploit Framework. Lo script permette anche di avviare rapidamente un listener per ricevere la reverse shell.

>⚠️ Attenzione
Questo script è destinato esclusivamente ad attività di test, formazione o ricerca in ambienti controllati.
Non utilizzarlo mai senza esplicito permesso sui sistemi di altri.
L’uso improprio è illegale!

## Descrizione
Lo script offre un semplice menu per:

- Creare un PDF malevolo che sfrutta una vulnerabilità storica di Adobe Reader tramite il modulo `adobe_pdf_embedded_exe` di Metasploit.

- Avviare un listener Metasploit per ricevere la connessione della vittima (reverse shell Meterpreter).

- Eseguire entrambe le azioni in sequenza.

I parametri come indirizzo IP, porta di ascolto, template PDF di partenza e nome del file generato sono configurabili nella parte iniziale dello script.

## Requisiti
- Sistema Linux o macOS

- Metasploit Framework (`msfconsole` deve essere presente nel PATH)

- Un file PDF template legittimo da usare come base (`template_msf.pdf`)

## Utilizzo
1. Clona il repository o copia lo script.

2. Modifica i parametri in testa allo script:

    - LHOST: indirizzo IP dell’attaccante (dove ricevere la shell)

    - LPORT: porta di ascolto (di default 4444)

    - TEMPLATE: percorso al PDF da usare come template

    - OUTPUT: nome del PDF generato

3. Rendi lo script eseguibile:

    ```bash
    chmod +x run.sh
    ```

4. Esegui lo script:

    ```bash
    ./run.sh
    ```

Segui il menu e scegli l’opzione desiderata.

## Esempio di output
```bash
Seleziona un'opzione:
  1) Crea solo il PDF malevolo
  2) Avvia solo il listener
  3) Crea il PDF e poi avvia il listener
Scelta [1-3]: 1
[*] Generazione PDF malevolo...
[*] PDF creato: offerta_lavorativa_automation.pdf
```

## Note tecniche
- Lo script crea temporaneamente un file .rc (resource file) per automatizzare Metasploit in modalità batch.

- Il modulo usato (`adobe_pdf_embedded_exe`) sfrutta una vulnerabilità delle vecchie versioni di Adobe Reader (ad es. CVE-2010-1240).

- Per questioni di etica e sicurezza, NON condividere PDF generati se non strettamente necessario per scopi legali/educativi.

## Disclaimer
Questo script è fornito a solo scopo didattico o di ricerca.
Gli autori non si assumono alcuna responsabilità per usi impropri o danni derivanti dall’uso dello script.