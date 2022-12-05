import qrcode
def faireQrCode(data, nomFichierSortie):
    qr = qrcode.QRCode(version=1,box_size=15,border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    if ".png" not in nomFichierSortie:
        nomFichierSortie = nomFichierSortie + ".png"
    img.save(nomFichierSortie)
    return img
#exemple 
faireQrCode("https://www.youtube.com/watch?v=QH2-TGUlwu4", "qrCode")