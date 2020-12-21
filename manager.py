import pickle
import os
from difflib import SequenceMatcher
from datetime import datetime

productFile = "productFile.txt"  # name and path of the file containg products list
employeeFile = "employeeFile.txt" # name and path of the file containg employee list
salesFile = "salesFile.txt"

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

    def managerLogin(self):
        defaultPassword = "admin"
        clear()
        print("\t- Manager Login -")
        password = input("\tEnter Password : ").lower()
        if password == defaultPassword:
            input("\tWelcome Manager !")
            return True
        else:
            input("Incorrect Password, Please try again !")
            return False

    def addEmployee(self):
        global employeeFile
        clear()
        print("\t- New Employee -")
        name = input("\tEnter Name : ").title()
        userName = input("\tEnter User Name : ").lower()
        password = input("\tEnter Password : ").lower()
        print("\tPassword :",password)
        employeeList = listInitializer(employeeFile)
        employeeList.append({'name':name, 'userName':userName, 'password':password})
        writeFile(employeeFile, employeeList)
        input("Employee Added !")

    def deleteEmployee(self):
        global employeeFile
        clear()
        print("\t- Delete Employee -")
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
                        input("Employee Deleted")
                        break
                    else:
                        input("Cancelled")
        else:
            input("No such employee found !")

    def viewEmployee(self):
        global employeeFile
        clear()
        employeeList = listInitializer(employeeFile)
        col_width = 30
        header = ["NAME:", "USER NAME:", "PASSWORD:"]
        print("-" * 28, "Employee List", "-" * 30, "\n")
        print("".join(word.ljust(col_width) for word in header))
        for employee in employeeList:
            print("".join(str(data).ljust(col_width) for data in employee.values()))
        print("\n")
        input("Press Enter to continue...")

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

    def addProduct(self):
        global productFile
        if os.path.exists(productFile):  # True if file exists
            if os.stat(productFile).st_size == 0:  # True if file is empty
                productList = []
            else:
                with open(productFile, "rb") as f:
                    productList = pickle.load(f)
        else:
            productList = []
        while True:
            clear()
            flag = 0
            print("\t- Adding Product -")
            name = input("\tEnter Name : ").title()
            for product in productList:
                if product['name'] == name:
                    flag = 1
                    print("The entered product:", name, ", already exists !\n")
                    break
            if flag == 0:
                quantity = int(input("\tEnter Quantity : "))
                price = float(input("\tEnter Price : "))
                productList.append({'name':name, 'quantity':quantity, 'price':price})  # Adding new product dictionary to list
                productList.sort(key=lambda product: product['name']) # to sort the list by productect names
            choice = input("Do you want to add another product? (y/n) : ").lower()
            if choice == "n":
                break
        with open(productFile, "wb") as f:
            pickle.dump(productList, f)
        input("Press Enter to continue...")

    def updateProduct(self):
        global productFile
        if os.path.exists(productFile):  # True if file exists
            if os.stat(productFile).st_size == 0:  # True if file is empty
                productList = []
            else:
                with open(productFile, "rb") as f:
                    productList = pickle.load(f)
        else:
            productList = []
        flag = 0
        suggestionList = []
        clear()
        print("\t- Update Product -")
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
            print("The entered product:", name, ", does not exist !")
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
            print("The entered product:", name, ", does not exist !\n")
        suggestionList.clear()
        with open(productFile, "wb") as f:
            pickle.dump(productList, f)
        input("Press Enter to continue...")

    def deleteProduct(self):
        global productFile
        if os.path.exists(productFile):  # True if file exists
            if os.stat(productFile).st_size == 0:  # True if file is empty
                productList = []
            else:
                with open(productFile, "rb") as f:
                    productList = pickle.load(f)
        else:
            productList = []
        flag = 0
        index = 0
        suggestionList = []
        clear()
        print("\t- Delete Product -")
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
            elif similar(name, product["name"])>= 0.6:
                suggestionList.append(i)
                flag = 3
        if flag == 1:
            print("\tCancelled")
        elif flag == 2:
            del productList[index]
            print("\tDeleted")
        elif flag == 3:
            print("The entered product:", name, ", does not exist !")
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
            print("The entered product:", name, ", does not exist !\n")
        suggestionList.clear()
        with open(productFile, "wb") as f:
            pickle.dump(productList, f)
        input("Press Enter to continue...")

    def viewSales(self):
        global salesFile
        salesList = listInitializer(salesFile)
        clear()
        print("-" * 40,"RETAIL SALES", "-" * 47, "\n")
        print("-" * 100)
        print("DATE:".ljust(18), "TIME:".ljust(22), "BILL NO:".ljust(18), "CASHIER:".ljust(25), "TOTAL:".rjust(10))
        print("-" * 100)
        for sales in salesList:
            print(sales['date'].ljust(18), sales['time'].ljust(22), sales['billNumber'].ljust(18), sales['employeeUserName'].ljust(25), str(sales['total']).rjust(10))
        print("-" * 100)
        input("Press Enter to continue...")
