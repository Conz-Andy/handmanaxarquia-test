# Generate the QR code images at build time (pure text input — nothing to corrupt).
import subprocess, sys
from pathlib import Path

VCARD = """BEGIN:VCARD
VERSION:3.0
N:;Handyman Axarquia;;;
FN:Handyman Axarquia
ORG:Handyman Axarquia
TEL;TYPE=CELL:+34711027432
EMAIL:info@handymanaxarquia.com
URL:https://handymanaxarquia.com
ADR;TYPE=WORK:;;Los Toscanos 33;Almayate Bajo;Malaga;29749;Spain
END:VCARD"""

def ensure(site: Path):
    try:
        import qrcode
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "qrcode"], check=True)
        import qrcode
    (site / "images").mkdir(parents=True, exist_ok=True)
    for data, name in (("https://handymanaxarquia.com", "qr_website.png"), (VCARD, "qr_vcard.png")):
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
        qr.add_data(data)
        qr.make(fit=True)
        qr.make_image(fill_color="black", back_color="white").save(site / "images" / name)
    print("qr codes generated")
