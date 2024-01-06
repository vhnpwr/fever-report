from tkinter import*
from tkinter import messagebox
root=Tk()

root.title("fever report")
root.geometry("600x600")

lbl1=Label(root,text="fever report")
lbl1.place(relx=0.5,rely=0.2,anchor=CENTER)

q1_radioBtn=StringVar(value="0")

q1=Label(root,text="do you have a headache and a sore throat")
q1.place(relx=0.5,rely=0.3,anchor=CENTER)

q1r1=Radiobutton(root,text="yes",variable=q1_radioBtn,value="yes")
q1r1.place(relx=0.4,rely=0.35,anchor=CENTER)

q1r2=Radiobutton(root,text="no",variable=q1_radioBtn,value="no")
q1r2.place(relx=0.6,rely=0.35,anchor=CENTER)

q2_radioBtn=StringVar(value="0")

q2=Label(root,text="is your body temperature high")
q2.place(relx=0.5,rely=0.5,anchor=CENTER)

q2r1=Radiobutton(root,text="yes",variable=q2_radioBtn,value="yes")
q2r1.place(relx=0.4,rely=0.55,anchor=CENTER)

q2r2=Radiobutton(root,text="no",variable=q2_radioBtn,value="no")
q2r2.place(relx=0.6,rely=0.55,anchor=CENTER)

q3_radioBtn=StringVar(value="0")

q3=Label(root,text="are there any symptoms eye redness")
q3.place(relx=0.5,rely=0.7,anchor=CENTER)

q3r1=Radiobutton(root,text="yes",variable=q3_radioBtn,value="yes")
q3r1.place(relx=0.4,rely=0.75,anchor=CENTER)

q3r2=Radiobutton(root,text="no",variable=q3_radioBtn,value="no")
q3r2.place(relx=0.6,rely=0.75,anchor=CENTER)

def feverScore():
    score=0
    if q1_radioBtn.get()=="yes":
        score=score+20
        
    if q2_radioBtn.get()=="yes":
        score=score+20
        
    if q3_radioBtn.get()=="yes":
        score=score+20
        
    if score<=20:
        messagebox.showinfo("report","you don't need to visit a doctor")
    elif score>20 and score<=40:
        messagebox.showinfo("report","you might have to visit a doctor ")
    else :
        messagebox.showinfo("report","you have been strongly advised to visit a doctor")
        
showResults=Button(root,text="show results",command=feverScore)
showResults.place(relx=0.5,rely=0.9,anchor=CENTER)


root.mainloop()
