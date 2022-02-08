from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import ImageTk,Image
import datetime
import math
import os
import random

date=datetime.datetime.now().date()

#connect to the database

conn=sqlite3.connect(r"D:\Klaus\OTHER PROJECTS\store system\Database\store.db")
c=conn.cursor()


#============= temporarly lists like sessions  ========
products_list = []
product_price= []
product_quantity = []
product_id = []

#labels list

labels_list = [ ]

#configure
def ajax():
    get_id = Id_entry.get()
    query="SELECT * FROM inventory WHERE id=?"
    result = c.execute(query,(get_id,))
    for r in result:
        get_id=r[0]
        get_name=r[1]
        get_price=r[4]


    productname = Label(left_side, font=('cambria 16 bold'),fg='red')
    productname.configure(text="Product's Name: " + str(get_name))
    productname.place(x=0,y=270)
    
    productprice = Label(left_side, font=('cambria 16 bold'),fg='red')
    productprice.configure(text="Price: Ksh. " + str(get_price))
    productprice.place(x=0,y=300)

def add_to_cart():
    get_id = Id_entry.get()
    query="SELECT * FROM inventory WHERE id=?"
    result = c.execute(query,(get_id,))
    for r in result:
        get_id=r[0]
        get_name=r[1]
        get_price=r[4]
        get_stock =r[2]
    quantity_value= int(quantity_e.get())
    if quantity_value > int(get_stock):
        tkinter.messagebox.showinfo("Error", " Not that many products in our inventory")
    else:

        #calculate the price 
        final_price = (float(quantity_value) * (get_price)) - (float(discount_e.get()))
        
        products_list.append(get_name)
        product_price.append(final_price)
        product_quantity.append(quantity_value)
        product_id.append(get_id)

        x_index=0
        y_index=100
        counter=0
        
        #total label and given amount.
        total_l=Label(right_side,text=" ", font=('cambria 28 bold'),bg='#e7eae5',fg='#043927')
        total_l.place(x=0,y=600)

        for p in products_list:
            tempname=Label(right_side, text=str(products_list[counter]),font=('cambria 14 bold'),bg='#4F7942',fg='white')
            tempname.place(x=0,y=y_index)
            labels_list.append(tempname)

            tempqt=Label(right_side, text=str(product_quantity[counter]),font=('cambria 14 bold'),bg='#4F7942',fg='white')
            tempqt.place(x=300,y=y_index)
            labels_list.append(tempqt)

            tempprice=Label(right_side, text=str(product_price[counter]),font=('cambria 14 bold'),bg='#4F7942',fg='white')
            tempprice.place(x=500,y=y_index)
            labels_list.append(tempprice)


            y_index += 40
            counter += 1
            
            total_l.configure(text=('Total:' + " " + str(sum(product_price))))
            

def customer_change():
    #calculating the change.
    entered_amount= change_e.get()
    final_amount=float(entered_amount) - float(str(sum(product_price)))

    final_bill_label=Label(right_side,text=" ", height=2,width=20, font=('cambria 16 bold'),fg='#043927')
    final_bill_label.configure(text=('Change:'+ " " + str(final_amount)))
    final_bill_label.place(x=350,y=600)

def generate_bill():
    #create the bill before updating the database 
    directory = "C:/Users\DENNIS/Desktop/store system/invoice/" + str(date) + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    #TEMPLATES FOR THE BILL
    company="\t\t\t\tMutithi Farmers' Association\n "
    address="\t\t\t\tNgurubani, Mwea\n"
    phone = "\t\t\t\t\t0728272483\n"
    sample= "\t\t\t\t\t Purchase Invoice\n"
    dt = "\t\t\t\t\t" + str(date)

    table_header= "\n\n\t\t\t-----------------------------\n\t\t\tSN.\Products\tQty\tAmount\n\t\t\t-----------------------------"
    final=company + address + phone + sample + dt + "\n" + table_header

    # open  file to write it to.
    file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
    f=open(file_name,'w')
    f.write(final)
    #fill the dynamics
    i=0
    r=1
    for t in products_list:
        f.write("\n\t\t\t" +str(r) + "\t" + str(products_list[i] + ".......")[:7] + "\t\t" + str(product_quantity[i]) + "\t\t" + str(product_price[i]))
        i+=1
        r +=1
        
    f.write("\n\n\t\t\tTotal: Ksh. " + str(sum(product_price)))
    f.write("\n\t\t\tThanks for Shopping with us")
    os.startfile(file_name,"print")
    f.close()


    #decrease the stock
    x=0

    initial = " SELECT * FROM inventory WHERE id=?"
    result = c.execute(initial, (product_id[x], ))

    for i in products_list:
        for r in result:
            old_stock = r[2]
            new_stock = int(old_stock) - int(product_quantity[x])
        #updating the stock

        sql="UPDATE inventory SET stock=? WHERE id=? "
        c.execute(sql, (new_stock, product_id[x]))
        conn.commit()

        #insert into the transactionss
        sql2= " INSERT INTO transactionss (productss, quantity, amount, date) VALUES ( ?,?,?,?)"
        c.execute(sql2, (products_list[x], product_quantity[x], product_price[x], date))
        conn.commit( )

        x=x+1
    for a in labels_list:
        a.destroy()

    del(products_list[:])
    del(product_id[:])
    del(product_quantity[:])
    del(product_price[:])

    tkinter.messagebox.showinfo("Success" , " Done everything succesfully")


root= Tk()
root.title("Mutithi Farmers ")
root.iconbitmap(r'tttt.ico')




left_side=Frame(root, width = 700, height=768,bg='#d6d7d2')
left_side.pack(side=LEFT)

right_side=Frame(root, width = 666, height=768,bg='#4F7942')
right_side.pack(side=RIGHT)

#===============logo requirements =================

farm_logo=Image.open(r"C:\Users\DENNIS\Desktop\store system\tttt.png")
image2=farm_logo.resize((170,150),Image.ANTIALIAS)
farm_logo2=ImageTk.PhotoImage(image2)

label_1=Label(left_side, image=farm_logo2)
label_1.place(x=0,y=0)
label_2=Label(root, text=" Mutithi Farmers' \n Association",font=('forte 24 bold'),bg='#d6d7d2',fg='green')
label_2.place(x=200,y=70)

date_l= Label(right_side, text="Today's Date: " + str(date), font=('cambria 16 bold'),bg='#4F7942',fg='#d6d7d2')
date_l.place(x=5, y=5)


#============table invoice requirements========
tProduct =Label(right_side, text='Products', font=('cambria 16 bold'),fg='#043927')
tProduct.place(x=0,y=60)

tQuantity=Label(right_side, text='Quantity', font=('cambria 16 bold'),fg='#043927')
tQuantity.place(x=300,y=60)

tAmount =Label(right_side, text='Amount', font=('cambria 16 bold'),fg='#043927')
tAmount.place(x=500,y=60)

#enter stuffs 

Enter_the_id=Label(left_side,text="Enter Products id", font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
Enter_the_id.place(x=0,y=170)

Id_entry = Entry(left_side, width=25,font=('arial 16 bold'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
Id_entry.place(x=240,y=170)
Id_entry.focus()


search_button=Button(left_side,text="Search",width=18,height=2,bg='green',fg='white',command=ajax)
search_button.place(x=350,y=220)

# create the quantity and discount label

quantity_l=Label(left_side, text="Enter Quantity",font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
quantity_l.place(x=0,y=370)

quantity_e=Entry(left_side, width=25, font=('arial 18 bold'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
quantity_e.place(x=190,y=370)
quantity_e.focus()

#discount

discount_l=Label(left_side, text="Enter Discount",font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
discount_l.place(x=0,y=410)

discount_e=Entry(left_side, width=25, font=('arial 18 bold'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
discount_e.place(x=190,y=410)
discount_e.insert(END, 0)

# add to cart button.

add_button=Button(left_side,text="Add to Cart",width=18,height=2,bg='green',fg='white', command=add_to_cart)
add_button.place(x=350,y=450)

 #generate bill and change
change_l=Label(left_side, text="Given Amount",font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
change_l.place(x=0,y=550)

change_e=Entry(left_side,width=25,font=('arial 18 bold'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
change_e.place(x=190,y=550)



#button change
change_button=Button(left_side,text="Calculate Change",width=18,height=2,bg='green',fg='white',command= customer_change)
change_button.place(x=350,y=590)

#generate bill button
bill_button=Button(left_side,text="Generate Bill",width=95,height=2,bg='red',command=generate_bill)
bill_button.place(x=0,y=640)


root.mainloop()
