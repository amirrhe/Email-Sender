from tkinter import *
import smtplib
import re

def login():
    if validate_login():
        global username
        global password
        username =str(entry1.get())
        password =str(entry2.get())
        global server
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        f2.pack()
        btn2.grid()
        label4['text']= "logged in !"
        root.after(10,root.grid)
        f1.pack_forget()
        root.after(10,root.grid)
        f3.pack()
        label9.grid_remove()
        root.after(10,root.grid)
        
        
def hide_login_label():
    f2.pack_forget()
    f3.pack_forget()
    root.after(10,root.grid)
    

def send_mail():
    if validate_massage():
        label9.grid_remove()
        root.after(10,root.grid)
        reciever=str(entry3.get())
        subject = str(entry4.get())
        msgbody = str(entry5.get())
        msg = "from : "+username+"\n"+"To: "+ reciever+'\n'+"Subject: "+subject+'\n'+msgbody
        try:
            server.sendmail(username,reciever,msg)
            label9.grid()
            label9['text'] = "mail sent"
            root.after(10,label9.grid)
        except Exception as e:
            label9.grid()
            label9['text'] ="error sending mail"
            root.after(10,label9.grid)
            

def logout():
    try:
        server.quit()
        f3.pack_forget()
        f2.pack()
        label4.grid()
        label4['text'] = "logged out succesfully"
        btn2.grid_remove()
        f1.pack()
        entry2.delete(0,END)
        root.after(10,root.grid)
    except Exception as e:
        label4['text']="error in loggout "

        
def validate_login():
    email_text = str(entry1.get())        
    pass_text = str(entry2.get())
    if (email_text=="") or (pass_text==""):
        f2.pack()
        label4.grid()
        label4['text'] = "fill all the fields"
        btn2.grid_remove()
        root.after(10,root.grid)
        return False
    else:
        
        email_regex = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        if not email_regex.match(email_text):
            f2.pack()
            label4.grid()
            label4['text'] = "enter valid email address"
            btn2.grid_remove()
            root.after(10,root.grid)
            return False
        else:
            return True
        


def validate_massage():
    email_text =str(entry3.get())
    sub_text = str(entry4.get())
    msg_text = str(entry5.get())                
    if (email_text == "" ) or (sub_text == "")  or (msg_text == ""):
        label9.grid()
        label9['text']="fill in all the places"
        root.after(10,root.grid)
        return False 
    else:
        email_regex = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        if not email_regex.match(email_text):
            label9.grid()
            label9['text']="enter valid email address"
            root.after(10,root.grid)
            return False 
        elif(len(sub_text)<3 or len(msg_text)<3):
            label9.grid()
            label9['text']="enter at least 3 characters"
            root.after(10,root.grid)
            return False 
        else:
            return True
            


root = Tk()
root.title("Email sender application")

f1 = Frame(root,width=1000,height=800)
f1.pack(side="top")

label1 = Label(f1,width=25,text="enter your crendetials: ",font=("Times", "24", "bold ")) 
label1.grid(row=0,columnspan=3,pady=10,padx=10)

label2 = Label(f1,text="Enter Email").grid(row=1,sticky=E,pady=5,padx=10)
label3 = Label(f1,text="Enter password").grid(row=2,sticky=E,pady=5,padx=10)

entry1 = Entry(f1)
entry2 = Entry(f1,show = '*')

entry1.grid(row=1,column=1,pady = 5)
entry2.grid(row=2,column=1)

btn1 = Button(f1,text="login",width=10,bg="black",fg="white",command=lambda:login())
btn1.grid(row=3,columnspan=3,pady=10)


f2 = Frame(root)
f2.pack(side=TOP,expand=NO,fill=NONE)

label4 = Label(f2,width=20,bg="cyan",fg="red",text="login succesfully",font=("Times", "20", "bold "))
label4.grid(row=0,column=0,columnspan=2,pady=5)

btn2 = Button(f2,text="Logout",bg="black",fg= "white",command=lambda:logout())
btn2.grid(row=0,column=4,sticky=E,pady = 10 ,padx = (5,0))


f3 = Frame(master=root)
f3.pack(side=TOP,expand=NO,fill=NONE)

label5 = Label(f3,width=20,text="Compose email",font=("Times", "20", "bold "))
label5.grid(row=0,columnspan=3,pady=10)

label6 = Label(f3,text="TO").grid(row=1,sticky=E,pady=5)
label7 = Label(f3,text="subject").grid(row=2,sticky=E,pady=5)
label8 = Label(f3,text="message").grid(row=3,sticky=E)

entry3=Entry(f3)
entry4=Entry(f3)
entry5=Entry(f3)

entry3.grid(row=1,column=1,pady=5)
entry4.grid(row=2,column=1,pady=5)
entry5.grid(row=3,column=1,pady=5,rowspan=3,ipady=10)

btn3 = Button(f3,text="send mail",width=10,bg="black",fg= "white",command=lambda:send_mail())
btn3.grid(row=6,columnspan=3,pady=10)

label9=Label(f3,width=20,fg="white",bg="black",font=("Times", "20", "bold "))
label9.grid(row=7,columnspan=3,pady=5)

hide_login_label()

root.mainloop()





