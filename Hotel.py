from tkinter import* 
from PIL import Image,ImageTk
from Customer import Cust_Win
from Room import Roombooking
from Details import DetailsRoom
from Feedback import Feedback

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1500x800+0+0')

        #====Image banner=====

        img1=Image.open(r'D:\Project\pics\Taj.jpg')
        img1=img1.resize((1500,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1500,height=140)

        #=====Logo Pic====
        img2=Image.open(r'D:\Project\pics\grand.jpg')
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=230,height=140)

        #================title=====
        lbl_title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=("times new roman",40,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1500,height=60)

        #====main frame==========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=200,width=1500,height=620)

        #==label menu=-==
        lbl_menu=Label(main_frame,text='MENU',font=("times new roman",20,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)        

        #====btn frame==========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=228,height=210)

        cust_btn=Button(btn_frame,text='CUSTOMER',command=self.cust_details,width=22,font=("times new roman",14,'bold'),bg='black',fg='gold',bd=2,cursor='hand1')
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text='ROOM',command=self.roombooking,width=22,font=("times new roman",14,'bold'),bg='black',fg='gold',bd=2,cursor='hand1')
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text='ROOM ENTRY',command=self.DetailsRoom,width=22,font=("times new roman",14,'bold'),bg='black',fg='gold',bd=2,cursor='hand1')
        details_btn.grid(row=2,column=0,pady=1)

        Feedback_btn=Button(btn_frame,text='FEEDBACK',width=22,command=self.Feedback,font=("times new roman",14,'bold'),bg='black',fg='gold',bd=2,cursor='hand1')
        Feedback_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text='LOGOUT',command=self.logout,width=22,font=("times new roman",14,'bold'),bg='black',fg='gold',bd=2,cursor='hand1')
        logout_btn.grid(row=4,column=0,pady=1) 

        #=============RIGHT image============
        img3=Image.open(r'D:\Project\pics\reception.jpg')
        img3=img3.resize((1130,520),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=225,y=0,width=1130,height=520)
        #======down imgs=-======
        img4=Image.open(r'D:\Project\pics\bed.jpg')
        img4=img4.resize((250,140),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=250,width=230,height=140)

        #2
        img5=Image.open(r'D:\Project\pics\food.jpg')
        img5=img5.resize((230,140),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=380,width=230,height=140)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def DetailsRoom(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def Feedback(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)

    #+===Logout==
    def logout(self):
        self.root.destroy()

if __name__=='__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()