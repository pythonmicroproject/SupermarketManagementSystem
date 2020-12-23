import pickle
import os
from difflib import SequenceMatcher
from datetime import datetime

productFile = "productFile.txt"  # name and path of the file containg products list
employeeFile = "employeeFile.txt" # name and path of the file containg employee list
billGeneratorFile = "billGeneratorFile.txt"
salesFile = "salesFile.txt"
storeInfoFile = "storeInfoFile.txt"

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(os.name is 'posix')
    else:
        os.system('clear')

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def listInitializer(file):
    if os.path.exists(file):  # True if file exists
        if os.stat(file).st_size == 0:  # True if file is empty
            list = []
        else:
            with open(file, "rb") as f:
                list = pickle.load(f)
    else:
        list = []
    return list

def storeInfoInitializer(file):
    if os.path.exists(file):  # True if file exists
        if os.stat(file).st_size == 0:  # True if file is empty
            storeInfo = {'name':'Store Name', 'city':'City/Town/Village', 'state':'State', 'pincode':'Pincode', 'phone':'Phone No.', 't&c1':"1.First terms and condition", 't&c2':"2.Second terms and condition"}
        else:
            with open(file, "rb") as f:
                storeInfo = pickle.load(f)
    else:
        storeInfo = {'name':'Store Name', 'city':'City/Town/Village', 'state':'State', 'pincode':'Pincode', 'phone':'Phone No.', 't&c1':"1.First terms and condition", 't&c2':"2.Second terms and condition"}
    return storeInfo

def writeFile(file, list):
    with open(file, "wb") as f:
        pickle.dump(list, f)

def billNumberGenerator():
    global billGeneratorFile
    billDictionary = {}
    now = datetime.now()
    if os.path.exists(billGeneratorFile):  # True if file exists
        if os.stat(billGeneratorFile).st_size == 0:  # True if file is empty
            billDictionary = {"counter":0, "year":now.year}
        else:
            with open(billGeneratorFile, "rb") as f:
                billDictionary = pickle.load(f)
    else:
        billDictionary = {"counter":0, "year":now.year}

    if now.year > billDictionary['year']:
        billDictionary['counter'] = 0
        billDictionary['year'] = now.year

    billDictionary['counter'] = billDictionary['counter'] + 1
    billNumber = str(billDictionary['counter'])+"/"+now.strftime("%Y")
    writeFile(billGeneratorFile, billDictionary)
    return billNumber

class employee():
    def __init__(self):
        self.name=""
        self.userName=""
        self.password=""
        self.todaysSales= 0

    def employeeMenuHeader(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        print(("DATE: "+date).ljust(20), ("USER: "+self.userName).ljust(45), ("TODAY'S SALES: "+str(self.todaysSales)).rjust(30))
        print("-"*100, end="\n\n")

    def employeeLogin(self):
        global employeeFile
        global salesFile
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        clear()
        print(" EMPLOYEE LOGIN ".center(100,"-"),end="\n\n")
        userName = input("\tEnter User Name : ").lower()
        password = input("\tEnter Password : ").lower()
        employeeList = listInitializer(employeeFile)
        flag = 0
        for employee in employeeList:
            if employee['userName'] == userName:
                flag = 1
                if employee['password'] == password:
                    self.name = employee["name"]
                    self.userName = userName
                    self.password = password
                    print(end="\n")
                    print((">>>>> Welcome "+self.name+" <<<<<").center(100))
                    salesList = listInitializer(salesFile)
                    for sales in salesList:
                        if sales['employeeUserName'] == self.userName and sales['date'] == date:
                            self.todaysSales = self.todaysSales + sales['total']
                    input()
                    return True
                else:
                    input("\tIncorrect Password, Please try again !")
                    return False
        if flag == 0:
            input("\tIncorrect Username & Password, Please try again !")
            return False

    def viewInventory(self):
        global productFile
        if os.path.exists(productFile):  # True if file exists
            if os.stat(productFile).st_size == 0:  # True if file is empty
                productList = []
            else:
                with open(productFile, "rb") as f:
                    productList = pickle.load(f)
        else:
            productList = []
        totalAmount=0
        totalItems=0
        totalQuantity=0
        clear()
        print(" INVENTORY ".center(100,"-"), end="\n")
        self.employeeMenuHeader()
        print("NAME:".ljust(50),"QUANTITY:".rjust(18), "RATE:".rjust(25))
        print("-" * 100)
        for product in productList:
            print(product['name'].ljust(50),(str(product['quantity'])).rjust(18), (str(product['price'])).rjust(25))
            totalItems = totalItems + 1
            totalQuantity = totalQuantity + product['quantity']
            totalAmount = totalAmount + (product['price']*product['quantity'])
        print("-" * 100)
        print(("ITEMS: "+str(totalItems)).ljust(30), ("QUANTITY: "+str(totalQuantity)).rjust(38), ("AMOUNT: "+str(totalAmount)).rjust(25))
        print("-" * 100)
        input("Press Enter to continue...")

    def cart(self):
        global productFile
        global salesFile
        global storeInfoFile
        if os.path.exists(productFile):  # True if file exists
            if os.stat(productFile).st_size == 0:  # True if file is empty
                productList = []
            else:
                with open(productFile, "rb") as f:
                    productList = pickle.load(f)
        else:
            productList = []
        cartList=[]
        summary=[]
        total=0
        items=0
        qty=0
        while True:
            total=0
            items=0
            qty=0
            clear()
            print(" CART ".center(100,'-'), end="\n")
            self.employeeMenuHeader()
            print("SN.".ljust(6),"ITEM:".ljust(40),"QTY:".rjust(10),"RATE:".rjust(18),"AMOUNT:".rjust(18))
            print("-" * 100)
            for sn, item in enumerate(cartList):
                print(str(sn+1).ljust(6),item['name'].ljust(40),str(item['quantity']).rjust(10),str(item['rate']).rjust(18),str(item['amount']).rjust(18))
            print(end="\n")
            print("-"*100,end= "\n")
            for item in cartList:
                total = item['amount'] + total
                qty = item['quantity'] + qty
                items=len(cartList)
            summary=["ITEMS: "+str(items), "QTY: "+str(qty), "TOTAL: "+str(total)]
            print(summary[0].ljust(30),summary[1].rjust(27), summary[2].rjust(37))
            print("-"*100)
            print("\n")
            print("\t1.Add Item")
            print("\t2.Update Item")
            print("\t3.Delete Item")
            print("\t4.Generate Bill")
            print("\t5.Cancel\n")
            print("-"*100, end="\n\n")
            choice = input("Enter choice : ")
            if choice == '1':
                suggestionList = []
                flag = 0
                name = input("\tEnter Item Name : ").title()
                if not any(item['name'] == name for item in cartList):
                    for index, product in enumerate(productList):
                        if product['name'] == name:
                            flag = 1
                            print("\tAvailable Quantity:", str(product["quantity"]))
                            quantity = int(input("\tEnter Quantity : "))
                            if quantity <= product['quantity']:
                                amount=quantity*product['price']
                                cartList.append({'name':name, 'quantity':quantity, 'rate':product['price'], 'amount': amount})
                                break
                            else:
                                input("\tInsufficient stock !")
                                break
                        elif similar(name, product["name"]) >= 0.6:
                            if not any(product["name"] == item['name'] for item in cartList):
                                suggestionList.append(index)
                                flag = 2
                    if flag==0:
                        input("\tProduct does not exist !")
                    elif flag == 2:
                        print("\tThe entered item:", name, ", does not exist !")
                        print("\tDid you mean : ")
                        for index in suggestionList:
                            print("\t---> ",productList[index]["name"], "? (y/n) : ", end="")
                            choice = input().lower()
                            if choice == "y":
                                print("\tAvailable Quantity:", str(productList[index]["quantity"]))
                                quantity = int(input("\tEnter Quantity : "))
                                if quantity <= productList[index]["quantity"]:
                                    amount=quantity*productList[index]['price']
                                    cartList.append({'name':productList[index]["name"], 'quantity':quantity, 'rate':productList[index]['price'], 'amount': amount})
                                    break
                                else:
                                    input("\tInsufficient stock !")
                                    break
                else:
                    input("\tItem already exists in cart, try Update item")

            elif choice == '2':
                suggestionList = []
                flag = 0
                name = input("\tEnter Item Name : ").title()
                for index, item in enumerate(cartList):
                    if item['name'] == name:
                        flag = 1
                        print("\tCurrent Quantity: ", str(item["quantity"]))
                        quantity=int(input("\tEnter new Quantity : "))
                        for product in productList:
                            if product['name'] == name:
                                if quantity <= product['quantity']:
                                    amount=quantity*product['price']
                                    item['quantity']=quantity
                                    item['amount']=amount
                                    break
                                else:
                                    input("\tInsufficient stock !")
                                    break
                        break
                    elif similar(name, item["name"]) >= 0.6:
                        suggestionList.append(index)
                        flag = 2
                if flag == 0:
                    input("\tItem does not exist in cart !")
                elif flag == 2:
                    print("\tThe entered item:", name, ", does not exist in the cart !")
                    print("\tDid you mean : ")
                    for index in suggestionList:
                        print("\t---> ",cartList[index]["name"], "? (y/n) : ", end="")
                        choice = input().lower()
                        if choice == "y":
                            print("\tCurrent Quantity: ", str(cartList[index]["quantity"]))
                            quantity=int(input("\tEnter new Quantity : "))
                            for product in productList:
                                if product['name'] == cartList[index]["name"]:
                                    if quantity <= product['quantity']:
                                        amount=quantity*product['price']
                                        cartList[index]['quantity']=quantity
                                        cartList[index]['amount']=amount
                                        break
                                    else:
                                        input("\tInsufficient stock !")
                                        break
                            break

            elif choice == '3':
                suggestionList = []
                flag=0
                name = input("\tEnter the Name of the item you wish to Delete : ").title()
                for index, item in enumerate(cartList):
                    if item["name"]== name:
                        flag = 1
                        print("\tName:", item["name"], ", Quantity:", str(item["quantity"]))
                        choice = input("\tDo you wish to Delete? (y/n) : ").lower()
                        if (choice == "y"):
                            del cartList[index]
                            break
                    elif similar(name, item["name"]) >= 0.6:
                        suggestionList.append(index)
                        flag = 2
                if flag==0:
                    input("\tItem does not exist in cart !")
                elif flag == 2:
                    print("\tThe entered item:", name, ", does not exist in the cart !")
                    print("\tDid you mean : ")
                    for index in suggestionList:
                        print("\t---> ",cartList[index]["name"], "? (y/n) : ", end="")
                        choice = input().lower()
                        if choice == "y":
                            print("\tName:", cartList[index]["name"], ", Quantity:", str(cartList[index]["quantity"]))
                            choice = input("\tDo you wish to Delete? (y/n) : ").lower()
                            if (choice == "y"):
                                del cartList[index]
                                break

            elif choice == '4':
                if items > 0:
                    customerName=input("\tEnter the name of the customer : ").title()
                    customerNumber=input("\tEnter the Phone no. of the customer : ")
                    choice=input("\tComplete Transaction? (y/n) : ").lower()
                    if choice == 'y':
                        clear()
                        now = datetime.now()
                        date=now.strftime("%d/%m/%Y")
                        time=now.strftime("%H:%M")
                        storeInfo = storeInfoInitializer(storeInfoFile)
                        for item in cartList:
                            for product in productList:
                                if product['name'] == item['name']:
                                    product['quantity'] = product['quantity']-item['quantity']
                        with open(productFile, "wb") as f:
                            pickle.dump(productList, f)
                        billNumber = billNumberGenerator()
                        print(" RETAIL BILL ".center(100,'-'),end= "\n\n")
                        print(storeInfo['name'].center(100))
                        print(storeInfo['city'].center(100))
                        print((storeInfo['state']+" - "+storeInfo['pincode']).center(100))
                        print(("Phone: "+storeInfo['phone']).center(100))
                        print("-" * 100)
                        print("ISSUED TO:".ljust(80),"Date: "+date)
                        print(customerName.ljust(80),"Time: "+time)
                        print(customerNumber.ljust(80),"Bill No: "+billNumber)
                        print(" "*81+"Cashier: "+self.userName)
                        print("-" * 100)
                        print("SN.".ljust(6),"ITEM:".ljust(40),"QTY:".rjust(10),"RATE:".rjust(18),"AMOUNT:".rjust(18))
                        print("-" * 100)
                        for sn, item in enumerate(cartList):
                            print(str(sn+1).ljust(6),item['name'].ljust(40),str(item['quantity']).rjust(10),str(item['rate']).rjust(18),str(item['amount']).rjust(18))
                        print(end="\n")
                        print("-"*100,end= "\n")
                        print(summary[0].ljust(30),summary[1].rjust(27), summary[2].rjust(37))
                        print("-" * 100)
                        print("\n\n")
                        print("\tTERMS & CONDITIONS:")
                        print("\t"+storeInfo['t&c1'])
                        print("\t"+storeInfo['t&c2'])
                        print("\n")
                        print(">>>> THANK YOU, VISIT AGAIN <<<<".center(100))
                        print("-" * 100)
                        salesList = listInitializer(salesFile)
                        salesList.append({
                        'date':date, 'time':time, 'customerName':customerName, 'customerNumber':customerNumber, 'employeeUserName':self.userName,
                        'billNumber':billNumber, 'cartList':cartList, 'quantity':qty, 'items':items, 'total':total
                        })
                        writeFile(salesFile,salesList)
                        self.todaysSales = self.todaysSales + total
                        cartList.clear()
                        input("Press any key to continue . . .")
                else:
                    input("\tEmpty Cart !")
            elif choice == '5':
                break
            else:
                input("Please enter a valid option !\n")
    def mySales(self):
        global salesFile
        salesList = listInitializer(salesFile)
        total=0
        clear()
        print(" MY SALES ".center(100,"-"),end="\n")
        self.employeeMenuHeader()
        print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
        print("-" * 100)
        for sales in salesList:
            if sales['employeeUserName'] == self.userName:
                print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                total = total + sales['total']
        print("-" * 100)
        print(("TOTAL: "+str(total)).rjust(97))
        print("-" * 100)
        input("Press Enter to continue...")

    def changeEmployeePassword(self):
        clear()
        print(" CHANGE PASSWORD ".center(100,"-"),end="\n")
        self.employeeMenuHeader()
        print("\tHello "+self.name+", Please enter your current Password : ", end='')
        password = input()
        global employeeFile
        employeeList = listInitializer(employeeFile)
        for employee in employeeList:
            if employee['userName'] == self.userName:
                if employee['password'] == password:
                    password = input("\tEnter new Password : ")
                    print("\n\t>>> Password Conformation :",password)
                    employee['password'] = password
                    self.password = password
                    writeFile(employeeFile, employeeList)
                    input("\tPassword changed, Press Enter to continue...")
                else:
                    input("\tIncorrect Password, Please try again !")
