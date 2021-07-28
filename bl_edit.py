from tkinter import *
from tkinter import messagebox
import random
import tkinter.messagebox as MessageBox
import time
import datetime
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = Entryname.get()

    if(id=="" or name==""):
        MessageBox.showinfo("Insert status", "All fields are reqiuired")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="",database="nama_pelanggan")
        cursor1 = con.cursor()
        cursor1.execute("insert into pelanggan values('"+  id  +"','"+ name +"')")
        cursor1.execute("commit")
        MessageBox.showinfo("Status ", "Saved ")
        con.close()

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete status", "Compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="",database="nama_pelanggan")
        cursor1 = con.cursor()
        cursor1.execute("delete from pelanggan where id='"+ e_id.get() +"'")
        cursor1.execute("commit")
        MessageBox.showinfo("Status ", " Deleted ")
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", passwd="",database="nama_pelanggan")
    cursor1 = con.cursor()
    cursor1.execute("select * from pelanggan")
    rows = cursor1.fetchall()
    for row in rows:
        insertData = str(row[0])+ '  '+ row[1]
        list.insert(list.size()+1, insertData)
    con.close()


root =Tk()
root.geometry("1350x750")
root.title("Cafe Billing System")
root.configure(background='#996633')

Tops = Frame(root,bg='brown',bd=5,pady=2,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=('Times',27,'bold'),text='Cafe Billing',bd=12,bg='white',justify=CENTER,width= 17)
lblTitle.grid(row=0)

var = StringVar()
label = Label( root, textvariable=var,font=('Times',10,),bd=7, relief=FLAT )
var.set("No.Meja")
label.place(x=20, y=100)

var = StringVar()
label = Label( root, textvariable=var,font=('Times',10,),bd=7, relief=FLAT )
var.set("Nama Pelanggan")
label.place(x=20, y=140)

var = StringVar()
Entryname = Entry( root, textvariable=var,font=('Times',10,'bold'),bd=7, width=30, relief=SUNKEN )
Entryname.place(x=150, y=140)

var = StringVar()
e_id = Entry( root, textvariable=var,font=('Times',10,'bold'),bd=7, width=30, relief=SUNKEN )
e_id.place(x=150, y=100)

insrt = Button(root, text=" IN ",font=('Times',8,),bd=5,relief=RAISED,command=insert)
insrt.place(x=150,y=175)

insrt = Button(root, text="OUT",font=('Times',8,),bd=5,relief=RAISED,command=delete)
insrt.place(x=200,y=175)

list = Listbox(root, width=25,height=9) 
list.place(x=400, y=100)
show()




f1 = Frame(root, width= 900, height=180, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width= 400, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width= 900, height=180, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width= 900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width = 440, height = 450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width = 440, height = 250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 400, height = 180, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 400, height = 180, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width = 450, height = 100, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width = 450, height = 100, bd=14, relief="raise")
f2ab.pack(side=RIGHT)


f1.configure(background='black')
f2.configure(background='black')







#================================================================================================================================

def HargaItem():
    Item1=float(E_Pancake_mangga.get())
    Item2=float(E_Mango_cheese.get())
    Item3=float(E_Oreo_dessert.get())
    Item4=float(E_Choco_brownies.get())

    Item5=float(E_Caramel.get())
    Item6=float(E_Lychee.get())
    Item7=float(E_Bubble.get())
    Item8=float(E_Cappuccino.get())


    PriceofDessert = (Item1 * 1.52) + (Item2 * 1.49) + (Item3 * 1.77) + (Item4 * 1.84)

    PriceofDrinks = (Item1 * 1.67) + (Item2 * 1.35) + (Item3 * 1.99) + (Item4 * 1.49)

    DrinksPrice = "$", str('%.2f'%(PriceofDrinks))
    DessertPrice = "$", str('%.2f'%(PriceofDessert))
    HargaMakanan.set(DessertPrice)
    HargaMinuman.set(DrinksPrice)
    BL = "$", str('%.2f'%(1.59))
    BiayaLayanan.set(BL)

    SubTotalofItems = "$", str('%.2f'%(PriceofDessert + PriceofDrinks + 1.59))
    SubTotal.set(SubTotalofItems)

    Kirim = "$", str('%.2f'%((PriceofDessert + PriceofDrinks + 1.59)*0.15))
    BiayaPengiriman.set(Kirim)

    AA = ((PriceofDessert + PriceofDrinks + 1.59)*0.15)
    AC = "$", str('%.2f'%(PriceofDessert + PriceofDrinks + 1.59 + AA))
    TotalHarga.set(AC)

def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        

def Reset():
    BiayaPengiriman.set("")
    SubTotal.set("")
    TotalHarga.set("")
    HargaMakanan.set("")
    HargaMinuman.set("")
    BiayaLayanan.set("")
    txtReceipt.delete("1.0", END)

    E_Pancake_mangga.set("0")
    E_Mango_cheese.set("0")
    E_Oreo_dessert.set("0")
    E_Choco_brownies.set("0")

    E_Caramel.set("0")
    E_Lychee.set("0")
    E_Bubble.set("0")
    E_Cappuccino.set("0")
    

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    

    txtPancake_mangga.configure(state= DISABLED)
    txtMango_cheese.configure(state= DISABLED)
    txtOreo_dessert.configure(state= DISABLED)
    txtChoco_brownies.configure(state= DISABLED)
    txtCaramel.configure(state= DISABLED)
    txtLychee.configure(state= DISABLED)
    txtBubble.configure(state= DISABLED)
    txtCappuccino.configure(state= DISABLED)




def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Info Receipt:\t\t\t'+ Receipt_Ref.get() +'\t\t'+ DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t\t'+ "Harga Item \n\n")
    
    txtReceipt.insert(END, 'Pancake Mangga: \t\t\t\t\t'+ E_Pancake_mangga.get()+ "\n")
    txtReceipt.insert(END, 'Mango Cheese: \t\t\t\t\t'+ E_Mango_cheese.get()+ "\n")
    txtReceipt.insert(END, 'Oreo Dessert: \t\t\t\t\t'+ E_Oreo_dessert.get()+ "\n")
    txtReceipt.insert(END, 'Choco Brownies: \t\t\t\t\t'+ E_Choco_brownies.get()+ "\n")
    txtReceipt.insert(END, 'Caramel: \t\t\t\t\t'+ E_Caramel.get()+ "\n")
    txtReceipt.insert(END, 'Lychee: \t\t\t\t\t'+ E_Lychee.get()+ "\n")
    txtReceipt.insert(END, 'Bubble: \t\t\t\t\t'+ E_Bubble.get()+ "\n")
    txtReceipt.insert(END, 'Cappuccino: \t\t\t\t\t'+ E_Cappuccino.get()+ "\n")

    txtReceipt.insert(END, 'Harga Minuman:\t\t' + HargaMinuman.get()  +  '\tBiaya Pengiriman:\t\t' + BiayaPengiriman.get()+"\n")
    txtReceipt.insert(END, 'Harga Makanan:\t\t' + HargaMakanan.get()  +  '\tSubTotal:\t\t' + SubTotal.get()+"\n")
    txtReceipt.insert(END, 'Biaya Layanan:\t\t' + BiayaLayanan.get()  +  '\tTotal Harga:\t\t' + TotalHarga.get()+"\n")



#==============================================CheckButton=======================================================================

def chkbutton_value():
    if (var1.get() == 1):
        txtPancake_mangga.configure(state= NORMAL)
    elif var1.get()== 0:
        txtPancake_mangga.configure(state= DISABLED)
        E_Pancake_mangga.set("0")
        
    if (var2.get() == 1):
        txtMango_cheese.configure(state= NORMAL)
    elif var2.get()== 0:
        txtMango_cheese.configure(state= DISABLED)
        E_Mango_cheese.set("0")

    if (var3.get() == 1):
        txtOreo_dessert.configure(state= NORMAL)
    elif var3.get()== 0:
        txtOreo_dessert.configure(state= DISABLED)
        E_Oreo_dessert.set("0")

    if (var4.get() == 1):
        txtChoco_brownies.configure(state= NORMAL)
    elif var4.get()== 0:
        txtChoco_brownies.configure(state= DISABLED)
        E_Choco_brownies.set("0")

    if (var5.get() == 1):
        txtCaramel.configure(state= NORMAL)
    elif var5.get()== 0:
        txtCaramel.configure(state= DISABLED)
        E_Caramel.set("0")

    if (var6.get() == 1):
        txtLychee.configure(state= NORMAL)
    elif var6.get()== 0:
        txtLychee.configure(state= DISABLED)
        E_Lychee.set("0")

    if (var7.get() == 1):
        txtBubble.configure(state= NORMAL)
    elif var7.get()== 0:
        txtBubble.configure(state= DISABLED)
        E_Bubble.set("0")

    if (var8.get() == 1):
        txtCappuccino.configure(state= NORMAL)
    elif var8.get()== 0:
        txtCappuccino.configure(state= DISABLED)
        E_Cappuccino.set("0")

#=================================================Variabel=========================================================================================
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
BiayaPengiriman=StringVar()
SubTotal=StringVar()
TotalHarga=StringVar()
HargaMakanan=StringVar()
HargaMinuman=StringVar()
BiayaLayanan=StringVar()

E_Pancake_mangga=StringVar()
E_Mango_cheese=StringVar()
E_Oreo_dessert=StringVar()
E_Choco_brownies=StringVar()

E_Caramel=StringVar()
E_Lychee=StringVar()
E_Bubble=StringVar()
E_Cappuccino=StringVar()

E_Pancake_mangga.set("0")
E_Mango_cheese.set("0")
E_Oreo_dessert.set("0")
E_Choco_brownies.set("0")

E_Caramel.set("0")
E_Lychee.set("0")
E_Bubble.set("0")
E_Cappuccino.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))


#=========================================================DESSERT========================================================================================================================
Pancake_mangga = Checkbutton(f1aa, text="Pancake Mangga \t", variable = var1, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 0, sticky=W)
 
Mango_cheese = Checkbutton(f1aa, text="Mango Cheese Cake \t\t", variable = var2, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 3, sticky=W)

Oreo_dessert = Checkbutton(f1aa, text="Oreo Dessert Cup \t\t", variable = var3, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 6, sticky=W)

Choco_brownies = Checkbutton(f1aa, text="Choco Brownies \t\t", variable = var4, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 7, sticky=W)

#========================================================DRINK=========================================================================================================================

Caramel = Checkbutton(f1ab, text="Caramel Macchiato \t", variable = var5, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 1, sticky=W)

Lychee = Checkbutton(f1ab, text="Lychee Tea \t", variable = var6, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 5, sticky=W)

Bubble = Checkbutton(f1ab, text="Bubble Taro Milk \t", variable = var7, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 6, sticky=W)

Cappuccino = Checkbutton(f1ab, text="Cappuccino \t", variable = var8, onvalue = 1, offvalue = 0, font=('arial',12,'bold'), command=chkbutton_value).grid(row = 7, sticky=W)

#==================================================WIDGET untuk DESSERT=============================================================================================================
txtPancake_mangga = Entry(f1aa, font=('arial',12,'bold'), textvariable=E_Pancake_mangga, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtPancake_mangga.grid(row = 0, column = 1)

txtMango_cheese = Entry(f1aa, font=('arial',12,'bold'), textvariable=E_Mango_cheese, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtMango_cheese.grid(row = 3, column = 1)

txtOreo_dessert = Entry(f1aa, font=('arial',12,'bold'), textvariable=E_Oreo_dessert, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtOreo_dessert.grid(row = 6, column = 1)

txtChoco_brownies = Entry(f1aa, font=('arial',12,'bold'), textvariable=E_Choco_brownies, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtChoco_brownies.grid(row = 7, column = 1)

#==================================================WIDGET untuk MINUMAN=============================================================================================================

txtCaramel = Entry(f1ab, font=('arial',12,'bold'), textvariable=E_Caramel, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtCaramel.grid(row = 1, column = 1)

txtLychee = Entry(f1ab, font=('arial',12,'bold'), textvariable=E_Lychee, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtLychee.grid(row = 5, column = 1)

txtBubble = Entry(f1ab, font=('arial',12,'bold'), textvariable=E_Bubble, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtBubble.grid(row = 6, column = 1)

txtCappuccino = Entry(f1ab, font=('arial',12,'bold'), textvariable=E_Cappuccino, bd = 8, width = 6, justify = 'left', state = DISABLED)
txtCappuccino.grid(row = 7, column = 1)

#===================================================Label Receipt====================================================================================

lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt:", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width = 59, height = 22, bg="white", bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

#================================================Informasi Harga Item===========================================================================

lblHargaMinuman = Label(f2aa, font=('arial', 10, 'bold'), text="Harga Minuman", bd=8)
lblHargaMinuman.grid(row = 2, column = 0, sticky = W)
txtHargaMinuman = Entry(f2aa, font=('arial', 10, 'bold'), bd=8, insertwidth=2, justify = 'left', textvariable=HargaMinuman)
txtHargaMinuman.grid(row = 2, column = 1, sticky = W)

lblHargaMakanan = Label(f2aa, font=('arial', 10, 'bold'), text="Harga Makanan", bd=8)
lblHargaMakanan.grid(row = 3, column = 0, sticky = W)
txtHargaMakanan = Entry(f2aa, font=('arial', 10, 'bold'), bd=8, justify = 'left', textvariable=HargaMakanan)
txtHargaMakanan.grid(row = 3, column = 1, sticky = W)

lblBiayaLayanan = Label(f2aa, font=('arial', 10, 'bold'), text="Biaya Layanan", bd=8)
lblBiayaLayanan.grid(row = 4, column = 0, sticky = W)
txtBiayaLayanan = Entry(f2aa, font=('arial', 10, 'bold'), bd=8, justify = 'left', textvariable=BiayaLayanan)
txtBiayaLayanan.grid(row = 4, column = 1, sticky = W)

#==================================================Informasi Pembayaran============================================================================

lblBiayaPengiriman = Label(f2ab, font=('arial', 10, 'bold'), text="Biaya Pengiriman", bd=8)
lblBiayaPengiriman.grid(row = 2, column = 0, sticky = W)
txtBiayaPengiriman = Entry(f2ab, font=('arial', 10, 'bold'), bd=8, justify = 'left', textvariable=BiayaPengiriman)
txtBiayaPengiriman.grid(row = 2, column = 1, sticky = W)

lblSubTotal = Label(f2ab, font=('arial', 10, 'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row = 3, column = 0, sticky = W)
txtSubTotal = Entry(f2ab, font=('arial', 10, 'bold'), bd=8, justify = 'left', textvariable=SubTotal)
txtSubTotal.grid(row = 3, column = 1, sticky = W)

lblTotalHarga = Label(f2ab, font=('arial', 10, 'bold'), text="Total Harga", bd=8)
lblTotalHarga.grid(row = 4, column = 0, sticky = W)
txtTotalHarga = Entry(f2ab, font=('arial', 10, 'bold'), bd=8, justify = 'left', textvariable=TotalHarga)
txtTotalHarga.grid(row = 4, column = 1, sticky = W)

#======================================================================================================================================
Total = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 10, 'bold'), width=5, text="Total", command = HargaItem).grid(row=0, column=0)

Receipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 10, 'bold'), width=5, text="Receipt", command = Receipt).grid(row=0, column=1)

Reset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 10, 'bold'), width=5, text="Reset", command = Reset).grid(row=0, column=2)

Exit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 10, 'bold'), width=5, text="Exit", command = qExit).grid(row=0, column=3)


#======================================================================================================================================

root.mainloop()
