# required to install two py libraries: qrcode and pillow
import os
from PIL import Image
import qrcode

def generate_qr():
    text = input('Enter the text/URL: ').strip()
    if not text:
        print('Error: No name provided')
        return

    filename = input('Enter the filename (.png/.jpg/.jpeg): ')
    filename = filename + '.jpg'        # default .jpg 
    qr = qrcode.QRCode(box_size = 10, border = 4)

    qr.add_data(text)
    image = qr.make_image(fill_color = 'black', back_color = 'white')
    image.save(filename)
    print(f'QR Code is generated successfully {filename}')
    
if __name__ == "__main__":
    generate_qr()
