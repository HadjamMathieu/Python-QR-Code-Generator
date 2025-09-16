import qrcode
import os

def genererqr(link, filename="qrcode.png"):
    if not filename.lower().endswith(".png"):
        filename += ".png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code généré et sauvegardé ici : {os.path.abspath(filename)}")

if __name__ == "__main__":
    link = input("Entrez le lien de redirection : ").strip()
    filename = input("Nom du fichier, sans extension : ").strip()

    if not filename:
        filename = "qrcode.png"

    genererqr(link, filename)
