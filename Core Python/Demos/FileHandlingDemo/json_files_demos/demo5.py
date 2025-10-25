# # Install the library first: pip install stdiomask
# import stdiomask

# username = input("Enter username: ")
# password = stdiomask.getpass(prompt="Enter password: ", mask="*")

# print("Username entered: ", username)
# print("Password entered: ", password)

import qrcode

upi_link = (
    "upi://pay?"
    "pa=7775090578@ybl&"
    "pn=YUVRAJ%20RAJENDRAKUMAR%20VARMA&"
    "mc=0000&"
    "mode=02&"
    "purpose=00&"
    "am=15000"
)

# Create a smaller QR version
qr = qrcode.QRCode(
    version=2,   # smaller version (1–40); 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,  # smaller boxes (mainly for image output)
    border=1     # smaller border in terminal
)
qr.add_data(upi_link)
qr.make(fit=True)
qr.print_ascii()  # print to console

