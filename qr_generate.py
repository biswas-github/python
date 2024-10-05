import qrcode
name=input("enter your name : \t")
img = qrcode.make(name)
type(img)  # qrcode.image.pil.PilImage
img.save(f"{name}.png")