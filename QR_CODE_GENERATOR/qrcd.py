import qrcode
from PIL import Image

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=1,

)

qr.add_data(input("enter URl: "))
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="yellow")
img.save("qrcode.png")