import qrcode

data = "https://www.google.com"

qr = qrcode.make(data)
qr.save("my_qr_code.png")
print("QR code generated successfully!")
