from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog as t
import io, os, pymysql
from sys import platform
import tkcalendar as tkcal
from datetime import date as dates
import datetime
import time
from email.mime.text import MIMEText
import smtplib as mail
from auto_mail import *

root = ctk.CTk()
ctk.set_appearance_mode('light')
window_height = 500
window_width = 500
disp_height = root.winfo_screenheight()
disp_width = root.winfo_screenwidth()
print(window_height, type(window_height))
print(window_width, type(window_width))
print(disp_height, type(disp_height))
print(disp_width, type(disp_width))
pos_top = int(disp_height//2 - window_height//2)
pos_right = int(disp_width//2 - window_width//2)
root.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
root.resizable(False, False)
blue_clr="#d8e8e8"
glossy_clr="#ecf3f3"
root.configure(fg_color="#B6CEF6")
root.title("Colors Center For Autism")
root.iconbitmap("icons/colors.ico")
root.resizable(height=False, width=False)

switch_var = ctk.StringVar(value="off")
global stud1
stud1 = []

stud = {"Art":{"Nandan":"Medium", "Shyaam":"Medium", "Sachin":"Advanced", "Aaryan": "Basic", "Prasanna":"Basic", "Aadu":"Basic", "Siddarth":"Medium", "Siddanth":"Medium", "Ishaan":"Basic", "Pranav":"Medium", "Tanvi":"Basic", "Gaurang":"Basic", "Denver":"Medium", "Saching":"Advanced"},
        "Computer":{"Nandan":"Advanced", "Shyaam":"Medium", "Sachin":"Advanced", "Aaryan": "Basic", "Prasanna":"Basic", "Aadu":"Basic", "Siddarth":"Medium", "Siddanth":"Medium", "Ishaan":"Basic", "Pranav":"Medium", "Tanvi":"Basic", "Gaurang":"Medium", "Denver":"Medium"},
        "Special Ed.":{"Nandan":"Medium",  "Shyaam":"Medium", "Sachin":"Advanced", "Aaryan": "Basic", "Prasanna":"Basic", "Aadu":"Basic", "Siddarth":"Medium", "Siddanth":"Medium", "Ishaan":"Basic", "Pranav":"Medium", "Tanvi":"Basic", "Gaurang":"Basic", "Denver":"Basic"}}
teachers = ['Abinash', 'Ankit', 'Gayathri', 'Kanchana', 'Mahesh', 'Mamatha', 'Micah', 'Nagaveni', 'Nalina', 'Radhika', 'Saranya', 'Suthir']
students = ['Aadu', 'Aaryan', 'Denver', 'Gaurang', 'Ishaan', 'Nandan', 'Pranav', 'Prasanna', 'Sachin', 'Shyaam', 'Siddanth', 'Siddarth', 'Tanvi']
lesson_no = [str(i) for i in range(1,21)]
lesson_no = tuple(lesson_no)
button_font = ('Georgia',12, 'bold')
option_font = ('Book Antiqua',14, 'bold')
font = ("Times New Roman", 16, "bold")
scr_font = ("Times New Roman", 14)
rsc_font = ('Times New Roman',14)
option_clr = '#5b7878'
blue_clr="#d8e8e8"
glossy_clr="#ecf3f3"
today = datetime.date.today()

back_img = Image.open("img/back.png")
back_img = ctk.CTkImage(back_img, size=(30,30))

cal_img = Image.open("img/date.png")
cal_img = ctk.CTkImage(cal_img, size=(19,19))

te=ctk.StringVar()
st=ctk.StringVar()

a = ctk.StringVar()
b = ctk.StringVar()    
c = ctk.StringVar()
d = ctk.StringVar()

radio_var1 = ctk.StringVar(value='No')
radio_var2 = ctk.StringVar(value='No')
radio_var3 = ctk.StringVar(value='No')
radio_var4 = ctk.StringVar(value='No')
radio_var5 = ctk.StringVar(value='No')

a1 = ctk.StringVar()
a2 = ctk.StringVar()
a3 = ctk.StringVar()
a4 = ctk.StringVar()

b1 = ctk.StringVar()
b2 = ctk.StringVar()
b3 = ctk.StringVar()
b4 = ctk.StringVar()

c1 = ctk.StringVar()
c2 = ctk.StringVar()
c3 = ctk.StringVar()
c4 = ctk.StringVar()

d1 = ctk.StringVar()
d2 = ctk.StringVar()
d3 = ctk.StringVar()
d4 = ctk.StringVar()

def ques():
    root.withdraw()
    ques = ctk.CTkToplevel()
    ques.title("Feedback Report")
    window_height = 600
    window_width = 720
    pos_top = int(disp_height//2 - window_height//2)
    pos_right = int(disp_width//2 - window_width//2)
    ques.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
    ques.resizable(False, False)
    ques.iconbitmap('icons/feedback.ico')
    if platform.startswith("win"):
        ques.after(200, lambda: ques.iconbitmap("icons/feedback.ico"))
    ques.configure(fg_color=blue_clr)
    ques.grab_set()

    frame1 = ctk.CTkFrame(ques, fg_color=glossy_clr, width=400, border_width=1)
    frame2 = ctk.CTkFrame(ques, fg_color=glossy_clr, width=400, border_width=1)
    frame3 = ctk.CTkFrame(ques, fg_color=glossy_clr, width=400, border_width=1)
    frame4 = ctk.CTkFrame(ques, fg_color=glossy_clr, width=400, border_width=1)
    frame5 = ctk.CTkFrame(ques, fg_color=glossy_clr, width=400, border_width=1)
    frame6 = ctk.CTkFrame(ques, fg_color=glossy_clr, width=400, border_width=1)
        
    frame1.grid(padx = 10, pady=15, row=0, column=0, sticky="nsew")
    frame2.grid(padx = 10, pady=15, row=0, column=0, sticky="nsew")
    frame3.grid(padx = 10, pady=15, row=0, column=0, sticky="nsew")
    frame4.grid(padx = 10, pady=15, row=0, column=0, sticky="nsew")
    frame5.grid(padx = 10, pady=15, row=0, column=0, sticky="nsew")
    frame6.grid(padx = 10, pady=15, row=0, column=0, sticky="nsew")
        
    def recal_1():
        frame6.grid()
    
    def recal_2():
        frame5.grid()
            
    def recal_3():
        frame4.grid()
            
    def recal_4():
        frame3.grid()
            
    def recal_5():
        frame2.grid()
        
    def savee_5():
            if (a1.get()!='') and (class1_name.get('1.0', 'end-1c')!='') and (class1_name1.get('1.0', 'end-1c')!=''):
                messagebox.showinfo(title="Submitted", message=f"Sports and {a1.get()} Data Submitted!")
                second()
                frame5.grid_remove()
            else:
                messagebox.showerror('Error', 'Check Details!')

    def savee_4():

        if (a2.get()!='') and (b2.get()!='') and (class2_name.get('1.0', 'end-1c')!='') and (class2out_name.get('1.0', 'end-1c')!=''):
            if (radio_var2.get()=='Yes') and (d2.get()==''):
                messagebox.showerror('Error','check Details!')
            else:
                messagebox.showinfo(title="Submitted", message=f"Art Data Submitted!")
                third()
                frame4.grid_remove()
        else:
            messagebox.showerror('Error','Check Details!')
                
    def savee_3():
        if (a3.get()!='') and (b3.get()!='') and (class3_name.get('1.0', 'end-1c')!='') and (class3out_name.get('1.0', 'end-1c')!=''):
            if (radio_var3.get()=='Yes') and (d3.get()==''):
                messagebox.showerror('Error','check Details!')
            else:
                messagebox.showinfo(title="Submitted", message=f"Computer Data Submitted!")
                fourth()
                frame3.grid_remove()
        else:
            messagebox.showerror('Error','Check Details!')
        
        
    def savee_2():
        ques.configure(cursor="exchange")
        ques.configure(cursor="exchange")
        global stud_name
        global st
        if (a4.get()!='') and (b4.get()!='') and (class4_name.get('1.0', 'end-1c')!='') and (class4out_name.get('1.0', 'end-1c')!=''):
            if (radio_var4.get()=='Yes') and (d4.get()==''):
                messagebox.showerror('Error',"Check Details Again!", master=ques)
                ques.configure(cursor="arrow")
            else: 
                m5 = messagebox.askquestion(title="Submit", message="Are You Sure to Submit ?")
                if(m5=='yes'):
                    frame1.configure(cursor="exchange")
                    time.sleep(1)
                    server = mail.SMTP_SSL('smtp.gmail.com','465')
                    server.login(user_id, password_id)
                    cur.execute(f"""INSERT INTO STUDENTS VALUES ('{datetime.date.today().strftime('%Y-%m-%d')}',
                                "{st.get()}",
                                "{te.get()}",
                                "{Activity_name.get('1.0', 'end-1c')}",
                                "{radio_var1.get()}",
                                "{d1.get()}",
                                "{a1.get()}",
                                "{class1_name.get('1.0', 'end-1c')}",
                                "{class1_name1.get('1.0', 'end-1c')}");
                                """)
                    cur.execute(f"""INSERT INTO CLASSES VALUES("{today.strftime('%Y-%m-%d')}",
                                "{st.get()}",
                                "Art",
                                "{a2.get()}",
                                "{b2.get()}",
                                "{stud['Art'][st.get()]}",
                                "{class2_name.get('1.0', 'end-1c')}",
                                "{class2out_name.get('1.0', 'end-1c')}",
                                "{radio_var2.get()}",
                                "{d2.get()}"),
                                ("{today.strftime('%Y-%m-%d')}",
                                "{st.get()}",
                                "Computer",
                                "{a3.get()}",
                                "{b3.get()}",
                                "{stud['Computer'][st.get()]}",
                                "{class3_name.get('1.0', 'end-1c')}",
                                "{class3out_name.get('1.0', 'end-1c')}",
                                "{radio_var3.get()}",
                                "{d3.get()}"),
                                ("{today.strftime('%Y-%m-%d')}",
                                "{st.get()}",
                                "Spl. Education",
                                "{a4.get()}",
                                "{b4.get()}",
                                "{stud['Special Ed.'][st.get()]}",
                                "{class4_name.get('1.0', 'end-1c')}",
                                "{class4out_name.get('1.0', 'end-1c')}",
                                "{radio_var4.get()}",
                                "{d4.get()}")
                                """)
                    message = EmailMessage()
                    message['From'] = user_id
                    message['To'] = ['abinash01562421@gmail.com','abinash01562421@outlook.com']
                    message['Cc'] = 'abinash01562421@gmail.com'
                    message['Subject'] = f"{st.get()} Feedback for {datetime.date.today().strftime('%d/%m/%Y')}"                                
                    body = (f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Colours</title>
                    
                            </head>
                            <body>
                                <h2> Student Name: {st.get()}<br>
                                    Assigned Staff: {te.get()}</h2><br>
                                <h3 style="color:darkblue; margin-bottom: -15px;"> Activity Hour details <br>
                                ---------------------------</h3>
                                <p style="line-height:20px;">
                                <b>Teacher       :</b> {te.get()}<br>
                                <b>Student       :</b> {st.get()}<br>
                                <b>Activity      :</b> {Activity_name.get('1.0', 'end-1c')}<br>
                                <b>Resource Used :</b> {radio_var1.get()}<br>
                                <b>Used Resource :</b> {d1.get()}
                                </p><br>
                                
                                <h3 style="color:darkblue; margin-bottom: -15px;"> 1st Hour details<br>
                                ------------------------</h3>
                                <p><b style="margin: 0px;">Subject       :</b> {a1.get()}<br>
                                <b>Activity      :</b> {class1_name.get('1.0', 'end-1c')}
                                </p><br>

                                <h3 style="color:darkblue; margin-bottom: -15px;"> Sports Hour details <br>
                                --------------------------</h3>
                                <p>
                                <b>Activity      :</b> {class1_name1.get('1.0', 'end-1c')}
                                </p><br>

                                <h3 style="color:darkblue; margin-bottom: -15px;"> Art Hour details <br>
                                ---------------------</h3>
                                <p>
                                <b>Teacher       :</b> {a2.get()}<br>
                                <b>Lesson Plan No:</b> {b2.get()}<br>
                                <b>Level         :</b> {stud['Art'][st.get()]}<br>
                                <b>Activity      :</b> {class2_name.get('1.0', 'end-1c')}<br>
                                <b>Outcome       :</b> {class2out_name.get('1.0', 'end-1c')}<br>
                                <b>Resource Used ?:</b> {radio_var2.get()}<br>
                                <b>Used Resource :</b> {d2.get()}
                                </p><br>
                            <h3 style="color:darkblue; margin-bottom: -15px;"> Computer Hour details <br>
                                -----------------------------</h3>
                                <p>
                                <b>Teacher       :</b> {a3.get()}<br>
                                <b>Lesson Plan No:</b> {b3.get()}<br>
                                <b>Level         :</b> {stud['Computer'][st.get()]}<br>
                                <b>Activity      :</b> {class3_name.get('1.0', 'end-1c')}<br>
                                <b>Outcome       :</b> {class3out_name.get('1.0', 'end-1c')}<br>
                                <b>Resource Used?:</b> {radio_var3.get()}<br>
                                <b>Used Resource :</b> {d3.get()}
                                </p><br>

                                <h3 style="color:darkblue; margin-bottom: -15px;"> Special Education Hour details <br>
                                ------------------------------------</h3>
                                <p><b>Teacher       :</b> {a4.get()}<br>
                                <b>Lesson Plan No:</b> {b4.get()}<br>
                                <b>Level         :</b> {stud['Special Ed.'][st.get()]}<br>
                                <b>Activity      :</b> {class4_name.get('1.0', 'end-1c')}<br>
                                <b>Outcome       :</b> {class4out_name.get('1.0', 'end-1c')}<br>
                                <b>Resource Used?:</b> {radio_var4.get()}<br>
                                <b>Used Resource :</b> {d4.get()}<br>
                                <h4> {len(students)-1} Students Pending.</h4>
                                </p>
                            </body>
                            </html>
                """)
                    message.add_alternative(body, subtype='html')
                    server.sendmail(user_id, recipient, message.as_string())
                    messagebox.showinfo(title="Submitted", message="Special Education Data Updated!", master=ques)
                    temp = students.index(st.get())
                    students.pop(temp)
                    stud_name.configure(values=students)
                    st.set(students[0])
                    a1.set('')
                    a2.set('')
                    a3.set('')
                    a4.set('')
                    b1.set('')
                    b2.set('')
                    b3.set('')
                    b4.set('')
                    d1.set('')
                    d2.set('')
                    d3.set('')
                    d4.set('')
                    te.set(teachers[0])
                    radio_var1.set('No')
                    radio_var2.set('No')
                    radio_var3.set('No')
                    radio_var4.set('No')
                    Activity_name.delete('1.0', 'end-1c')
                    class1_name.delete('1.0', 'end-1c')
                    class1_name1.delete('1.0', 'end-1c')
                    class2_name.delete('1.0', 'end-1c')
                    class2out_name.delete('1.0', 'end-1c')
                    class3_name.delete('1.0', 'end-1c')
                    class3out_name.delete('1.0', 'end-1c')
                    class3_name.delete('1.0', 'end-1c')
                    class3out_name.delete('1.0', 'end-1c')
                    stud2_lev_nam.configure(text='')
                    stud3_lev_nam.configure(text='')
                    stud4_lev_nam.configure(text='')      
                    frame1.grid()
                    frame2.grid()
                    frame3.grid()
                    frame4.grid()
                    frame5.grid()
                    frame6.grid()
                    ques.configure(cursor="arrow")
                else:
                    frame1.grid()
                    ques.configure(cursor="arrow")
        else:
            messagebox.showerror('Error', 'Check Details Again!', master=ques)
            ques.configure(cursor="arrow")

    def savee():
            if (te.get()!='') and (st.get()!='') and (Activity_name.get('1.0', 'end-1c')!=''):
                if  (radio_var1.get()=='Yes')and (d1.get()==''):
                    messagebox.showerror('Error', 'Check Details!')
                else:
                    messagebox.showinfo("Submitted","Activity Data Submitted!")
                    first()
                    frame6.grid_remove()
            else:
                messagebox.showerror('Error', 'Check Details!')

    def rootback():
        ques.withdraw()
        root.deiconify()
        root.grab_set()

## Activity Window
    def activity():
        global Activity_name
        global stud_name
        global st
        def opt():
            if (radio_var1.get()=="Yes"):
                Resource1_usedent.configure(state= "normal")
                d1.set('')
                Resource1_usedent.focus()
            else:
                d1.set("Nil")
                Resource1_usedent.configure(state= "disabled")
        label_0 = ctk.CTkLabel(frame6, text="Activity   Details", width=620, height=40, font=("Times New Roman", 30, "bold"), corner_radius=50)
        label_0.grid(row=0, column=0, columnspan=4, padx=(70,10), pady=(40,40), sticky="")

        teach_lab = ctk.CTkLabel(frame6, text="Teacher :", font=("Times New Roman", 16, "bold"))
        teach_lab.grid(row=1, column=0, sticky="w", padx=(20,0))

        teach_name = ctk.CTkOptionMenu(frame6,  font=option_font, variable =te, values=teachers, fg_color='#5b7878')
        teach_name.grid(row=1, column=0, columnspan=2, padx=100, sticky="w")

        stud_lab = ctk.CTkLabel(frame6, text="Student :", font=("Times New Roman", 16, "bold"))
        stud_lab.grid(row=1, column=1, padx=(300,10))

        stud_name = ctk.CTkOptionMenu(frame6, font=option_font, variable=st, values=students, fg_color=option_clr)
        stud_name.grid(row=1, column=2, padx=(0,10))

        Activity_lab = ctk.CTkLabel(frame6, text="Activity :", font=("Times New Roman", 16, "bold"))
        Activity_lab.grid(row=2, column=0, sticky="nw", padx=(20,10), pady=(30,10))

        Activity_name = ScrolledText(frame6, wrap=tk.WORD, width=75, height=11, font=scr_font)
        Activity_name.grid(row =2, columnspan=3, column=0, sticky="w", padx=(125,20), pady=(40,10))
        
        Resource1_lab = ctk.CTkLabel(frame6, text="Resource Used : ", font=("Times New Roman", 16, "bold"))
        Resource1_lab.grid(row=3, column=0, sticky="w", padx=(20,10), pady=(10,10))

        Resource1_value = ctk.CTkRadioButton(frame6, text="Yes",fg_color = '#35B637', border_width_checked=6,
                                                 variable= radio_var1, command=opt, value="Yes")
        Resource2_value = ctk.CTkRadioButton(frame6, text="No", fg_color = '#F36A45', border_width_checked=6,
                                                 variable= radio_var1, command=opt, value="No")
        
        Resource1_value.grid(row=3, columnspan=2, column=1, sticky="w", padx=30, pady=(10,10))
        Resource2_value.grid(row=3, column=1, sticky="w", padx=(200,10), pady=(10,10))

        Resource1_used = ctk.CTkLabel(frame6, text="Mention Used Resources : ", font=("Times New Roman", 16, "bold"))
        Resource1_used.grid(row=4, column = 0, columnspan=2, sticky="w", padx=(20,10), pady=(30,10))

        Resource1_usedent = ctk.CTkEntry(frame6, font = rsc_font, textvariable = d1, width=460)
        Resource1_usedent.grid(row=4, column=1, columnspan=3, sticky="w", padx=(60,10), pady=(30,10))

        te.set(teachers[0])
        st.set(students[0])
        Resource1_usedent.configure(state='disabled')
        d1.set("Nil")
            
        page_lab1 = ctk.CTkLabel(frame6, text="Page 1 of 5", font=("times new roman", 12, "italic"))
        page_lab1.grid(row=5, columnspan=3, sticky="se", padx=(0,10))

        exit_but1 = ctk.CTkButton(frame6, text="Exit", font=('Georgia',12, 'bold'), command = rootback)
        exit_but1.grid(row=6, columnspan=2, padx=(100,0), pady=(10,10), sticky="w")

        save_but1 = ctk.CTkButton(frame6, text="Next", font=('Georgia',12, 'bold'), command=savee)
        save_but1.grid(row=6, columnspan=2, column=1, padx=(60,80), pady=(10,10), sticky="e")
    
## 1st Hour Window
    def first():
        global class1_name
        global class1_name1
        
        label_1 = ctk.CTkLabel(frame5, text="1st Hour Details", bg_color=glossy_clr, font=("Times New Roman", 26, "bold"), corner_radius=5)
        label_1.grid(row=0, column=0, columnspan=2, padx=(30,0), pady=(40,40), sticky="nsew")

        sub_lab = ctk.CTkLabel(frame5, text="Subject :", font=("Times New Roman", 16, "bold"))
        sub_lab.grid(row=1, column=0, sticky="w", padx=(10,5))

        sub_name = ctk.CTkOptionMenu(frame5, width=150, font=option_font, fg_color=option_clr, variable =a1, values=("Yoga", "Drama", "S.T.E.M", "Dance", "Pottery"))
        sub_name.grid(row=1, column=0, columnspan=2, padx=(80,19),sticky="w")

        class1_lab = ctk.CTkLabel(frame5, text="Class Activity :", font=("Times New Roman", 16, "bold"))
        class1_lab.grid(row=2, column=0, sticky="w", padx=(10,5), pady=(20,5))

        class1_name = ScrolledText(frame5, wrap=tk.WORD, font=scr_font, width=35, height=17)
        class1_name.grid(row =3, columnspan=2, column=0, sticky="w", ipadx=5, padx=(50,20), pady=(5,5))

        label_2 = ctk.CTkLabel(frame5, text="Sports Details", fg_color=glossy_clr, font=("Times New Roman", 26, "bold"), corner_radius=5)
        label_2.grid(row=0, column=2, columnspan=2, padx=(10,10), pady=(40,40), sticky="nsew")

        class1_lab1 = ctk.CTkLabel(frame5, text="Class Activity :", font=("Times New Roman", 16, "bold"))
        class1_lab1.grid(row=2, column=2, sticky="w", padx=(40,5), pady=(20,5))

        class1_name1 = ScrolledText(frame5 ,wrap=tk.WORD, font=scr_font, width=35, height=17)
        class1_name1.grid(row =3, columnspan=2, column=2, sticky="w", ipadx=5, padx=(68,20), pady=8)
        
        page_lab11 = ctk.CTkLabel(frame5, text="Page 2 of 5", font=("times new roman", 12, "italic"))
        page_lab11.grid(row=4, columnspan=4, sticky="se", padx=(0,15), pady=(6,0))

        back_but111 = ctk.CTkButton(frame5, text="Back", font = button_font, command = recal_1)
        back_but111.grid(row=5, column=0, columnspan=2, padx=(80,0), pady=(10,10), sticky="sw")

        save_but111 = ctk.CTkButton(frame5, text="Next", font = button_font, command=savee_5)
        save_but111.grid(row=5, column=3, padx=(0,70), pady=(10,10), stick="se")

## 2nd Hour Window
    def second():
        global class2_name
        global class2out_name
        global Resource2_usedent
        global stud2_lev_nam
        global d2
        
        def opt():
            if (radio_var2.get()=="Yes"):
                Resource2_usedent.configure(state= "normal")
                d2.set('')
                Resource2_usedent.focus()
            else:
                d2.set("Nil")
                Resource2_usedent.configure(state= "disabled")
        
        label_2 = ctk.CTkLabel(frame4, text="Art Hour Details", bg_color=glossy_clr, width=620, height=10,font=("Times New Roman", 26, "bold"), corner_radius=5)
        label_2.grid(row=0, column=0, columnspan=4, padx=(10,0),pady=(40,40), sticky="nsew")

        sub2_lab = ctk.CTkLabel(frame4, text="Teacher :", font=("Times New Roman", 16, "bold"))
        sub2_lab.grid(row=1, column=0, sticky="w", padx=(30,5))

        sub2_name = ctk.CTkOptionMenu(frame4, font=option_font, fg_color=option_clr, width=150, variable =a2, values=teachers)
        sub2_name.grid(row=1, column=0, columnspan=2, padx=(110,20),sticky="w")

        stud2_les_lab = ctk.CTkLabel(frame4, text="Lesson No :", font=("Times New Roman", 16, "bold"))
        stud2_les_lab.grid(row=1, column=1, padx=(150,10), sticky='w')
        
        stud2_les_name = ctk.CTkOptionMenu(frame4, dropdown_font=('Times New', 10,'bold'), font=option_font, fg_color=option_clr, variable = b2, width=60, values=lesson_no)
        stud2_les_name.grid(row=1, column=1, padx=(240,30), columnspan=2, sticky="w")

        stud2_lev_lab = ctk.CTkLabel(frame4, text="Level :", font=("Times New Roman", 16, "bold"))
        stud2_lev_lab.grid(row=1, column=2, padx=(120,10), sticky='w')

        stud2_lev_nam = ctk.CTkLabel(frame4, text=f"{stud['Art'][st.get()]}", font=("Times New Roman", 16, "bold"))
        stud2_lev_nam.grid(row=1, column=2, columnspan=3, padx=(180,10), sticky='w')

        class2_lab = ctk.CTkLabel(frame4, text="Class Activity :", font=("Times New Roman", 16, "bold"))
        class2_lab.grid(row=2, column=0, sticky="nw", padx=(30,5), pady=(20,5))

        class2_name = ScrolledText(frame4, wrap=tk.WORD, font=scr_font, width=35, height=12)
        class2_name.grid(row =3, columnspan=3, column=0, sticky="w", ipadx=5, padx=(45,20), pady=(5,5))

        class2out_lab = ctk.CTkLabel(frame4, text="Class Outcome :", font=("Times New Roman", 16, "bold"))
        class2out_lab.grid(row=2, column=2, columnspan=2,sticky="w", padx=(10,5), pady=(20,5))

        class2out_name = ScrolledText(frame4, wrap=tk.WORD, font=scr_font, width=35, height=12)
        class2out_name.grid(row =3, columnspan=3, column=2, sticky="w", ipadx=5, padx=(15,10), pady=(5,5))
        
        Resource2_lab = ctk.CTkLabel(frame4, text="Resource Used : ", font=("Times New Roman", 16, "bold"))
        Resource2_lab.grid(row=4, column=0, sticky="w", padx=(30,10), pady=(10,10))

        Resource12_value = ctk.CTkRadioButton(frame4, text="Yes", fg_color = '#35B637', command=opt, border_width_checked=6,
                                                 variable= radio_var2, value="Yes")
        Resource22_value = ctk.CTkRadioButton(frame4, text="No", fg_color = '#F36A45', command=opt, border_width_checked=6,
                                                 variable= radio_var2, value="No")
        
        Resource12_value.grid(row=4, columnspan=2, column=1, sticky="w", padx=10, pady=(10,10))
        Resource22_value.grid(row=4, column=2, sticky="w", padx=(30,10), pady=(10,10))

        Resource2_used = ctk.CTkLabel(frame4, text="Mention Used Resources : ", font=("Times New Roman", 16, "bold"))
        Resource2_used.grid(row=5, column = 0, columnspan=2, sticky="w", padx=(30,10), pady=(10,10))

        Resource2_usedent = ctk.CTkEntry(frame4, font = rsc_font, width=420, textvariable=d2)
        Resource2_usedent.grid(row=5, column=1, columnspan=3, sticky="w", padx=(80,10), pady=(10,10))

        d2.set("Nil")
        
        page_lab2 = ctk.CTkLabel(frame4, text="Page 3 of 5", font=("times new roman", 12, "italic"))
        page_lab2.grid(row=6, column=3, sticky="se", padx=(10,0), pady=(2,0))

        back_but12 = ctk.CTkButton(frame4, text="Back", font = button_font, command = recal_2)
        back_but12.grid(row=7, columnspan=2, pady=(10,10))

        save_but12 = ctk.CTkButton(frame4, text="Next", font = button_font, command=savee_4)
        save_but12.grid(row=7, columnspan=2, column=2, pady=(10,10))

        Resource2_usedent.configure(state='disabled')
        
## 3rd Hour Window
    def third():
        global class3_name
        global class3out_name
        global Resource3_usedent
        global stud3_lev_nam
        def opt():
            if (radio_var3.get()=="Yes"):
                Resource3_usedent.configure(state= "normal")
                d3.set('')
                Resource3_usedent.focus()
            else:
                d3.set("Nil")
                Resource3_usedent.configure(state= "disabled")
                
        label_3 = ctk.CTkLabel(frame3, text="Computer Hour Details", bg_color=glossy_clr, width=50, height=10,font=("Times New Roman", 26, "bold"), corner_radius=5)
        label_3.grid(row=0, column=0, columnspan=4, padx=(10,0),pady=(40,40), sticky="nsew")

        sub3_lab = ctk.CTkLabel(frame3, text="Teacher :", font=("Times New Roman", 16, "bold"))
        sub3_lab.grid(row=1, column=0, sticky="w", padx=(30,5))

        sub3_name = ctk.CTkOptionMenu(frame3, font=option_font, fg_color=option_clr, width=150, variable =a3, values=teachers)
        sub3_name.grid(row=1, column=0, columnspan=2, padx=(110,20),sticky="w")

        stud3_les_lab = ctk.CTkLabel(frame3, text="Lesson No :", font=("Times New Roman", 16, "bold"))
        stud3_les_lab.grid(row=1, column=1, padx=(150,10), sticky='w')
        
        stud3_les_name = ctk.CTkOptionMenu(frame3, dropdown_font=('Times New', 10,'bold'), font=option_font, fg_color=option_clr, variable =b3, width=60, values=lesson_no)
        stud3_les_name.grid(row=1, column=1, padx=(240,30), columnspan=2, sticky="w")

        stud3_lev_lab = ctk.CTkLabel(frame3, text="Level :", font=("Times New Roman", 16, "bold"))
        stud3_lev_lab.grid(row=1, column=2, padx=(120,10), sticky='w')

        stud3_lev_nam = ctk.CTkLabel(frame3, text=f"{stud['Computer'][st.get()]}", font=("Times New Roman", 16, "bold"))
        stud3_lev_nam.grid(row=1, column=2, columnspan=3, padx=(180,10), sticky='w')

        class3_lab = ctk.CTkLabel(frame3, text="Class Activity :", font=("Times New Roman", 16, "bold"))
        class3_lab.grid(row=2, column=0, sticky="nw", padx=(30,5), pady=(20,5))

        class3_name = ScrolledText(frame3, wrap=tk.WORD, font=scr_font, width=35, height=12)
        class3_name.grid(row =3, columnspan=3, column=0, sticky="w", ipadx=5, padx=(45,20), pady=(5,5))

        class3out_lab = ctk.CTkLabel(frame3, text="Class Outcome :", font=("Times New Roman", 16, "bold"))
        class3out_lab.grid(row=2, column=2, columnspan=2,sticky="w", padx=(10,5), pady=(20,5))

        class3out_name = ScrolledText(frame3, wrap=tk.WORD, font=scr_font, width=35, height=12)
        class3out_name.grid(row =3, columnspan=3, column=2, sticky="w", ipadx=5, padx=(15,10), pady=(5,5))
        
        Resource3_lab = ctk.CTkLabel(frame3, text="Resource Used : ", font=("Times New Roman", 16, "bold"))
        Resource3_lab.grid(row=4, column=0, sticky="w", padx=(30,10), pady=(10,10))

        Resource13_value = ctk.CTkRadioButton(frame3, text="Yes", fg_color = '#35B637', command=opt, border_width_checked=6,
                                                 variable= radio_var3, value="Yes")
        Resource23_value = ctk.CTkRadioButton(frame3, text="No", fg_color = '#F36A45', command=opt, border_width_checked=6,

                                                 variable= radio_var3, value="No")
        
        Resource13_value.grid(row=4, columnspan=2, column=1, sticky="w", padx=10, pady=(10,10))
        Resource23_value.grid(row=4, column=2, sticky="w", padx=(30,10), pady=(10,10))
        
        Resource3_used = ctk.CTkLabel(frame3, text="Mention Used Resources : ", font=("Times New Roman", 16, "bold"))
        Resource3_used.grid(row=5, column = 0, columnspan=2, sticky="w", padx=(30,10), pady=(10,10))

        Resource3_usedent = ctk.CTkEntry(frame3, font = rsc_font, width=420, textvariable=d3)
        Resource3_usedent.grid(row=5, column=1, columnspan=3, sticky="w", padx=(80,10), pady=(10,10))

        d3.set("Nil")
        
        page_lab3 = ctk.CTkLabel(frame3, text="Page 4 of 5", font=("times new roman", 12, "italic"))
        page_lab3.grid(row=6, column=3, sticky="se", padx=(10,0), pady=(2,0))

        back_but13 = ctk.CTkButton(frame3, text="Back", font = button_font, command = recal_3)
        back_but13.grid(row=7, columnspan=2, pady=(10,10))

        save_but13 = ctk.CTkButton(frame3, text="Next", font = button_font, command=savee_3)
        save_but13.grid(row=7, columnspan=2, column=2, pady=(10,10))

        Resource3_usedent.configure(state='disabled')

## 4th Hour Window
    def fourth():
        global class4_name
        global class4out_name
        global Resource4_usedent
        global stud4_lev_nam

        def opt():
            if (radio_var4.get()=="Yes"):
                Resource4_usedent.configure(state= "normal")
                d4.set('')
                Resource4_usedent.focus()
            else:
                d4.set("Nil")
                Resource4_usedent.configure(state= "disabled")
        
        label_4 = ctk.CTkLabel(frame2, text="Special Education Hour Details", bg_color=glossy_clr, width=50, height=10,font=("Times New Roman", 26, "bold"), corner_radius=5)
        label_4.grid(row=0, column=0, columnspan=4, padx=(10,0),pady=(40,40), sticky="nsew")

        sub4_lab = ctk.CTkLabel(frame2, text="Teacher :", font=("Times New Roman", 16, "bold"))
        sub4_lab.grid(row=1, column=0, sticky="w", padx=(30,5))

        sub4_name = ctk.CTkOptionMenu(frame2, font=option_font, fg_color=option_clr, width=150, variable =a4, values=teachers)
        sub4_name.grid(row=1, column=0, columnspan=2, padx=(110,20),sticky="w")

        stud4_les_lab = ctk.CTkLabel(frame2, text="Lesson No :", font=("Times New Roman", 16, "bold"))
        stud4_les_lab.grid(row=1, column=1, padx=(150,10), sticky='w')
        
        stud4_les_name = ctk.CTkOptionMenu(frame2, dropdown_font=('Times New', 10,'bold'), font=option_font, fg_color=option_clr, variable =b4, width=60, values=lesson_no)
        stud4_les_name.grid(row=1, column=1, padx=(240,30), columnspan=2, sticky="w")

        stud4_lev_lab = ctk.CTkLabel(frame2, text="Level :", font=("Times New Roman", 16, "bold"))
        stud4_lev_lab.grid(row=1, column=2, padx=(120,10), sticky='w')

        stud4_lev_nam = ctk.CTkLabel(frame2, text=f"{stud['Special Ed.'][st.get()]}", font=("Times New Roman", 16, "bold"))
        stud4_lev_nam.grid(row=1, column=2, columnspan=3, padx=(180,10), sticky='w')

        class4_lab = ctk.CTkLabel(frame2, text="Class Activity :", font=("Times New Roman", 16, "bold"))
        class4_lab.grid(row=2, column=0, sticky="nw", padx=(30,5), pady=(20,5))

        class4_name = ScrolledText(frame2, wrap=tk.WORD, font=scr_font, width=35, height=12)
        class4_name.grid(row =3, columnspan=3, column=0, sticky="w", ipadx=5, padx=(45,20), pady=(5,5))

        class4out_lab = ctk.CTkLabel(frame2, text="Class Outcome :", font=("Times New Roman", 16, "bold"))
        class4out_lab.grid(row=2, column=2, columnspan=2,sticky="w", padx=(10,5), pady=(20,5))

        class4out_name = ScrolledText(frame2, wrap=tk.WORD, font=scr_font, width=35, height=12)
        class4out_name.grid(row =3, columnspan=3, column=2, sticky="w", ipadx=5, padx=(15,10), pady=(5,5))
        
        Resource4_lab = ctk.CTkLabel(frame2, text="Resource Used : ", font=("Times New Roman", 16, "bold"))
        Resource4_lab.grid(row=4, column=0, sticky="w", padx=(30,10), pady=(10,10))

        Resource14_value = ctk.CTkRadioButton(frame2, text="Yes", fg_color = '#35B637', command=opt, border_width_checked=6,
                                                 variable= radio_var4, value="Yes")
        Resource24_value = ctk.CTkRadioButton(frame2, text="No", fg_color = '#F36A45', command=opt, border_width_checked=6,

                                                 variable= radio_var4, value="No")
        
        Resource14_value.grid(row=4, columnspan=2, column=1, sticky="w", padx=10, pady=(10,10))
        Resource24_value.grid(row=4, column=2, sticky="w", padx=(30,10), pady=(10,10))

        Resource4_used = ctk.CTkLabel(frame2, text="Mention Used Resources : ", font=("Times New Roman", 16, "bold"))
        Resource4_used.grid(row=5, column = 0, columnspan=2, sticky="w", padx=(30,10), pady=(10,10))

        Resource4_usedent = ctk.CTkEntry(frame2, font = rsc_font, width=420, textvariable=d4)
        Resource4_usedent.grid(row=5, column=1, columnspan=3, sticky="w", padx=(80,10), pady=(10,10))

        d4.set("Nil")
        
        page_lab4 = ctk.CTkLabel(frame2, text="Page 5 of 5", font=("times new roman", 12, "italic"))
        page_lab4.grid(row=6, column=3, sticky="se", padx=(20,0), pady=(2,0))

        back_but14 = ctk.CTkButton(frame2, text="Back", font = button_font, command = recal_4)
        back_but14.grid(row=7, columnspan=2, pady=(10,10))

        save_but14 = ctk.CTkButton(frame2, text="Next", font = button_font, command=savee_2)
        save_but14.grid(row=7, columnspan=2, column=2, pady=(10,10))
        
    activity()
    ques.protocol("WM_DELETE_WINDOW", root.destroy)
    
def help():
    new=ctk.CTkToplevel()
    new.title("Help")
    window_height = 150
    window_width = 200
    pos_top = int(disp_height//2 - window_height//2)
    pos_right = int(disp_width//2 - window_width//2)
    new.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
    new.resizable(False, False)
    new.iconbitmap('icons/help.ico')
    if platform.startswith("win"):
        new.after(200, lambda: new.iconbitmap("icons/help.ico"))
    new.grab_set()
    des1 = ctk.CTkLabel(new, text='Director',font=font)
    name1 = ctk.CTkLabel(new, text='Bella Joshi', font=scr_font)
    num1 = ctk.CTkLabel(new, text='+91 9876543210', font=scr_font)
    des1.grid(row=0, column=0, columnspan=2, sticky='nsew')
    name1.grid(row=1, column=0, padx=15, pady=10, sticky='e')
    num1.grid(row =1, column = 1)
    des2 = ctk.CTkLabel(new, text='Developer', font=font)
    name2 = ctk.CTkLabel(new, text='Abinash', font=scr_font)
    num2 = ctk.CTkLabel(new, text='+91 63824 82617', font=scr_font)
    des2.grid(row=2, column=0, columnspan=2, sticky='nsew')
    name2.grid(row=3, column=0, padx=15, pady=10, sticky='e')
    num2.grid(row =3, column = 1)
    
    new.protocol("WM_DELETE_WINDOW", new.destroy)
    new.mainloop()

def view_prod():
    global prod
    prod = ctk.CTkToplevel()
    prod.grab_set()
    prod.config(cursor="exchange") 
    global frame1
    global frame2
    window_height = 700
    window_width = 850
    pos_top = int(disp_height//2 - window_height//2)
    pos_right = int(disp_width//2 - window_width//2)
    prod.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
    prod.resizable(False, False)
    prod.title("For Sale")
    
    prod.iconbitmap('icons/view.ico')
    if platform.startswith("win"):
        prod.after(200, lambda: prod.iconbitmap("icons/view.ico"))

    def back():
        prod.destroy()
        adminn.deiconify()
        
    def update(a,b,c,d,e):
        global pro
        prod.config(cursor='exchange')
        try:    
            code= a
            sold_price = int(b)
            sold_place = c
            sold_date = d
            sold_date1 = sold_date.split('/')
            date = int(sold_date1[0])
            month = int(sold_date1[1])
            year = int(sold_date1[2])
            sold_date1 = datetime.date(year, month, date)
            sold_date = sold_date1.strftime('%Y-%m-%d')
            sold_date1 = datetime.date(year, month, date)
            if (sold_date1<=today) and (sold_place!='') and (type(sold_price)==type(int())):
                if (sold_date1<=today):
                    cur.execute(f"UPDATE {str(pro)} SET STATUS='SOLD', SOLD_PRICE={sold_price}, PLACE='{sold_place}', SOLD_DATE='{sold_date}' WHERE IMG_ID='{code}';")
                    confirm.destroy()
                    messagebox.showinfo('Success', f"{code} Updated")
                    prod.config(cursor='arrow')
                    functio(e)
                else:
                    prod.config(cursor='arrow')
                    messagebox.showerror('Error','Check Sold Date!', master=confirm)
            else:
                prod.config(cursor='arrow')
                messagebox.showerror('Error', 'Check again!', master=confirm)
        except Exception as e:
            prod.config(cursor='arrow')
            messagebox.showerror('Error', 'Check Details again!', master=confirm)
        
    def checkk(a,i, c):
        global code
        global p_date_ent
        global confirm
        code=f'{i[a]}'
        if a==1:
            confirm = ctk.CTk(blue_clr)
            window_height = 250
            window_width = 350
            pos_top = int(disp_height//2 - window_height//2)
            pos_right = int(disp_width//2 - window_width//2)
            confirm.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
            confirm.title(f"Update {code}")
            frame1 = ctk.CTkFrame(confirm,fg_color=blue_clr)
            p_code_lab = ctk.CTkLabel(frame1, text="Product Code :", font=font)
            p_code_ent = ctk.CTkLabel(frame1, text=f"{i[1]}", font=scr_font)
            p_price_lab = ctk.CTkLabel(frame1, text="Price :",font=font)
            p_price_ent = ctk.CTkEntry(frame1, textvariable=sold_price)
            p_event_lab = ctk.CTkLabel(frame1, text="Event :", font=font)
            p_event_ent = ctk.CTkEntry(frame1, textvariable=sold_place)
            p_date_lab = ctk.CTkLabel(frame1, text="Date (DD/MM/YYYY) :", font=font)
            p_date_ent = ctk.CTkEntry(frame1, textvariable=sold_date)
            but = ctk.CTkButton(frame1, text='Update', width=10, font=button_font, command=lambda k=i: update(i[1],p_price_ent.get(),p_event_ent.get(),p_date_ent.get(), c), hover_color=glossy_clr)
            p_code_lab.grid(padx=10, pady=10, row=0, column=0, sticky='w')
            p_code_ent.grid(padx=10, pady=10, row=0, column=1)
            p_price_lab.grid(padx=10, pady=10, row=1, column=0, sticky='w')
            p_price_ent.grid(padx=10, pady=10, row=1, column=1)
            p_event_lab.grid(padx=10, pady=10, row=2, column=0, sticky='w')
            p_event_ent.grid(padx=10, pady=10, row=2, column=1)
            p_date_lab.grid(padx=10, pady=10, row=3, column=0, sticky='w')
            p_date_ent.grid(padx=10, pady=10, row=3, column=1)
            but.grid(padx=100, pady=10, row=4, columnspan=2, sticky="nsew")
            frame1.grid(padx=10, sticky='nsew')
            def rec():
                confirm.configure(cursor='exchange')
                functio(c)
                confirm.destroy()
               
            confirm.protocol("WM_DELETE_WINDOW", rec)
            confirm.mainloop()
        else:
            pass
        
    def functio(a):
        global frame1
        global frame2
        global check
        global l
        global pro
        global chk_val
        global adminn
        prod.configure(cursor='exchange')
        frame2.destroy()
        adminn.withdraw()
        b=[]
        m=[]
        no=1
        frame2 = ctk.CTkScrollableFrame(prod, fg_color=glossy_clr, width=800, height=530, border_width=1)
        if a=="Lippan Art":
            pro="LA"
        elif a=="Bottle Art":
            pro="BA"
        elif a=="Jaipur Art":
            pro="JA"
        elif a=="Pottery":
            pro="PO"
        else:
            pass
        
        dat = cur.execute(f"Select ID, IMG_ID, STATUS, IMAGE, PRICE, DATE_FORMAT(MADE_DATE,  '%d-%m-%Y') as converted_date from {pro} where status='FOR_SALE' order by MADE_DATE Desc;")
        dat = cur.fetchall()
        for i in dat:
            l=ctk.IntVar()
            mn=ctk.StringVar()
            img = Image.open(io.BytesIO(i[3]))
            img = ctk.CTkImage(img, size=(100,100))
            
            lab = ctk.CTkLabel(frame2, text=no, font=("Times New Roman", 16))
            date = ctk.CTkLabel(frame2, text=i[5], font=("Times New Roman", 16))
            lab_ = ctk.CTkLabel(frame2, text=i[1], font=("Times New Roman", 16))
            price = ctk.CTkLabel(frame2, text=f"₹ {i[4]}", font=("Times New ROman", 16))
            img_lab = ctk.CTkLabel(frame2, image=img, text='')
            check = ctk.CTkCheckBox(frame2, text='',variable=l, command=lambda j=l, k=i: checkk(j.get(), k, pro))

            m.append(check)
            lab.grid(row=no, column=0, padx=(53,33), sticky="nsew")
            date.grid(row=no, column=1, padx=45, sticky="nsew")
            lab_.grid(row=no, column=2, padx=20, sticky="nsew")
            price.grid(row=no, column=4, padx=50, sticky="e")
            img_lab.grid(row=no, column=3, padx=45, pady=5, sticky="nsew")
            check.grid(row=no, column=5, padx=(40,10), sticky="nsew")
            no+=1
        frame2.grid(row=2, padx = 15, pady=10, sticky="nsew")
        prod.configure(cursor='arrow')
        return pro
        
    prod.configure(fg_color=blue_clr)
    dat = cur.execute("Select * from PO;")
    dat = cur.fetchall()
    frame1 = ctk.CTkFrame(prod, fg_color=glossy_clr, width=800, height=100, border_width=1)
    frame2 = ctk.CTkScrollableFrame(prod, fg_color=glossy_clr, width=800, height=530, border_width=1)
    no = ctk.CTkLabel(frame1, text="SL. NO ", font=("Times New Roman", 16, "bold"), width=50, height=30)
    no.grid(row=0,column=0, padx=(50,30), pady=5, sticky="nsew")
    date = ctk.CTkLabel(frame1, text="DATE", font=("Times New Roman", 16, "bold"), height=20)
    date.grid(row=0,column=1, padx=30, pady=5, sticky="nsew")
    ino = ctk.CTkLabel(frame1, text="ITEM NO", font=("Times New Roman", 16, "bold"), height=20)
    ino.grid(row=0,column=2, padx=30, pady=5, sticky="nsew")
    price = ctk.CTkLabel(frame1, text="PRICE", font=("Times New Roman", 16, "bold"), height=20)
    price.grid(row=0,column=4, padx=60, pady=5, sticky="nsew")
    ipic = ctk.CTkLabel(frame1, text="PICTURE", font=("Times New Roman", 16, "bold"), height=20)
    ipic.grid(row=0,column=3, padx=30, pady=5, sticky="nsew")
    stat = ctk.CTkLabel(frame1, text="SOLD", font=("Times New Roman", 16, "bold"), height=20)
    stat.grid(row=0,column=5, padx=30, sticky="E")
    b = []
    chk_val=[]
    sel=[]
    sold_date = ctk.StringVar()
    sold_price = ctk.IntVar()
    sold_place = ctk.StringVar()
    pro=str()

    lab_ = ctk.CTkLabel(frame2, text="Select Valid Product!", font=("Times New Roman", 20), text_color="red")
    lab_.grid(row=3, column=3, padx=300, pady=250, sticky="nsew")

    opt = ctk.CTkLabel(prod, text="Select Product : ", font=font)
    opt.grid(row=0, column=0, padx=(0,200), pady=(10,0), sticky="E")

    opt_ = ctk.CTkOptionMenu(prod, font=option_font, fg_color=option_clr, anchor='center', command=functio, values=['Lippan Art','Bottle Art','Jaipur Art','Pottery'])
    opt_.grid(row=0, column=0, padx=(0,15), pady=(10,0),sticky="E")
    opt_.set("-")

    img_but = ctk.CTkButton(prod, image=back_img, text="", command=back, width=1, height=10, corner_radius=100, fg_color="transparent", hover_color=glossy_clr)
    img_but.grid(row=0, column=0, padx=(15,30), pady=(10,0),  sticky="W")
    
    frame1.grid(row=1, pady=(30,10), padx = 15, sticky="nsew")
    frame2.grid(row=2, padx = 15, pady=10, sticky="nsew")
    adminn.withdraw()
    prod.config(cursor="arrow")
    prod.protocol("WM_DELETE_WINDOW", root.destroy)
    prod.mainloop()

def sold_prod():
    sold = ctk.CTkToplevel()
    sold.grab_set()
    adminn.withdraw()
    window_height = 700
    window_width = 850
    pos_top = int(disp_height//2 - window_height//2)
    pos_right = int(disp_width//2 - window_width//2)
    sold.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
    sold.resizable(False, False)
    sold.title("Sold")
    sold.configure(fg_color=blue_clr)
    sold.iconbitmap('icons/sold.ico')
    if platform.startswith("win"):
        sold.after(200, lambda: sold.iconbitmap("icons/sold.ico"))
        
    global frame1
    global frame2
    frame1 = ctk.CTkFrame(sold, fg_color = glossy_clr, width=800, height=100, border_width=1)
    frame2 = ctk.CTkScrollableFrame(sold, fg_color = glossy_clr, width=800, height=530, border_width=1)
    no = ctk.CTkLabel(frame1, text="SL. NO", font=("Times New Roman", 16, "bold"), width=50, height=30)
    no.grid(row=0,column=0, padx=(20,20), pady=5, sticky="nsew")
    date = ctk.CTkLabel(frame1, text="SOLD DATE", font=("Times New Roman", 16, "bold"), width=50, height=30)
    date.grid(row=0,column=1, padx=(30,30), pady=5, sticky="nsew")
    ino = ctk.CTkLabel(frame1, text="ITEM NO", font=("Times New Roman", 16, "bold"), height=20)
    ino.grid(row=0,column=2, padx=(20,20), pady=5, sticky="nsew")
    place = ctk.CTkLabel(frame1, text="PRODUCT", font=("Times New Roman", 16, "bold"), width=50, height=30)
    place.grid(row=0,column=3, padx=30, pady=5, sticky="nsew")
    price = ctk.CTkLabel(frame1, text="SOLD PRICE", font=("Times New Roman", 16, "bold"), width=50, height=30)
    price.grid(row=0,column=4, padx=(20,50), pady=5, sticky="nsew")
    ipic = ctk.CTkLabel(frame1, text="EVENT", font=("Times New Roman", 16, "bold"), height=20)
    ipic.grid(row=0,column=5, padx=(50,5), sticky="E")

    def back():
        sold.destroy()
        adminn.deiconify()
        
    def stat(val):
        global frame1
        global frame2
        sold.configure(cursor='exchange')
        frame2.destroy()
        b=[]
        no=1
        frame2 = ctk.CTkScrollableFrame(sold, fg_color = glossy_clr, width=800, height=530, border_width=1)
        if val=="Lippan Art":
            val="LA"
        elif val=="Bottle Art":
            val="BA"
        elif val=="Jaipur Art":
            val="JA"
        elif val=="Pottery":
            val="PO"
            
        dat = cur.execute(f"Select IMG_ID, DATE_FORMAT(SOLD_DATE,  '%d-%m-%Y') as converted_date, PLACE, SOLD_PRICE, IMAGE from {val} WHERE STATUS='SOLD' ORDER BY SOLD_DATE desc;")
        dat = cur.fetchall()
        
        for i in dat:
            img = Image.open(io.BytesIO(i[4]))
            img = ctk.CTkImage(img, size=(100,100))
            lab = ctk.CTkLabel(frame2, text=no, font=("Times New Roman", 16), width=50)
            code = ctk.CTkLabel(frame2, text=i[0], font=("Times New Roman", 16))
            date = ctk.CTkLabel(frame2, text=i[1], font=("Times New Roman", 16))
            place = ctk.CTkLabel(frame2, text=i[2], font=("Times New Roman", 16))
            price = ctk.CTkLabel(frame2, text=F"₹ {i[3]}", font=("Times New Roman", 16))
            img = ctk.CTkLabel(frame2, text="", image=img)

            lab.grid(row=no, column=0, padx=(15,28), sticky="w")
            date.grid(row=no, column=1, padx=30, sticky="nsew")
            code.grid(row=no, column=2, padx=(40,30), sticky="nsew")
            img.grid(row=no, column=3, padx=30, pady=5, sticky="nsew")
            price.grid(row=no, column=4, padx=40, sticky="e")
            place.grid(row=no, column=5, padx=(10,5), sticky="w")
            no+=1
        frame2.grid(row=2, padx = 15, pady=10, sticky="NSEW")
        sold.configure(cursor='arrow')
        
    lab_ = ctk.CTkLabel(frame2, text="Select Valid Product!", font=("Times New Roman", 20), text_color="red")
    lab_.grid(row=3, column=3, padx=300, pady=250, sticky="nsew")   

    opt = ctk.CTkLabel(sold, text="Select Product : ", font=font)
    opt.grid(row=0, column=0, padx=(0,200), pady=(10,0), sticky="E")

    opt_ = ctk.CTkOptionMenu(sold, font=option_font, fg_color=option_clr, anchor='center', command=stat, values=['Lippan Art','Bottle Art','Jaipur Art','Pottery'])
    opt_.grid(row=0, column=0, padx=(0,15), pady=(10,0),sticky="E")
    opt_.set('-')
    
    img_but = ctk.CTkButton(sold, image=back_img, text="", command=back, width=1, height=10, corner_radius=100, fg_color="transparent", hover_color=glossy_clr)
    img_but.grid(row=0, column=0, padx=(15,30), pady=(10,0),  sticky="W")
    
    frame1.grid(row=1, pady=(30,10), padx = 15, sticky="nsew")
    frame2.grid(row=2, padx = 15, pady=10, sticky="nsew")
    sold.protocol("WM_DELETE_WINDOW", root.destroy)
    sold.mainloop()

def add_prod():
    global add
    add = ctk.CTkToplevel()
    window_height = 500
    window_width = 500
    pos_top = int(disp_height//2 - window_height//2)
    pos_right = int(disp_width//2 - window_width//2)
    add.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
    add.resizable(False, False)
    add.iconbitmap('icons/add.ico')
    add.title("Add items")
    if platform.startswith("win"):
        add.after(200, lambda: add.iconbitmap("icons/add.ico"))
    adminn.withdraw()
    add.configure(fg_color=blue_clr)
    global a
    global c
    global file_upl
    global date
    global chk_dt
    price = ctk.StringVar()
    date = ctk.StringVar()
    a = ctk.StringVar()
    c = ctk.StringVar(add, "Select Product")

    frame = ctk.CTkFrame(add, fg_color=glossy_clr, width=350, height=200, border_width=1)
    head_lab = ctk.CTkLabel(frame, text='Upload Images', font=("Times New Roman", 26, "bold"))
    head_lab.grid(row=0, columnspan=4, sticky="nsew", pady=(50,50), padx=10)

    opt = ctk.CTkLabel(frame, text="Select Product : ", font=font)
    opt.grid(row=1, column=0, padx=50, sticky='w')
    
    lab = ctk.CTkLabel(frame, text = 'Item Code : ',font=font)
    lab.grid(row=2, column=0, padx=50, pady=(20,10), sticky='w')

    lab_code = ctk.CTkLabel(frame, text="", text_color='red', textvariable=c, width=50, font=font)
    lab_code.grid(row=2, column=1, padx=50, pady=(20,10))

    file_lab = ctk.CTkLabel(frame, text = 'Upload Image :', width=20, font=font)
    file_lab.grid(row=3, column=0, padx=(50,10), pady=(10,20), sticky='w')           

    def recallll():
        add.withdraw()
        adminn.deiconify()
        
    def fetch(val):
        global b
        global d
        if (val=="Lippan Art"):
            val='LA'
        elif (val=="Bottle Art"):
            val='BA'
        elif (val=="Jaipur Art"):
            val='JA'
        elif (val=="Pottery"):
            val='PO'
        else:
            pass
        exe = cur.execute(f"SELECT * FROM {val} ORDER BY ID DESC LIMIT 1;")
        data = cur.fetchall()
        for item in data:
            b=item[0]
            b=b+1
            b=str(b)

        b = ctk.StringVar(frame, f"{val}-{b}")
        file_upl.configure(state="NORMAL", cursor="hand2")
        b = b.get()
        b = str.split(b, sep="-")[-1]
        b = int(b)
        c.set(f"{val}-{str(b)}")
        lab_code.configure(text_color='green')
        
        d=val
        return d
        return b
##        add.update()
        
    def fileopen():
        global up_da
        global file_sta
        a = t.askopenfilename(filetypes=[("JPEG files", ".jpg"),("PNG files", ".png")])
        da = str.split(a, sep='/')
        da = da[-1]
        da = str.split(da, sep='.')
        da = da[0]
        if a!='':
            messagebox.showinfo(title='File Selected', message = f'{da} Selected')
            date_but.configure(state="NORMAL", cursor="hand2")
            file_upl.configure(text=f"{da}")
            sub.configure(state="NORMAL", cursor="hand2")
            price_ent.focus_set()
            with open(a, 'rb') as f:
                up_da = f.read()
                return up_da

            with open(up_da, 'rb') as f:
                img=f.read()
                img.show()

        else:
            messagebox.showerror(title='Error', message = f'Select a Valid File!')
            
    def submit():
        global c
        global b
        global d
        global up_da
        global file_up1
        global chk_dt
        day = date_ent.get()
        datess = day.split('/')[0]
        month = day.split('/')[1]
        year = day.split('/')[2]
        m_date = datetime.date(int(year),int(month),int(datess))
        try:
            if(d!='')and(b!='')and(up_da!='')and(price.get()!='')and(m_date<=dates.today()):
                query=f"INSERT INTO {d} (IMG_ID, IMAGE, STATUS, PRICE, MADE_DATE) VALUES (%s, %s, %s, %s, %s);"
                values = (str(d)+'-'+str(b),up_da,'FOR_SALE', int(price.get()), chk_dt)
                cur.execute(query,values)
                messagebox.showinfo(title="Success", message=f"{d+'-'+str(b)} added Successfully")
                b=int(b)+1
                c.set(f"{str(d)+'-'+str(b)}")
                file_upl.configure(text='Select File')
                price.set('')
                up_da=''
                date.set(str(dates.today().strftime('%d/%m/%Y')))
                sub.configure(state="disabled")
            else:
                messagebox.showerror('Error', "Please check Date!")
        except:
            messagebox.showerror('Error', "Please check all the details!")
            
            
    def get_cal():
        global date_up
        global cal
        global chk_dt
        global date
        global day
        global month
        global year
        date.set(str(date_up.get_date()))
        chk_dt = date_up.get_date()
        day=chk_dt.split('/')[0]
        month=chk_dt.split('/')[1]
        year=chk_dt.split('/')[2]
        chk_dt = year+'/'+month+'/'+day
        date_ent.configure(state='disabled')
        sub.focus_set()
        cal.destroy()
        return day, month, year
        
    def cal():
        global date_up
        global cal
        cal = ctk.CTkToplevel()
        cal.configure(fg_color=blue_clr)
        cal.title('Date')
        window_height = 210
        window_width = 215
        pos_top = int(disp_height//2 - window_height//2)
        pos_right = int(disp_width//2 - window_width//2)
        cal.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
        cal.resizable(False, False)
        cal.iconbitmap('icons/date.ico')
        if platform.startswith("win"):
            cal.after(200, lambda: cal.iconbitmap("icons/date.ico"))
        cal.grab_set()
        date_up = tkcal.Calendar(cal, date_pattern='dd/mm/yyyy')
        date_up.grid(row=0, column=0, padx=10, pady=(10,5))
        date_sub = ctk.CTkButton(cal, text='Done', font=button_font, width=10, command=get_cal)
        date_sub.grid(row=1,column=0, padx=10, pady=(5,5))
        cal.mainloop()
    
    opt_ = ctk.CTkOptionMenu(frame, font=option_font, fg_color=option_clr, anchor='center', command=fetch, values=['Lippan Art','Bottle Art','Jaipur Art','Pottery'])
    opt_.grid(row=1, column=1, padx=30, sticky='e')
    
    file_upl = ctk.CTkButton(frame, state="disabled",text='Select File', width=15, command=fileopen, font=font)
    file_upl.grid(row=3, column=1, padx=30, pady=(10,20), sticky='nsew')

    date_lab = ctk.CTkLabel(frame, text='Date (DD/MM/YYYY) :', font=font)
    date_lab.grid(row=5, column=0, padx=(50,10), sticky='w')

    date_ent = ctk.CTkEntry(frame, textvariable=date, width=140)
    date_ent.grid(row=5, column=1, padx=(0,30), sticky='e')
    
    date_but = ctk.CTkButton(frame, state='disabled', image=cal_img, text='', command = cal, height=3, width=3, border_width=1, corner_radius=10)
    date_but.grid(row=5, column=1, padx=(60,33), sticky='e')

    price_lab = ctk.CTkLabel(frame, text='Price :', font=font)
    price_lab.grid(row=4, column=0, padx=50, pady=(10,20), sticky='w')
    
    price_ent = ctk.CTkEntry(frame, placeholder_text='0', textvariable=price, font=('times',12,'italic'))
    price_ent.grid(row=4, column=1, padx=30, pady=(10,20), sticky='e')
    
    sub = ctk.CTkButton(frame, text="Submit", cursor=None, width=10, state="disabled", command = submit, font=font)
    sub.grid(row=6, columnspan=2, padx=150, pady=(20,10), sticky='nsew')

    exit_but = ctk.CTkButton(add, image=back_img, text="", fg_color=blue_clr, width=1, height=10, hover_color=glossy_clr, corner_radius=100, command = recallll, font=font)
    exit_but.grid(row=0, column=0, padx=40, pady=10, sticky='w')

    chk_dt = dates.today().strftime('%Y/%m/%d')
    opt_.set('-')    
    date.set(dates.today().strftime('%d/%m/%Y'))

    frame.grid(row = 1, column=0, padx = 40, pady =5, sticky="nsew")
    add.protocol("WM_DELETE_WINDOW", root.destroy)
    add.mainloop()
    
def recalll():
    adminn.withdraw()
    root.deiconify()
    root.grab_set()

def admin():
    global adminn
    adminn=ctk.CTkToplevel()
    adminn.configure(fg_color=blue_clr)
    window_height = 500
    window_width = 500
    pos_top = int(disp_height//2 - window_height//2)
    pos_right = int(disp_width//2 - window_width//2)
    adminn.geometry(f"{window_width}x{window_height}+{pos_right}+{pos_top}")
    adminn.resizable(False, False)
    adminn.title('Products')
    adminn.iconbitmap('icons/paintings.ico')
    if platform.startswith("win"):
        adminn.after(200, lambda: adminn.iconbitmap("icons/paintings.ico"))
    root.withdraw()

    frame = ctk.CTkFrame(adminn, fg_color=glossy_clr, width=400, height=100, border_width=1)
    
    admin_head = ctk.CTkLabel(frame, text="Project Colours", width=5, font=("Times New Roman", 20, "bold"))
    view_but = ctk.CTkButton(frame, text="Available Products", font=("Times New Roman", 18, "bold"), command=view_prod)
    sold_but = ctk.CTkButton(frame, text="Sold Products", font=("Times New Roman", 18, "bold"), command=sold_prod)
    add_but = ctk.CTkButton(frame, text="Add Products", font=("Times New Roman", 18, "bold"), command=add_prod)
    back_but = ctk.CTkButton(frame, text="Back", font=("Times New Roman", 18, "bold"), command=recalll)

    admin_head.grid(row=0, column=0, padx=10, pady=(10,30), sticky="nsew")
    view_but.grid(row=1,column=0, sticky="nsew", pady=5, padx=40)
    sold_but.grid(row=2, column=0, sticky="nsew",  pady=5, padx=40)
    add_but.grid(row=3, column=0, sticky="nsew",  pady=5, padx=40)
    back_but.grid(row=4, column=0, sticky="nsew", pady=(50,20), padx=40)

    frame.grid(row=0, column=0, sticky="nsew", padx=150, pady=150)
    adminn.protocol("WM_DELETE_WINDOW", root.destroy)
    adminn.mainloop()
    
img = Image.open(f"img/Colours-logo-final.png")
img=ctk.CTkImage(light_image=Image.open(f"img/Colours-logo-final.png"),size=(250,186))

header=ctk.CTkFrame(master=root, width=500, height=30)
imglab=ctk.CTkLabel(master=header, image=img, width=500, height=100, text="", fg_color="#B6CEF6")
body = ctk.CTkFrame(master=root, width=250, height=250, fg_color="#E7EFFC", border_width=1)
user = ctk.CTkButton(master=body, font=('Book Antiqua',18, 'bold'),text="User Login", command = ques)
admin = ctk.CTkButton(master=body, font=('Book Antiqua',18, 'bold'), text = "Project Colours", command = admin)
settings = ctk.CTkButton(master=body, font=('Book Antiqua',18, 'bold'), text = "Settings")
help1 = ctk.CTkButton(master=body, font=('Book Antiqua',18, 'bold'), text = "Help", command = help)
exit=ctk.CTkButton(master=body, font=('Book Antiqua',18, 'bold'), text="Exit", command=root.destroy)
footer=ctk.CTkFrame(master=root, width=50, height=30, fg_color="#B6CEF6")
copyright1=ctk.CTkLabel(master=footer, text="© 2022 - 2023 Colors Center for Autism", width=40)

header.pack(fill='both', expand=True)
imglab.pack(ipady=10, fill='both', expand=True)
body.pack()
user.place(relx=0.5, rely=0.20, anchor=ctk.CENTER)
admin.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)
settings.place(relx=0.5, rely=0.50, anchor=ctk.CENTER)
help1.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)
exit.place(relx=0.5, rely=0.80, anchor=ctk.CENTER)
copyright1.place(relx=0.5,rely=0.5, anchor=ctk.CENTER)
footer.pack(fill='x')

try:
    connection = pymysql.connect(host='db4free.net',
                             user='colours',
                             password='colours12',
                             database='project_colours',
                             autocommit=True)
    cur = connection.cursor()
    cur.execute(f"SELECT NAME FROM STUDENTS WHERE DATE='{datetime.date.today().strftime('%Y-%m-%d')}';")
    stude = list(cur.fetchall())
    for x in stude:
        for i in x:
            students.remove(i)
    root.mainloop()
except:
    messagebox.showerror("Error", "Error is Database Connection", master=root)
