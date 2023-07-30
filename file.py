from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from tkinter import messagebox
import webbrowser 
root=Tk()
root.geometry("800x600")
root.configure(background="#000000")
root.title("HTML IDE")
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
run_img=ImageTk.PhotoImage(Image.open("run.png"))
label_file_name=Label(root,text="File name",bg="black",fg="white")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root,borderwidth=0,bg="#333",fg="white")
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,bg="purple",fg="white",borderwidth=0,height=30,width=100)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)
name=""
run=""
def openfile():
    try:
        global name
        global run
        my_text.delete(1.0,END)
        input_file_name.delete(0,END)
        HTML_file=filedialog.askopenfilename(title="Open HTML File",filetypes=(("HTML Files","*.html"),))
        run=HTML_file
        name=os.path.basename(HTML_file)
        formated_name=name.split('.')[0]
        input_file_name.insert(END,formated_name)
        root.title(formated_name)
        HTML_file=open(HTML_file,'r')
        paragraph=HTML_file.read()
        my_text.insert(END,paragraph)
        HTML_file.close()
    except:
        messagebox.showerror("Error","Unable to open file, please try again")
def save():
    input_name=input_file_name.get()
    file=open(input_name+".html","w")
    data=my_text.get("1.0",END)
    print(data)
    file.write(data)
    messagebox.showinfo("Update","File Saved")
def run():
        webbrowser.open(run)
open_button=Button(root,text="Open file",command=openfile,image=open_img,borderwidth=0,bg="black")
open_button.place(relx=0.05,rely=0.05,anchor=CENTER)
save_button=Button(root,text="SAVE",image=save_img,command=save,borderwidth=0,bg="black")
save_button.place(relx=0.12,rely=0.05,anchor=CENTER)
run_button=Button(root,text="RUN",image=run_img,command=run,borderwidth=0,bg="black")
run_button.place(relx=0.19,rely=0.05,anchor=CENTER)
root.mainloop()