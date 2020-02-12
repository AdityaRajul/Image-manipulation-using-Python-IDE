from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from PIL import ImageFilter,ImageEnhance
from tkinter.font import Font
import sys
import os
import cv2
from tkinter.filedialog import asksaveasfile
import random




def BLUR():
    global img
    im = Image.open(root.filename)
    im1 = im.filter(ImageFilter.BLUR)
    img=im1.filter(ImageFilter.MinFilter(size=3))
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def BLUR1():
    global img
    im = Image.open(root.filename)
    im1 = im.filter(ImageFilter.BLUR)
    img=im1.filter(ImageFilter.MaxFilter(size=3))
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def COLOR():
     global img

     im = Image.open(root.filename)
     color_converter = ImageEnhance.Color(im)
     img= color_converter.enhance(w.get())
     canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
     canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def RESET():
    canvas.image= ImageTk.PhotoImage(my_image.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def BW():
    global img
    print ("hello")
    im = Image.open(root.filename)
    r, g, b = im.split()
    img=g
    canvas.image= ImageTk.PhotoImage(g.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def BW1():
    global img
    print ("hello")
    im = Image.open(root.filename)
    r, g, b = im.split()
    img=g
    canvas.image= ImageTk.PhotoImage(b.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def BW2():
    global img
    print ("hello")
    im = Image.open(root.filename)
    r, g, b = im.split()
    img=g
    canvas.image= ImageTk.PhotoImage(r.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def SATURATION():
    print ("hello")
    global img
    im1 = Image.open(root.filename)
    r1, g1, b1 = im1.split()
    img = Image.merge("RGB",(g1, b1, r1))
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')



def CONTRAST():
    global img
    image = Image.open(root.filename)
    contrast_converter = ImageEnhance.Contrast(image)
    img= contrast_converter.enhance(w.get())

    #image = ImageEnhance.Contrast(image).enhance(10)
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def SAT():
     global img


     im = Image.open(root.filename)
     r1,g1,b1 = im.split()
     img = Image.merge("RGB",(b1, r1, g1))
     canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
     canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def SATUR():
     global img


     im = Image.open(root.filename)
     r1,g1,b1 = im.split()
     img = Image.merge("RGB",(r1, b1, g1))
     canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
     canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def BRIGHT():
     global img
     im = Image.open(root.filename)
     brightness_converter = ImageEnhance.Brightness(img)
     img = brightness_converter.enhance(w.get())
     canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
     canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def SHARP():
     global img
     im = Image.open(root.filename)
     sharpness_converter = ImageEnhance.Sharpness(im)
     img = sharpness_converter.enhance(w.get())
     canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
     canvas.create_image(0, 0, image=canvas.image, anchor='nw')




def SQUARE():
    #flip
    global img
    print ("hello")
    im = Image.open(root.filename)
    img = im.transpose(Image.FLIP_LEFT_RIGHT)
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def SPIN_T():
    global img
    print ("hello")
    im = Image.open(root.filename)
    img = im.transpose(Image.ROTATE_180)
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def SPIN_L():
    print ("hello")
    global img
    im = Image.open(root.filename)
    img= im.transpose(Image.ROTATE_90)
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def SPIN_R():
    print ("hello")
    global img
    im = Image.open(root.filename)
    img= im.transpose(Image.ROTATE_270)
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def RESIZE():
    global img
    print ("hello")
    im = Image.open(root.filename)
    a=textBox1.get("1.0","end-1c")
    b=textBox2.get("1.0","end-1c")
    x=int(a)
    y=int(b)
    img = im.resize((x,y))
    canvas.image= ImageTk.PhotoImage(img.resize((x,y),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    



def MODES():
    global img
    print ("ho")
    global edges
    im = Image.open(root.filename)
    img = im.filter(ImageFilter.FIND_EDGES)
    canvas.image= ImageTk.PhotoImage(img.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

def savefile():

     #files = [('All Files', '*.*'), ('Python Files', '*.py'),('Text Document', '*.txt'),('Image file','*.jpg')]
     #file = asksaveasfile(filetypes = files, defaultextension = files)
     x=random.randint(1,50)
     y=str(x)
     
     filename="newimage"+y+".png"
     img.save(filename)


#-------------------------------------------------------face detection function end---------------------------------

def fd():
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Aditya Chauhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    img = cv2.imread(root.filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(type(faces))
    print(faces)

    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)

    #resized = cv2.resize(img (int(img.shape[1]/2),int(img.shape[0])))

    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#-------------------------------------------------------face detection function end---------------------------------

#------------------------------------------------------------webcam-----------------------------------------------#
def webcam():
    
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Aditya chauhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml') 
    eye_cascade = cv2.CascadeClassifier('C:\\Users\\Aditya chauhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')  
    cap = cv2.VideoCapture(0) 
    while 1:
        ret, img = cap.read()   
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)   
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
  
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
           break
               
    cap.release() 
    cv2.waitkey(0)   
    cv2.destroyAllWindows()  

#---------------------------------------------------------------webcam------------------------------------------#    

root = Tk()
root.title(root)



webcam= Button(root, text = 'WebCam Detection',font = "arial 10 bold underline",width="15",height="2",bg="GREY",command = webcam,fg ='#001dff')
webcam.pack( side = BOTTOM)
webcam.place(x=740,y=530)
blur= Button(root, text = 'BLUR',font = "arial 10 bold underline",width="10",height="2",bg="GREY",command = BLUR,fg ='#001dff')
blur.pack( side = BOTTOM)
blur.place(x=740,y=70)

blur1= Button(root, text = 'BLUR1',font = "arial 10 bold underline",width="10",height="2",bg="GREY",command = BLUR1,fg ='#001dff')
blur1.pack( side = BOTTOM)
blur1.place(x=740,y=130)

contrast= Button(root, text = 'CONTRAST',font = "arial 10 bold underline",width="10",height="2",bg="GREY",command = CONTRAST,fg ='#001dff')
contrast.pack( side = BOTTOM)
contrast.place(x=600,y=580)

BRIGHT= Button(root, text = 'BRIGHTNESS',font = "arial 10 bold underline",width="10",height="2",bg="GREY",command = BRIGHT,fg ='#001dff')
BRIGHT.pack( side = BOTTOM)
BRIGHT.place(x=480,y=580)

SHARP= Button(root, text = 'SHARPNESS',font = "arial 10 bold underline",width="10",height="2",bg="GREY",command = SHARP,fg ='#001dff')
SHARP.pack( side = BOTTOM)
SHARP.place(x=360,y=580)

COLOR= Button(root, text = 'COLOR',font = "arial 10 bold underline",width="10",height="2",bg="GREY",command = COLOR,fg ='#001dff')
COLOR.pack( side = BOTTOM)
COLOR.place(x=240,y=580)

save = Button(root,text="SAVE",font = "arial 12 bold underline",width="10",height="2",bg="GREY", command= lambda : savefile(),fg ='#d10f0f')
save.pack(side=BOTTOM)
save.place(x=780,y=640)

fd = Button(root,text="Face Detection",font = "arial 10 bold underline",width="15",height="2",bg="GREY", command= fd,fg ='#001dff')
fd.pack(side=BOTTOM)
fd.place(x=50,y=530)


blackndwhite= Button(root, text = 'BLack nd White',width="10",bg="GREY",height="2",font = "arial 10 bold underline",fg ='#001dff',command = BW)
blackndwhite.pack( side = BOTTOM)
blackndwhite.place(x=70,y=310)

sat= Button(root, text = 'SATURATION',width="10",height="2",bg="GREY",command = SATURATION,font = "arial 10 bold underline",fg ='#001dff')
sat.pack( side = BOTTOM)
sat.place(x=70,y=250)


resize= Button(root, text = 'FLIP',width="10",height="2",bg="GREY",command = SQUARE,font = "arial 10 bold underline",fg ='#001dff',)
resize.pack( side = BOTTOM)
resize.place(x=740,y=10)

spin= Button(root, text = 'SPIN_R',width="10",height="2",bg="GREY",command = SPIN_R,font = "arial 10 bold underline",fg ='#001dff',)
spin.pack( side = BOTTOM)
spin.place(x=70,y=130)
spin= Button(root, text = 'SPIN_180',width="10",height="2",bg="GREY",command = SPIN_T,font = "arial 10 bold underline",fg ='#001dff',)
spin.pack( side = BOTTOM)
spin.place(x=70,y=10)
spin= Button(root, text = 'SPIN_L',width="10",height="2",bg="GREY",command = SPIN_L,font = "arial 10 bold underline",fg ='#001dff',)
spin.pack( side = BOTTOM)
spin.place(x=70,y=70)

square= Button(root, text = 'RESIZE',width="10",height="2",bg="GREY",command = RESIZE,font = "arial 10 bold underline",fg ='#001dff',)
square.pack( side = BOTTOM)
square.place(x=70,y=190)


modes= Button(root, text = 'EDGES',width="10",height="2",bg="GREY",command = MODES,font = "arial 10 bold underline",fg ='#001dff',)
modes.pack( side = BOTTOM)
modes.place(x=70,y=370)

satu= Button(root, text = 'FILTER 2',width="10",height="2",bg="GREY",command = SAT,font = "arial 10 bold underline",fg ='#001dff')
satu.pack( side = BOTTOM)
satu.place(x=740,y=250)

satur= Button(root, text = 'FILTER 1',width="10",height="2",bg="GREY",command = SATUR,font = "arial 10 bold underline",fg ='#001dff')
satur.pack( side = BOTTOM)
satur.place(x=740,y=190)

bw1= Button(root, text = 'FILTER 3',width="10",height="2",bg="GREY",command = BW1,font = "arial 10 bold underline",fg ='#001dff')
bw1.pack( side = BOTTOM)
bw1.place(x=740,y=310)
bw2= Button(root, text = 'FILTER 4',width="10",height="2",bg="GREY",command = BW2,font = "arial 10 bold underline",fg ='#001dff')
bw2.pack( side = BOTTOM)
bw2.place(x=740,y=370)





def open():
    global my_image

    root.filename = filedialog.askopenfilename(initialdir="/",title="select a file",filetype=(("png files",".jpg"),("all files",".")))
    my_image = Image.open(root.filename)
    canvas.image= ImageTk.PhotoImage(my_image.resize((500,500),Image.ANTIALIAS))
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

#img = PhotoImage(Image.open("group2.png"))

canvas = Canvas(width=500, height=500,bg="#c4cbcc")
canvas.pack(expand=NO, fill=NONE)

my_btn = Button(root,text="open file ", command = open).pack()



reset= Button(root, text = 'RESET',width="10",height="2",bg="GREY",command = RESET,font = "arial 12 bold underline",fg ='#d10f0f')
reset.pack( side = BOTTOM)
reset.place(x=40,y=640)

w = Scale(root, from_=0, to = 50, orient = HORIZONTAL,fg="black",bg="#476646",)
w.pack()
w.place(x=405,y=530)

textBox1=Text(root, height=2, width=10)
textBox1.pack()
textBox1.place(x=200,y=530)
textBox2=Text(root, height=2, width=10)
textBox2.pack()
textBox2.place(x=250,y=530)

root.geometry("900x700")
root.minsize(700,500)
root.maxsize(1100,1100)
#root.attributes("-alpha",0.95)
root.configure(bg="grey")
root.mainloop()
