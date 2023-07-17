from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry('1120x494+232+213')

        #===============Variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        #================title=====
        lbl_title=Label(self.root,text='ADD CUSTOMER DETAILS',font=("times new roman",18,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1120,height=40)

       #=====Logo Pic====
        img2=Image.open(r'D:\Project\pics\grand.jpg')
        img2=img2.resize((100,30),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=5,y=5,width=100,height=30)

        #=======LABEL FRAME====
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',font=("times new roman",12,'bold'),padx=2)
        labelframeleft.place(x=5,y=40,width=360,height=450)

        #=====label and entry===
        lbl_cust_ref=Label(labelframeleft,text='Customer Ref',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,width=25,textvariable=self.var_ref,font=("times new roman",12,'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)

        #=====cname and entry===
        cname=Label(labelframeleft,text='Customer Name',font=("arial",12,'bold'),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,width=25,textvariable=self.var_cust_name,font=("times new roman",12,'bold'))
        txtcname.grid(row=1,column=1)

        #=====mother name and entry===
        lblmname=Label(labelframeleft,text='Mother Name',font=("arial",12,'bold'),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,width=25,textvariable=self.var_mother,font=("times new roman",12,'bold'))
        txtmname.grid(row=2,column=1)

        #=====gender combo===
        lbl_gender=Label(labelframeleft,text='Gender',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("times new roman",12,'bold'),textvariable=self.var_gender,width=23,state='readonly')
        combo_gender['value']=('Select','Male','Female','Transgender','Other')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #====post code-===
        lblpost=Label(labelframeleft,text='Pin Code',font=("arial",12,'bold'),padx=2,pady=6)
        lblpost.grid(row=4,column=0,sticky=W)

        txtpost=ttk.Entry(labelframeleft,width=25,textvariable=self.var_post,font=("times new roman",12,'bold'))
        txtpost.grid(row=4,column=1)

        #====mobile-===
        lblmobile=Label(labelframeleft,text='Mobile No.',font=("arial",12,'bold'),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,width=25,textvariable=self.var_mobile,font=("times new roman",12,'bold'))
        txtmobile.grid(row=5,column=1)

        #====email-===
        lblemail=Label(labelframeleft,text='Email',font=("arial",12,'bold'),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,width=25,textvariable=self.var_email,font=("times new roman",12,'bold'))
        txtemail.grid(row=6,column=1)

        #====Nationality-===
        lblnationality=Label(labelframeleft,text='Nationality',font=("arial",12,'bold'),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelframeleft,font=("times new roman",12,'bold'),textvariable=self.var_nationality,width=23,state='readonly')
        combo_nation['value']=('Select','Indian','American','Koriean','Other')
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)

        #====ID proof-===
        lblidproof=Label(labelframeleft,text='ID Proof',font=("arial",12,'bold'),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font=("times new roman",12,'bold'),textvariable=self.var_id_proof,width=23,state='readonly')
        combo_id['value']=('Select','Addahar','Passport','Drivers Licence','Other')
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #====id no.-===
        lblid_number=Label(labelframeleft,text='ID Proof No.',font=("arial",12,'bold'),padx=2,pady=6)
        lblid_number.grid(row=9,column=0,sticky=W)

        txtid_number=ttk.Entry(labelframeleft,width=25,textvariable=self.var_id_number,font=("times new roman",12,'bold'))
        txtid_number.grid(row=9,column=1)

        #====Address===
        lbladdress=Label(labelframeleft,text='Address',font=("arial",12,'bold'),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,width=25,textvariable=self.var_address,font=("times new roman",12,'bold'))
        txtaddress.grid(row=10,column=1)

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

        #=============Label fram Search Sys=======
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',font=("times new roman",12,'bold'),padx=2)
        table_frame.place(x=370,y=40,width=747,height=450)   

        #====search===
        lblsearchby=Label(table_frame,text='Search By',font=("arial",12,'bold'))
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman",12,'bold'),width=15,state='readonly')
        combo_search['value']=('Select','Mobile','Ref')
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,width=20,textvariable=self.txt_search,font=("times new roman",12,'bold'))
        txtsearch.grid(row=0,column=2)

        btn_search=Button(table_frame,command=self.search,text='Search',font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall=Button(table_frame,text='Show All',command=self.fetch_data,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_showall.grid(row=0,column=4,padx=0)

        #===========show data======
        details_frame=Frame(table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=40,width=740,height=387)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.Cust_details_table=ttk.Treeview(details_frame,column=('ref','name','mother','gender','post','mobile',
                                             'email',"nationality",'idproof','idnumber','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading('ref',text='Refer No')
        self.Cust_details_table.heading('name',text='Name')
        self.Cust_details_table.heading('mother',text='Mother\'s Name')
        self.Cust_details_table.heading('gender',text='Gender')
        self.Cust_details_table.heading('post',text='Pin Code')
        self.Cust_details_table.heading('mobile',text='Mobile')
        self.Cust_details_table.heading('email',text='Email')
        self.Cust_details_table.heading('nationality',text='Nationality')
        self.Cust_details_table.heading('idproof',text='Id Proof')
        self.Cust_details_table.heading('idnumber',text='Id Number')
        self.Cust_details_table.heading('address',text='Address')

        self.Cust_details_table['show']='headings'

        self.Cust_details_table.column('ref',width=100)
        self.Cust_details_table.column('name',width=100)
        self.Cust_details_table.column('mother',width=100)
        self.Cust_details_table.column('gender',width=100)
        self.Cust_details_table.column('post',width=100)
        self.Cust_details_table.column('mobile',width=100)
        self.Cust_details_table.column('email',width=100)
        self.Cust_details_table.column('nationality',width=100)
        self.Cust_details_table.column('idproof',width=100)
        self.Cust_details_table.column('idnumber',width=100)
        self.Cust_details_table.column('address',width=100)
        
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                    self.var_ref.get(),
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Customer has been added',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from customer')
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in row:
                self.Cust_details_table.insert('',END,values=i)
            conn.commit()
            conn.close()
            
    def get_cursor(self,event=''):
        cursor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=='':
            messagebox.showerror('Error','Please enter mobile number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
            my_cursor=conn.cursor()
        

            my_cursor.execute('update customer set name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s',(
                                                                                                                                                                            self.var_cust_name.get(),
                                                                                                                                                                            self.var_mother.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_post.get(),
                                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_nationality.get(),
                                                                                                                                                                            self.var_id_proof.get(),
                                                                                                                                                                            self.var_id_number.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_ref.get()
                                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update','Customer details has been updated',parent=self.root)

    def delete(self):
        delete=messagebox.askyesno('Hotel Management Syastem','Do you want to delete this customer',parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
            my_cursor=conn.cursor()
            query='delete from customer where ref=%s'
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(''),
        self.var_cust_name.set(''),
        self.var_mother.set(''),
        self.var_gender.set('Select'),
        self.var_post.set(''),
        self.var_mobile.set(''),
        self.var_email.set(''),
        self.var_nationality.set('Select'),
        self.var_id_proof.set('Select'),
        self.var_id_number.set(''),
        self.var_address.set('')

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from customer where '+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in row:
                self.Cust_details_table.insert('',END,values=i)
            conn.commit()
            conn.close()

if __name__=='__main__':
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()