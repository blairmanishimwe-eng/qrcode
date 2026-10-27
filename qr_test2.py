import qrcode
qr = qrcode.QRCode(version=1, box_size=10,border=5)
qr.add_data("https://google.com")
qr.make(fit=True)

img = qr.make_image(fill_color="#000000")
img.save("my_qr.png")