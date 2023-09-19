import qrcode

def generate_qrcode(link):
  """Generates a QR code for the given link.

  Args:
    link: The link to generate the QR code for.

  Returns:
    A QR code image as a PIL Image object.
  """

  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(link)
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")
  return img

# Get the link from the user.
link = input("Enter the link to generate the QR code for: ")

# Generate the QR code.
qr_code_image = generate_qrcode(link)

# Save the QR code to a PNG file.
qr_code_image.save("qr_code.png")

# Print a message to the user.
print("The QR code has been saved to the file qr_code.png.")
