from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry('1120x494+232+213')
        #============Variable=========
        self.var_ref=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_damage=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        #================title=====
        lbl_title=Label(self.root,text='ROOM BOOKING',font=("times new roman",18,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1120,height=40)

       #=====Logo Pic====
        img2=Image.open(r'D:\Project\pics\grand.jpg')
        img2=img2.resize((100,30),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=5,y=5,width=100,height=30)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking',font=("times new roman",12,'bold'),padx=2)
        labelframeleft.place(x=5,y=40,width=360,height=450)

        #=====Ref and entry===
        lbl_cust_ref=Label(labelframeleft,text='Customer ID',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=17,font=("times new roman",12,'bold'))
        entry_ref.grid(row=0,column=1,sticky=W)
        #=============Fecth btn======
        btn_fetch=Button(labelframeleft,text='Fetch Data',command=self.Fetch_ref,font=("arial",8,'bold'),bg="black",fg='Gold',width=7)
        btn_fetch.place(x=292,y=4)

        #=====Check in date and entry===
        check_in_date=Label(labelframeleft,text='Check in Date',font=("arial",12,'bold'),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,width=25,textvariable=self.var_checkin,font=("times new roman",12,'bold'))
        txtcheck_in_date.grid(row=1,column=1)

        #=====Check out date and entry===
        lbl_Check_out=Label(labelframeleft,text='Check out Date',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)

        txt_Check_out=ttk.Entry(labelframeleft,width=25,textvariable=self.var_checkout,font=("times new roman",12,'bold'))
        txt_Check_out.grid(row=2,column=1)


        #=====roomtype combo===
        lbl_roomtype=Label(labelframeleft,text='Room Type',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select DISTINCT RoomType from `hotel_mang.`.details ORDER BY RoomType ASC')
        row3=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,font=("times new roman",12,'bold'),textvariable=self.var_roomtype,width=23,state='readonly')
        combo_roomtype['value']=row3
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        #====avialable rooms-===
        lblRoomAvailable=Label(labelframeleft,text='Available Rooms',font=("arial",12,'bold'),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        # txtRoomAvailable=ttk.Entry(labelframeleft,width=25,textvariable=self.var_roomavailable,font=("times new roman",12,'bold'))
        # txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details where Floor=0")
        rows=my_cursor.fetchall()
        combo_RoomNo=ttk.Combobox(labelframeleft,font=("times new roman",12,'bold'),textvariable=self.var_roomavailable,width=23,state='readonly')
        combo_RoomNo['value']=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #====damage Cost-===
        lbldamage=Label(labelframeleft,text='Damage Cost',font=("arial",12,'bold'),padx=2,pady=6)
        lbldamage.grid(row=5,column=0,sticky=W)

        txtdamage=ttk.Entry(labelframeleft,width=25,textvariable=self.var_damage,font=("times new roman",12,'bold'))
        txtdamage.grid(row=5,column=1)

        #====No. of days-===
        lblnoofdays=Label(labelframeleft,text='No Of Days',font=("arial",12,'bold'),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,width=25,textvariable=self.var_noofdays,font=("times new roman",12,'bold'))
        txtnoofdays.grid(row=6,column=1)

        #====Tax paid-===
        lbl_paidtax=Label(labelframeleft,text='Paid Tax',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_paidtax.grid(row=7,column=0,sticky=W)

        txt_paidtax=ttk.Entry(labelframeleft,width=25,textvariable=self.var_paidtax,font=("times new roman",12,'bold'))
        txt_paidtax.grid(row=7,column=1)

        #====sub total=======
        lbl_subtotal=Label(labelframeleft,text='Sub Total',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_subtotal.grid(row=8,column=0,sticky=W)

        txt_subtotal=ttk.Entry(labelframeleft,width=25,textvariable=self.var_actualtotal,font=("times new roman",12,'bold'))
        txt_subtotal.grid(row=8,column=1)

        #====total=======
        lbl_total=Label(labelframeleft,text='Total',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_total.grid(row=9,column=0,sticky=W)

        txt_total=ttk.Entry(labelframeleft,width=25,textvariable=self.var_total,font=("times new roman",12,'bold'))
        txt_total.grid(row=9,column=1)

        #========Bill btn======
        btn_bill=Button(labelframeleft,text='Bill',command=self.total,font=("arial",10,'bold'),bg="black",fg='Gold',width=7)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)

        #buttons============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=6,y=384,width=330,height=39)

        btn_add=Button(btn_frame,text='Add',command=self.add_data,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text='Update',command=self.update,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',command=self.delete,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text='Reset',command=self.reset,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_reset.grid(row=0,column=3,padx=1)

        #============Right Side Image=========
        img3=Image.open(r'D:\Project\pics\bedroom.jpg')
        img3=img3.resize((500,200),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg3.place(x=620,y=40,width=500,height=200)

        #=============Label fram Search Sys=======
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',font=("times new roman",12,'bold'),padx=2)
        table_frame.place(x=370,y=240,width=747,height=250)   

        #====search===
        lblsearchby=Label(table_frame,text='Search By',font=("arial",12,'bold'))
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman",12,'bold'),width=15,state='readonly')
        combo_search['value']=('Select','Ref','Room') #Customer id as Contact
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,width=20,textvariable=self.txt_search,font=("times new roman",12,'bold'))
        txtsearch.grid(row=0,column=2)

        btn_search=Button(table_frame,text='Search',command=self.search,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall=Button(table_frame,text='Show All',command=self.fetch_data,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_showall.grid(row=0,column=4,padx=0)

        #===========Show Data Table======
        details_frame=Frame(table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=40,width=740,height=186)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_frame,column=('ref','checkin','checkout','roomtype','roomavailable','damage','noofdays'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('ref',text='Reference ID')
        self.room_table.heading('checkin',text='Check In Date')
        self.room_table.heading('checkout',text='Check Out Date')
        self.room_table.heading('roomtype',text='Room Type')
        self.room_table.heading('roomavailable',text='Room No.')
        self.room_table.heading('damage',text='Damage Cost')
        self.room_table.heading('noofdays',text='No Of Days')

        self.room_table['show']='headings'

        self.room_table.column('ref',width=100)
        self.room_table.column('checkin',width=100)
        self.room_table.column('checkout',width=100)
        self.room_table.column('roomtype',width=100)
        self.room_table.column('roomavailable',width=100)
        self.room_table.column('damage',width=100)
        self.room_table.column('noofdays',width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    #======Add Data====
    def add_data(self):
        if self.var_ref.get()=="" or self.var_checkin.get()=='' or self.var_roomavailable.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into room values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                            self.var_ref.get(),
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_damage.get(),
                                                                                            self.var_noofdays.get()
                                                                                                    
                                                                                            ))
                                                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Room Booked',parent=self.root)
                conn2=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor2=conn2.cursor()   
                my_cursor2.execute('SET SQL_SAFE_UPDATES = 0')
                conn2.commit()
                conn2.close()
                conn1=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor1=conn1.cursor()   
                li =self.var_roomavailable.get()
                lst=li.split()
                my_cursor1.execute('update details set Floor=1 where RoomNo=%s',(
                                                                                lst
                                                                                    ))
                conn1.commit()
                conn1.close()
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)

    #======fetch data=
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from room')
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row:
                self.room_table.insert('',END,values=i)
            conn.commit()
            conn.close()
    #+=======Get curser======
    def get_cursor(self,event=''):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_damage.set(row[5]),
        self.var_noofdays.set(row[6])
    #========Update+=========
    def update(self):
            if self.var_ref.get()=='':
                messagebox.showerror('Error','Please enter Customer ID',parent=self.root)
            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                my_cursor.execute('update room set check_in=%s,check_out=%s,roomtype=%s,room=%s,damage=%s,noofdays=%s where ref=%s',(
                                                                                                                                                        
                                                                                                                                                        self.var_checkin.get(),
                                                                                                                                                        self.var_checkout.get(),
                                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                                        self.var_damage.get(),
                                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Update','Room details has been updated',parent=self.root)
    def delete(self):
        delete=messagebox.askyesno('Hotel Management Syastem','Do you want to delete this Room details',parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
            my_cursor=conn.cursor()
            query='delete from room where ref=%s'
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(''),
        self.var_checkin.set(''),
        self.var_checkout.set(''),
        self.var_roomtype.set(''),
        self.var_roomavailable.set(''),
        self.var_damage.set(''),
        self.var_noofdays.set('')
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

 #================All data Fetch===============
    def Fetch_ref(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error",'Please Enter Customer ID',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
            my_cursor=conn.cursor()
            query=("select name from customer where ref=%s")
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Customer Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=365,y=44,width=255,height=200)
                #=============Name========
                lblname=Label(showdataframe,text="Name",font=("arial",10,"bold"))
                lblname.place(x=0,y=0)
                
                lbl=Label(showdataframe,text=row,font=('arial',10,'bold'))
                lbl.place(x=90,y=0)
                #======Gender========
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                query=("select gender from customer where ref=%s")
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showdataframe,text="Gender",font=("arial",10,"bold"))
                lblgender.place(x=0,y=30)
                
                lbl2=Label(showdataframe,text=row,font=('arial',10,'bold'))
                lbl2.place(x=90,y=30)

                #======email========
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                query=("select email from customer where ref=%s")
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showdataframe,text="Email",font=("arial",10,"bold"))
                lblemail.place(x=0,y=60)
                
                lbl3=Label(showdataframe,text=row,font=('arial',10,'bold'))
                lbl3.place(x=90,y=60)

                #======Nationality========
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                query=("select nationality from customer where ref=%s")
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showdataframe,text="Nationality",font=("arial",10,"bold"))
                lblnationality.place(x=0,y=90)
                
                lbl4=Label(showdataframe,text=row,font=('arial',10,'bold'))
                lbl4.place(x=90,y=90)

                #======Address========
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                query=("select address from customer where ref=%s")
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showdataframe,text="Address",font=("arial",10,"bold"))
                lbladdress.place(x=0,y=120)
                
                lbl5=Label(showdataframe,text=row,font=('arial',10,'bold'))
                lbl5.place(x=90,y=120)

    #===Search System
    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from room where '+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row:
                self.room_table.insert('',END,values=i)
            conn.commit()
            conn.close()

    #=====Total Cost=======
    def total(self):
        inDate=self.var_checkin.get()   
        outDate=self.var_checkout.get()    
        inDate=datetime.strptime(inDate,"%d/%m/%Y")     
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_roomtype.get()=='Select'):
            messagebox.showerror("Error","Please Select Room Type")
        
        elif (self.var_roomtype.get()=='Duplex'):
            q1=float(self.var_damage.get())                   #Damage Cost "self.var_meal" as "self.var_damage"
            q2=float(1500)#room
            q3=float(self.var_noofdays.get())
            q4=float(q3*q2)
            Tax="Rs."+str('%.2f'%((q4)*0.1))
            ST="Rs."+str('%.2f'%((q4)))
            TT="Rs."+str('%.2f'%(q4+((q4)*0.1)+q1))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_roomtype.get()=='Luxuary'):
            q1=float(self.var_damage.get())                   #Damage Cost "self.var_meal" as "self.var_damage"
            q2=float(1000)#room
            q3=float(self.var_noofdays.get())
            
            q4=float(q3*q2)
            Tax="Rs."+str('%.2f'%((q4)*0.1))
            ST="Rs."+str('%.2f'%((q4)))
            TT="Rs."+str('%.2f'%(q4+((q4)*0.1)+q1))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_roomtype.get()=='Double'):
            q1=float(self.var_damage.get())                   #Damage Cost "self.var_meal" as "self.var_damage"
            q2=float(700)#room
            q3=float(self.var_noofdays.get())
            q4=float(q3*q2)
            Tax="Rs."+str('%.2f'%((q4)*0.1))
            ST="Rs."+str('%.2f'%((q4)))
            TT="Rs."+str('%.2f'%(q4+((q4)*0.1)+q1))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_roomtype.get()=='Single'):
            q1=float(self.var_damage.get())                   #Damage Cost "self.var_meal" as "self.var_damage"
            q2=float(400)#room
            q3=float(self.var_noofdays.get())
            q4=float(q3*q2)
            Tax="Rs."+str('%.2f'%((q4)*0.1))
            ST="Rs."+str('%.2f'%((q4)))
            TT="Rs."+str('%.2f'%(q4+((q4)*0.1)+q1))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__=='__main__':
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()