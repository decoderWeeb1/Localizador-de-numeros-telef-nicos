from ast import operator
from itertools import count
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+400+100")
root.resizable(False,False)

def track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)

    #País
    locate=geocoder.description_for_number(number,"en")
    country.config(text=locate)

    #Operador
    operator=carrier.name_for_number(number,"en")
    sim.config(text=operator)

    #Lugar/Ciudad
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)

    #Longitud y Latitud
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    #Hora en el país
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)

#Logo
logo=PhotoImage(file="logo image.png")
Label(root,image=logo).place(x=240,y=70)

#Texto TRACK NUMBER
Heading=Label(root,text="TRACK NUMBER",font=("arial",15,"bold"))
Heading.place(x=90,y=110)

#Entrada
Entry_back=PhotoImage(file="search png.png")
Label(root,image=Entry_back).place(x=20,y=190)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,bd=0,font=("arial",20),justify="center")
enter_number.place(x=50,y=220)

#Botón
Search_image=PhotoImage(file="search.png")
search=Button(image=Search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=35,y=300)

#Botón de la parte inferior
Box=PhotoImage(file="bottom png.png")
Label(root,image=Box).place(x=-2,y=355)


#Datos de salida
country=Label(root,text="Country:",bg="#57adff",fg="black",font=("arial",10,"bold"))
country.place(x=50,y=400)

sim=Label(root,text="SIM:",bg="#57adff",fg="black",font=("arial",10,"bold"))
sim.place(x=200,y=400)

zone=Label(root,text="TimeZone:",bg="#57adff",fg="black",font=("arial",10,"bold"))
zone.place(x=50,y=450)

clock=Label(root,text="Phone Time:",bg="#57adff",fg="black",font=("arial",10,"bold"))
clock.place(x=200,y=450)

longitude=Label(root,text="Longitude:",bg="#57adff",fg="black",font=("arial",10,"bold"))
longitude.place(x=50,y=500)

latitude=Label(root,text="Latitude:",bg="#57adff",fg="black",font=("arial",10,"bold"))
latitude.place(x=200,y=500)

root.mainloop()
