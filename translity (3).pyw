from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import codecs
import nltk

root = Tk()
root.geometry('900x610')
root.minsize(900,610)
# root.maxsize(900,610)
root.title("Converter")
root.configure(bg='light grey')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

content=str(encoding="utf-8")

def open_file():
    file = askopenfile(mode="rb", initialdir = "/",title = "Select file",filetypes = (
        ("text file","*.txt"),("pdf file","*.pdf"),("docx file","*.docx"), ("doc file","*.doc"),("all files","*.*")))
                                                
    
    if file is not None:
        
        content= file.read()
        inputtxt.insert('end', content)
    	

def box():
    messagebox.showinfo(title="Dastur tuzuvchi haqida ma'lumot",message="Dastur tuzuvchi: Mamaraimov Mirjalol TATU_SF talabasi.  Bog'lanish uchun  _+998997126479_")


def boxes():
   messagebox.showwarning("Bu dasturning vazifasi.", " < Kiril > alifbosida yozilgan matnni < Lotin > alifbosidagi matnga o'girib beradi.")


def ClearAll():
    inputtxt.delete(1.0, END)
    output.delete(1.0, END)

def file_save():
    if len(inputtxt.get("1.0","end-1c"))!=0 and len(output.get("1.0","end-1c"))!=0:
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = asksaveasfile('w', defaultextension=".txt" , filetypes=files, title = "Save as", initialdir = 'dir')

        print(output.get("1.0","end-1c"))                                                                                
        if file is None:
            return
        
        contents = ""
        contents += output.get("1.0","end-1c")
        file.write(contents)
        file.close()

stemmer=nltk.PorterStemmer()
def share():
    text= str(inputtxt.get("1.0","end-1c"))
    t=(nltk.word_tokenize(text))
    k=nltk.pos_tag(t)
    
    new_text= str()
    if len(text)== 0 and len(output.get("1.0" , "end-1c")) !=0:
        messagebox.showerror("Error" , "Enter the text in the box provided!!!")
    output.delete("1.0" , END)
    
    

    output.insert("1.0", str(k))
    

inputtxt=Text(root, bg='#F5FFFA', width =100, height=15)
inputtxt.pack(expand=True, fill=BOTH, padx=10, pady = 10)


myButton=Button(root,text='Convert' ,fg="Black", command = share)
myButton.pack(fill=BOTH,pady=5,padx=10)

output= Text(root, bg="#F5FFFA", width =100, height=15)
output.pack(expand=True, fill=BOTH, padx=10, pady = 10)


bbutton=Button(root,text="Clear",fg="Black",command=ClearAll)
bbutton.pack(fill=BOTH,pady=10,padx=10)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=box)
helpmenu.add_command(label="Help Index", command=boxes)


root.call('encoding', 'system', 'utf-8')
root.config(menu=menubar)
mainloop()

