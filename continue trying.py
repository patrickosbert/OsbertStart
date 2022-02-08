import tkinter
from tkinter import *
import os
import tkinter.messagebox
import sqlite3
from PIL import ImageTk,Image
import datetime
import math
import random


date=datetime.datetime.now().date()
#connect to the database
conn=sqlite3.connect(r"C:\Users\DENNIS\Desktop\another store system\store system\Database\store.db")
c=conn.cursor()


file = 'tempfile.temp'

def Signup(): # the user creates a username and a password
    
    global nameEntry
    global pwordEntry
    global homes

    homes = Tk()
    homes.title("Signup")
    homes.geometry("500x500")
    homes.maxsize(500,500)
    homes.configure(background='#1DC0A8')

    instruction =Label (homes,text='Create an account\n',font=('Arial Bold',10),fg='white',bg='#1DC0A8')
    instruction.grid(row=0,column=0,sticky=W,padx=5,pady=5)

    name_label = Label(homes, text='New Username')
    pword_label = Label(homes, text='New Password')
    name_label.grid(row = 1, column=0,sticky=W,padx=5,pady=5)
    pword_label.grid(row=2,column=0,sticky=W,padx=5,pady=5)

    nameEntry=Entry(homes)
    pwordEntry=Entry(homes, show='*')
    nameEntry.grid(row=1,column=1)
    pwordEntry.grid(row=2, column=1)

    signupButton = Button(homes, text='Signup',bg='red',fg='black',command=CreateUser)
    signupButton.grid(columnspan=2,sticky=E,padx=5,pady=5)

    loginnButton = Button(homes, text='Login',bg='yellow',fg='black',command=CreateUser)
    loginnButton.grid(row=3,column=0,sticky=W,padx=5,pady=5)
    homes.mainloop()

def CreateUser():
    f=open(file, 'w')
    f.write(nameEntry.get())
    f.write('\n')
    f.write(pwordEntry.get())
    f.close()
    homes.destroy()
    Login() #this redirects to the login page..


def Login():

    global nameEntryLogin
    global pwordEntryLogin
    global homeL

    homeL=Tk()
    homeL.title('Login')
    homeL.geometry("500x500")
    homeL.maxsize(500,500)
    homeL.configure(background='#447867')

    instruction = Label(homeL, text='Please Login to access the dashboard\n', font=("Arial Bold",10),fg='white',bg='#447867')
    instruction.grid(sticky=E)

    nameLabel= Label(homeL, text='Username: ')
    pwordLabel = Label(homeL,text='Password: ')
    nameLabel.grid(row=1, sticky=W, padx=5,pady=5)
    pwordLabel.grid(row=2,sticky=W,padx=5,pady=5)


    nameEntryLogin = Entry(homeL)
    pwordEntryLogin =Entry(homeL,show='*')
    nameEntryLogin.grid(row=1,column=1,padx=5,pady=5)
    pwordEntryLogin.grid(row=2, column = 1, padx=5,pady=5)

    loginButton = Button(homeL, text='Login', bg='#153060',fg='white',command=CheckLogin) #Check Login method
    loginButton.grid(row=3,column=1,sticky=E,padx=5,pady=5)

    removeUser = Button(homeL, text='Sign Up',fg='black',bg='red',command=DelUser)
    removeUser.grid(row=3, sticky=W, padx=5,pady=5)

    homeL.mainloop()


def CheckLogin():
    f=open(file)
    data = f.readlines()
    print(data)

    uname =data[0].rstrip()
    pword =data[1].rstrip()
    
    if nameEntryLogin.get() ==uname and pwordEntryLogin.get() ==pword:
        homeL.destroy()
        home()
    else:
        tkinter.messagebox.showerror('Logininfo..','Invalid Login \n Check Username and password') # An error message if the password or username is wrong
        
def DelUser():
    os.remove(file)
    homeL.destroy()
    Signup()



def home():
    global home
    home=Tk()
    home.geometry("1500x650+0+0")
    home.maxsize(1400,700)
    home.wm_minsize(1300,650)
    home.title("National Irrigation Board")
    home.iconbitmap(r'tttt.ico')

    menubar=Menu(home, bg="red")
    filemenu =Menu(menubar, tearoff=0,activeborderwidth=7)
    filemenu.add_command(label="Open Inventory",activebackground="green", command = second_win)
    filemenu.add_command(label="Make a Transaction",activebackground="blue", command = first_win)
    menubar.add_cascade(label="file",menu=filemenu)
    home.config(menu=menubar)

    
    #========================= soil composition functions ============================
    def add_to_comp ():
        calcium = calcium_e.get()
        nitrogen = nitrogen_e.get()
        zinc = Zinc_e.get()
        iron = iron_e.get()
        ph=ph_e.get()
        region=region_var.get()
        seasons=season_var.get()
        year=year_entry.get()

        totalcomp=float(calcium) + float(nitrogen) + float(zinc) + float(iron)

        if calcium == '' or nitrogen == '' or zinc == '' or iron == '':
            tkinter.messagebox.showinfo("Error", "The required entries are mandatory")
        

        else:
            c.execute("INSERT INTO composition (calcium, nitrogen, zinc, iron, ph, totalcomp,region,seasons,year) VALUES(?,?,?,?,?,?,?,?,?)",(calcium, nitrogen, zinc, iron, ph, totalcomp,region,seasons,year))
            conn.commit()

            tkinter.messagebox.showinfo("success", " successfully added into the soil composition database")


    def Totalcompositionn():
        calcium = calcium_e.get()
        nitrogen = nitrogen_e.get()
        zinc = Zinc_e.get()
        iron = iron_e.get()

        final_p = float(calcium) + float(nitrogen) + float(zinc) + float(iron)
        totalComposition_e.insert(END,final_p)

    def Clear_fertility():
        calcium_e.delete (0,END)
        nitrogen_e.delete (0,END)
        Zinc_e.delete (0,END)
        iron_e.delete (0,END)
        ph_e.delete (0,END)
        totalComposition_e.delete(0,END)
        year_entry.delete(0,END)


    def Suggestcomposition():
        # condition requirements to nutrients ppliction. 
        # if the totl composotion  is less thn 50%, the frm hs deficieny n shoul be pplied ure(N), mmonium nitrte (NaCl), 
        # a 2 times chemicl ppliction rich in noiu n clcium.
        # if the oil i t optiml, the farme at all time houl conier pplyig right mout of fertiizer n chemicl to maintain the fertility. 
        # if the pH level low conier dding more sline during topdressing.
        #high composition will rsult to high input rtion, 

        calcium = calcium_e.get()
        nitrogen = nitrogen_e.get()
        zinc = Zinc_e.get()
        iron = iron_e.get()
        season_var.get()
        region_var.get()
        year_entry.get()

        final_p = float(calcium) + float(nitrogen) + float(zinc) + float(iron)
        

        inserted = float(final_p)
        if 0 < inserted <= 50:
            tBox.delete(1.0, END)
            tBox.insert(END, "ON" + " " + str(season_var.get()) + " " + str(region_var.get()) + " " + "REGION, YEAR" + " " + str(year_entry.get()) + " " + "The Farm has a fertilty level of:"  + str(inserted) + "\n"
            "Consider pishori 270 and 360,BW 196 seed variety\n"
            "Apply 25kg of zinc sulplhate - b4 transplating \n"
            "NPK or Muriate of Potash (0-5 days) after transplanting \n"
            "YaraMila CEREAL fertiliser  21 - 25 days, high in Ni, Ca, Iron\n"
            "Final Top dressing  45-50 dys, N, Sulphur, MOP \n"
            "yelowish leaves - 1st spray(urea, calcium)\n"
            "Second Spray -  use appropriate insectside\n"
            "pH below optium - apply Hydrated lime \n"
            "pH above optium - apply- aluminum sulfate, iron sulfate \n")
            tkinter.messagebox.showinfo("working on range below 50. ")

        elif 50 < inserted <= 75:
            tBox.delete(1.0, END)
            tBox.insert(END, "ON" + " " + str(season_var.get()) + " " + str(region_var.get()) + " " + "REGION, YEAR" + " " + str(year_entry.get()) + " " + "The Farm has a fertilty level of:"  + str(inserted) + "\n"
            "Favourable for all Seed variety, e.g (Basmati 370, Basmat 217,\n BW 196, BG-90-2, BR 51-74-6 and IR 2793-80-1)\n"
            "Best for Pishori seed variety\n"
            "Soil PH of 4.5 to 7.0\n"
            "NPK or DAP, or TSP or Muriate of Potash (MOP) (0-5 days) after transplanting \n"
            "21 - 25 days after transplanting apply Ammonium Sulphate(AS) or (CAN),or Urea\n"
            "RECOMMENDED: Use urea fertilizer\n "
            "Final Top dressing (panicle initiation)  45-50 dys, apply combination of sulphur fertilizer + Urea\n"  
            "Chemical application -  Use recommended insectside\n" 
            "pH below optium - apply Hydrated lime \n" 
            "pH above optium - apply- aluminum sulfate, iron sulfate \n")
            tkinter.messagebox.showinfo("working great at a range above 50 and below 75")

        elif 75 < inserted <= 100:
            tBox.delete(1.0, END)
            tBox.insert(END, "ON" + " " + str(season_var.get()) + " " + str(region_var.get()) + " " + "REGION, YEAR" + " " + str(year_entry.get()) + " " + "The Farm has a fertilty level of:"  + str(inserted) + "\n"
            "Favourable for all variety, e.g (Basmati 370, Basmat 217, BW 196, BG-90-2, BR 51-74-6 and IR 2793-80-1)\n"
            "Soil PH of 4.5 to 7.0\n"
            "NPK or DAP (0-5 days) after transplanting \n"
            "21 - 25 days after transplanting apply Ammonium Sulphate(AS) or (CAN),or Urea\n"
            "Final Top dressing (panicle initiation)  45-50 dys, apply combination of thiosulphate + Urea\n"  
            "Chemical application -  Use recommended insectside\n" 
            "pH below optium - apply Hydrated lime \n" 
            "pH above optium - apply- aluminum sulfate, iron sulfate \n")

            tkinter.messagebox.showinfo("working great at a range above 75")

        elif inserted > 100:
            tkinter.messagebox.showinfo("please counter check the inputs. operation out of range")
        #drop down menu definition.
    def change(*args):
            return

    def season(*args):
            return
    

    analyst_side=Frame(home, width = 1500, height=650)
    analyst_side.pack()

    #================nlyst title requirement ===========
    analyst_l=Label(analyst_side, text=" Soil Fertility' Composition",font=('Cambria 24 bold'),bg='lightblue',fg='green')
    analyst_l.place(x=0,y=10)

    #=========analyst button requirements =============
    analyst_btn_add=Button(analyst_side, text="Calculate Total",width=15,height=2,bg='red',fg='white',command=Totalcompositionn)
    analyst_btn_add.place(x=30,y=400)

    analyst_btn_update=Button(analyst_side, text="Add Composition",width=15,height=2,bg='green',fg='white',command=add_to_comp)
    analyst_btn_update.place(x=120,y=400)

    analyst_btn_total=Button(analyst_side, text="Clear All",width=15,height=2,bg='red',fg='white',command=Clear_fertility)
    analyst_btn_total.place(x=240,y=400)

    analyst_btn_suggest=Button(analyst_side, text="Suggest",width=15,height=2,bg='green',fg='white', command=Suggestcomposition)
    analyst_btn_suggest.place(x=360,y=400)

    #===============labels for the anlyst side ===============

    calcium_l=Label(analyst_side, text='Calcium Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    calcium_l.place(x=0, y=110)

    nitrogen_l=Label(analyst_side, text='Nitrogen Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    nitrogen_l.place(x=0, y=160)

    zinc_l=Label(analyst_side, text='Zinc Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    zinc_l.place(x=0, y=210)

    iron_l=Label(analyst_side, text='Iron Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    iron_l.place(x=0, y=260)

    ph_l=Label(analyst_side, text='pH Conc. Level', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    ph_l.place(x=0, y=310)

    totalComposition_l=Label(analyst_side, text='Total Composition', width='16',  font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    totalComposition_l.place(x=0, y=360)


    #list of strings
    #my list is called options comprising of 5 regions with an index range as fro 0 to 4
    OPTIONS=[
        "Thiba",
        "Karaba",
        "Wamumu",
        "Nderwa",
        "T3-T9",
        "W3-W5"
    ]

    region_var = StringVar(analyst_side)
    region_var.set(OPTIONS[0])
    region_var.trace("w", change)


    regionLabel= Label(analyst_side,text='Regions', width='8', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    regionLabel.place(x=270,y=110)

    dropDownMenu = OptionMenu(analyst_side,region_var,OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5])
    dropDownMenu.configure(width=5, font=('cambria 10'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0 )
    dropDownMenu.place(x=370,y=110)


    # year label.

    year_label= Label(analyst_side,text='Year', width='8', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    year_label.place(x=270,y=160)
    year_entry = Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    year_entry.place(x=370,y=160)

    #list of strings
    #my list is called options comprising of 5 regions with an index range as fro 0 to 4
    OPTIONS=[
        "season 1",
        "season 2",
        "an annual basis",

    ]

    season_var = StringVar(analyst_side)
    season_var.set(OPTIONS[0])
    season_var.trace("w", season)

    season_label= Label(analyst_side,text='Season', width='8', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    season_label.place(x=270,y=210)

    drop_DownMenu = OptionMenu(analyst_side,season_var,OPTIONS[0],OPTIONS[1],OPTIONS[2])
    drop_DownMenu.configure(width=5, font=('cambria 10'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    drop_DownMenu.place(x=370,y=210)


    #=====================lbles for the scle side side soil composition requirements. 

    Composition_scle=Label(analyst_side, text='Soil Composition Scale',  font=('cambria 14 bold'),bg='lightblue',fg='grey')
    Composition_scle.place(x=500, y=110)

    lowComposition_l=Label(analyst_side, text='Low :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    lowComposition_l.place(x=500, y=135)

    lowComposition_leb=Label(analyst_side, text='0-49%',  font=('cambria 12 bold'),bg='lightblue' ,fg='#043927')
    lowComposition_leb.place(x=550, y=135)

    MediumComposition_l=Label(analyst_side, text='Optimum :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    MediumComposition_l.place(x=500, y=160)

    MediumComposition_leb=Label(analyst_side, text='50-74%',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    MediumComposition_leb.place(x=580, y=160)

    HighComposition_l=Label(analyst_side, text='High :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    HighComposition_l.place(x=500, y=185)

    HighComposition_leb=Label(analyst_side, text='75-100%',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    HighComposition_leb.place(x=560, y=185)

    #=============lbles for pH specifictions ==========================

    PHLEVEL_CONC_l=Label(analyst_side, text='pH level Conc.',  font=('cambria 14 bold'),bg='lightblue',fg='grey')
    PHLEVEL_CONC_l.place(x=500, y=260)

    lowPH_l=Label(analyst_side, text='Low :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    lowPH_l.place(x=500, y=290)

    lowPH_l_leb=Label(analyst_side, text='0-4',  font=('cambria 12 bold'),bg='lightblue' ,fg='#043927')
    lowPH_l_leb.place(x=550, y=290)

    MediumPH_l=Label(analyst_side, text='Neutral :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    MediumPH_l.place(x=500, y=310)

    MediumPH_leb=Label(analyst_side, text='4.5-7',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    MediumPH_leb.place(x=550, y=310)

    HighPH_l=Label(analyst_side, text='High :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    HighPH_l.place(x=500, y=330)

    HighPH_leb=Label(analyst_side, text='7.5-14',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
    HighPH_leb.place(x=560, y=330)


    #======entries for the nalyst side=============

    calcium_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    calcium_e.place(x=180,y=110)

    nitrogen_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    nitrogen_e.place(x=180,y=160)

    Zinc_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    Zinc_e.place(x=180,y=210)

    iron_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    iron_e.place(x=180,y=260)

    ph_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    ph_e.place(x=180,y=310)

    totalComposition_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    totalComposition_e.place(x=180,y=360)

    #====text for the logs=====================
    tBox=Text(analyst_side,width=70,height=27,highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    tBox.place(x=720,y=90)

    
    home.mainloop()


def first_win():
    date=datetime.datetime.now().date()

    #============= temporarly lists like sessions  ========
    products_list = []
    product_price= []
    product_quantity = []
    product_id = []

    #labels list

    labels_list = [ ]

    def product_select(*arg):
        return

    #configure
    def ajax():
        get_id = Id_entry.get()
        get_pro = Id_entry.get()
        query="SELECT * FROM inventory WHERE id=? or name=?"
        result = c.execute(query,(get_id,get_pro,))
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

    def chelsea():
        get_product_name = product_var.get()
        quering="SELECT * FROM inventory WHERE name=?"
        resulting = c.execute(quering,(get_product_name,))
        for r in resulting:
            get_name=r[1]
            get_price=r[4]


        productname_l = Label(left_side, font=('cambria 16 bold'),fg='red')
        productname_l.configure(text="Product's Name: " + str(get_name))
        productname_l.place(x=0,y=270)
        
        productprice_l = Label(left_side, font=('cambria 16 bold'),fg='red')
        productprice_l.configure(text="Price: Ksh. " + str(get_price))
        productprice_l.place(x=0,y=300)

    def add_to_cart():
        get_id = Id_entry.get() or product_var.get()
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
        company="\t\t\t\tNational Irrigation Board\n "
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

        tkinter.messagebox.showinfo("Success", "Transaction Completed succesfully")


    home =Toplevel()
    home.title("National Irrigation Board ")
    home.iconbitmap(r'tttt.ico')



    left_side=Frame(home, width = 700, height=768,bg='#d6d7d2')
    left_side.pack(side=LEFT)

    right_side=Frame(home, width = 666, height=768,bg='#4F7942')
    right_side.pack(side=RIGHT)

    #===============logo requirements =================

    label_2=Label(home, text=" National Irrigation' \n Board",font=('forte 24 bold'),bg='#d6d7d2',fg='green')
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


    #list of strings
    #my list is called options comprising of 5 regions with an index range as fro 0 to 4
    OPTIONS=[
        "Type 1 (Pishori seed)",
        "Type 2 (B. rice seed)",
        "fertilizer (NPK)",
        "Fertilizer ( Muriate of Potash",
        "Fertilizer ( DAP)",
        "Chemical (first chemical)",
        "chemical ( second chemical)",
        "Equipment (sickle)",
        "Equipment (knaps sprayer)"
    ]

    product_var = StringVar(left_side)
    product_var.set(OPTIONS[0])
    product_var.trace("w", product_select)


    regionLabel_p= Label(left_side,text='products', width='8', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
    regionLabel_p.place(x=0,y=200)

    dropDownMenu_p = OptionMenu(left_side,product_var,OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8])
    dropDownMenu_p.configure(width=5, font=('cambria 10'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0 )
    dropDownMenu_p.place(x=240,y=200)


    search_button=Button(left_side,text="Search",width=10,height=2,bg='green',fg='white',command=ajax)
    search_button.place(x=350,y=220)

    search_button_2=Button(left_side,text="Sty",width=18,height=2,bg='green',fg='white',command=chelsea)
    search_button_2.place(x=380,y=250)

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

def second_win():
    #============================ inventory fucntions =============================
    def inventory_add_database():
        name=name_e.get()
        stock=stock_e.get()
        cp=cp_e.get()
        sp=sp_e.get()
        vendor=vendor_e.get()
        vendor_phone=vendor_phone_e.get()

        totalcp=float(cp) * float(stock)
        totalsp=float(sp) * float(stock)
        assumed_profit=float(totalsp-totalcp)


        if name == '' or stock == '' or cp == '' or sp == '':
            tkinter.messagebox.showinfo("Error", "The required entries are mandatory")
        

        else:
            c.execute("INSERT INTO inventory(name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phone) VALUES(?,?,?,?,?,?,?,?,?)",(name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phone))
            conn.commit()

            tkinter.messagebox.showinfo("success", " successfully added into the database")
            



    def search_values():
        sql="SELECT * FROM inventory WHERE id=? or name=?"
        result=c.execute(sql, (id_leb.get(), name_e.get(), ))
        for r in result:
            n1 =r[1] #name
            n2 =r[2] #stock
            n3 =r[3] #cp
            n4 =r[4] #sp
            n5 =r[5] #totalcp
            n6 =r[6] #totalsp
            n7 =r[7] #assumed_profit
            n8 =r[8] #vendor
            n9 =r[9] #vendor_phone

        conn.commit()

        #insert into the entries to update
        name_e.delete(0,END)
        name_e.insert(0,str(n1))

        stock_e.delete(0,END)
        stock_e.insert(0,str(n2))

        cp_e.delete(0,END)
        cp_e.insert(0,str(n3))

        sp_e.delete(0,END)
        sp_e.insert(0,str(n4))

        totalcp_e.delete(0,END)
        totalcp_e.insert(0,str(n5))

        totalsp_e.delete(0,END)
        totalsp_e.insert(0,str(n6))

        vendor_e.delete(0,END)
        vendor_e.insert(0,str(n8))

        vendor_phone_e.delete(0,END)
        vendor_phone_e.insert(0,str(n9))

    def update_database():
        u1=name_e.get()
        u2=stock_e.get()
        u3=cp_e.get()
        u4=sp_e.get()
        u5=totalcp_e.get()
        u6=totalsp_e.get()
        u7=vendor_e.get()
        u8=vendor_phone_e.get()

        query="UPDATE inventory SET name =?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,vendor=?,vendor_phone=? WHERE id=?"
        c.execute(query,(u1,u2,u3,u4,u5,u6,u7,u8,id_leb.get(),))
        conn.commit()

        tkinter.messagebox.showinfo("Success", " The database has successfully been updated")


    def Clear_ll():
        name_e.delete(0,END)
        stock_e.delete(0,END)
        cp_e.delete(0,END)
        sp_e.delete(0,END)
        vendor_e.delete(0,END)
        vendor_phone_e.delete(0,END)

    #size composition 
    
    global home
    home=Tk()
    home.geometry("1500x650+0+0")
    home.maxsize(700,700)
    home.wm_minsize(700,650)
    home.title("National Irrigation Board")
    home.iconbitmap(r'tttt.ico')

    inventory_side=Frame(home, width = 900, height=650)
    inventory_side.pack()

    #=======label and entry for id =============

    id_le=Label(inventory_side, text='Enter ID', font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    id_le.place(x=0, y=50)

    id_leb=Entry(inventory_side, width=10, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    id_leb.place(x=200,y=50)

    btn_search = Button(inventory_side, text="search", width=15,height=2,bg='red',command=search_values)
    btn_search.place(x=370,y=50)

    #==============labels for homes inventory side ===========================
    name_l=Label(inventory_side, text='Enter Product Name',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    name_l.place(x=0, y=100)

    stock_l=Label(inventory_side, text='Enter Stock (KG.)',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    stock_l.place(x=0, y=150)

    cp_l=Label(inventory_side, text='Enter Cost Price (Ksh.)',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    cp_l.place(x=0, y=200)

    sp_l=Label(inventory_side, text='Enter Selling Price',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    sp_l.place(x=0, y=250)

    totalcp_l=Label(inventory_side, text='Total Cost Price',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    totalcp_l.place(x=0, y=300)

    totalsp_l=Label(inventory_side, text='Total Selling Price',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    totalsp_l.place(x=0, y=350)

    vendor_l=Label(inventory_side, text='Enter Vendor Name ',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    vendor_l.place(x=0, y=400)

    vendor_phone_l=Label(inventory_side, text='Enter Vendor Phone No.', font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
    vendor_phone_l.place(x=0, y=450)


    #================entries for the labels inventory=====================
    name_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    name_e.place(x=200,y=100)

    stock_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    stock_e.place(x=200,y=150)

    cp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    cp_e.place(x=200,y=200)

    sp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    sp_e.place(x=200,y=250)

    totalcp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    totalcp_e.place(x=200,y=300)
    totalcp_e.delete(END, 0)

    totalsp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    totalsp_e.place(x=200,y=350)

    vendor_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    vendor_e.place(x=200,y=400)

    vendor_phone_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    vendor_phone_e.place(x=200,y=450)

    #=======button to add to the database==================
    btn_add=Button(inventory_side, text="Add to Database",width=20,height=2,bg='green',fg='white',command=inventory_add_database)
    btn_add.place(x=70,y=520)

    btn_update=Button(inventory_side, text="Update Database",width=20,height=2,bg='green',fg='white',command=update_database)
    btn_update.place(x=220,y=520)

    btn_clear=Button(inventory_side, text="Clear All",width=20,height=2,bg='red',fg='white',command=Clear_ll)
    btn_clear.place(x=370,y=520)


    home.mainloop()

Signup()



