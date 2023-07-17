from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from Hotel import HotelManagementSystem

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r'D:\Project\pics\Mat.webp')

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=540,y=170,width=320,height=430)

        img1=Image.open(r"D:\Project\pics\logo.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=645,y=200,width=100,height=100)

        get_str=Label(frame,text='Get Started',font=('times new roman',20,'bold'),fg='white',bg='black')
        get_str.place(x=85,y=130)

        #Label
        username=lbl=Label(frame,text='Username(Email ID)',font=('time new roman',10,'bold'),fg='white',bg='black')
        username.place(x=30,y=175)

        self.txtuser=ttk.Entry(frame,font=('time new roman',10,'bold'))
        self.txtuser.place(x=30,y=200,width=270)

        password=lbl=Label(frame,text='Password',font=('time new roman',10,'bold'),fg='white',bg='black')
        password.place(x=30,y=250)

        self.password=ttk.Entry(frame,show='*',font=('time new roman',10,'bold'))
        self.password.place(x=30,y=275,width=270)

        #icon images
        img2=Image.open(r"D:\Project\pics\User.jpg")
        img2=img2.resize((15,15),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg='black',borderwidth=0)
        lblimg2.place(x=700,y=345,width=25,height=25)

        img3=Image.open(r"D:\Project\pics\Pass.png")
        img3=img3.resize((22,22),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg='black',borderwidth=0)
        lblimg3.place(x=642,y=419,width=25,height=25)

        #button
        loginbutton=Button(frame,command=self.login,text='Login',font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey')
        loginbutton.place(x=100,y=310,width=120,height=35)
        #Sign up button
        registerbutton=Button(frame,text='Sign Up',command=self.window,font=('times new roman',8,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey',activeforeground='white',activebackground='black')
        registerbutton.place(x=110,y=350,width=96)
        #forget password
        Forgetbutton=Button(frame,text='Forget Password',command=self.forget_pass_window,font=('times new roman',8,'bold'),borderwidth=0,relief=RIDGE,fg='white',bg='black',activeforeground='white',activebackground='black')
        Forgetbutton.place(x=100,y=400,width=120) 

    def window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        

    def login(self):
        #===========variables=========
        # self.var_email=StringVar()
        # self.var_password=StringVar()

        if self.txtuser.get()=='' or self.password.get()=='':
            messagebox.showerror('Error','all field required')
           
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Test@2023',database='new_schema')
            my_cursor=conn.cursor()
            query=('select * from new_schema.register where email=%s and password=%s')
            values=(self.txtuser.get(),self.password.get())
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            # print(row)
            # print(self.txtuser.get())
            # print(self.password.get())    
            if row==None:
                messagebox.showerror('Error','Invalid Username or Password')
            else:
                open_main=messagebox.askyesno('YesNo','Access only admin')
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_window)
                         #after bulding project paste code in this file and change Project to 'projects actual name' video time 40.00
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()
                



    #==========Reset  password===================
    def reset_pass(self):
        if self.combo_security_q.get()=='Select':
            messagebox.showerror('Error',"Select the Security Question ",parent=self.root2)
        elif self.security_a_entry.get()=='':
            messagebox.showerror('Error','Please Enter Security Answer',parent=self.root2)
        elif self.new_pass_entry.get()=='':
            messagebox.showerror('Error','Please Enter a New Password',parent=self.root2)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Test@2023',database='new_schema')
            my_cursor=conn.cursor()
            query=('select * from new_schema.register where email=%s and security_q=%s and security_a=%s')
            value=(self.txtuser.get(),self.combo_security_q.get(),self.security_a_entry.get())#entry.get()
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Please Enter Correct Answer',parent=self.root2)
            else:
                query=("update new_schema.register set password=%s where email=%s")
                value=(self.new_pass_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Info','Your password has been reseted, please login using new password',parent=self.root2)
                self.root2.destroy()



    #==========forget password window============
    def forget_pass_window(self):
        if self.txtuser.get()=='':
            messagebox.showerror('Error','Please Enter Email')
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Test@2023',database='new_schema')
            my_cursor=conn.cursor()
            query=('select * from new_schema.register where email=%s')
            values=(self.txtuser.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            #print(row)


            if row==None:
                messagebox.showerror('Error','Please Enter a Valid Username ')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry('340x450+610+170')
            

                l=Label(self.root2,text='Forget Password',font=('time new roman',15,'bold'),fg='red',bg='white')
                l.place(x=0,y=10,relwidth=1)

                #Row 3
                security_q=Label(self.root2,text='Security Question',font=('times new roman',15,'bold'),bg='white')
                security_q.place(x=50,y=80)
                #combo
                self.combo_security_q=ttk.Combobox(self.root2,font=('times new roman',10,'bold'),state='readonly')
                self.combo_security_q['values']=('Select','My School Name','My Pet Name','My Place of Birth')
                self.combo_security_q.place(x=50,y=110,width=220)
                self.combo_security_q.current(0)

                security_a=Label(self.root2,text='Security Answer',font=('times new roman',15,'bold'),bg='white')
                security_a.place(x=50,y=140)

                self.security_a_entry=ttk.Entry(self.root2,font=('times new roman',10,'bold'))
                self.security_a_entry.place(x=50,y=170,width=220)


                self.new_pass=Label(self.root2,text='New Password',font=('times new roman',15,'bold'),bg='white')
                self.new_pass.place(x=50,y=220)

                self.new_pass_entry=ttk.Entry(self.root2,font=('times new roman',10,'bold'))
                self.new_pass_entry.place(x=50,y=250,width=220)
                #Reset button
                btn=Button(self.root2,text='Reset',command=self.reset_pass,font=('times new roman',10,'bold'),fg='white',bg='green')
                btn.place(x=100,y=290,width=100)
                   


#======Sign up window====
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
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'))
        b2.place(x=290,y=330,width=300)

    #Fuction decleration

    def register_data(self):
        if self.var_fname.get()=='' or self.var_email.get=='' or self.var_combo_security_q.get()=='Select':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        elif self.var_password.get()=='':
            messagebox.showerror('Error','Enter Password',parent=self.root)
        elif self.var_password.get()!=self.var_cpass.get():
            messagebox.showerror('Error','Password & Confirm Password must be same',parent=self.root)
        elif self.var_checkbutton.get()==0:
            messagebox.showerror('Error','Please agree Terms&Conditions',parent=self.root)
        else:
            if self.var_dsa.get()=='2546@Grand':
                conn=mysql.connector.connect(host='localhost',user='root',password='Test@2023',database='new_schema')
                my_cursor=conn.cursor()
                query=('select * from register where email=%s')
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror('Error','User already exist, please try another email',parent=self.root)
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
                    messagebox.showinfo('Success','Registered succesfuly',parent=self.root)  
            else:
                messagebox.showerror('Error','Please Enter DSA Password',parent=self.root)

    def return_login(self):
        self.root.destroy()        


if __name__=='__main__':
    main()
