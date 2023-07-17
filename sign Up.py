from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Sign Up')
        self.root.geometry('1600x900+0+0')
        #variables
        self.var_fname=StringVar()
        self.var_l_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_combo_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_password=StringVar()
        self.var_cpass=StringVar()


        self.bg=ImageTk.PhotoImage(file=r'D:\Project\pics\Sign.jpg')
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=170,width=700,height=400)
        #Label
        register_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,'bold'),fg='green',bg='white')
        register_lbl.place(x=20,y=20)
        #Entry row 1
        fname=Label(frame,text='First Name',font=('times new roman',15,'bold'),bg='white')
        fname.place(x=50,y=70)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman',10,'bold'))
        fname_entry.place(x=50,y=100,width=220)

        l_name=Label(frame,text='Last Name ',font=('times new roman',15,'bold'),bg='white')
        l_name.place(x=300,y=70)

        l_name_entry=ttk.Entry(frame,textvariable=self.var_l_name,font=('times new roman',10,'bold'))
        l_name_entry.place(x=300,y=100,width=220)
        #row 2
        condact=Label(frame,text='Contact',font=('times new roman',15,'bold'),bg='white')
        condact.place(x=50,y=130)

        condact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=('times new roman',10,'bold'))
        condact_entry.place(x=50,y=160,width=220)

        email=Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white')
        email.place(x=300,y=130)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=('times new roman',10,'bold'))
        email_entry.place(x=300,y=160,width=220)
        #Row 3
        security_q=Label(frame,text='Security Question',font=('times new roman',15,'bold'),bg='white')
        security_q.place(x=50,y=190)
        #combo
        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_combo_security_q,font=('times new roman',10,'bold'),state='readonly')
        self.combo_security_q['values']=('Select','My School Name','My Pet Name','My Place of Birth')
        self.combo_security_q.place(x=50,y=220,width=220)
        self.combo_security_q.current(0)

        security_a=Label(frame,text='Security Answer',font=('times new roman',15,'bold'),bg='white')
        security_a.place(x=300,y=190)

        security_a_entry=ttk.Entry(frame,textvariable=self.var_security_a,font=('times new roman',10,'bold'))
        security_a_entry.place(x=300,y=220,width=220)
        #row 4
        password=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white')
        password.place(x=50,y=250)

        password_entry=ttk.Entry(frame,show='*',textvariable=self.var_password,font=('times new roman',10,'bold'))
        password_entry.place(x=50,y=280,width=220)

        cpass=Label(frame,text='Confirm Password',font=('times new roman',15,'bold'),bg='white')
        cpass.place(x=300,y=250)

        cpass_entry=ttk.Entry(frame,show='*',textvariable=self.var_cpass,font=('times new roman',10,'bold'))
        cpass_entry.place(x=300,y=280,width=220)
        self.var_dsa=StringVar()
        dsa_pass=Label(frame,text='DSA Pass',font=('times new roman',12,'bold'),bg='white')
        dsa_pass.place(x=530,y=250)

        dsa_entry=ttk.Entry(frame,show='*',textvariable=self.var_dsa,font=('times new roman',10,'bold'))
        dsa_entry.place(x=530,y=280,width=100)
        DSA_PASS='2546@Grand'

        #checkbutton
        self.var_checkbutton=IntVar()
        self.checkbutton=Checkbutton(frame,variable=self.var_checkbutton,text='I Agree The Terms & Conditions',font=('times new roman',8,'bold'),onvalue=1,offvalue=0)
        self.checkbutton.place(x=50,y=310)

        #Button
        img=Image.open(r'D:\Project\pics\Sign_up.png')
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'))
        b1.place(x=40,y=330,width=300)

        img1=Image.open(r'D:\Project\pics\Login1.png')
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'))
        b2.place(x=290,y=330,width=300)

    #Fuction decleration

    def register_data(self):
        if self.var_fname.get()=='' or self.var_email.get=='' or self.var_combo_security_q.get()=='Select':
            messagebox.showerror('Error','All filde are required')
        elif self.var_password.get()=='':
            messagebox.showerror('Error','Enter Password')
        elif self.var_password.get()!=self.var_cpass.get():
            messagebox.showerror('Error','Password &Confirm Password must be same')
        elif self.var_checkbutton.get()==0:
            messagebox.showerror('Error','Please agree Terms&Conditions')
        else:
            if self.var_dsa.get()=='2546@Grand':
                conn=mysql.connector.connect(host='localhost',user='root',password='Test@2023',database='new_schema')
                my_cursor=conn.cursor()
                query=('select * from register where email=%s')
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror('Error','User already exist, please try another email')
                else:
                    my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                            self.var_fname.get(),
                                                                                            self.var_l_name.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_combo_security_q.get(),
                                                                                            self.var_security_a.get(),
                                                                                            self.var_password.get()
                                                                                        ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Success','Registered succesfuly')  
            else:
                messagebox.showerror('Error','Please Enter DSA Password')

if __name__=='__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()
    