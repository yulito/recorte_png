from PIL import Image

# altura y anchura del cuadrado
w=50
h=50
#posicion (irá cambiando con cada iteración)
y=0
x=0
#conteo para el ciclo
count=0

img = Image.open("img.png")

def fin():
    print("Proceso finalizado!")

def cuartaLinea(y,x,w,h,count,img):
    while count < 32:
        img_recortada = img.crop(box = (x,y,w+x,h))
        img_recortada.save("img_"+str(count)+".png")
        x += 50
        count += 1
    fin()
    
def terceraLinea(y,x,w,h,count,img):
    while count < 24:
        img_recortada = img.crop(box = (x,y,w+x,h))
        img_recortada.save("img_"+str(count)+".png")
        x += 50
        count += 1
    x=0
    y=150
    h=200
    #count=0
    cuartaLinea(y,x,w,h,count,img)
    
def segundaLinea(y,x,w,h,count,img):
    while count < 16:
        img_recortada = img.crop(box = (x,y,w+x,h))
        img_recortada.save("img_"+str(count)+".png")
        x += 50
        count += 1
    x=0
    y=100
    h=150
    #count=0
    terceraLinea(y,x,w,h,count,img)
    
def primeraLinea(x,y,w,h,count,img):    
    while count < 8:
        img_recortada = img.crop(box = (x,y,w+x,h))
        img_recortada.save("img_"+str(count)+".png")
        x += 50
        count += 1
    x=0
    y=50
    h=100
    #count=0
    segundaLinea(y,x,w,h,count,img)

primeraLinea(y,x,w,h,count,img)


#################################
### forma resumida
#################################
##img = Image.open("x.png")
###( izquierda, arriba, width, height )
##img_recortada = img.crop(box = (0,50,50,100))
###img_recortada.show()
##
##img_recortada.save("x_copia.png")#p1x....png
