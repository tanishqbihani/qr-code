import qrcode
import PIL.Image

# Load the image of the Python QR code
img = PIL.Image.open('maths.jpg')
data = "https://drive.google.com/drive/folders/1_GYqfLM0dajaLwbQr_DGds9b2nWOB5_O?usp=drive_link"
qr = qrcode.QRCode(version=1, box_size=10, border=15)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="cyan", back_color="black")

# Load the image of the logo
logo = PIL.Image.open('maths.jpg')

# Resize the logo so that it is smaller than the QR code
logo = logo.resize((80, 80))

# Paste the logo into the center of the QR code
img.paste(logo, (300, 300))

# Save the image
img.save('maths.jpg')

