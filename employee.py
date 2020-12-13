import pickle
import os
from difflib import SequenceMatcher

productFile = "productFile.txt"  # name and path of the file containg products list

class employee():
    def __init__(self):
        self.name=""
        self.age=0
        self.password=""
        self.sale=0

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
