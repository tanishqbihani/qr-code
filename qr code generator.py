# The data you want to encode in the QR code
import qrcode
data = "https://the-gamers-paradise.business.site/?utm_source=gmb&utm_medium=referral"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
# Create an image with black QR code and white background
image_path = "tanishq.jpg"
# Specify the path and filename for the image
img.save(image_path)

