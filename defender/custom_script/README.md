# Static Suspicious PDF Scanner
**Script Python** che esegue una **scansione statica di PDF** alla ricerca di keyword tipicamente associate a comportamenti sospetti o potenzialmente malevoli (es. JavaScript embedded, azioni automatiche, file eseguibili incorporati, etc.).
Lo script è pensato per una **prima analisi veloce** di file PDF.

## Descrizione
Cosa fa lo script:

1. **Apre il PDF in modalità binaria**
2. **Conta le occorrenze di keyword sospette** (es. `/JavaScript`, `/Launch`, `/EmbeddedFile`, ecc.)
3. **Stampa un report compatto** indicando quali keyword sono state rilevate e quante volte compaiono
4. Se **nessuna keyword sospetta viene trovata**, avverte che il PDF sembra "pulito" secondo questa analisi preliminare

## Requisiti
* **Python 3.x**
* Nessuna dipendenza esterna: solo moduli standard (`os`, `re`, `sys`)

## Utilizzo

1. **Clona il repository o copia lo script in una cartella**
2. **Esegui la scansione su un file PDF**:

   ```bash
   python3 run.py /path/to/file.pdf
   ```

## Output
* Se **nessuna keyword sospetta** viene trovata:

  ```
  [*] Scansione PDF sospetto: test.pdf

  Nessuna keyword sospetta trovata. Il PDF sembra “pulito” (da prima analisi statica).
  ```
* Se **vengono trovate keyword sospette**:

  ```
  [*] Scansione PDF sospetto: sample_malicious.pdf

  Keyword sospette rilevate:
    /JavaScript      → 2 occorrenze
    /OpenAction      → 1 occorrenze
    /EmbeddedFile    → 1 occorrenze
  ```

## Keyword monitorate

Lo script cerca queste keyword note nel file PDF (case sensitive, a livello binario):

* `/JavaScript`
* `/JS`
* `/OpenAction`
* `/AA`
* `/Annot`
* `/Launch`
* `/EmbeddedFile`
* `/RichMedia`
* `/XFA`

*(Puoi modificarle aggiungendo/rimuovendo voci dalla variabile `SUSPICIOUS_KEYWORDS` in cima allo script)*

## Note tecniche
* **Analisi statica**: la scansione si limita a cercare pattern noti nel file; non apre/decodifica stream o oggetti compressi.
* **False negativi/positivi**: la presenza di keyword è solo un **indicatore**, non la prova definitiva di un PDF malevolo.
  **Per analisi approfondite, combinare con altri strumenti** (QuickSand, VirusTotal, sandbox dinamiche, ecc).
* **Portabilità**: gira su qualsiasi sistema con Python 3 (Linux, Windows, Mac).

## Disclaimer

Lo script è fornito **a scopo didattico, di laboratorio o per test rapidi**.
Non garantisce di rilevare tutte le minacce reali né sostituisce l’analisi professionale.
