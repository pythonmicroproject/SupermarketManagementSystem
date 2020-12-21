import pickle
import os
from difflib import SequenceMatcher
from datetime import datetime

productFile = "productFile.txt"  # name and path of the file containg products list
employeeFile = "employeeFile.txt" # name and path of the file containg employee list
billGeneratorFile = "billGeneratorFile.txt"
salesFile = "salesFile.txt"

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
        self.age=0
        self.password=""
        self.sale=0

    def employeeLogin(self):
        global employeeFile
        clear()
        print("\t- Employee Login -")
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
                    print("\tWelcome "+self.name+" !",end="")
                    input()
                    return True
                else:
                    input("Incorrect Password, Please try again !")
                    return False
        if flag == 0:
            input("Incorrect Username & Password, Please try again !")
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
        col_width = 30
        header = ["NAME:", "QUANTITY:", "PRICE:"]
        clear()
        print("\n")
        print("-" * 28, "INVENTORY", "-" * 30, "\n")
        print("".join(word.ljust(col_width) for word in header))
        for product in productList:
            print("".join(str(data).ljust(col_width) for data in product.values()))
        print("\n")
        input("Press Enter to continue...")

    def cart(self):
        global productFile
        global salesFile
        if os.path.exists(productFile):  # True if file exists
            if os.stat(productFile).st_size == 0:  # True if file is empty
                productList = []
            else:
                with open(productFile, "rb") as f:
                    productList = pickle.load(f)
        else:
            productList = []
        cartList=[]
        col_width = 27
        header = ["ITEM:", "QTY:", "RATE:","AMOUNT:"]
        total=0
        items=0
        qty=0
        while True:
            clear()
            print("-" * 45, "CART", "-" * 49)
            print("-" * 100)
            print("SN.".ljust(5),"".join(word.ljust(col_width) for word in header))
            print("-" * 100)
            for sn, item in enumerate(cartList):
                print(str(sn+1).ljust(5),"".join(str(data).ljust(col_width) for data in item.values()))
            print("-"*100)
            print("\n")
            print("\t1.Add Item")
            print("\t2.Update Item")
            print("\t3.Delete Item")
            print("\t4.Generate Bill")
            print("\t5.Cancel\n")
            choice = int(input("Enter choice : "))
            if choice == 1:
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
                                input("Insufficient stock !")
                                break
                        elif similar(name, product["name"]) >= 0.6:
                            if not any(product["name"] == item['name'] for item in cartList):
                                suggestionList.append(index)
                                flag = 2
                    if flag==0:
                        input("Product does not exist !")
                    elif flag == 2:
                        print("The entered item:", name, ", does not exist !")
                        print("\tDid you mean : ")
                        for index in suggestionList:
                            print("\t---> ",productList[index]["name"], "? (y/n) : ", end="")
                            choice = input().lower()
                            if choice == "y":
                                print("Available Quantity:", str(productList[index]["quantity"]))
                                quantity = int(input("\tEnter Quantity : "))
                                if quantity <= productList[index]["quantity"]:
                                    amount=quantity*productList[index]['price']
                                    cartList.append({'name':productList[index]["name"], 'quantity':quantity, 'rate':productList[index]['price'], 'amount': amount})
                                    break
                                else:
                                    input("Insufficient stock !")
                                    break
                else:
                    input("item already exists in cart, try update item")
            elif choice == 2:
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
                                    input("Insufficient stock !")
                                    break
                        break
                    elif similar(name, item["name"]) >= 0.6:
                        suggestionList.append(index)
                        flag = 2
                if flag == 0:
                    input("Item does not exist in cart !")
                elif flag == 2:
                    print("The entered item:", name, ", does not exist in the cart !")
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
                                        input("Insufficient stock !")
                                        break
                            break
            elif choice == 3:
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
                    input("Item does not exist in cart !")
                elif flag == 2:
                    print("The entered item:", name, ", does not exist in the cart !")
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

            elif choice == 4:
                items=len(cartList)
                if items > 0:
                    customerName=input("Enter the name of the customer : ").title()
                    customerNumber=input("Enter the Phone no. of the customer : ")
                    choice=input("Complete Transaction? (y/n) : ").lower()
                    if choice == 'y':
                        clear()
                        now = datetime.now()
                        date=now.strftime("%d/%m/%Y")
                        time=now.strftime("%H:%M")
                        for item in cartList:
                            total = item['amount'] + total
                            qty = item['quantity'] + qty
                            for product in productList:
                                if product['name'] == item['name']:
                                    product['quantity'] = product['quantity']-item['quantity']
                        with open(productFile, "wb") as f:
                            pickle.dump(productList, f)
                        summary=["ITEMS: "+str(items), "QTY: "+str(qty), "TOTAL: "+str(total)]
                        billNumber = billNumberGenerator()
                        print("-" * 40,"RETAIL BILL", "-" * 47, "\n")
                        print(" "*35,"THE GARRISON PVT LTD.")
                        print(" "*41,"Kakkanad")
                        print(" "*38, "Kerala - 682039")
                        print(" "*36, "Phone: 0484 266 0999")
                        print("-" * 100)
                        print("ISSUED TO:".ljust(80),"Date: "+date)
                        print(customerName.ljust(80),"Time: "+time)
                        print(customerNumber.ljust(80),"Bill No: "+billNumber)
                        print(" "*81+"Cashier: "+self.userName)
                        print("-" * 100)
                        print("SN.".ljust(5),"".join(word.ljust(col_width) for word in header))
                        print("-" * 100)
                        for sn, item in enumerate(cartList):
                            print(str(sn+1).ljust(5),"".join(str(data).ljust(col_width) for data in item.values()))
                        print("-" * 100)
                        print(summary[0].ljust(31),summary[1].ljust(50), summary[2])
                        print("-" * 100)
                        print("\n\n")
                        print("\tTERMS & CONDITIONS:")
                        print("\t1.Goods once sold will not be taken back.")
                        print("\t2.Exchange if any, will be accepted within 7 days only.")
                        print("\n")
                        print("\t\t\t\t    THANK YOU, VISIT AGAIN")
                        print("-" * 100)
                        salesList = listInitializer(salesFile)
                        salesList.append({
                        'date':date, 'time':time, 'customerName':customerName, 'customerNumber':customerNumber, 'employeeUserName':self.userName,
                        'billNumber':billNumber, 'cartList':cartList, 'quantity':qty, 'items':items, 'total':total
                        })
                        writeFile(salesFile,salesList)
                        input("Press any key to continue . . .")
                        total=0
                        items=0
                        qty=0
                        cartList.clear()
                else:
                    input("Empty Cart !")
            elif choice == 5:
                break
            else:
                input("Please enter a valid option !\n")
