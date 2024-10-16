import qrcode

# Génération du code QR qui redirige vers l'application Flask (URL à adapter selon le déploiement)
url = "http://192.168.1.4:5001/"
qr = qrcode.make(url)
qr.save("qr_code.png")
