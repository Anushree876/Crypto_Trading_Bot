from bot import TradeBot
import logging
from tkinter import *
from tkinter import messagebox


background='#CADCAE'
font=("Georgia",13,"normal")

bot=TradeBot()

# logging the response,errors
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# getting the req. details.
# fnx that places order .
def submit_order():

    symbol=symbol_input.get().upper().strip()
    side=side_input.get().upper().strip()
    quantity=quantity_input.get().strip()
    type=type_var.get()
    price=price_input.get().strip()
    stopprice=stopprice_input.get().strip()

    # error handling
    if side not in ["BUY","SELL"]:
        messagebox.showerror("Error","Side must be BUY OR SELL")
        return

    try:
        quantity=float(quantity)
    except ValueError:
        messagebox.showerror("Error","Invalid quantity.Must be a number. ")
        return

    try:
        if type=="LIMIT":
            price=float(price)
            stopprice=None
        elif type=="STOP_LIMIT":
            price=float(price)
            stopprice=float(stopprice)
        else:
            price=None
            stopprice=None

    except ValueError:
        messagebox.showerror("Error","Invalid price or stop price.")
        return
    try:
        response = bot.place_order(symbol, side, type, quantity, price=price, stopprice=stopprice)
        messagebox.showinfo("ORDER DETAILS",f"Order response!\n\n{response}")
        logging.info(f"Order placed: {response}")
        print (response)

    except Exception as e:
        messagebox.showerror("Order Failed",str(e))
        logging.error(f"Error placing order: {str(e)}")


# fnx that updates the gui based on the order type
def update_fields(event=None):
    type=type_var.get().upper().strip()
    if type == "MARKET":
        price_title.grid_remove()
        stopprice_title.grid_remove()
        price_input.grid_remove()
        stopprice_input.grid_remove()
    elif type=="LIMIT":
        stopprice_input.grid_remove()
        stopprice_title.grid_remove()
        price_title.grid(column=0,row=5)
        price_input.grid(column=1,row=5)
    elif type =="STOP_LIMIT":
        price_input.grid(column=1, row=5)
        price_title.grid(column=0,row=5)
        stopprice_input.grid(column=1, row=6)
        stopprice_title.grid(column=0,row=6)


# GUI SETUP using tkinter
window=Tk()
window.title("Crypto Bot")

window.config(padx=50,pady=10,bg=background)

title_label=Label(window,text="Trade",bg=background,font=("Georgia",25,"normal"))
title_label.grid(column=0,row=0,columnspan=3,pady=20)

symbol_title=Label(window,text="Enter trading symbol(e.g.,BTCUSDT):",background=background)
symbol_title.grid(column=0,row=1)
symbol_input=Entry(window)
symbol_input.grid(column=1,row=1)

side_title=Label(window,text="Enter side (BUY OR SELL):",background=background)
side_title.grid(column=0,row=2)
side_input=Entry(window)
side_input.grid(column=1,row=2)

quantity_title=Label(window,text="Enter the quantity:",background=background)
quantity_title.grid(column=0,row=3)
quantity_input=Entry(window)
quantity_input.grid(column=1,row=3)

type_title=Label(window,text="Enter the order type:",background=background)
type_title.grid(column=0,row=4)
type_var=StringVar(window)
type_var.set("MARKET")
type_input=OptionMenu(window,type_var,"MARKET","LIMIT","STOP_LIMIT")
type_input.grid(column=1,row=4)
type_var.trace_add("write",lambda *args: update_fields())

price_title=Label(window,text="Enter limit price:",background=background)
price_title.grid(column=0,row=5)
price_input=Entry(window)
price_input.grid(column=1,row=5)

stopprice_title=Label(window,text="Enter the stop price:",background=background)
stopprice_title.grid(column=0,row=6)
stopprice_input=Entry(window)
stopprice_input.grid(column=1,row=6)

# triggers submit_order
submit_button = Button(window, text="Submit Order", command=submit_order,width=20,height=1)
submit_button.grid(column=0, row=7, pady=10,columnspan=3)

# for gui update
update_fields()

window.mainloop()

















