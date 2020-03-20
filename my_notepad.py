from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import*
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END) #removes 0th character from first line till end
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])

    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close        
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()  

            root.title(os.path.basename(file)+"-Notepad")
            print("file saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()  
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>")) #event generate automatically handles cut event
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def About():
   showinfo("Notepad","Notepad by Vanishree Desai")


if __name__=='__main__':
    root=Tk()
    root.title("Untitled-Notepad")
    root.iconbitmap('C:/Users/hp/Downloads/somewhat.ico')
    root.geometry("644x788")
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    MenuBar=Menu(root)

    
    #filemenu stars
    FileMenu=Menu(MenuBar,tearoff=0)

#open new file
    FileMenu.add_command(label="new",command=newFile)
#open existing file
    FileMenu.add_command(label="open",command=openFile)
#saving file
    FileMenu.add_command(label="save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
#filemenu ends
    
#edit menu starts
    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="cut",command=cut)
    EditMenu.add_command(label="copy",command=copy)
    EditMenu.add_command(label="paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
#edit menu ends

#help starst
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About notepad",command=About)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    
    


#adding scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)



root.config(menu=MenuBar)
root.mainloop()
    

