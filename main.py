import customtkinter as ctk 
import os, random, string
import sqlite3 as sl 
from PIL import Image


address = __file__.replace("\\","/")
for i in range(len(address)-1, 0, -1):
    if address[i] == '/':
        address = address[:i]
        break
os.chdir(address)

user = ""

root = ctk.CTk()

root.geometry("1100x580")
root.title("Trust Box")
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")


frame_1 = ctk.CTkFrame(root, width=300, height=320)
frame_1.grid(row=0, column=0, padx=20, pady=20)

frame_2 = ctk.CTkFrame(root, width=420, height=320)
frame_2.grid(row=0, column=1, padx=0, pady=0)

frame_3 = ctk.CTkScrollableFrame(root, width=280, height=530)
frame_3.grid(row=0, column=2, padx=20, pady=20, rowspan=2)

frame_4 = ctk.CTkFrame(root, width=740, height=200)
frame_4.grid(row=1, column=0, padx=(20,0), pady=(0,20) , columnspan=2)


def welcome(username, root):
    frame_1 = ctk.CTkFrame(root, width=300, height=320)
    frame_1.grid(row=0, column=0, padx=20, pady=20, )

    label_1 = ctk.CTkLabel(frame_1, text="Welcome", 
        font=("vivaldi", 60, "bold"))
    label_1.pack(pady=(90,0), padx=45)

    label_2 = ctk.CTkLabel(frame_1, text="{}".format(username).capitalize()[:15],
        font=("vivaldi", 30, "bold"))
    label_2.pack(padx=0, pady=(0,100))

    frame2()
    frame3(username)
    frame4("","")

def login():

    frame_5 = ctk.CTkFrame(root, width=300, height=320)
    frame_5.grid(row=0, column=0)

    label_1 = ctk.CTkLabel(frame_5, text="Sign Up \n ____",
     font=ctk.CTkFont("font", size=26, weight="bold"))
    label_1.place(in_=frame_5, x=115, rely=0.07)

    entry_1 = ctk.CTkEntry(frame_5, placeholder_text="Username", 
        width=250, height=37, font=("font", 18))
    entry_1.place(in_=frame_5, x=25, rely=0.35)

    entry_2 = ctk.CTkEntry(frame_5, placeholder_text="Password", show="*",
        width=250, height=37, font=("font", 18))
    entry_2.place(in_=frame_5, x=25, rely=0.55)


    button_1 = ctk.CTkButton(frame_5, text="Submit", 
        command=lambda:login2(entry_1.get(),entry_2.get(),frame_5),
        font=ctk.CTkFont("font", size=20), height=37)
    button_1.place(in_=frame_5, x=80, rely=0.8)

    button_2 = ctk.CTkButton(frame_5, text="<", border_width=1, command=frame1, 
        font=ctk.CTkFont(size=30), height=47, width=47, fg_color="transparent")
    button_2.place(in_=frame_5, x=20, rely=0.07) 

def login2(username, password, frame_5):


    label_1 = ctk.CTkLabel(frame_5, text="*Invalid Username", height=1,
            font=("font", 12), text_color="red", fg_color="transparent")
    if username == "":
        label_1.place(in_=frame_5, x=25, rely=0.47)
        return
    label_1.configure(text = "                                  ")
    label_1.place(in_=frame_5, x=25, rely=0.47)


    label_2 = ctk.CTkLabel(frame_5, text="*Invalid Password", height=1,
        font=("font", 12), text_color="red", fg_color="transparent")
    if password == "":
        label_2.place(in_=frame_5, x=25, rely=0.67)
        return
    label_2.configure(text="                                  ")
    label_2.place(in_=frame_5, x=25, rely=0.67)


    label_3 = ctk.CTkLabel(frame_5, text="*User Already Exists", height=1,
        font=("font", 15), text_color="red", fg_color="transparent")
    if os.path.isfile(username):
        label_3.place(in_=frame_5, x=82, rely=0.72)
        return
    label_3.configure(text="                                                     ")
    label_3.place(in_=frame_5, x=82, rely=0.72)


    con = sl.connect("{}".format(username))

    command = "CREATE TABLE DATA(domain TEXT, password TEXT)"
    con.execute(command)

    command = "INSERT INTO DATA(domain, password) values(?,?)"
    data = ("password", "{}".format(password))
    con.execute(command, data)

    con.commit()

    label_3 = ctk.CTkLabel(frame_5, text="*Successfully Created...Login now", height=1,
        font=("font", 15), text_color="green", fg_color="transparent")
    label_3.place(in_=frame_5, x=25, rely=0.72)

    root.mainloop()

def signup():

    frame_5 = ctk.CTkFrame(root, width=300, height=320)
    frame_5.grid(row=0, column=0)

    label_1 = ctk.CTkLabel(frame_5, text="Login \n ____",
     font=ctk.CTkFont("font", size=26, weight="bold"))
    label_1.place(in_=frame_5, x=100, rely=0.05)

    entry_1 = ctk.CTkEntry(frame_5, placeholder_text="Username", 
        width=250, height=37, font=("font", 18))
    entry_1.place(in_=frame_5, x=25, rely=0.35)

    entry_2 = ctk.CTkEntry(frame_5, placeholder_text="Password", show="*",
        width=250, height=37, font=("font", 18))
    entry_2.place(in_=frame_5, x=25, rely=0.55)

    button_1 = ctk.CTkButton(frame_5, text="Submit", 
        command=lambda:signup2(entry_1.get(),entry_2.get(),frame_5), 
        font=ctk.CTkFont("font", size=20), height=37)
    button_1.place(in_=frame_5, x=80, rely=0.8)

    button_2 = ctk.CTkButton(frame_5, text="<", border_width=1, command=frame1, 
        font=ctk.CTkFont(size=30), height=47, width=47, fg_color="transparent")
    button_2.place(in_=frame_5, x=20, rely=0.07)

def signup2(username, password, frame_5):


    label_1 = ctk.CTkLabel(frame_5, text="*Invalid Username", height=1,
            font=("font", 12), text_color="red", fg_color="transparent")
    if username == "":
        label_1.place(in_=frame_5, x=25, rely=0.47)
        return
    label_1.configure(text = "                                  ")
    label_1.place(in_=frame_5, x=25, rely=0.47)


    label_2 = ctk.CTkLabel(frame_5, text="*Invalid Password", height=1,
        font=("font", 12), text_color="red", fg_color="transparent")
    if password == "":
        label_2.place(in_=frame_5, x=25, rely=0.67)
        return
    label_2.configure(text="                                  ")
    label_2.place(in_=frame_5, x=25, rely=0.67)


    label_3 = ctk.CTkLabel(frame_5, text="*Invalid Credentials", height=1,
        font=("font", 15), text_color="red", fg_color="transparent")
    if not os.path.isfile(username):
        label_3.place(in_=frame_5, x=82, rely=0.72)
        return
    label_3.configure(text="                                                     ")
    label_3.place(in_=frame_5, x=82, rely=0.72)


    con = sl.connect(username)

    command = "SELECT password FROM DATA WHERE domain='password'"
    data = con.execute(command)

    for row in data:
        stored_password = row

    label_3 = ctk.CTkLabel(frame_5, text="*Invalid Credentials", height=1,
            font=("font", 15), text_color="red", fg_color="transparent")
    if stored_password[0] != password or not os.path.isfile(username):
        label_3.place(in_=frame_5, x=82, rely=0.72)
        return
    label_3.configure(text="                                                     ")
    label_3.place(in_=frame_5, x=82, rely=0.72)

    welcome(username, root)
    global user 
    user = username

    root.mainloop()

def frame1():

    frame_1 = ctk.CTkFrame(root, width=300, height=320)
    frame_1.grid(row=0, column=0, padx=20, pady=20)

    label_1 = ctk.CTkLabel(frame_1, text="Trust Box \n ____",
     font=ctk.CTkFont("font", size=30, weight="bold"))
    label_1.place(in_=frame_1, x=70, rely=0.1)

    button_1 = ctk.CTkButton(frame_1, text="Sign Up", 
        font=ctk.CTkFont("font", size=20), command=login, height=40)
    button_1.place(in_=frame_1, relx=0.25, rely=0.6)

    button_2 = ctk.CTkButton(frame_1, text="Login", 
        font=ctk.CTkFont("font", size=20), command=signup, height=40)
    button_2.place(in_=frame_1, relx=0.25, rely=0.4)


def save_password2(domain, password, frame_5):


    label_1 = ctk.CTkLabel(frame_5, text="*Invalid Domain", height=1,
            font=("font", 12), text_color="red", fg_color="transparent")
    if domain == "":
        label_1.place(in_=frame_5, x=60, rely=0.47)
        return
    label_1.configure(text = "                                  ")
    label_1.place(in_=frame_5, x=60, rely=0.47)


    label_2 = ctk.CTkLabel(frame_5, text="*Invalid Password", height=1,
        font=("font", 12), text_color="red", fg_color="transparent")
    if password == "":
        label_2.place(in_=frame_5, x=60, rely=0.67)
        return
    label_2.configure(text="                                  ")
    label_2.place(in_=frame_5, x=60, rely=0.67)

    store(domain, password)

def store(domain, password):

    con = sl.connect("{}".format(user))

    command = "INSERT INTO DATA(domain, password) values(?,?)"
    data = (domain, password)
    con.execute(command, data)
    con.commit()
    frame3(user)
    frame4(domain, password)

    root.mainloop()

def save_password():
    frame_1 = ctk.CTkFrame(root, width=420, height=320, border_width=2)
    frame_1.grid(row=0, column=1, padx=0, pady=0)

    entry_1 = ctk.CTkEntry(frame_1, placeholder_text="Domain Name", 
        width=300, height=37, font=("font", 22))
    entry_1.place(in_=frame_1, x=60, rely=0.35)

    entry_2 = ctk.CTkEntry(frame_1, placeholder_text="Password", show="*",
        width=300, height=37, font=("font", 22))
    entry_2.place(in_=frame_1, x=60, rely=0.55)


    button_1 = ctk.CTkButton(frame_1, text="Save", 
        command=lambda:save_password2(entry_1.get(),entry_2.get(),frame_1),
        font=ctk.CTkFont("font", size=20), height=37)
    button_1.place(in_=frame_1, x=140, rely=0.8)

    button_2 = ctk.CTkButton(frame_1, text="<", border_width=1, command=frame2, 
        font=ctk.CTkFont(size=30), height=47, width=47, fg_color="transparent")
    button_2.place(in_=frame_1, x=20, rely=0.07)

def generate_password2(domain, frame_1):

    label_1 = ctk.CTkLabel(frame_1, text="*Invalid Domain", height=1,
            font=("font", 12), text_color="red", fg_color="transparent")
    if domain == "":
        label_1.place(in_=frame_1, x=60, rely=0.47)
        return
    label_1.configure(text = "                                  ")
    label_1.place(in_=frame_1, x=60, rely=0.47)

    password = password_generate()

    store(domain, password)

def generate_password():

    frame_1 = ctk.CTkFrame(root, width=420, height=320, border_width=2)
    frame_1.grid(row=0, column=1, padx=0, pady=0)

    entry_1 = ctk.CTkEntry(frame_1, placeholder_text="Domain Name", 
        width=300, height=37, font=("font", 22))
    entry_1.place(in_=frame_1, x=60, rely=0.35)


    button_1 = ctk.CTkButton(frame_1, text="Generate", 
        command=lambda:generate_password2(entry_1.get(), frame_1),
        font=ctk.CTkFont("font", size=20), height=37)
    button_1.place(in_=frame_1, x=140, rely=0.6)

    button_2 = ctk.CTkButton(frame_1, text="<", border_width=1, command=frame2, 
        font=ctk.CTkFont(size=30), height=47, width=47, fg_color="transparent")
    button_2.place(in_=frame_1, x=20, rely=0.07)

def frame2():
    frame_1 = ctk.CTkFrame(root, width=420, height=320, border_width=1)
    frame_1.grid(row=0, column=1, padx=0, pady=0)

    button_1 = ctk.CTkButton(frame_1, text="Save Password",
        font=ctk.CTkFont("font", size=22), command=save_password, height=50, width=300,
        border_color="white")
    button_1.place(in_=frame_1, relx=0.15, rely=0.25)

    button_2 = ctk.CTkButton(frame_1, text="Generate Password", 
        font=ctk.CTkFont("font", size=22), command=generate_password, height=50, width=300,
        border_color="white")
    button_2.place(in_=frame_1, relx=0.15, rely=0.55)


def show(domain, user):
    con = sl.connect(user)
    command2 = "SELECT password FROM DATA WHERE domain=={}".format("'"+domain+"'")
    data2 = con.execute(command2)
    password=""
    for row2 in data2:
        password = row2
    frame4(domain, password)

def frame3(user):

    frame_5 = ctk.CTkFrame(root, width=250, height=35, 
        border_width=2, fg_color="transparent")
    frame_5.place(x=805, y=10)

    label_51 = ctk.CTkLabel(frame_5, text="Saved Passwords", 
        font=ctk.CTkFont("font", size=20, weight="bold"))
    label_51.grid(row=0, column=0, padx=40, pady=5)

    con = sl.connect(user)

    command = "SELECT domain FROM DATA WHERE domain!='password'"
    data = con.execute(command)
    step=0
    for row in data:
        x = row[0]

        if step==0:
            button_31 = ctk.CTkButton(frame_3, text="{}".format(x.capitalize().strip()[:18]), 
                    width=250, height=55, font=("", 22), fg_color="transparent", 
                    border_width=1, border_color="white", hover_color="#808080", 
                    command=lambda x=row[0] :show(x, user))
            button_31.grid(row=step, column=0, padx=(20,30), pady=(50,12))
        else:
            button_31 = ctk.CTkButton(frame_3, text="{}".format(x.capitalize().strip()[:18]), 
                width=250, height=55, font=("", 22), fg_color="transparent", 
                border_width=1, border_color="white", hover_color="#808080", 
                command=lambda x=row[0] :show(x, user))
            button_31.grid(row=step, column=0, padx=(20,30), pady=12)
        step += 1


def frame4(domain, password):

    frame_4 = ctk.CTkFrame(root, width=740, height=200)
    frame_4.grid(row=1, column=0, padx=(20,0), pady=(0,20) , columnspan=2)

    frame_6 = ctk.CTkFrame(root, width=150, height=10, 
        border_width=2, fg_color="transparent")
    frame_6.place(x=35, y=350)

    label_1 = ctk.CTkLabel(frame_6, text="Display", 
        font=ctk.CTkFont("font", size=20, weight="bold"))
    label_1.grid(row=0, column=0, padx=50, pady=3)

    label_2 = ctk.CTkLabel(frame_4, text="Domain : ",
        font=ctk.CTkFont("font", size=22, weight="bold"))
    label_2.place(in_=frame_4, x=50, y=60)

    label_3 = ctk.CTkLabel(frame_4, text="Password :", 
        font=ctk.CTkFont("font", size=22, weight="bold"))
    label_3.place(in_=frame_4, x=50, y=110)

    label_4 = ctk.CTkLabel(frame_4, text=domain.capitalize(), 
        font=ctk.CTkFont("HelvLight", size=25))
    label_4.place(in_=frame_4, x=200, y=60)

    label_5 = ctk.CTkLabel(frame_4, text=password, 
        font=ctk.CTkFont("HelvLight", size=25))
    label_5.place(in_=frame_4, x=200, y=110)


def password_generate():
    size = random.randint(8,16)
    lower_alpha = list(string.ascii_lowercase)
    upper_alpha = list(string.ascii_uppercase)
    alpha = list(string.ascii_letters)

    digits = ['0','1','2','3','4','5','6','7','8','9']
    special = ['@','#','$','%','&','*','_','=']

    password = [""] * size

    random1 = random.randint(0,size-1)
    password[random1] = random.choice(upper_alpha)

    while(True):
        random2 = random.randint(0,size-1)
        if(password[random2] != ''):
            continue
        password[random2] = random.choice(digits)
        break

    while(True):
        random3 = random.randint(0,size-1)
        if(password[random3] != ''):
            continue
        password[random3] = random.choice(special)
        break

    while(True):
        random4 = random.randint(0,size-1)
        if(password[random4] != ''):
            continue
        password[random4] = random.choice(lower_alpha)
        break

    password_string = ""
    for i in range(len(password)):
        if password[i] == '':
            temp = random.choice([lower_alpha, upper_alpha, special, digits])
            password[i] = random.choice(temp)
        password_string += password[i]

    return password_string

frame1()

root.mainloop()

