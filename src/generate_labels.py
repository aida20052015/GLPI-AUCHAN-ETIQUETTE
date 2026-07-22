from barcode import Code128
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm
import os


# dossier de sortie
OUTPUT = "output"

os.makedirs(OUTPUT, exist_ok=True)


# Exemple matériel GLPI
asset = {
    "id": 1,
    "name": "DESKTOP-2EJRKV0",
    "serial": "MP2497H7"
}


# Code interne de l'étiquette
code = f"GLPI-{asset['id']}"


print("Création :", code)


# Génération code barre
barcode_path = Code128(
    code,
    writer=ImageWriter()
).save(
    f"{OUTPUT}/{code}"
)


print("Code barre créé")


# Création PDF
pdf = f"{OUTPUT}/{code}.pdf"

c = canvas.Canvas(
    pdf,
    pagesize=(70*mm,40*mm)
)


c.setFont(
    "Helvetica-Bold",
    10
)

c.drawString(
    10*mm,
    30*mm,
    "AUCHAN SENEGAL"
)


c.drawString(
    10*mm,
    22*mm,
    asset["name"]
)


c.drawString(
    10*mm,
    15*mm,
    asset["serial"]
)


c.drawImage(
    barcode_path,
    10*mm,
    2*mm,
    width=50*mm,
    height=10*mm
)


c.save()


print("PDF créé :", pdf)