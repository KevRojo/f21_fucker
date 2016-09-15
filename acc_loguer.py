import requests
from bs4 import BeautifulSoup
from tqdm import trange
from time import sleep
import tkinter as tk
import io
import base64
from urllib.request import urlopen
sessions = requests.session()
username = ""
password = ""


def f21_log(user, passw):

    payload={'__EVENTTARGET': 'ctl00$MainContent$LoginForm$LoginButton',
             'ctl00$MainContent$LoginForm$UserName': user,
             'ctl00$MainContent$LoginForm$Password': passw}
    data = sessions.post('https://www.forever21.com/Login/Login.aspx?br=f21&rtn=http%3a%2f%2fwww.forever21.com%2fAccoun'
                         't%2fOverView.aspx%3fbr%3df21', data=payload)
    r = sessions.get("https://www.forever21.com/Order/PastOrders.aspx?br=f21")
    pa_la_sopa = r.text

    soup = BeautifulSoup(pa_la_sopa, "html.parser")
    if username in data.text:
        print("Inside")
    else:
        print("Error al entrar al sistema.")

    return None

def item_viewer():
    root = tk.Tk()
    root.title("Item_Viewer")
    w = 520
    h = 320
    x = 80
    y = 100

    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

    image_url = "http://cdn4.sosueme.ie/wp-content/uploads/2010/12/FOREVER21-BUZZ.gif"

    image_byt = urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)
    photo = tk.PhotoImage(data = image_b64)

    cv = tk.Canvas(bg = 'white')
    cv.pack(side = 'top', fill = 'both', expand = 'yes')

    cv.create_image(10, 10, image = photo, anchor = 'nw')

    root.mainloop()

    return None

def get_item_id(baselink):


    return None


#MENU MATAPOLLO 3,000#
x = 1
while x != 0:
    print("Welcome to the 21 fucker: \n")
    print("Menu:\n 1 = Login into F21 \n 2 = Logout \n 3 = Add Items to bag \n 0 = Close the script \n")
    menu = int(input("Choose a option: "))
    if menu == 1:
        username = input("Username:")
        password = input("Password")
        for i in trange(10, desc='Entrando al sistema.'):
            sleep(0.5)
        print(f21_log(username, password))
    if menu == 2:
        resp = int(input("Dese salir de la cuenta? \n 1 = si \n 0 = no"))

        if resp == 1:
            r = sessions.get("https://www.forever21.com/Login/Logout.aspx")
            pa_la_sopa = r.text
            soup = BeautifulSoup(pa_la_sopa, "html.parser")
            if username in soup.text:
                print("Error al salir del sistema.")
            else:
                print("Salida Exitosa del sistema.")
        if resp == 0:
            None


