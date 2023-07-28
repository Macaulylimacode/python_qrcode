import qrcode
# Crie um objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# Adicione o texto ao código QR
qr.add_data(f"https://www.linkedin.com/in/macauly-lima-75984a269")

# Gere o código QR como uma imagem
qr.make_image(fill="black", back_color="white").save("qr_code.png")
print("fim")