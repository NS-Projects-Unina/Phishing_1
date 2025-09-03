# VirusTotal PDF Analyzer
Script Python per **analizzare file PDF (o altri file) tramite le API di [VirusTotal](https://www.virustotal.com/)**.
Permette di controllare rapidamente se un file è già noto, inviarlo per l’analisi e stampare un report dettagliato dei risultati, direttamente da terminale.
**Utile in laboratorio, per progetti di sicurezza o analisi forense di file sospetti.**

## Descrizione
Lo script esegue in automatico:

1. Calcola l’hash SHA256 del file fornito.
2. Cerca il file su VirusTotal usando la chiave API (API key).
3. Se il file **è già noto** a VirusTotal, recupera il report esistente.
4. Se il file **non è presente**, lo carica automaticamente su VirusTotal e attende la fine dell’analisi.
5. Stampa un report dettagliato con i risultati delle varie engine antivirus.

Il tutto **direttamente da linea di comando**.

## Requisiti
* **Python 3.7+**
* **Libreria [vt-py](https://github.com/VirusTotal/vt-py)**
  
  - Installa con:

    ```bash
    pip install vt-py
    ```
* **Chiave API di VirusTotal** (gratuita o commerciale)
  
  - [Vedi qui](https://www.virustotal.com/gui/join-us).

## Installazione
1. **Clona il repository o copia lo script.**
2. **Installa le dipendenze:**

   ```bash
   pip install vt-py
   ```

   *(opzionale ma consigliato: usa un ambiente virtuale)*
3. **Esporta la chiave API** nell’ambiente:

   ```bash
   export VT_API_KEY="la_tua_api_key"
   ```

## Utilizzo

```bash
python3 run.py <file.pdf>
```

Ad esempio:

```bash
python3 run.py offerta_lavorativa_automation.pdf
```

## Output
Lo script stampa:

* L’hash SHA256 del file
* Lo stato del file su VirusTotal (già noto o appena caricato)
* Una **tabella riassuntiva** dei motori antivirus che hanno rilevato il file come sospetto/malevolo
* Il **link diretto al report su VirusTotal**
* Numero di rilevazioni (Malicious, Suspicious, Harmless, etc.)

## Esempio di Output

```
SHA256: 2a1b...e6fc
[*] Using existing analysis

=== REPORT for 2a1b...e6fc ===
Detection stats:
  Harmless       : 63
  Malicious      : 12
  Suspicious     : 3
  Undetected     : 45

Permalink: https://www.virustotal.com/gui/file/2a1b...e6fc/detection

Engines flags:
  • Avast: malicious
  • BitDefender: malicious
  • ESET-NOD32: suspicious
  ...
```

## Disclaimer
Lo script è pensato per **scopi didattici, di laboratorio o ricerca**.
Non abusare delle API VirusTotal (rispettare i limiti e le condizioni d’uso).
**Gli autori non si assumono responsabilità per usi non autorizzati o danni.**
