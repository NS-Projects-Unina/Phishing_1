# Custom Reverse Shell Detector (Windows, PowerShell)
**Script PowerShell** che monitora in tempo reale le connessioni di rete attive sulla macchina Windows e rileva potenziali **reverse shell** (es. Meterpreter, Netcat, ecc.) in base alle porte di destinazione e al nome del processo.
**Ideale per laboratori, simulazioni di attacco/difesa, esercitazioni di awareness o contesto forense.**

## Descrizione
Lo script effettua un monitoraggio ciclico delle connessioni TCP stabilite verso un set di porte “sospette” (configurabili) e identifica i processi coinvolti, con la possibilità di:

* **Escludere processi di sistema/benigni** (es. explorer.exe, svchost.exe)
* **Loggare automaticamente** tutte le connessioni sospette in un file CSV consultabile successivamente
* **Terminare automaticamente** i processi sospetti (“AutoKill”) su richiesta dell’utente
* **Configurare intervallo di scansione, porte e percorso log** direttamente da parametro/script

## Requisiti

* **Windows 10/11** (o Windows Server recenti)
* **PowerShell 5.x o superiore** (integrato nei sistemi moderni)
* **Permessi amministrativi** (necessari per vedere tutti i processi e terminarli)

## Utilizzo

1. **Scarica lo script** (es. `ReverseShellDetector.ps1`)
2. *(Facoltativo) Personalizza parametri all’inizio dello script*:

   * `$ExcludedProcesses`: elenco processi da ignorare
   * `$WatchPorts`: porte di destinazione sospette (default: 4444, 5555, 6666)
   * `$LogPath`: percorso file CSV di log
   * `$IntervalSeconds`: intervallo tra una scansione e l’altra
3. **Avvia PowerShell come amministratore** *(necessario per vedere tutti i processi)*
4. **Esegui lo script**:

   ```powershell
   .\run.ps1
   ```
5. **All’avvio** ti verrà chiesto se vuoi abilitare l’**AutoKill**:

   * S/N (Sì/No)
   * Se abilitato, i processi sospetti saranno automaticamente terminati

## Esempio di Output

```
Vuoi abilitare l'autokill dei processi sospetti? (S/N)
AutoKill abilitato: i processi sospetti verranno terminati.
Avvio monitoraggio reverse shell. Controllo ogni 10 secondi...

[ALERT] cmd.exe PID 4521 connesso a 192.168.56.1:4444
Trovate 1 connessioni sospette. Log aggiornato in C:\Logs\ReverseShellDetection.csv.

[KILLED] cmd.exe PID 4521
```

## Disclaimer

Lo script è fornito **a solo scopo didattico, di test o di awareness in ambiente controllato**.
**Non è un sostituto di un IDS/IPS professionale**.
Utilizzare solo con autorizzazione e consapevolezza, soprattutto in ambienti condivisi.
