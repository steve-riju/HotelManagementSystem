from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Add Room")
        self.root.geometry('1120x494+232+213')

        #================title=====
        lbl_title=Label(self.root,text='ROOM ENTRY',font=("times new roman",18,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1120,height=40)

       #=====Logo Pic====
        img2=Image.open(r'D:\Project\pics\grand.jpg')
        img2=img2.resize((100,30),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=5,y=5,width=100,height=30)

        #======Labbel Frame=-======
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Add New Room',font=("times new roman",12,'bold'),padx=2)
        labelframeleft.place(x=5,y=40,width=475,height=310)
        #==========Variable=====
        self.var_floor=StringVar()
        self.var_room=StringVar()
        self.var_roomtype=StringVar()
        #=====Floor and entry===
        lbl_floor=Label(labelframeleft,text='Floor',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        entry_floor=ttk.Entry(labelframeleft,width=25,textvariable=self.var_floor,font=("times new roman",12,'bold'))
        entry_floor.grid(row=0,column=1,sticky=W)

        #=====Room No and entry===
        lbl_RoomNo=Label(labelframeleft,text='Room No.',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        entry_RoomNo=ttk.Entry(labelframeleft,width=25,textvariable=self.var_room,font=("times new roman",12,'bold'))
        entry_RoomNo.grid(row=1,column=1)

        #=====Room TYpe and entry===
        lbl_RoomType=Label(labelframeleft,text='Room Type',font=("arial",12,'bold'),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=25,font=("times new roman",12,'bold'))
        entry_RoomType.grid(row=2,column=1)

        #buttons============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=6,y=184,width=330,height=39)

        btn_add=Button(btn_frame,text='Add',command=self.add_data,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text='Update',command=self.update,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',command=self.delete,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text='Reset',command=self.reset,font=("arial",12,'bold'),bg="black",fg='Gold',width=7)
        btn_reset.grid(row=0,column=3,padx=1)

        #=============Label fram View Room =======
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Room Details ',font=("times new roman",12,'bold'),padx=2)
        table_frame.place(x=500,y=40,width=490,height=310)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,column=('floor','roomno','roomtype'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('floor',text='Floor')
        self.room_table.heading('roomno',text='Room No')
        self.room_table.heading('roomtype',text='Room Type')

        self.room_table['show']='headings'

        self.room_table.column('floor',width=100)
        self.room_table.column('roomno',width=100)
        self.room_table.column('roomtype',width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    #======Add Data====
    def add_data(self):
        if self.var_floor.get()=="" or self.var_room.get()=='' or self.var_roomtype.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into details values(%s,%s,%s)',(
                                                                                            self.var_floor.get(),
                                                                                            self.var_room.get(),
                                                                                            self.var_roomtype.get()
                                                                                            ))
                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','New Room Assigned',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)

    #======fetch data=
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from details')
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

        self.var_floor.set(row[0]),
        self.var_room.set(row[1]),
        self.var_roomtype.set(row[2])

    #========Update+=========
    def update(self):
            if self.var_floor.get()=='' or self.var_room.get()=='':
                messagebox.showerror('Error','Please Enter Floor & Room No.',parent=self.root)
            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
            

                my_cursor.execute('update details set Floor=%s,RoomType=%s where RoomNo=%s',(
                                                                                                                                                        
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_room.get()
                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Update','Room details has been updated',parent=self.root)

    def delete(self):
        if self.var_room.get()=="":
            messagebox.showerror("Error","Select Details",parent=self.root)
        else:
            delete=messagebox.askyesno('Hotel Management System','Do you want to delete this Room details',parent=self.root)
            if delete>0:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@2023',database='hotel_mang.')
                my_cursor=conn.cursor()
                query='delete from details where RoomNo=%s'
                value=(self.var_room.get(),)
                my_cursor.execute(query,value)
            else:
                 if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()

    def reset(self):
        self.var_floor.set(''),
        self.var_room.set(''),
        self.var_roomtype.set('')

if __name__=='__main__':
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()