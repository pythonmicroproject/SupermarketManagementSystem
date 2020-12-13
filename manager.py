import pickle
import os
from difflib import SequenceMatcher

productFile = "productFile.txt"  # name and path of the file containg products list

class manager():
    def __init__(self):
        self.name = ""
        self.password = ""

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
        print("\n")
        print("-" * 28, "INVENTORY", "-" * 30, "\n")
        print("".join(word.ljust(col_width) for word in header))
        for product in productList:
            print("".join(str(data).ljust(col_width) for data in product.values()))
        print("\n")

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

    def updateProduct(self):
        global productFile
        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()
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

    def deleteProduct(self):
        global productFile
        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()
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
