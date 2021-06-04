from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageColor

def Datos():
    im = Image.open("MC_Link.png")
    print(im.filename,im.palette,im.format, im.size, im.mode)
    im.show()
    im.save('MC_Link.png')

def Rotar():
    imageObject = Image.open("MC_Link.png")
    imageObject.show()
    hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
    hori_flippedImage.show()
    vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
    vert_flippedImage.show()
    degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
    degree_flippedImage.show()

def Thumbnail():
    try:
        image = Image.open('MC_Link.png')
        image.thumbnail((90,90))
        image.save('Testeos/thumbnail.png')
        image1 = Image.open('Testeos/thumbnail.png')
        image1.show()
    except IOError:
        pass

def Mezclar_colores():
    image = Image.open("MC_Link.png")
    r, g, b, a = image.split()
    image.show()
    image = Image.merge("RGBA", (r, b, g, a))
    image.save('Testeos/MC_Link1.png')
    image.show()
    image = Image.merge("RGBA", (g, r, b, a))
    image.save('Testeos/MC_Link2.png')
    image.show()
    image = Image.merge("RGBA", (g, b, r, a))
    image.save('Testeos/MC_Link3.png')
    image.show()
    image = Image.merge("RGBA", (b, r, g, a))
    image.save('Testeos/MC_Link4.png')
    image.show()
    image = Image.merge("RGBA", (b, g, r, a))
    image.save('Testeos/MC_Link5.png')
    image.show()

def Collage():
    image1 = Image.open('MC_Link.png')
    image1.show()
    image2 = Image.open('Testeos/MC_Link1.png')
    image2.show()
    image3 = Image.open('Testeos/MC_Link2.png')
    image3.show()
    image4 = Image.open('Testeos/MC_Link3.png')
    image4.show()
    image5 = Image.open('Testeos/MC_Link4.png')
    image5.show()
    image6 = Image.open('Testeos/MC_Link5.png')
    image6.show()
    #image1 = image1.resize((400, 400))
    image1_size = image1.size
    new_image = Image.new('RGBA',(3*image1_size[0], 2*image1_size[1]), (250,250,250,1))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    new_image.paste(image3,(2*image1_size[0],0))
    new_image.paste(image4,(0,image1_size[1]))
    new_image.paste(image5,(image1_size[0],image1_size[1]))
    new_image.paste(image6,(2*image1_size[0],image1_size[1]))
    new_image.save("Testeos/merged_image.png")
    new_image.show()

def Blur():
    #ImageFilter
    OriImage = Image.open('MC_Link.png')
    OriImage.show()

    blurImage = OriImage.filter(ImageFilter.BLUR)
    blurImage.show()
    blurImage.save('Testeos/blur.png')

    boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
    boxImage.show()
    boxImage.save('Testeos/boxblur.png')

    gaussImage = OriImage.filter(ImageFilter.GaussianBlur(10))
    gaussImage.show()
    gaussImage.save('Testeos/gaussblur.png')

def Crop():
    im = Image.open('MC_Link.png')
    im.show()
    cropped = im.crop((0,0,200,400))
    cropped.show()
    cropped.save('Testeos/cropped.png')

def Resize():
    im = Image.open("MC_Link.png")
    im.show()
    resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
    resized_im.show()
    resized_im.save('Testeos/resized.png')

def Watermark():
    #ImageDraw, ImageFont
    im = Image.open('MC_Link.png')
    width, height = im.size
    draw = ImageDraw.Draw(im)
    text = "Excelsior"
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)
    #margin = 10
    #x = width - textwidth - margin
    #y = height - textheight - margin
    draw.text((135, 250), text, font=font, fill=(255, 114, 0, 255))
    im.show()
    im.save('Testeos/watermark.png')

def Filter():
    #ImageFilter
    from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
    )

    img = Image.open('Maine_Coon.jpg')
    img.show()
    img1 = img.filter(BLUR)
    img1.save('Testeos/ImageFilter_BLUR.jpg')
    img1.show()
    img2 = img.filter(CONTOUR)
    img2.save('Testeos/ImageFilter_CONTOUR.jpg')
    img2.show()
    img3 = img.filter(DETAIL)
    img3.save('Testeos/ImageFilter_DETAIL.jpg')
    img3.show()
    img4 = img.filter(EDGE_ENHANCE)
    img4.save('Testeos/ImageFilter_EDGE_ENHANCE.jpg')
    img4.show()
    img5 = img.filter(EDGE_ENHANCE_MORE)
    img5.save('Testeos/ImageFilter_EDGE_ENHANCE_MORE.jpg')
    img5.show()
    img6 = img.filter(EMBOSS)
    img6.save('Testeos/ImageFilter_EMBOSS.jpg')
    img6.show()
    img7 = img.filter(FIND_EDGES)
    img7.save('Testeos/ImageFilter_FIND_EDGES.jpg')
    img7.show()
    img8 = img.filter(SMOOTH)
    img8.save('Testeos/ImageFilter_SMOOTH.jpg')
    img8.show()
    img9 = img.filter(SMOOTH_MORE)
    img9.save('Testeos/ImageFilter_SMOOTH_MORE.jpg')
    img9.show()
    img10 = img.filter(SHARPEN)
    img10.save('Testeos/ImageFilter_SHARPEN.jpg')
    img10.show()

def Colores():
    #ImageColor
    img = ImageColor.getrgb("blue")
    print(img)
    img1 = ImageColor.getrgb("purple")
    print(img1)
    img = Image.new("RGB", (256, 256), ImageColor.getrgb("#add8e6"))
    img.show()
    
opcion = 0

print('''1) Conseguir datos de una imagen 
    2) Rotar una imagen
    3) Crear una thumbnail en base a una imagen
    4) Mezclar los colores de una imagen
    5) Hacer un collage de la opcion 4
    6) Blurear una imagen
    7) Cortar una imagen
    8) Cambiar el tamaño de una imagen
    9) Generar una marca de agua sobre una imagen
    10) Aplicar filtros sobre una imagen
    11) Obtener colores
    12) Salir del programa''')

while opcion != 12:
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        Datos()
    elif opcion == 2:
        Rotar()
    elif opcion == 3:
        Thumbnail()
    elif opcion == 4:
        Mezclar_colores()
    elif opcion == 5:
        Collage()
    elif opcion == 6:
        Blur()
    elif opcion == 7:
        Crop()
    elif opcion == 8:
        Resize()
    elif opcion == 9:
        Watermark()
    elif opcion == 10:
        Filter()
    elif opcion == 11:
        Colores()
    elif opcion == 12:
        break
    else:
        print("No ingreso una opcion valida")