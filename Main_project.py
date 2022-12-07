from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random
import time

root=Tk()
root.title("Resturant Managment System")
root.geometry("1490x760")
root.resizable(False,False)
root.config(bg="firebrick4")

#===================================FUNCTION===================================
def exit():
    ans=messagebox.askyesno('Exit','Do you want to exit?')
    if ans:
        root.destroy()
def reset():
    reciptarea.delete(1.0,END)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    e1.set('0')
    e2.set('0')
    e3.set('0')
    e4.set('0')
    e5.set('0')
    e6.set('0')
    e7.set('0')
    e8.set('0')
    e9.set('0')
    e10.set('0')
    e11.set('0')
    e12.set('0')
    e13.set('0')
    e14.set('0')
    e15.set('0')
    e16.set('0')
    e17.set('0')
    e18.set('0')
    e19.set('0')
    e20.set('0')
    e21.set('0')
    e22.set('0')
    e23.set('0')
    e24.set('0')
    e25.set('0')
    e26.set('0')
    e27.set('0')

    entry1.config(state=DISABLED)
    entry2.config(state=DISABLED)
    entry3.config(state=DISABLED)
    entry4.config(state=DISABLED)
    entry5.config(state=DISABLED)
    entry6.config(state=DISABLED)
    entry7.config(state=DISABLED)
    entry8.config(state=DISABLED)
    entry9.config(state=DISABLED)
    entry10.config(state=DISABLED)
    entry11.config(state=DISABLED)
    entry12.config(state=DISABLED)
    entry13.config(state=DISABLED)
    entry14.config(state=DISABLED)
    entry15.config(state=DISABLED)
    entry16.config(state=DISABLED)
    entry17.config(state=DISABLED)
    entry18.config(state=DISABLED)
    entry19.config(state=DISABLED)
    entry20.config(state=DISABLED)
    entry21.config(state=DISABLED)
    entry22.config(state=DISABLED)
    entry23.config(state=DISABLED)
    entry24.config(state=DISABLED)
    entry25.config(state=DISABLED)
    entry26.config(state=DISABLED)
    entry27.config(state=DISABLED)

    e_food.set('')
    e_drink.set('')
    e_cake.set('')
    e_subtotal.set('')
    e_gst.set('')
    e_total.set('')
def save():
    if int(e1.get()) != 0 or int(e2.get()) != 0 or int(e3.get()) != 0 or int(e4.get()) != 0 or int(
            e5.get()) != 0 or int(e6.get()) != 0 or int(e7.get()) != 0 or int(e8.get()) != 0 or int(e9.get()) != 0 or \
            int(e10.get()) != 0 or int(e11.get()) != 0 or int(e12.get()) != 0 or int(e13.get()) != 0 or int(
        e14.get()) != 0 or int(e15.get()) != 0 or int(e16.get()) != 0 or int(e17.get()) != 0 or \
            int(e18.get()) != 0 or int(e19.get()) != 0 or int(e20.get()) != 0 or int(e21.get()) != 0 or int(
        e22.get()) != 0 or int(e23.get()) != 0 or int(e24.get()) != 0 or int(e25.get()) != 0 or int(e26.get()) != 0 or \
            int(e27.get()) != 0:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        bill_data=reciptarea.get(1.0,END)
        url.write(bill_data)
        url.close()
        messagebox.showinfo('Information','Your bill is successfully saved!')
    else:
        messagebox.showerror("Error","NO ITEMS SELECTED")
def total():
    if int(e1.get())!=0 or int(e2.get())!=0 or int(e3.get())!=0 or int(e4.get())!=0 or int(e5.get())!=0 or int(e6.get())!=0 or int(e7.get())!=0 or int(e8.get())!=0 or int(e9.get())!=0 or\
    int(e10.get()) != 0 or int(e11.get())!=0 or int(e12.get())!=0 or int(e13.get())!=0 or int(e14.get())!=0 or int(e15.get())!=0 or int(e16.get())!=0 or int(e17.get())!=0 or\
    int(e18.get()) != 0 or int(e19.get())!=0 or int(e20.get())!=0 or int(e21.get())!=0 or int(e22.get())!=0 or int(e23.get())!=0 or int(e24.get())!=0 or int(e25.get())!=0 or int(e26.get())!=0 or\
    int(e27.get())!=0:
        f1=int(e1.get())
        f2=int(e2.get())
        f3=int(e3.get())
        f4=int(e4.get())
        f5=int(e5.get())
        f6=int(e6.get())
        f7=int(e7.get())
        f8=int(e8.get())
        f9=int(e9.get())
        d1=int(e10.get())
        d2=int(e11.get())
        d3=int(e12.get())
        d4=int(e13.get())
        d5=int(e14.get())
        d6=int(e15.get())
        d7=int(e16.get())
        d8=int(e17.get())
        d9=int(e18.get())
        c1=int(e19.get())
        c2=int(e20.get())
        c3=int(e21.get())
        c4=int(e22.get())
        c5=int(e23.get())
        c6=int(e24.get())
        c7=int(e25.get())
        c8=int(e26.get())
        c9=int(e27.get())
        food=f1*10+f2*50+f3*90+f4*80+f5*150+f6*100+f7*200+f8*120+f9*140
        e_food.set(str(food)+'Rs.')
        drink=d1*8+d2*20+d3*15+d4*30+d5*35+d6*20+d7*30+d8*40+d9*50
        e_drink.set(str(drink)+'Rs.')
        cake=c1*250+c2*330+c3*400+c4*200+c5*230+c6*300+c7*280+c8*350+c9*450
        e_cake.set(str(cake)+'Rs.')
        sub_total=cake+food+drink
        e_subtotal.set(str(sub_total)+'Rs.')
        gst=round(sub_total*9/100,2)
        e_gst.set(str(gst)+'Rs.')
        total=sub_total+gst
        e_total.set(str(total)+'Rs.')
    else:
        messagebox.showerror("Error","NO ITEMS SELECTED")

def recipt():
    if int(e1.get()) != 0 or int(e2.get()) != 0 or int(e3.get()) != 0 or int(e4.get()) != 0 or int(
            e5.get()) != 0 or int(e6.get()) != 0 or int(e7.get()) != 0 or int(e8.get()) != 0 or int(e9.get()) != 0 or \
            int(e10.get()) != 0 or int(e11.get()) != 0 or int(e12.get()) != 0 or int(e13.get()) != 0 or int(
        e14.get()) != 0 or int(e15.get()) != 0 or int(e16.get()) != 0 or int(e17.get()) != 0 or \
            int(e18.get()) != 0 or int(e19.get()) != 0 or int(e20.get()) != 0 or int(e21.get()) != 0 or int(
        e22.get()) != 0 or int(e23.get()) != 0 or int(e24.get()) != 0 or int(e25.get()) != 0 or int(e26.get()) != 0 or \
            int(e27.get()) != 0:
        reciptarea.delete(1.0,END)
        x=random.randint(100,10000)
        s='Bill No.' + str(x)
        date=time.strftime('%d/%m/%y')
        reciptarea.insert(END,'Recipt Ref:\t\t         '+s+'\t\t             '+date+'\n\n')
        reciptarea.insert(END,'*******************************************************************\n\n')
        reciptarea.insert(END,"ITEMS\t          QUANTITY \t           COST OF ITEMS(Rs.)\n")
        reciptarea.insert(END,"*******************************************************************\n")
        if int(e1.get())!=0:
            reciptarea.insert(END,f"Roti\t\t {e1.get()}\t\t\t{int(e1.get())*10}\n\n")
        if int(e2.get())!=0:
            reciptarea.insert(END,f"Dal\t\t {e2.get()}\t\t\t{int(e2.get())*50}\n\n")
        if int(e3.get()) != 0:
            reciptarea.insert(END, f"Fish\t\t {e3.get()}\t\t\t{int(e3.get()) * 90}\n\n")
        if int(e4.get()) != 0:
            reciptarea.insert(END, f"Sabji\t\t {e4.get()}\t\t\t{int(e4.get()) * 80}\n\n")
        if int(e5.get()) != 0:
            reciptarea.insert(END, f"Kebab\t\t {e5.get()}\t\t\t{int(e5.get()) * 150}\n\n")
        if int(e6.get()) != 0:
            reciptarea.insert(END, f"Chawal\t\t {e6.get()}\t\t\t{int(e6.get()) * 100}\n\n")
        if int(e7.get()) != 0:
            reciptarea.insert(END, f"Mutton\t\t {e7.get()}\t\t\t{int(e7.get()) * 200}\n\n")
        if int(e8.get()) != 0:
            reciptarea.insert(END, f"Panner\t\t {e8.get()}\t\t\t{int(e8.get()) * 120}\n\n")
        if int(e9.get()) != 0:
            reciptarea.insert(END, f"Chicken\t\t {e9.get()}\t\t\t{int(e9.get()) * 140}\n\n")
        if int(e10.get()) != 0:
            reciptarea.insert(END, f"Tea\t\t {e10.get()}\t\t\t{int(e10.get()) * 8}\n\n")
        if int(e11.get()) != 0:
            reciptarea.insert(END, f"Lassi\t\t {e11.get()}\t\t\t{int(e11.get()) * 20}\n\n")
        if int(e12.get()) != 0:
            reciptarea.insert(END, f"Coffee\t\t {e12.get()}\t\t\t{int(e12.get()) * 15}\n\n")
        if int(e13.get()) != 0:
            reciptarea.insert(END, f"Faluda\t\t {e13.get()}\t\t\t{int(e13.get()) * 30}\n\n")
        if int(e14.get()) != 0:
            reciptarea.insert(END, f"Shikanji\t\t {e14.get()}\t\t\t{int(e14.get()) * 35}\n\n")
        if int(e15.get()) != 0:
            reciptarea.insert(END, f"Jal-Jeera\t\t {e15.get()}\t\t\t{int(e15.get()) * 20}\n\n")
        if int(e16.get()) != 0:
            reciptarea.insert(END, f"Roohafza\t\t {e16.get()}\t\t\t{int(e16.get()) * 30}\n\n")
        if int(e17.get()) != 0:
            reciptarea.insert(END, f"Badam Milk\t\t {e17.get()}\t\t\t{int(e17.get()) * 40}\n\n")
        if int(e18.get()) != 0:
            reciptarea.insert(END, f"Cold Drinks\t\t {e18.get()}\t\t\t{int(e18.get()) * 50}\n\n")
        if int(e19.get()) != 0:
            reciptarea.insert(END, f"Oreo\t\t {e19.get()}\t\t\t{int(e19.get()) * 250}\n\n")
        if int(e20.get()) != 0:
            reciptarea.insert(END, f"Apple\t\t {e20.get()}\t\t\t{int(e20.get()) * 330}\n\n")
        if int(e21.get()) != 0:
            reciptarea.insert(END, f"Kitkat\t\t {e21.get()}\t\t\t{int(e21.get()) * 400}\n\n")
        if int(e22.get()) != 0:
            reciptarea.insert(END, f"Vanila\t\t {e22.get()}\t\t\t{int(e22.get()) * 200}\n\n")
        if int(e23.get()) != 0:
            reciptarea.insert(END, f"Banana\t\t {e23.get()}\t\t\t{int(e23.get()) * 230}\n\n")
        if int(e24.get()) != 0:
            reciptarea.insert(END, f"Brownie\t\t {e24.get()}\t\t\t{int(e24.get()) * 300}\n\n")
        if int(e25.get()) != 0:
            reciptarea.insert(END, f"Pineapple\t\t {e25.get()}\t\t\t{int(e25.get()) * 280}\n\n")
        if int(e26.get()) != 0:
            reciptarea.insert(END, f"Chocolate\t\t {e26.get()}\t\t\t{int(e26.get()) * 350}\n\n")
        if int(e27.get())!= 0:
            reciptarea.insert(END, f"Black_Forest\t\t {e27.get()}\t\t\t{int(e27.get()) * 450}\n\n")
        f1=int(e1.get())
        f2=int(e2.get())
        f3=int(e3.get())
        f4=int(e4.get())
        f5=int(e5.get())
        f6=int(e6.get())
        f7=int(e7.get())
        f8=int(e8.get())
        f9=int(e9.get())
        d1=int(e10.get())
        d2=int(e11.get())
        d3=int(e12.get())
        d4=int(e13.get())
        d5=int(e14.get())
        d6=int(e15.get())
        d7=int(e16.get())
        d8=int(e17.get())
        d9=int(e18.get())
        c1=int(e19.get())
        c2=int(e20.get())
        c3=int(e21.get())
        c4=int(e22.get())
        c5=int(e23.get())
        c6=int(e24.get())
        c7=int(e25.get())
        c8=int(e26.get())
        c9=int(e27.get())
        food=f1*10+f2*50+f3*90+f4*80+f5*150+f6*100+f7*200+f8*120+f9*140
        drink=d1*8+d2*20+d3*15+d4*30+d5*35+d6*20+d7*30+d8*40+d9*50
        cake=c1*250+c2*330+c3*400+c4*200+c5*230+c6*300+c7*280+c8*350+c9*450
        sub_total=cake+food+drink
        gst=round(sub_total*9/100,2)
        total=sub_total+gst
        reciptarea.insert(END,"*******************************************************************\n")
        reciptarea.insert(END,"*******************************************************************\n\n")
        if food !=0:
            reciptarea.insert(END,f"Cost of Food\t\t\t\t{food}Rs.\n\n")
        if drink !=0:
            reciptarea.insert(END,f"Cost of Drink\t\t\t\t{drink}Rs.\n\n")
        if cake !=0:
            reciptarea.insert(END,f"Cost of Cake\t\t\t\t{cake}Rs.\n\n")
        reciptarea.insert(END, "*******************************************************************\n\n")
        reciptarea.insert(END, "*******************************************************************\n\n")
        reciptarea.insert(END,f"Sub Total       \t\t\t\t{sub_total}Rs.\n\n")
        reciptarea.insert(END,f"Gst             \t\t\t\t{gst}Rs.\n\n")
        reciptarea.insert(END,f"Total             \t\t\t\t{total}Rs.\n\n")
        reciptarea.insert(END, "*******************************************************************\n\n")
        reciptarea.insert(END, "*******************************************************************\n\n")
    else:
        messagebox.showerror("Error", "NO ITEMS SELECTED")


def roti():
    s=var1.get()
    if s==1:
        entry1.config(state=NORMAL)
        entry1.delete(0,END)
        entry1.focus()
    else:
        entry1.config(state=DISABLED)
        e1.set('0')
def dal():
    s=var2.get()
    if s==1:
        entry2.config(state=NORMAL)
        entry2.delete(0,END)
        entry2.focus()
    else:
        entry2.config(state=DISABLED)
        e2.set('0')
def fish():
    s=var3.get()
    if s==1:
        entry3.config(state=NORMAL)
        entry3.delete(0,END)
        entry3.focus()
    else:
        entry3.config(state=DISABLED)
        e3.set('0')
def sabji():
    s=var4.get()
    if s==1:
        entry4.config(state=NORMAL)
        entry4.delete(0,END)
        entry4.focus()
    else:
        entry4.config(state=DISABLED)
        e4.set('0')
def kebab():
    s=var5.get()
    if s==1:
        entry5.config(state=NORMAL)
        entry5.delete(0,END)
        entry5.focus()
    else:
        entry5.config(state=DISABLED)
        e5.set('0')
def chawal():
    s=var6.get()
    if s==1:
        entry6.config(state=NORMAL)
        entry6.delete(0,END)
        entry6.focus()
    else:
        entry6.config(state=DISABLED)
        e6.set('0')
def mutton():
    s=var7.get()
    if s==1:
        entry7.config(state=NORMAL)
        entry7.delete(0,END)
        entry7.focus()
    else:
        entry7.config(state=DISABLED)
        e7.set('0')
def panner():
    s=var8.get()
    if s==1:
        entry8.config(state=NORMAL)
        entry8.delete(0,END)
        entry8.focus()
    else:
        entry8.config(state=DISABLED)
        e8.set('0')
def chicken():
    s=var9.get()
    if s==1:
        entry9.config(state=NORMAL)
        entry9.delete(0,END)
        entry9.focus()
    else:
        entry9.config(state=DISABLED)
        e9.set('0')
def tea():
    s=var10.get()
    if s==1:
        entry10.config(state=NORMAL)
        entry10.delete(0,END)
        entry10.focus()
    else:
        entry10.config(state=DISABLED)
        e10.set('0')
def lassi():
    s=var11.get()
    if s==1:
        entry11.config(state=NORMAL)
        entry11.delete(0,END)
        entry11.focus()
    else:
        entry11.config(state=DISABLED)
        e11.set('0')
def coffee():
    s=var12.get()
    if s==1:
        entry12.config(state=NORMAL)
        entry12.delete(0,END)
        entry12.focus()
    else:
        entry12.config(state=DISABLED)
        e12.set('0')
def faluda():
    s=var13.get()
    if s==1:
        entry13.config(state=NORMAL)
        entry13.delete(0,END)
        entry13.focus()
    else:
        entry13.config(state=DISABLED)
        e13.set('0')
def shikanji():
    s=var14.get()
    if s==1:
        entry14.config(state=NORMAL)
        entry14.delete(0,END)
        entry14.focus()
    else:
        entry14.config(state=DISABLED)
        e14.set('0')
def jal_jeera():
    s=var15.get()
    if s==1:
        entry15.config(state=NORMAL)
        entry15.delete(0,END)
        entry15.focus()
    else:
        entry15.config(state=DISABLED)
        e15.set('0')
def roohafza():
    s=var16.get()
    if s==1:
        entry16.config(state=NORMAL)
        entry16.delete(0,END)
        entry16.focus()
    else:
        entry16.config(state=DISABLED)
        e16.set('0')
def badam_milk():
    s=var17.get()
    if s==1:
        entry17.config(state=NORMAL)
        entry17.delete(0,END)
        entry17.focus()
    else:
        entry17.config(state=DISABLED)
        e17.set('0')
def cold_drinks():
    s=var18.get()
    if s==1:
        entry18.config(state=NORMAL)
        entry18.delete(0,END)
        entry18.focus()
    else:
        entry18.config(state=DISABLED)
        e18.set('0')
def oreo():
    s=var19.get()
    if s==1:
        entry19.config(state=NORMAL)
        entry19.delete(0,END)
        entry19.focus()
    else:
        entry19.config(state=DISABLED)
        e19.set('0')
def apple():
    s=var20.get()
    if s==1:
        entry20.config(state=NORMAL)
        entry20.delete(0,END)
        entry20.focus()
    else:
        entry20.config(state=DISABLED)
        e20.set('0')
def kitkat():
    s=var21.get()
    if s==1:
        entry21.config(state=NORMAL)
        entry21.delete(0,END)
        entry21.focus()
    else:
        entry21.config(state=DISABLED)
        e21.set('0')
def vanila():
    s=var22.get()
    if s==1:
        entry22.config(state=NORMAL)
        entry22.delete(0,END)
        entry22.focus()
    else:
        entry22.config(state=DISABLED)
        e22.set('0')
def banana():
    s=var23.get()
    if s==1:
        entry23.config(state=NORMAL)
        entry23.delete(0,END)
        entry23.focus()
    else:
        entry23.config(state=DISABLED)
        e23.set('0')
def brownie():
    s=var24.get()
    if s==1:
        entry24.config(state=NORMAL)
        entry24.delete(0,END)
        entry24.focus()
    else:
        entry24.config(state=DISABLED)
        e24.set('0')
def pineapple():
    s=var25.get()
    if s==1:
        entry25.config(state=NORMAL)
        entry25.delete(0,END)
        entry25.focus()
    else:
        entry25.config(state=DISABLED)
        e25.set('0')
def chocolate():
    s=var26.get()
    if s==1:
        entry26.config(state=NORMAL)
        entry26.delete(0,END)
        entry26.focus()
    else:
        entry26.config(state=DISABLED)
        e26.set('0')
def black_forest():
    s=var27.get()
    if s==1:
        entry27.config(state=NORMAL)
        entry27.delete(0,END)
        entry27.focus()
    else:
        entry27.config(state=DISABLED)
        e27.set('0')
#=================VARIABLES======================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e1=StringVar()
e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
e6=StringVar()
e7=StringVar()
e8=StringVar()
e9=StringVar()
e10=StringVar()
e11=StringVar()
e12=StringVar()
e13=StringVar()
e14=StringVar()
e15=StringVar()
e16=StringVar()
e17=StringVar()
e18=StringVar()
e19=StringVar()
e20=StringVar()
e21=StringVar()
e22=StringVar()
e23=StringVar()
e24=StringVar()
e25=StringVar()
e26=StringVar()
e27=StringVar()

e_food=StringVar()
e_drink=StringVar()
e_cake=StringVar()
e_subtotal=StringVar()
e_gst=StringVar()
e_total=StringVar()

e1.set('0')
e2.set('0')
e3.set('0')
e4.set('0')
e5.set('0')
e6.set('0')
e7.set('0')
e8.set('0')
e9.set('0')
e10.set('0')
e11.set('0')
e12.set('0')
e13.set('0')
e14.set('0')
e15.set('0')
e16.set('0')
e17.set('0')
e18.set('0')
e19.set('0')
e20.set('0')
e21.set('0')
e22.set('0')
e23.set('0')
e24.set('0')
e25.set('0')
e26.set('0')
e27.set('0')


#=================TITLE===============
titleframe=Frame(root,bg="firebrick4",borderwidth=10,relief=RIDGE)
titleframe.place(x=0,y=0,height=80,width=1490)
titlelabel=Label(titleframe,text="RESTURANT MANAGEMENT SYSTEM",font="arial 34 bold",justify=CENTER,bg='firebrick4',fg='yellow').pack()

#============================MENU=========================

menu_frame=Frame(root,borderwidth=10,relief=RIDGE,bg='firebrick4')
menu_frame.place(x=0,y=80,height=680,width=1040)

#=======================FOOD==============================

foodframe=LabelFrame(menu_frame,text='FOOD',font='arial 20 bold',borderwidth=10,relief=RIDGE,fg="red4")
foodframe.place(x=0,y=0,height=520,width=340)

roti=Checkbutton(foodframe,text='Roti 10Rs.',font='arial 14 bold',pady=10,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)
dal=Checkbutton(foodframe,text='Dal 50Rs.',font='arial 14 bold',pady=10,variable=var2,command=dal)
dal.grid(row=1,column=0,sticky=W)
fish=Checkbutton(foodframe,text='Fish 90Rs.',font='arial 14 bold',pady=10,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)
sabji=Checkbutton(foodframe,text='Sabji 80Rs.',font='arial 14 bold',pady=10,variable=var4,command=sabji)
sabji.grid(row=3,column=0,sticky=W)
kebab=Checkbutton(foodframe,text='Kebab 150Rs.',font='arial 14 bold',pady=10,variable=var5,command=kebab)
kebab.grid(row=4,column=0,sticky=W)
chawal=Checkbutton(foodframe,text='Chawal 100Rs.',font='arial 14 bold',pady=10,variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)
mutton=Checkbutton(foodframe,text='Mutton 200Rs.',font='arial 14 bold',pady=10,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)
paneer=Checkbutton(foodframe,text='Paneer 120Rs.',font='arial 14 bold',pady=10,variable=var8,command=panner)
paneer.grid(row=7,column=0,sticky=W)
chicken=Checkbutton(foodframe,text='Chicken 140Rs.',font='arial 14 bold',pady=10,variable=var9,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

entry1=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e1)
entry1.grid(row=0,column=1)
entry2=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e2)
entry2.grid(row=1,column=1)
entry3=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e3)
entry3.grid(row=2,column=1)
entry4=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e4)
entry4.grid(row=3,column=1)
entry5=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e5)
entry5.grid(row=4,column=1)
entry6=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e6)
entry6.grid(row=5,column=1)
entry7=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e7)
entry7.grid(row=6,column=1)
entry8=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e8)
entry8.grid(row=7,column=1)
entry9=Entry(foodframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e9)
entry9.grid(row=8,column=1)

#=================================DRINKS=====================================

drinkframe=LabelFrame(menu_frame,text='DRINK',font='arial 20 bold',borderwidth=10,relief=RIDGE,fg="red4")
drinkframe.place(x=340,y=0,height=520,width=340)

tea=Checkbutton(drinkframe,text='Tea 8Rs.',font='arial 14 bold',pady=10,variable=var10,command=tea)
tea.grid(row=0,column=0,sticky=W)
lassi=Checkbutton(drinkframe,text='Lassi 20Rs.',font='arial 14 bold',pady=10,variable=var11,command=lassi)
lassi.grid(row=1,column=0,sticky=W)
coffee=Checkbutton(drinkframe,text='Coffee 15Rs.',font='arial 14 bold',pady=10,variable=var12,command=coffee)
coffee.grid(row=2,column=0,sticky=W)
faluda=Checkbutton(drinkframe,text='Faluda 30Rs.',font='arial 14 bold',pady=10,variable=var13,command=faluda)
faluda.grid(row=3,column=0,sticky=W)
shikanji=Checkbutton(drinkframe,text='Shikanji 35Rs.',font='arial 14 bold',pady=10,variable=var14,command=shikanji)
shikanji.grid(row=4,column=0,sticky=W)
jal_jeera=Checkbutton(drinkframe,text='Jal-jeera 20Rs.',font='arial 14 bold',pady=10,variable=var15,command=jal_jeera)
jal_jeera.grid(row=5,column=0,sticky=W)
roohafza=Checkbutton(drinkframe,text='Roohafza 30Rs.',font='arial 14 bold',pady=10,variable=var16,command=roohafza)
roohafza.grid(row=6,column=0,sticky=W)
badam_milk=Checkbutton(drinkframe,text='Badam Milk 40Rs.',font='arial 14 bold',pady=10,variable=var17,command=badam_milk)
badam_milk.grid(row=7,column=0,sticky=W)
cold_drinks=Checkbutton(drinkframe,text='Cold Drinks 50Rs.',font='arial 14 bold',pady=10,variable=var18,command=cold_drinks)
cold_drinks.grid(row=8,column=0,sticky=W)


entry10=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e10)
entry10.grid(row=0,column=1)
entry11=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e11)
entry11.grid(row=1,column=1)
entry12=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e12)
entry12.grid(row=2,column=1)
entry13=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e13)
entry13.grid(row=3,column=1)
entry14=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e14)
entry14.grid(row=4,column=1)
entry15=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e15)
entry15.grid(row=5,column=1)
entry16=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e16)
entry16.grid(row=6,column=1)
entry17=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e17)
entry17.grid(row=7,column=1)
entry18=Entry(drinkframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e18)
entry18.grid(row=8,column=1)

#============================CAKES==========================

cakeframe=LabelFrame(menu_frame,text='CAKE',font='arial 20 bold',borderwidth=10,relief=RIDGE,fg="red4")
cakeframe.place(x=680,y=0,height=520,width=340)

oreo=Checkbutton(cakeframe,text='Oreo 250Rs.',font='arial 14 bold',pady=10,variable=var19,command=oreo)
oreo.grid(row=0,column=0,sticky=W)
apple=Checkbutton(cakeframe,text='Apple 330Rs.',font='arial 14 bold',pady=10,variable=var20,command=apple)
apple.grid(row=1,column=0,sticky=W)
kitkat=Checkbutton(cakeframe,text='Kitkat 400Rs.',font='arial 14 bold',pady=10,variable=var21,command=kitkat)
kitkat.grid(row=2,column=0,sticky=W)
vanila=Checkbutton(cakeframe,text='Vanila 200Rs.',font='arial 14 bold',pady=10,variable=var22,command=vanila)
vanila.grid(row=3,column=0,sticky=W)
banana=Checkbutton(cakeframe,text='Banana 230Rs.',font='arial 14 bold',pady=10,variable=var23,command=banana)
banana.grid(row=4,column=0,sticky=W)
brownie=Checkbutton(cakeframe,text='Brownie 300Rs.',font='arial 14 bold',pady=10,variable=var24,command=brownie)
brownie.grid(row=5,column=0,sticky=W)
pineapple=Checkbutton(cakeframe,text='Pineapple 280Rs.',font='arial 14 bold',pady=10,variable=var25,command=pineapple)
pineapple.grid(row=6,column=0,sticky=W)
chocolate=Checkbutton(cakeframe,text='Chocolate 350Rs.',font='arial 14 bold',pady=10,variable=var26,command=chocolate)
chocolate.grid(row=7,column=0,sticky=W)
black_forest=Checkbutton(cakeframe,text='Black Forest 450Rs.',font='arial 14 bold',pady=10,variable=var27,command=black_forest)
black_forest.grid(row=8,column=0,sticky=W)

entry19=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e19)
entry19.grid(row=0,column=1)
entry20=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e20)
entry20.grid(row=1,column=1)
entry21=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e21)
entry21.grid(row=2,column=1)
entry22=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e22)
entry22.grid(row=3,column=1)
entry23=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e23)
entry23.grid(row=4,column=1)
entry24=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e24)
entry24.grid(row=5,column=1)
entry25=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e25)
entry25.grid(row=6,column=1)
entry26=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e26)
entry26.grid(row=7,column=1)
entry27=Entry(cakeframe,width=7,borderwidth=5,relief=RIDGE,state=DISABLED,font='arial 14 bold',textvariable=e27)
entry27.grid(row=8,column=1)

#=====================TOTAL COSTS==========================

totalframe=Frame(menu_frame,bd=10,relief=RIDGE,bg='firebrick4')
totalframe.place(x=0,y=520,height=140,width=1020)

foodcost=Label(totalframe,text="Total Food Cost:",font='arial 16 bold',bg='firebrick4',fg='white',padx=15,pady=15)
foodcost.grid(row=0,column=0)
drinkcost=Label(totalframe,text="Total Drink Cost:",font='arial 16 bold',bg='firebrick4',fg='white',padx=15,pady=10).grid(row=0,column=2)
cakecost=Label(totalframe,text="Total Cake Cost:",font='arial 16 bold',bg='firebrick4',fg='white',padx=15,pady=10).grid(row=0,column=4)

e_foodcost=Entry(totalframe,state='readonly',font='arial 14 bold',width=10,borderwidth=5,relief=RIDGE,textvariable=e_food)
e_foodcost.grid(row=0,column=1,padx=5)
e_drinkcost=Entry(totalframe,state='readonly',font='arial 14 bold',width=10,borderwidth=5,relief=RIDGE,textvariable=e_drink)
e_drinkcost.grid(row=0,column=3,padx=5)
e_cakecost=Entry(totalframe,state='readonly',font='arial 14 bold',width=10,borderwidth=5,relief=RIDGE,textvariable=e_cake)
e_cakecost.grid(row=0,column=5,padx=5)

sub_totalcost=Label(totalframe,text='Sub Total:',font='arial 16 bold',bg='firebrick4',fg='white',padx=15,pady=10).grid(row=1,column=0)
gstcost=Label(totalframe,text='GST(9%):',font='arial 16 bold',bg='firebrick4',fg='white',padx=15,pady=10).grid(row=1,column=2)
totalcost=Label(totalframe,text='Total:',font='arial 16 bold',bg='firebrick4',fg='white',padx=15,pady=10).grid(row=1,column=4)

e_subtotalcost=Entry(totalframe,state='readonly',font='arial 14 bold',width=10,borderwidth=5,relief=RIDGE,textvariable=e_subtotal)
e_subtotalcost.grid(row=1,column=1,padx=5)
e_gstcost=Entry(totalframe,state='readonly',font='arial 14 bold',width=10,borderwidth=5,relief=RIDGE,textvariable=e_gst)
e_gstcost.grid(row=1,column=3,padx=5)
e_totalcost=Entry(totalframe,state='readonly',font='arial 14 bold',width=10,borderwidth=5,relief=RIDGE,textvariable=e_total)
e_totalcost.grid(row=1,column=5,padx=5)


#==========================RECIPT AND BUTTONS=============================

rightframe=Frame(root,bg='firebrick4',bd=10,relief=RIDGE)
rightframe.place(x=1040,y=80,height=680,width=450)

reciptarea=Text(rightframe,bd=10,font='arial 12 bold',relief=RIDGE,height=30,width=45)
reciptarea.grid(row=0,column=0)

buttonframe=Frame(rightframe,borderwidth=10,relief=RIDGE,bg='firebrick4')
buttonframe.grid(row=1,column=0,sticky=S)

button1=Button(buttonframe,text="TOTAL",width=7,height=2,font='arial 12 bold',bg='firebrick4',fg='white',command=total).grid(row=0,column=0,padx=1,)
button2=Button(buttonframe,text="RECIPT",width=7,height=2,font='arial 12 bold',bg='firebrick4',fg='white',command=recipt).grid(row=0,column=1,padx=1)
button3=Button(buttonframe,text="SAVE",width=7,height=2,font='arial 12 bold',bg='firebrick4',fg='white',command=save).grid(row=0,column=2,padx=1,)
button4=Button(buttonframe,text="RESET",width=7,height=2,font='arial 12 bold',bg='firebrick4',fg='white',command=reset).grid(row=0,column=3,padx=1,)
button5=Button(buttonframe,text="EXIT",width=7,height=2,font='arial 12 bold',bg='firebrick4',fg='white',command=exit).grid(row=0,column=4,padx=1,)

root.mainloop()