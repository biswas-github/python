import qrcode
name=input("Enter your name ")
phone=input("enter the phone no")
details=[name,phone]
img = qrcode.make(details)
type(img)  # qrcode.image.pil.PilImage
img.save("DETAILS.png")