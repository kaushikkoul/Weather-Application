from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city=city_name.get()
    data=requests.get("TYPE YOUR="+city+"+API LINK HERE").json()
    w_Label1.config(text=data["weather"][0]["main"])
    wd_Label1.config(text=data["weather"][0]["description"])
    temp_Label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pres_Label1.config(text=data["main"]["pressure"])

win=Tk()
win.title("Weather Application")
win.config(bg="#404040")
win.geometry("900x600")

# Search Box
Search_Image=PhotoImage(file="heading.png")
myimage=Label(image=Search_Image)
myimage.place(x=20,y=20)
name_Label = Label(win,text="Weather Application",justify="center",width=20,font=("Times New Roman",25,"bold"),bg="#404040",border=0,fg="white")
name_Label.place(x=50,y=40)

# Logo
Logo_Image=PhotoImage(file="logo.png")
logo=Label(image=Logo_Image)
logo.place(x=600,y=20)


list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()
com=ttk.Combobox(win,text="Weather Application",values=list_name,font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

# Weather Climate
w_Label = Label(win,text="Weather Climate:",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
w_Label.place(x=25,y=260,height=50,width=210)

w_Label1 = Label(win,text="",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
w_Label1.place(x=250,y=260,height=50,width=210)


# Weather Description
wd_Label = Label(win,text="Weather Description:",width=20,font=("Times New Roman",17,"bold"),bg="#404040",border=0,fg="white")
wd_Label.place(x=25,y=330,height=50,width=210)

wd_Label1 = Label(win,text="",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
wd_Label1.place(x=250,y=330,height=50,width=210)

# Temperature
temp_Label = Label(win,text="Temperature:",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
temp_Label.place(x=25,y=400,height=50,width=210)

temp_Label1 = Label(win,text="",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
temp_Label1.place(x=250,y=400,height=50,width=210)

# Pressure
pres_Label = Label(win,text="Pressure:",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
pres_Label.place(x=25,y=470,height=50,width=210)

pres_Label1 = Label(win,text="",width=20,font=("Times New Roman",20,"bold"),bg="#404040",border=0,fg="white")
pres_Label1.place(x=250,y=470,height=50,width=210)

# Submit Button
done_button=Button(win,text="Submit",font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()