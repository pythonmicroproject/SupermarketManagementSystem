import pickle
import os
from difflib import SequenceMatcher
from datetime import datetime

productFile = "productFile.txt"  # name and path of the file containg products list
employeeFile = "employeeFile.txt" # name and path of the file containg employee list
salesFile = "salesFile.txt"
storeInfoFile = "storeInfoFile.txt"

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

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(os.name is 'posix')
    else:
        os.system('clear')

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

class manager():
    def __init__(self):
        self.name = ""
        self.password = ""

    def managerMenuHeader(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        print(("DATE: "+date).ljust(85), ("MANAGER").ljust(13))
        print("-"*100, end="\n\n")

    def managerLogin(self):
        defaultPassword = "admin"
        clear()
        print(" MANAGER LOGIN ".center(100,"-"), end="\n\n")
        password = input("\tEnter Password : ").lower()
        if password == defaultPassword:
            print(end="\n")
            print(">>>>> Welcome Manager <<<<<".center(100), end="\n")
            input()
            return True
        else:
            input("\tIncorrect Password, Please try again !")
            return False

    def addEmployee(self):
        global employeeFile
        clear()
        print(" NEW EMPLOYEE ".center(100,"-"), end="\n")
        self.managerMenuHeader()
        name = input("\tEnter Employee Name : ").title()
        if len(name) == 0 or name.isspace() : #checks whether the Name is empty or only contains spaces
            input("\tInvalid Name, Please try again !")
            return
        userName = input("\tEnter User Name : ").lower()
        if len(userName) == 0 or userName.isspace() : #checks whether the userName is empty or only contains spaces
            input("\tInvalid User Name, Please try again !")
            return
        password = input("\tEnter Password : ").lower()
        if len(password) == 0 or password.isspace() : #checks whether the password is empty or only contains spaces
            input("\tInvalid Password, Please try again !")
            return
        print("\n\t>>> Password Conformation :",password,"\n")
        employeeList = listInitializer(employeeFile)
        if not any(employee['userName']==userName for employee in employeeList):
            employeeList.append({'name':name, 'userName':userName, 'password':password})
            writeFile(employeeFile, employeeList)
            input("\tEmployee Added !")
        else:
            print("\t"+userName, "is already in use, Please try a different one !",end="")
            input()

    def deleteEmployee(self):
        global employeeFile
        clear()
        print(" DELETE EMPLOYEE ".center(100,"-"), end="\n")
        self.managerMenuHeader()
        userName = input("\tEnter the User Name of the employee you wish to delete : ").lower()
        employeeList = listInitializer(employeeFile)
        if any(employee['userName'] == userName for employee in employeeList):
            for index, employee in enumerate(employeeList):
                if employee['userName'] == userName:
                    print("\tName:", employee['name'], ", User Name:", employee['userName'], ", Password:",employee['password'])
                    choice = input("\tDo you wish to Delete? (y/n) : ").lower()
                    if (choice == "y"):
                        del employeeList[index]
                        writeFile(employeeFile, employeeList)
                        input("\tEmployee Deleted")
                        break
                    else:
                        input("\tCancelled")
        else:
            input("\tNo such employee found !")

    def viewEmployee(self):
        global employeeFile
        employeeList = listInitializer(employeeFile)
        employeeCount=0
        clear()
        print(" EMPLOYEE LIST ".center(100,"-"), end="\n")
        self.managerMenuHeader()
        print("NAME:".ljust(40), "USER NAME:".ljust(35), "PASSWORD:".ljust(18))
        print("-" * 100)
        for employee in employeeList:
            print(employee['name'].ljust(40), employee['userName'].ljust(35), employee['password'].ljust(18))
            employeeCount = employeeCount + 1
        print("-" * 100)
        print("Employee Count: "+str(employeeCount))
        print("-" * 100)
        input("\nPress Enter to continue...")

    def viewInventory(self):
        global productFile
        productList = listInitializer(productFile)
        totalAmount=0
        totalItems=0
        totalQuantity=0
        clear()
        print(" INVENTORY ".center(100,"-"), end="\n")
        self.managerMenuHeader()
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
        input("\nPress Enter to continue...")

    def addProduct(self):
        global productFile
        productList = listInitializer(productFile)
        while True:
            clear()
            flag = 0
            print(" NEW PRODUCT ".center(100,'-'),end="\n")
            self.managerMenuHeader()
            name = input("\tEnter Name : ").title()
            if len(name) == 0 or name.isspace(): #checks whether the product name is empty or only contains spaces
                input("\tInvalid Product Name, Please try again !")
                break
            for product in productList:
                if product['name'] == name:
                    flag = 1
                    print("\tThe entered product:", name, ", already exists !\n")
                    break
            if flag == 0:
                quantity = int(input("\tEnter Quantity : "))
                price = float(input("\tEnter Price : "))
                productList.append({'name':name, 'quantity':quantity, 'price':price})  # Adding new product dictionary to list
                productList.sort(key=lambda product: product['name']) # to sort the list by product names (alphabetical order)
            choice = input("\tDo you want to add another product? (y/n) : ").lower()
            if choice == "n":
                break
        writeFile(productFile, productList)
        input("\nPress Enter to continue...")

    def updateProduct(self):
        global productFile
        productList = listInitializer(productFile)
        flag = 0
        suggestionList = []
        clear()
        print(" UPDATE PRODUCT ".center(100,'-'),end="\n")
        self.managerMenuHeader()
        name = input("\tEnter the Name of the product you wish to Update : ").title()
        for index, product in enumerate(productList):
            if product['name'] == name:
                flag = 1
                print("\tCurrent Quantity:", str(product["quantity"]))
                choice = input("\tDo you wish to update Quantity? (y/n) : ").lower()
                if choice == "y":
                    product["quantity"] = int(input("\tEnter new Quantity : "))
                print("\tCurrent Price:", str(product["price"]))
                choice = input("\tDo you wish to update Price? (y/n) : ").lower()
                if choice == "y":
                    product["price"] = float(input("\tEnter new Price : "))
                break
            elif similar(name, product["name"]) >= 0.6:
                suggestionList.append(index)
                flag = 2
        if flag == 2:
            print("\tThe entered product:", name, ", does not exist !")
            print("\tDid you mean : ")
            for index in suggestionList:
                print("\t---> ",productList[index]["name"], "? (y/n) : ", end="")
                choice = input().lower()
                if choice == "y":
                    print("\tCurrent Quantity:", str(productList[index]["quantity"]))
                    choice = input("\tDo you wish to update Quantity? (y/n) : ").lower()
                    if choice == "y":
                        productList[index]["quantity"] = int(input("\tEnter new Quantity : "))
                    print("\tCurrent Price:", str(productList[index]["price"]))
                    choice = input("\tDo you wish to update Price? (y/n) : ").lower()
                    if choice == "y":
                        productList[index]["price"] = float(input("\tEnter new Price : "))
                    break
        elif flag == 0:
            print("\tThe entered product:", name, ", does not exist !\n")
        suggestionList.clear()
        writeFile(productFile, productList)
        input("\nPress Enter to continue...")

    def deleteProduct(self):
        global productFile
        productList = listInitializer(productFile)
        flag = 0
        index = 0
        suggestionList = []
        clear()
        print(" DELETE PRODUCT ".center(100,'-'),end="\n")
        self.managerMenuHeader()
        name = input("\tEnter the Name of the product you wish to Delete : ").title()
        for i, product in enumerate(productList):
            if product["name"]== name:
                flag = 1
                print(
                    "\tName:",
                    product["name"],
                    ", Quantity:",
                    str(product["quantity"]),
                    ", Price:",
                    str(product["price"]),
                )
                choice = input("\tDo you wish to Delete? (y/n) : ").lower()
                if (choice == "y"):
                    flag = 2
                    index = i
                    break
                break
            elif similar(name, product["name"])>= 0.6:
                suggestionList.append(i)
                flag = 3
        if flag == 1:
            print("\tCancelled")
        elif flag == 2:
            del productList[index]
            print("\tDeleted")
        elif flag == 3:
            print("\tThe entered product:", name, ", does not exist !")
            print("\tDid you mean : ")
            for index in suggestionList:
                print("\t---> ",productList[index]["name"], "? (y/n) : ", end="")
                choice = input().lower()
                if choice == "y":
                    print(
                        "\tName:",
                        productList[index]["name"],
                        ", Quantity:",
                        str(productList[index]["quantity"]),
                        ", Price:",
                        str(productList[index]["price"]),
                    )
                    choice = input("\tDo you wish to Delete? (y/n) : ").lower()
                    if (choice == "y"):
                        del productList[index]
                        print("\tDeleted")
                        break
                    else:
                        print("\tCancelled")
                        break
        elif flag == 0:
            print("\tThe entered product:", name, ", does not exist !\n")
        suggestionList.clear()
        writeFile(productFile, productList)
        input("\nPress Enter to continue...")

    def viewSales(self):
        global salesFile
        salesList = listInitializer(salesFile)
        total=0
        clear()
        print(" RETAIL SALES ".center(100,"-"),end="\n")
        self.managerMenuHeader()
        print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
        print("-" * 100)
        for sales in salesList:
            print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
            total = total + sales['total']
        print("-" * 100)
        print(("TOTAL: "+str(total)).rjust(97))
        print("-" * 100)
        input("\nPress Enter to continue...")

    def updateStoreInfo(self):
        global storeInfoFile
        storeInfo = storeInfoInitializer(storeInfoFile)
        clear()
        print(" UPDATE STORE INFORMATION ".center(100,"-"),end="\n")
        self.managerMenuHeader()
        print("\tCurrent Store Name:", storeInfo['name'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['name'] = (input("\tEnter new Store Name : "))
            print("\t Updated !")

        print("\tCurrent City/Town/Village:", storeInfo['city'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['city'] = (input("\tEnter new City/Town/Village : "))
            print("\t Updated !")

        print("\tCurrent State:", storeInfo['state'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['state'] = (input("\tEnter new State : "))
            print("\t Updated !")

        print("\tCurrent Pincode:", storeInfo['pincode'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['pincode'] = (input("\tEnter new Pincode : "))
            print("\t Updated !")

        print("\tCurrent Phone Number:", storeInfo['phone'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['phone'] = (input("\tEnter new Phone Number : "))
            print("\t Updated !")

        print("\tTerms & Conditions:")
        print("\tCurrent T&C 1:", storeInfo['t&c1'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['t&c1'] = (input("\tEnter new T&C 1 : "))
            print("\t Updated !")
        print("\tCurrent T&C 2:", storeInfo['t&c2'])
        choice = input("\tDo you wish to update ? (y/n) : ").lower()
        if choice == "y":
            storeInfo['t&c2'] = (input("\tEnter new T&C 2 : "))
            print("\t Updated !")

        writeFile(storeInfoFile, storeInfo)
        input("\nPress Enter to continue...")

    def searchProduct(self):
        global productFile
        global salesFile
        productList = listInitializer(productFile)
        salesList = listInitializer(salesFile)
        suggestionList = []
        productData = {}
        clear()
        flag = 0
        print(" SEARCH PRODUCT ".center(100,'-'),end="\n")
        self.managerMenuHeader()
        name = input("\tEnter the Name of the product : ").title()
        for index, product in enumerate(productList):
            if product['name'] == name:
                productData.update({'name':name, 'qty':product['quantity'], 'rate':product['price'], 'soldQty':0, 'soldAmount':0.0})
                flag = 1
                break
            elif similar(name, product["name"])>= 0.6:
                suggestionList.append(index)
                flag = 2
        if flag == 0:
            print("\tThe entered product:", name, ", does not exist !",end="")
            input()
            return
        elif flag == 2:
            print("\tThe entered product:", name, ", does not exist !")
            print("\tDid you mean : ")
            for index in suggestionList:
                print("\t---> ",productList[index]["name"], "? (y/n) : ", end="")
                choice = input().lower()
                if choice == "y":
                    name = productList[index]["name"]
                    productData.update({'name':name, 'qty':productList[index]['quantity'], 'rate':productList[index]['price'], 'soldQty':0, 'soldAmount':0.0})
                    flag = 1
                    break

        if flag == 1:
            for sales in salesList:
                for item in sales['cartList']:
                    if item['name'] == name:
                        productData['soldQty'] = productData['soldQty'] + item['quantity']
                        productData['soldAmount'] = productData['soldAmount'] + item['amount']
            clear()
            print(" SEARCH PRODUCT ".center(100,'-'),end="\n")
            self.managerMenuHeader()
            print("NAME:".ljust(28),"QUANTITY:".rjust(10), "RATE:".rjust(18), "SOLD:".rjust(18), "SALES WORTH:".rjust(18))
            print("-" * 100)
            print(productData['name'].ljust(28),str(productData['qty']).rjust(10), str(productData['rate']).rjust(18), str(productData['soldQty']).rjust(18), str(productData['soldAmount']).rjust(18))
            input("\nPress Enter to continue...")
        elif flag == 2:
            input("\nPress Enter to continue...")

    def searchBill(self):
        global salesFile
        global storeInfoFile
        salesList = listInitializer(salesFile)
        flag = 0
        clear()
        print(" SEARCH BILL ".center(100,"-"),end="\n")
        self.managerMenuHeader()
        billNumber = input("\tEnter the Bill Number : ")
        for sales in salesList:
            if sales['billNumber'] == billNumber:
                flag = 1
                storeInfo = storeInfoInitializer(storeInfoFile)
                summary=["ITEMS: "+str(sales['items']), "QTY: "+str(sales['quantity']), "TOTAL: "+str(sales['total'])]
                clear()
                print(" RETAIL BILL ~ COPY ".center(100,'-'),end= "\n\n")
                print(storeInfo['name'].center(100))
                print(storeInfo['city'].center(100))
                print((storeInfo['state']+" - "+storeInfo['pincode']).center(100))
                print(("Phone: "+storeInfo['phone']).center(100))
                print("-" * 100)
                print("ISSUED TO:".ljust(80),"Date: "+sales['date'])
                print(sales['customerName'].ljust(80),"Time: "+sales['time'])
                print(sales['customerNumber'].ljust(80),"Bill No: "+sales['billNumber'])
                print(" "*81+"Cashier: "+sales['employeeUserName'])
                print("-" * 100)
                print("SN.".ljust(6),"ITEM:".ljust(40),"QTY:".rjust(10),"RATE:".rjust(18),"AMOUNT:".rjust(18))
                print("-" * 100)
                for sn, item in enumerate(sales['cartList']):
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
                input("\nPress Enter to continue...")
                break
        if flag == 0:
            input("\tNo Bill found !")

    def salesBreakdown(self):
        global salesFile
        global employeeFile
        salesList = listInitializer(salesFile)
        employeeList = listInitializer(employeeFile)
        employeeUserNames = []
        overallTotal = 0
        now = datetime.now()
        todaysDate = now.strftime("%d/%m/%Y")
        clear()
        print(" SALES BREAKDOWN ".center(100,"-"),end="\n")
        self.managerMenuHeader()
        date = input("\tEnter the date ( ALL / TODAY / dd-mm-yyyy ) : ").upper()

        if date == "ALL":
            for sales in salesList:
                if sales['employeeUserName'] not in employeeUserNames:
                    employeeUserNames.append(sales['employeeUserName'])
            if len(employeeUserNames) == 0:
                input("\tNo Sales found !")
                return
            clear()
            print(" SALES BREAKDOWN ".center(100,"-"),end="\n")
            self.managerMenuHeader()
            print("ALL SALES".center(100),end="\n")
            for userName in employeeUserNames:
                total = 0
                if not any(employee['userName'] == userName for employee in employeeList): # if employee is inactive, i.e. Not in the employee list
                    print("\tEMPLOYEE : "+userName+" (INACTIVE)")
                    print("-" * 100)
                    print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
                    print("-" * 100)
                    for sales in salesList:
                        if sales['employeeUserName'] == userName:
                            print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                            total = total + sales['total']
                            overallTotal = overallTotal + sales['total']
                    print("-" * 100)
                    print(("TOTAL: "+str(total)).rjust(97))
                    print("-" * 100, end="\n\n")
                else:
                    print("\tEMPLOYEE : "+userName)
                    print("-" * 100)
                    print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
                    print("-" * 100)
                    for sales in salesList:
                        if sales['employeeUserName'] == userName:
                            print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                            total = total + sales['total']
                            overallTotal = overallTotal + sales['total']
                    print("-" * 100)
                    print(("TOTAL: "+str(total)).rjust(97))
                    print("-" * 100, end="\n\n")
            print(("OVERALL TOTAL: "+str(overallTotal)).rjust(97))
            print("-" * 100)

        elif date == "TODAY" or date == todaysDate:
            for sales in salesList:
                if sales['date'] == todaysDate:
                    if sales['employeeUserName'] not in employeeUserNames:
                        employeeUserNames.append(sales['employeeUserName'])
            if len(employeeUserNames) == 0:
                input("\tNo Sales found !")
                return
            clear()
            print(" SALES BREAKDOWN ".center(100,"-"),end="\n")
            self.managerMenuHeader()
            print("TODAY'S SALES".center(100),end="\n")
            for userName in employeeUserNames:
                total = 0
                if not any(employee['userName'] == userName for employee in employeeList): # if employee is inactive, i.e. Not in the employee list
                    print("\tEMPLOYEE : "+userName+" (INACTIVE)")
                    print("-" * 100)
                    print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
                    print("-" * 100)
                    for sales in salesList:
                        if sales['date'] == todaysDate:
                            if sales['employeeUserName'] == userName:
                                print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                                total = total + sales['total']
                                overallTotal = overallTotal + sales['total']
                    print("-" * 100)
                    print(("TOTAL: "+str(total)).rjust(97))
                    print("-" * 100, end="\n\n")
                else:
                    print("\tEMPLOYEE : "+userName)
                    print("-" * 100)
                    print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
                    print("-" * 100)
                    for sales in salesList:
                        if sales['date'] == todaysDate:
                            if sales['employeeUserName'] == userName:
                                print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                                total = total + sales['total']
                                overallTotal = overallTotal + sales['total']
                    print("-" * 100)
                    print(("TOTAL: "+str(total)).rjust(97))
                    print("-" * 100, end="\n\n")
            print(("OVERALL TOTAL: "+str(overallTotal)).rjust(97))
            print("-" * 100)

        else:
            for sales in salesList:
                if sales['date'] == date:
                    if sales['employeeUserName'] not in employeeUserNames:
                        employeeUserNames.append(sales['employeeUserName'])
            if len(employeeUserNames) == 0:
                input("\tNo Sales found !")
                return
            clear()
            print(" SALES BREAKDOWN ".center(100,"-"),end="\n")
            self.managerMenuHeader()
            print(("SALES AS ON : "+date).center(100),end="\n")
            for userName in employeeUserNames:
                total = 0
                if not any(employee['userName'] == userName for employee in employeeList): # if employee is inactive, i.e. Not in the employee list
                    print("\tEMPLOYEE : "+userName+" (INACTIVE)")
                    print("-" * 100)
                    print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
                    print("-" * 100)
                    for sales in salesList:
                        if sales['date'] == date:
                            if sales['employeeUserName'] == userName:
                                print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                                total = total + sales['total']
                                overallTotal = overallTotal + sales['total']
                    print("-" * 100)
                    print(("TOTAL: "+str(total)).rjust(97))
                    print("-" * 100, end="\n\n")
                else:
                    print("\tEMPLOYEE : "+userName)
                    print("-" * 100)
                    print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "AMOUNT:".rjust(10))
                    print("-" * 100)
                    for sales in salesList:
                        if sales['date'] == date:
                            if sales['employeeUserName'] == userName:
                                print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
                                total = total + sales['total']
                                overallTotal = overallTotal + sales['total']
                    print("-" * 100)
                    print(("TOTAL: "+str(total)).rjust(97))
                    print("-" * 100, end="\n\n")
            print(("OVERALL TOTAL: "+str(overallTotal)).rjust(97))
            print("-" * 100)

        input("\nPress Enter to continue...")

    def bestSellingProducts(self):
        global salesFile
        salesList = listInitializer(salesFile)
        soldProductsList = []
        for sales in salesList:
            for item in sales['cartList']:
                if not any(item['name'] == soldProduct['name'] for soldProduct in soldProductsList):
                    soldProductsList.append({'name':item['name'], 'qty':item['quantity']})
                else:
                    for soldProduct in soldProductsList:
                        if item['name'] == soldProduct['name']:
                            soldProduct['qty'] = soldProduct['qty'] + item['quantity']

        clear()
        print(" BEST SELLING PRODUCTS ".center(100,"-"),end="\n")
        self.managerMenuHeader()
        if len(soldProductsList) == 0:
            print("\tInsufficient sales data, Please try again later",end="\n\n")
        else:
            soldProductsList.sort(key=lambda soldProduct: soldProduct['qty'], reverse = True) # sorts list in decreasing order of sold quantity
            print("NAME:".ljust(70),"QUANTITY SOLD:".rjust(23))
            print("-" * 100)
            for soldProduct in soldProductsList:
                print(soldProduct['name'].ljust(70),(str(soldProduct['qty'])).rjust(23))
            print("-" * 100)
        input("\nPress Enter to continue...")

    def restockSuggestions(self):
        global productFile
        productList = listInitializer(productFile)
        clear()
        print(" RESTOCK SUGGESTIONS ".center(100,"-"),end="\n")
        self.managerMenuHeader()
        if len(productList) == 0:
            print("\tNo Items found in Inventory, Please try again later",end="\n\n")
        else:
            productList.sort(key=lambda product: product['quantity']) # sorts product list in increasing order of available quantity
            if productList[0]['quantity'] < 10:    # checks if the quantity of the lowest quantity product is less than 10
                print("\t The following Items are running short (qty < 10) :\n")
                print("NAME:".ljust(50),"QUANTITY:".rjust(18), "RATE:".rjust(25))
                print("-" * 100)
                for product in productList:
                    if product['quantity'] < 10:
                        print(product['name'].ljust(50),(str(product['quantity'])).rjust(18), (str(product['price'])).rjust(25))
                print("-" * 100)
            else:
                print("\tAll Items are sufficiently stocked (qty >= 10)",end="\n\n")
        input("\nPress Enter to continue...")
