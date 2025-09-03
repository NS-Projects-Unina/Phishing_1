# Spear Phishing Attack & Defense Lab

**Università degli Studi di Napoli Federico II – Progetto di Software Security (A.A. 2024/2025)**

*Studente: Riziero Graziani – Docente: Prof. Simon Pietro Romano*

## Descrizione del Progetto
Questo repository documenta **un laboratorio pratico di Network Security** dedicato allo studio delle campagne di phishing, dalla fase di attacco fino all’implementazione e analisi delle principali tecniche di difesa.
Il progetto dimostra **come un allegato PDF apparentemente innocuo possa essere utilizzato come vettore per eseguire codice malevolo** e stabilire una reverse shell verso l’attaccante, con successiva analisi delle contromisure più efficaci (statiche, dinamiche e di rete).

## Architettura del Laboratorio

* **Attaccante:** Kali Linux VM, utilizzo di strumenti open-source:

  * **Metasploit Framework** (creazione payload e PDF malevolo)
  * **Mailpit** (server SMTP/POP3 locale per recapito email)
  * **GoPhish** (simulazione campagna phishing e gestione invii)
* **Vittima:** Windows VM, configurata per ricevere e aprire email tramite client (Thunderbird), con controllo delle difese lato endpoint.

**Obiettivo:** Indurre la vittima ad aprire un PDF malevolo che apre una reverse shell Meterpreter verso l’attaccante.

## Fasi del Laboratorio

1. **OSINT & Social Engineering:** Raccolta informazioni pubbliche (LinkedIn, Google Dorking, ecc.) per personalizzare l’attacco di spear phishing.
2. **Preparazione Attacco:**

   * Creazione payload con Metasploit (`CVE-2010-1240` su Adobe Reader 9.3.x)
   * Incapsulamento payload in PDF tramite exploit Metasploit
   * Allestimento listener Meterpreter
3. **Consegna Email:**

   * Configurazione GoPhish per invio di campagne email personalizzate
   * Utilizzo di Mailpit come mail server locale per l’invio/recapito in sicurezza
   * Automazione delle campagne tramite API GoPhish
4. **Simulazione Comportamento Vittima:**

   * Scaricamento e apertura dell’allegato PDF
   * Attivazione payload e connessione reverse shell
5. **Contromisure & Difesa:**

   * Analisi statica PDF con QuickSand (YARA rules)
   * Script Python per analisi keyword sospette nei PDF
   * Analisi VirusTotal via API
   * Reverse Shell Detection con PowerShell su Windows
   * Monitoraggio rete e detection con Snort (regole custom)

## Strumenti & Script Inclusi

### **Attacco**

* **Bash script per automazione Metasploit:**
  Genera PDF malevolo e listener in batch.
* **Script di automazione GoPhish (Python):**
  Crea campagne phishing e allega PDF via API.
* **Mailpit automation script (Bash):**
  Installa e avvia Mailpit come SMTP/POP3 server locale.

### **Difesa**

* **QuickSand**: Analisi statica e scoring file PDF tramite YARA rules.
* **Static PDF Keyword Scanner (Python):**
  Cerca keyword sospette nei PDF per una prima analisi veloce.
* **VirusTotal API Scanner (Python):**
  Carica PDF e genera report automatico aggregando i risultati di decine di motori AV.
* **Reverse Shell Detector (PowerShell):**
  Monitora porte sospette e può “killare” automaticamente i processi sospetti su Windows.
* **Snort rules**:
  Esempi di regole personalizzate per detection di reverse shell da Metasploit.

## Struttura del Repository

```
/
├── defender/
│   ├── custom_script/
|   |   ├── README.md
|   |   └── run.py
|   ├── quicksand/
|   |   ├── README.md
|   |   └── run.sh
│   ├── reverse_shell_detector/
|   |   ├── README.md
|   |   └── run.ps1
|   ├── snort/
|   |   └── local.rules
|   └── virustotal/
|   |   ├── README.md
|   |   └── run.py
├── hacker/
│   ├── gophish/
|   |   ├── README.md
|   |   ├── requirements.txt
|   |   └── run.py
|   ├── mailpit/
|   |   ├── README.md
|   |   └── run.sh
|   └── metasploit/
|   |   ├── README.md
|   |   ├── run.sh
|   |   └── template_msf.pdf
├── [Report] NS_Phishing_Project.pdf
├── [Powerpoint] NS_Phishing_Project.pdf
└── README.md
```

## Come eseguire il laboratorio

1. **Clona il repository e installa le dipendenze indicate nei singoli script**.
2. **Configura le VM Attaccante e Vittima** secondo le istruzioni del report PDF.
3. **Segui i passaggi del laboratorio:**

   * Lato attaccante: genera il PDF, avvia la campagna di phishing e il listener.
   * Lato vittima: ricevi l’email, apri l’allegato e verifica il comportamento.
4. **Applica le contromisure:**

   * Analizza il PDF con QuickSand, VirusTotal e script statici.
   * Esegui il Reverse Shell Detector su Windows.
   * Avvia Snort e carica le regole di detection personalizzate.
5. **Consulta il report PDF per dettagli step-by-step, risultati, screenshot e spiegazioni approfondite.**

## Riferimenti Utili

* [Metasploit Framework](https://www.metasploit.com/)
* [Mailpit](https://github.com/axllent/mailpit)
* [GoPhish](https://getgophish.com/)
* [QuickSand](https://github.com/tylabs/quicksand)
* [VirusTotal](https://www.virustotal.com/)
* [Snort](https://www.snort.org/)
* [PDF YARA Rules](https://github.com/tylabs/quicksand/blob/main/src/quicksand/quicksand_pdf.yara)

## ⚠️ Disclaimer

Questo progetto e tutti gli script sono pensati **esclusivamente per uso didattico e di ricerca in ambiente controllato**.
**Non utilizzare queste tecniche contro sistemi o utenti senza autorizzazione.
Gli autori declinano ogni responsabilità per un uso improprio.**

**Per dettagli tecnici, risultati sperimentali, esempi di output e approfondimenti consulta il report PDF incluso (`[Report] NS_Phishing_Project.pdf`).**
