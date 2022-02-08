from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import ImageTk,Image
import math



conn=sqlite3.connect(r"D:\Klaus\OTHER PROJECTS\store system\Database\store.db")
c=conn.cursor()

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
        tkinter.messagebox.showinfo("please counter check the inputs. opertion out of rnge")
#drop down menu definition.
def change(*args):
    return

def season(*args):
    return

    
root = Tk()

root.geometry("1366x768+0+0")
root.wm_minsize(1000,600)
root.title("Mutithi Farmers Association")
root.iconbitmap(r'tttt.ico')
root.configure(background='#d6d7d2')




inventory_side=Frame(root, width = 600, height=768)
inventory_side.pack(side=LEFT)

analyst_side=Frame(root, width = 766, height=768,bg='lightblue')
analyst_side.pack(side=RIGHT)

#============================farm logo=================================

farm_logo=Image.open(r"C:\Users\DENNIS\Desktop\store system\tttt.png")
image2=farm_logo.resize((170,150),Image.ANTIALIAS)
farm_logo2=ImageTk.PhotoImage(image2)

label_1=Label(inventory_side, image=farm_logo2)
label_1.place(x=20,y=5)
label_2=Label(root, text=" National Irrigation \n Board \n Management System",font=('forte 22 bold'),bg='#d6d7d2',fg='green')
label_2.place(x=220,y=10)



#=======label and entry for id =============

id_le=Label(inventory_side, text='Enter ID', font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
id_le.place(x=0, y=170)

id_leb=Entry(inventory_side, width=10, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
id_leb.place(x=200,y=170)

btn_search = Button(inventory_side, text="search", width=15,height=2,bg='red',command=search_values)
btn_search.place(x=370,y=170)

#================nlyst title requirement ===========
analyst_l=Label(analyst_side, text=" Soil Fertility' Composition",font=('Cambria 24 bold'),bg='lightblue',fg='green')
analyst_l.place(x=80,y=10)



#=========anlyst button requirements =============

analyst_btn_add=Button(analyst_side, text="Calculate Total",width=15,height=2,bg='red',fg='white',command=Totalcompositionn)
analyst_btn_add.place(x=0,y=370)

analyst_btn_update=Button(analyst_side, text="Add Composition",width=15,height=2,bg='green',fg='white',command=add_to_comp)
analyst_btn_update.place(x=120,y=370)

analyst_btn_clear=Button(analyst_side, text="Update",width=15,height=2,bg='green',fg='white')
analyst_btn_clear.place(x=240,y=370)

analyst_btn_total=Button(analyst_side, text="Clear All",width=15,height=2,bg='red',fg='white',command=Clear_fertility)
analyst_btn_total.place(x=360,y=370)

analyst_btn_suggest=Button(analyst_side, text="Suggest",width=15,height=2,bg='green',fg='white', command=Suggestcomposition)
analyst_btn_suggest.place(x=480,y=370)

#==============labels for roots inventory side =======================

name_l=Label(inventory_side, text='Enter Product Name',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
name_l.place(x=0, y=220)

stock_l=Label(inventory_side, text='Enter Stock (KG.)',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
stock_l.place(x=0, y=270)

cp_l=Label(inventory_side, text='Enter Cost Price (Ksh.)',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
cp_l.place(x=0, y=320)

sp_l=Label(inventory_side, text='Enter Selling Price',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
sp_l.place(x=0, y=370)

totalcp_l=Label(inventory_side, text='Total Cost Price',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
totalcp_l.place(x=0, y=420)

totalsp_l=Label(inventory_side, text='Total Selling Price',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
totalsp_l.place(x=0, y=470)

vendor_l=Label(inventory_side, text='Enter Vendor Name ',  font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
vendor_l.place(x=0, y=520)

vendor_phone_l=Label(inventory_side, text='Enter Vendor Phone No.', font=('cambria 16 bold'),bg='#e7eae5',fg='#043927')
vendor_phone_l.place(x=0, y=570)

#===============labels for the anlyst side ===============
calcium_l=Label(analyst_side, text='Calcium Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
calcium_l.place(x=0, y=80)

nitrogen_l=Label(analyst_side, text='Nitrogen Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
nitrogen_l.place(x=0, y=130)

zinc_l=Label(analyst_side, text='Zinc Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
zinc_l.place(x=0, y=180)

iron_l=Label(analyst_side, text='Iron Conc. (%)', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
iron_l.place(x=0, y=230)

ph_l=Label(analyst_side, text='pH Conc. Level', width='16', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
ph_l.place(x=0, y=280)

totalComposition_l=Label(analyst_side, text='Total Composition', width='16',  font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
totalComposition_l.place(x=0, y=330)


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
regionLabel.place(x=270,y=80)

dropDownMenu = OptionMenu(analyst_side,region_var,OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5])
dropDownMenu.configure(width=5, font=('cambria 10'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0 )
dropDownMenu.place(x=370,y=80)


# year label.

year_label= Label(analyst_side,text='Year', width='8', font=('cambria 12 bold'),bg='#e7eae5',fg='#043927')
year_label.place(x=270,y=130)
year_entry = Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
year_entry.place(x=370,y=130)

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
season_label.place(x=270,y=180)

drop_DownMenu = OptionMenu(analyst_side,season_var,OPTIONS[0],OPTIONS[1],OPTIONS[2])
drop_DownMenu.configure(width=5, font=('cambria 10'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
drop_DownMenu.place(x=370,y=180)


#=====================lbles for the scle side side soil composition requirements. 

Composition_scle=Label(analyst_side, text='Soil Composition Scale',  font=('cambria 14 bold'),bg='lightblue',fg='grey')
Composition_scle.place(x=500, y=80)

lowComposition_l=Label(analyst_side, text='Low :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
lowComposition_l.place(x=500, y=105)

lowComposition_leb=Label(analyst_side, text='0-49%',  font=('cambria 12 bold'),bg='lightblue' ,fg='#043927')
lowComposition_leb.place(x=550, y=105)

MediumComposition_l=Label(analyst_side, text='Optimum :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
MediumComposition_l.place(x=500, y=130)

MediumComposition_leb=Label(analyst_side, text='50-74%',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
MediumComposition_leb.place(x=580, y=130)

HighComposition_l=Label(analyst_side, text='High :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
HighComposition_l.place(x=500, y=155)

HighComposition_leb=Label(analyst_side, text='75-100%',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
HighComposition_leb.place(x=560, y=155)

#=============lbles for pH specifictions ==========================

PHLEVEL_CONC_l=Label(analyst_side, text='pH level Conc.',  font=('cambria 14 bold'),bg='lightblue',fg='grey')
PHLEVEL_CONC_l.place(x=500, y=230)

lowPH_l=Label(analyst_side, text='Low :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
lowPH_l.place(x=500, y=260)

lowPH_l_leb=Label(analyst_side, text='0-4',  font=('cambria 12 bold'),bg='lightblue' ,fg='#043927')
lowPH_l_leb.place(x=550, y=260)

MediumPH_l=Label(analyst_side, text='Neutral :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
MediumPH_l.place(x=500, y=280)

MediumPH_leb=Label(analyst_side, text='4.5-7',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
MediumPH_leb.place(x=550, y=280)

HighPH_l=Label(analyst_side, text='High :',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
HighPH_l.place(x=500, y=300)

HighPH_leb=Label(analyst_side, text='7.5-14',  font=('cambria 12 bold'),bg='lightblue',fg='#043927')
HighPH_leb.place(x=560, y=300)




#================entries for the labels inventory=====================
name_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
name_e.place(x=200,y=220)

stock_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
stock_e.place(x=200,y=270)

cp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
cp_e.place(x=200,y=320)

sp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
sp_e.place(x=200,y=370)

totalcp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
totalcp_e.place(x=200,y=420)
totalcp_e.delete(END, 0)

totalsp_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
totalsp_e.place(x=200,y=470)

vendor_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
vendor_e.place(x=200,y=520)

vendor_phone_e=Entry(inventory_side, width=20, font=('cambria 16'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
vendor_phone_e.place(x=200,y=570)



#======entries for the nalyst side=============

calcium_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
calcium_e.place(x=180,y=80)

nitrogen_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
nitrogen_e.place(x=180,y=130)

Zinc_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
Zinc_e.place(x=180,y=180)

iron_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
iron_e.place(x=180,y=230)

ph_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
ph_e.place(x=180,y=280)

totalComposition_e=Entry(analyst_side, width=8, font=('cambria 12'),highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
totalComposition_e.place(x=180,y=330)

#=======button to add to the database==================
btn_add=Button(inventory_side, text="Add to Database",width=20,height=2,bg='green',fg='white',command=inventory_add_database)
btn_add.place(x=70,y=620)

btn_update=Button(inventory_side, text="Update Database",width=20,height=2,bg='green',fg='white',command=update_database)
btn_update.place(x=220,y=620)

btn_clear=Button(inventory_side, text="Clear All",width=20,height=2,bg='red',fg='white',command=Clear_ll)
btn_clear.place(x=370,y=620)

#====text for the logs=====================
tBox=Text(analyst_side,width=78,height=17,highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
tBox.place(x=10,y=420)



root.mainloop()
