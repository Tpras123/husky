import random
import time
local_date=time.strftime("%d/%m/%Y", time.localtime(time.time()))
local_clock=time.strftime("%r",time.localtime(time.time()))
pres_month_year=time.strftime("%m/%Y",time.localtime(time.time()))
datetime=time.strftime("%d/%m/%Y %H:%M:%S",time.localtime(time.time()))
ticket_no=random.randint(1,200)
option='y'
tot_ad=0
tot_ch=0
tot_con=0
tot_pur=0
category=[]
unit_cost=[]
tot_qty=[]
tot_cost=[]
print('#'*100)
print(local_clock+"\t\t\t\t\t\t"+"Welcome To ticket booking app"+"\t\t\t\t\t\t"+' '+local_date)
print("#"*100)

print("\n")


def price_show():
    print('')
    print("price details:")
    print(' ')
    print("Ticket category\t\t\t\tcost")
    print("-"*35)
    print("Adult\t\t\t\t\t\t100$")
    print("children\t\t\t\t\t20$")
    print("concession\t\t\t\t\t70$")
    print("-"*35)
def calculate():
    print("select category:\n")
    print("1)Adult")
    print("2)children")
    print("3)concession")

    y=int(input("enter the no of category tickets from listed above:"))
    if y>3 or y==0:
        print("invalid type")
    else:
        for i in range(y):
            choose_category=input("choose category adult or children concession:")
            if choose_category=="Adult":
                ad=int(input("How many adult tickets do you want to purchase?"))
                print(' ')
                tot_ad =ad*100
                category.append(choose_category)
                unit_cost.append(100)
                tot_qty.append(ad)
                tot_cost.append(tot_ad)
            elif choose_category=="children":
                ch = int(input("how many child tickets do you want to purchase?"))
                print(' ')
                tot_ch = ch * 20
                category.append(choose_category)
                unit_cost.append(20)
                tot_qty.append(ch)
                tot_cost.append(tot_ch)
            elif choose_category=="concession":
                con = int(input("how many concession tickets do you want to purchase?"))
                print(' ')
                tot_con = con * 70
                category.append(choose_category)
                unit_cost.append(70)
                tot_qty.append(con)
                tot_cost.append(tot_con)
            else:
               print('')
               print("enter valid category")
               print(' ')

def card_details():
    print('')
    print("Bill details:")
    print("Category\t\tunitcost\t\tqty\t\ttotalcost\t\t")
    print("-"*50)
    s=0
    for i in range(len(category)):
        print(category[i],"\t\t",unit_cost[i],"\t\t",tot_qty[i],"\t\t",tot_cost[i])
        s=s+int(tot_cost[i])
    print("-"*50)
    print("subtotal: "+str(s))
    print('')
    tax=s*0.15
    print("Tax amount: "+str(tax))
    print('')
    tot=tax+s
    print("total cost of all tickets with gst(15%): "+str(tot))

def ticket_recipt():
    print("*"*80)
    print("Ticket no:",ticket_no,"\t\t\t\t\t","Date:",datetime)
    print("*" * 80)
    print("\n")
    print("-"*80)
    print("category","\t\t\t","unitcost","\t\t\t","qty","\t\t\t","total cost")
    print("-"*80)
    s = 0
    for i in range(len(category)):
        print(category[i], "\t\t\t", unit_cost[i], "\t\t\t", tot_qty[i], "\t\t\t", tot_cost[i])
        s = s + int(tot_cost[i])
    print("_"*80)
    print("subtotal: " + str(s))
    print('')
    tax = s * 0.15
    print("Tax amount: " + str(tax))
    print('')
    tot = tax + s
    print("total cost of all tickets with gst(15%):  " + str(tot))
def data_store_file(category,tot_qty,unit_cost,tot_cost):
    with open('transaction.txt','w') as f:
        f.write("*****************************\n")
        f.write("Ticket No: %d\n"%ticket_no)
        f.write(datetime)
        f.write("\n")
        f.write("******************************\n")
        s=0
        for i in range(len(category)):
            f.write("category:")
            f.write("%s\n"%category[i])
            f.write("Qty:")
            f.write("%s\n"%tot_qty[i])
            f.write("unit cost:")
            f.write("%s\n"%unit_cost[i])
            f.write("total cost:")
            f.write("%s\n"%tot_cost[i])
            f.write("\n")
        f.write("*"*50)
        s=0
        for i in range(len(tot_cost)):
            s=s+tot_cost[i]
        f.write("Total cost(in $) %.f\n"%s)
        tax=s*0.15
        tot=tax+s
        f.write("Total cost with tax(in $) %.f\n"%tot)
        f.close()

def purchase_details():

    show=input("Do you want  know the price of tickets y or n?")
    if show=='y':
        price_show()
    elif show=='n':
        print("purchase tickets")
        print(" ")
    else:
       print("sorry ur ans is invalid")
    calculate()
    print(' ')
    card_details()
    print('')
    print("enter credit card details for payment:")
    print('')
    print("credit card details:")
    print("-"*30)
    card_no=input("enter card no: ")
    if len(card_no)<14 or len(card_no)>14:
        print("invalid card no")
    print(" ")
    ex_data=input("enter expiry data of your card:")
    if ex_data <= pres_month_year:
        print("invalid expiry date")
        print(' ')
    print("Thanks you for your information,we will process your payment..")
    print(' ')
    print("you have successfully purchased tickets")
    print(' ')
    ticket_recipt()
    data_store_file(category, tot_qty, unit_cost, tot_cost)

if option=='y':

    print("select options:")
    print("1.show price details")
    print("2.purchase tickets")
    print("3.exit")
    print("\n")
    choice=input("choose option 1 or 2 or 3 to proceed further:")
    print(' ')
    if choice == '1':
        price_show()
        buy_ticket=input("do you want to purchase tickets y/n?")
        print(' ')
        if buy_ticket=='y':
            purchase_details()
    elif choice=='2':
        purchase_details()
    elif choice=='3':
        print("thank you for visiting!!!")

    else:
        print("choose valid option")

      # See PyCharm help at https://www.jetbrains.com/help/pycharm/
