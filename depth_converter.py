import numpy as np
import cv2 as cv
import ntpath

from tkinter import *
#from tkinter import Tk, Frame, Button, Label, BOTH, X, Y, TOP, BOTTOM
from tkinter import filedialog as fd
from pathlib import Path


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="#1e1e1e")
        self.parent = parent
        self.parent.title("Depth Converter")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()
        

    def centerWindow(self):
        w = 320
        h = 400
 
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
 
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.parent.resizable(False, False)
    
    def initUI(self):
        #C = Canvas(self, bg = "White", height=100, width=320)
        #C.pack(fill = X, expand = True)
        labelText = Label( self, text = "Depth Converter", bg = "#1e1e1e", foreground="white")
        labelText.pack(pady = 25)
        labelText.configure(font=("Impact", 24))

        labelImportFormat = Label(self, text="Import image (only .bmp support):", bg="#1e1e1e", foreground="white")
        labelImportFormat.pack(fill=X, side=TOP, expand=0)


        btn = Button(self, text="Open..", command=self.openFile, bg="#5378ba", foreground="white", activebackground='#3c537a') 
        btn.pack(fill=X, side=TOP, expand=0, padx=5, pady=5)
        self.label1 = Label(self, text="", bg="#1e1e1e", foreground="white")
        self.label1.pack(fill=X, side=TOP, expand=0)
        labelspace = Label(self, text="", bg="#1e1e1e")
        labelspace.pack(fill=X, side=TOP, expand=0, padx=5, pady=5)
        self.variable = StringVar(self)
        self.variable.set("exr") # default value
        #label2 = Label(self, text="export format:", bg="#1e1e1e", foreground="white")
        #label2.pack(fill=X, side=TOP, expand=0)
        

        #w = OptionMenu(self, self.variable, "exr", "bmp", "png")
        #w.configure(bg='#5378ba', activebackground='#3c537a', foreground="white",)
        #w.pack(fill=X, side=TOP, expand=0, padx=5, pady=5)

        self.var = BooleanVar()
        self.cb = Checkbutton(self, text="Enable Preview", bg="#1e1e1e", foreground="white", selectcolor="#282828", activebackground='#282828', variable=self.var)
        self.cb.pack(fill=X, side=TOP, expand=0, padx=5, pady=5)

        #self.varBit = BooleanVar()
        #self.cbBit = Checkbutton(self, text="16/24bit processing", bg="#1e1e1e", foreground="white", selectcolor="#282828", activebackground='#282828', variable=self.varBit)
        #self.cbBit.pack(fill=X, side=TOP, expand=0, padx=5, pady=5)

        self.btnProcess = Button(self, text="Process", command=self.Process, bg="#5378ba",  foreground="white", activebackground='#3c537a') 
        self.btnProcess.pack(fill=X, side=BOTTOM, expand=0, padx=5, pady=5)
        self.btnProcess["state"] = DISABLED
        self.labelDone = Label(self, text="", bg="#1e1e1e", foreground="white" )
        self.labelDone.pack(fill=X, side=BOTTOM, expand=0, padx=5, pady=15)

    def openFile(self):  
        #self.filedir = fd.askopenfilename(filetypes = (("BMP","*.bmp"),("PNG","*.png"),("JPEG","*.jpg"),("all files","*.*")))
        self.filedir = fd.askopenfilename(filetype = (("BMP","*.bmp"),("all files","*.*"))) #only bmp files support
        filename = ntpath.basename(self.filedir)
        self.label1.configure(text=filename)
        self.labelDone.configure(text="")
        if self.filedir:
            self.btnProcess["state"] = NORMAL 
        else:
            self.btnProcess["state"] = DISABLED

    def Process(self):  
        filename = ntpath.basename(self.filedir)
        name = filename.split('.')
        print(name[0])
        img = cv.imread(self.filedir, cv.IMREAD_UNCHANGED)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        arr = np.asarray([256.0, 256.0*256.0, 256.0*256.0*256.0])

        #No needed, only exr export

        #if self.varBit.get():
        #    arr = np.asarray([256.0*256.0, 256.0, 1.0])
        #else:
        #    arr = np.asarray([1.0, 256.0*256.0, 256.0])
        #    b,g,r = cv.split(img)
        #    b = b * 0
        #    img = cv.merge((b,g,r))


        arr = (1.0 / arr)
        img = (img.dot(arr)) * (256.0*256.0*256.0) / (256.0*256.0*256.0 - 1.0)
        #img = img/256
        imgPreview = img
        img = img.astype("float32")
        Path("./output").mkdir(parents=True, exist_ok=True)
        cv.imwrite('./output/' + name[0] + '_depth.exr', img)
        print('Successful export: EXR')
        self.labelDone.configure(text="Successful export: EXR")

        #Not working anymore

        #if self.variable.get() == 'exr' :
        #    img = img.astype("float32")
        #    Path("./output").mkdir(parents=True, exist_ok=True)
        #    cv.imwrite('./output/' + name[0] + '_depth.exr', img)
        #    print('Successful export: EXR')
        #    self.labelDone.configure(text="Successful export: EXR")
        #if self.variable.get() == 'png' :
        #    img = img * 255
        #    img = img.astype("float")
        #    img = cv.merge((img,img,img))
        #    Path("./output").mkdir(parents=True, exist_ok=True)
        #    cv.imwrite('./output/' + name[0] + '_depth.png', img)
        #    print('Successful export: PNG')
        #    self.labelDone.configure(text="Successful export: PNG")
        #if self.variable.get() == 'bmp' :
        #    img = img * 255
        #    img = img.astype("float")
        #    img = cv.merge((img,img,img))
        #    Path("./output").mkdir(parents=True, exist_ok=True)
        #    cv.imwrite('./output/' + name[0] + '_depth.bmp', img)
        #    print('Successful export: BMP')
        #    self.labelDone.configure(text="Successful export: BMP")

        if self.var.get():
            img = img * 255
            imgPreview = imgPreview.astype("float")
            scale_percent = imgPreview.shape[0] / 900
            print(imgPreview.shape[0] / scale_percent)
            print(imgPreview.shape[1] / scale_percent)
            width = int(imgPreview.shape[1] / scale_percent)
            height = int(imgPreview.shape[0] / scale_percent)
            dim = (width, height)
            imgPreview = cv.resize(imgPreview, dim, interpolation = cv.INTER_AREA)
            cv.imshow('image',imgPreview)
            cv.waitKey(0)
            cv.destroyAllWindows()

def main():
    window = Tk()
    ex = Example(window)
    window.mainloop()
    
if __name__ == '__main__':
    main()