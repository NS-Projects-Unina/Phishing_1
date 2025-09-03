# Gophish Automation Script
Script Python che **automatizza la creazione di una campagna di phishing simulata tramite le API di [Gophish](https://getgophish.com/)**, incluso un template email con **allegato PDF**, landing page, SMTP profile, gruppo destinatari e avvio della campagna.
Pensato per **ambiente di laboratorio, ricerca o simulazioni** etiche.

## Descrizione
Lo script automatizza i seguenti step:

1. **Connessione all’API di Gophish** (locale o remota, tramite API key).
2. **Caricamento e codifica base64 di un allegato PDF** (es. PDF malevolo).
3. **Creazione di un template email** con contenuto HTML personalizzato e allegato.
4. **Creazione di una landing page** fittizia, con cattura credenziali e redirect.
5. **Configurazione di un profilo SMTP** (può essere Mailpit in ascolto su `127.0.0.1:1025`).
6. **Creazione di un gruppo destinatari** (esempio singolo utente, ma facilmente estendibile).
7. **Avvio di una campagna** che invia immediatamente le email di phishing secondo il template, verso i destinatari e utilizzando il profilo SMTP specificato.

## Requisiti

* **Python 3.6+**
* **Librerie**: vedi i requirements
* **PDF** da allegare (tipicamente creato con Metasploit)
* Opzionalmente: **Mailpit** o un altro SMTP catcher per testare l’invio

## Utilizzo
1. **Copia lo script in una directory di lavoro.**
2. **Installa le librerie necessarie**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Configura i parametri principali** nello script:

   * `api_key`: la tua Gophish API key (`Settings > API Key` nell’interfaccia di Gophish)
   * `host`: indirizzo dell’istanza Gophish (default `https://127.0.0.1:3333`)
   * **SMTP profile:** verifica che la porta e la mail mittente siano corretti
   * Sostituisci o aggiungi destinatari reali in laboratorio nel gruppo
   * Aggiorna il path e il nome del file PDF da allegare, se necessario
4. **Esegui lo script**:

   ```bash
   python3 run.py
   ```
5. **Monitora la campagna**: accedi alla dashboard di Gophish per visualizzare risultati e tracking delle email.

## Esempio di Output

```bash
Template creato con ID: 8
Campagna lanciata con ID: 5
```

## Parametri personalizzabili

* **Template email**: puoi modificare sia l’HTML che il nome/subject direttamente nello script.
* **Landing Page**: sostituisci l’HTML o l’URL di redirect per i tuoi test.
* **SMTP**: puoi configurare un altro relay se necessario.
* **Gruppo destinatari**: aggiungi o rimuovi target a piacere.

## Disclaimer

Questo script è fornito **esclusivamente per scopi didattici, di test o ricerca in ambienti controllati**.
Non utilizzarlo mai senza autorizzazione su target reali.
**Gli autori non si assumono alcuna responsabilità per usi non etici o danni.**
