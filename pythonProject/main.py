import requests
import tkinter as tk
from datetime import datetime

def checkBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    priceUSD = response["USD"]
    priceEUR = response["EUR"]
    priceJPY = response["JPY"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(priceUSD)+" USD\n"+ str(priceEUR)+" EUR\n"+ str(priceJPY) + " JPY")
    labelTime.config(text="Updated at: " + time)

    canvas.after(1000, checkBitcoin)

canvas = tk.Tk()
canvas.geometry("300x300")
canvas.title("Bitcoin Checker")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

checkBitcoin()

canvas.mainloop()