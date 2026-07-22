from get_assets import get_assets
from barcode import Code128
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm
import os


def generate_inventory_number(asset_type, asset_id):

    prefixes = {
        "Computer": "PC",
        "Monitor": "MON",
        "Printer": "IMP",
        "Phone": "TEL",
        "Mobilier": "MOB",
        "Electromenager": "ELEC"
    }

    prefix = prefixes.get(asset_type, "MAT")

    return f"AUCH-{prefix}-{asset_id:05d}"



OUTPUT = "output"

os.makedirs(OUTPUT, exist_ok=True)


assets = get_assets()
for asset in assets:
    print(asset["asset_type"], asset["name"])
print("Nombre de matériels :", len(assets))



for asset in assets:

    asset_id = asset["id"]
    name = asset.get("name", "")
    serial = asset.get("serial", "")


    inventory_number = generate_inventory_number(
        asset["asset_type"],
        asset_id
    )


    code = inventory_number

    print("Création étiquette :", code)


    barcode_file = Code128(
        code,
        writer=ImageWriter()
    ).save(
        f"{OUTPUT}/{code}"
    )


    pdf_file = f"{OUTPUT}/{code}.pdf"


    c = canvas.Canvas(
        pdf_file,
        pagesize=(70*mm,40*mm)
    )


    c.setFont(
        "Helvetica-Bold",
        10
    )


    c.drawString(
        10*mm,
        32*mm,
        "AUCHAN SENEGAL"
    )


    c.drawString(
        10*mm,
        25*mm,
        inventory_number
    )


    c.drawString(
        10*mm,
        19*mm,
        name[:25]
    )


    c.drawString(
        10*mm,
        14*mm,
        f"SN : {serial}"
    )


    c.drawImage(
        barcode_file,
        10*mm,
        2*mm,
        width=50*mm,
        height=10*mm
    )


    c.save()



print("Toutes les étiquettes sont générées")