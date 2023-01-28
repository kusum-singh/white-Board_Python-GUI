from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab


#Defining Class and constructor of the Program
class Draw():
    def __init__(self,root):

# main screen code
        self.root =root
        self.root.title("Making Drawing FUN")
        self.root.geometry("810x530")
        self.root.configure(background="Royal blue")
        self.root.resizable(0,0)
 
#definig pointer and Eraser   
        self.pointer= "black"
        self.erase="white"
# colouring the pannel and alloting it as a button
        self.pick_color = LabelFrame(self.root,text='Colors',font =('Asther',15),bd=5,relief=RIDGE,bg="royal blue")
        self.pick_color.place(x=0,y=40,width=90,height=185)

        colors = ['blue','red','green', 'orange','violet','black','yellow','purple','pink','gold','brown','indigo']
        i=j=0
        for color in colors:
            Button(self.pick_color,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1

 # buttons and their features  
        self.eraser_btn= Button(self.root,text="Eraser",bd=4,bg='royal blue',command=self.eraser,width=9,relief=RIDGE)
        self.eraser_btn.place(x=0,y=197)

        self.clear_screen= Button(self.root,text="Clear Screen",bd=4,bg='royal blue',command= lambda : self.background.delete('all'),width=9,relief=RIDGE)
        self.clear_screen.place(x=0,y=227)

        self.save_btn= Button(self.root,text="Save",bd=4,bg='royal blue',command=self.save_drawing,width=9,relief=RIDGE)
        self.save_btn.place(x=0,y=257)

        self.bg_btn= Button(self.root,text="Background",bd=4,bg='royal blue',command=self.canvas_color,width=9,relief=RIDGE)
        self.bg_btn.place(x=0,y=287)


#Scale for increasing the size for pointer
        self.pointer_frame= LabelFrame(self.root,text='size',bd=5,bg='royal blue',font=('arial',15,'bold'),relief=RIDGE)
        self.pointer_frame.place(x=0,y=320,height=200,width=70)

        self.pointer_size =Scale(self.pointer_frame,orient=VERTICAL,from_ =48 , to =0, length=168)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0,column=1,padx=15)


#Defining a background color for the Canvas 
        self.background = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=470,width=680)
        self.background.place(x=80,y=40)
        # activationg mouse click
        self.background.bind("<B1-Motion>",self.paint)         


# Functions

# Paint Function for Drawing the lines on Canvas
    def paint(self,event):       
        x1,y1 = (event.x-2), (event.y-2)  
        x2,y2 = (event.x+2), (event.y+2)  

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=self.pointer_size.get())

# Function for choosing the color of pointer  
    def select_color(self,col):
        self.pointer = col

# Function for defining the eraser
    def eraser(self):
        self.pointer= self.erase

# Function for choosing the background color of the Canvas    
    def canvas_color(self):
        color=colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase= color[1]

# saving the pic 
    def save_drawing(self):
        try:
            # self.background update()
            file_ss =filedialog.asksaveasfilename(defaultextension='jpg')
            #print(file_ss)
            x=self.root.winfo_rootx() + self.background.winfo_x()
            #print(x, self.background.winfo_x())
            y=self.root.winfo_rooty() + self.background.winfo_y()
            #print(y)

            x1= x + self.background.winfo_width() 
            #print(x1)
            y1= y + self.background.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x , y, x1, y1)).save(file_ss)
            messagebox.showinfo('Screenshot Successfully Saved as' + str(file_ss))

        except:
            print("Error in saving the screenshot")

if __name__ =="__main__":
    root = Tk()
    p= Draw(root)
    root.mainloop()