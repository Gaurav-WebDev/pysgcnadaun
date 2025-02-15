import qrcode

data = input("Enter your text or url to generate a qr code :")
qr = qrcode.make(data)
qr.save("qrcode.png")

print("Info : your qr code save as qrcode")