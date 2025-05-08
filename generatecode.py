import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)

# qr.add_data("https://www.youtube.com/")
qr.add_data("https://github.com/SHREYA311220")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode1.png")