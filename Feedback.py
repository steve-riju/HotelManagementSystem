from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title("Feed Back")
        self.root.geometry('1120x494+232+213')

        #================title=====
        lbl_title=Label(self.root,text='Feed Back',font=("times new roman",18,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1120,height=40)

       #=====Logo Pic====
        img2=Image.open(r'D:\Project\pics\grand.jpg')
        img2=img2.resize((100,30),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=5,y=5,width=100,height=30)

        #============Variable=========
        self.var_ref=StringVar()
        self.var_rate=StringVar()
        self.var_feedback=StringVar()

        #======Labbel Frame=-======
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Feed Back',font=("times new roman",12,'bold'),padx=2)
        labelframeleft.place(x=5,y=40,width=400,height=450)

        #=====Ref and entry===
        lbl_floor=Label(labelframeleft,text='Reference ID',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_floor.pack()

        entry_floor=ttk.Entry(labelframeleft,width=25,textvariable=self.var_ref,font=("times new roman",12,'bold'))
        entry_floor.pack()

        #=====Rating and entry===
        # Rating label and scale
        label_rating = Label(labelframeleft, text="Rating",font=("arial",12,'bold'),padx=2,pady=6)
        label_rating.pack()
        rating_scale=ttk.Entry(labelframeleft,width=25,textvariable=self.var_rate,font=("times new roman",12,'bold'))
        rating_scale.pack()

        #=====Feed Back and entry===
        lbl_Feedback=Label(labelframeleft,text='Feed Back',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_Feedback.pack()

        entry_Feedback=ttk.Entry(labelframeleft,width=25,textvariable=self.var_feedback,font=("times new roman",12,'bold'))
        entry_Feedback.pack()    

        #buttons============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=6,y=384,width=330,height=39)

        btn_add=Button(btn_frame,text='Add',font=("arial",12,'bold'),command=self.add_data,bg="black",fg='Gold',width=7)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text='Update',font=("arial",12,'bold'),command=self.update,bg="black",fg='Gold',width=7)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',font=("arial",12,'bold'),command=self.delete,bg="black",fg='Gold',width=7)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text='Reset',font=("arial",12,'bold'),command=self.reset,bg="black",fg='Gold',width=7)
        btn_reset.grid(row=0,column=3,padx=1)
    
        #=============Label fram Search Sys=======
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Feed Back And Search System',font=("times new roman",12,'bold'),padx=2)
        table_frame.place(x=404,y=40,width=720,height=450)    

        #====search===
        lblsearchby=Label(table_frame,text='Search By',font=("arial",12,'bold'))
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman",12,'bold'),width=15,state='readonly')
        combo_search['value']=('Select','Ref') #Customer id as Contact
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,width=20,textvariable=self.txt_search,font=("times new roman",12,'bold'))
        txtsearch.grid(row=0,column=2)

        btn_search=Button(table_frame,text='Search',font=("arial",12,'bold'),command=self.search,bg="black",fg='Gold',width=7)
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall=Button(table_frame,text='Show All',command=self.fetch_data,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_showall.grid(row=0,column=4,padx=0)

        #===========Show Data Table======
        details_frame=Frame(table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=40,width=710,height=385)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_frame,column=('ref','rating','feedback'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('ref',text='Reference ID')
        self.room_table.heading('rating',text='Rating')
        self.room_table.heading('feedback',text='FeedBack')

        self.room_table['show']='headings'

        self.room_table.column('ref',width=20)
        self.room_table.column('rating',width=20)
        self.room_table.column('feedback',width=20)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    #===Search System
    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from feedback where '+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row:
                self.room_table.insert('',END,values=i)
            conn.commit()
            conn.close()

    #======fetch data=
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from feedback')
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row:
                self.room_table.insert('',END,values=i)
            conn.commit()
            conn.close()

    def add_data(self):
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into feedback values(%s,%s,%s)',(
                                                                                            self.var_ref.get(),
                                                                                            self.var_rate.get(),
                                                                                            self.var_feedback.get()
                                                                                            ))
                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Thanks For The FeedBack',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)

    #========Update+=========
    def update(self):
            if self.var_ref.get()=='':
                messagebox.showerror('Error','Please Enter Reference ID',parent=self.root)
            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
            

                my_cursor.execute('update feedback set rating=%s,comments=%s where Ref=%s',(
                                                                                                                                                        
                                                                                        self.var_rate.get(),
                                                                                        self.var_feedback.get(),
                                                                                        self.var_ref.get()
                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Update','FeedBack has been updated',parent=self.root)

    def delete(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Enter Reference ID",parent=self.root)
        else:
            delete=messagebox.askyesno('Hotel Management System','Do you want to delete this FeedBack',parent=self.root)
            if delete>0:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                query='delete from feedback where Ref=%s'
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
        self.var_rate.set(''),
        self.var_feedback.set('')

    #+=======Get curser=====
    def get_cursor(self,event=''):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_rate.set(row[1])
        self.var_feedback.set(row[2])


if __name__=='__main__':
    root=Tk()
    obj=Feedback(root)
    root.mainloop()