#
#  Copyright © 2021 Alan Benny, Antony Kollannur, Hafis K, Roshin Rajesh, Sidharth Anilkumar, Simon Alexander, Thomas Manoj, Thomas Philip.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import manager
import employee
import os

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(os.name is 'posix')
    else:
        os.system('clear')

def runManager():
    user = manager.manager()
    if not user.managerLogin():
        return
    while True:
        clear()
        print(" MANAGER MENU ".center(100,'-'),end= "\n")
        user.managerMenuHeader()
        print("\t1.Inventory Management\n")
        print("\t2.Employee Management\n")
        print("\t3.Sales Management\n")
        print("\t4.Update Store Information\n")
        print("\t5.LOG OUT\n")
        print("-"*100, end="\n\n")
        choice = input("Enter choice : ")
        if choice == '1':
            while True:
                clear()
                print(" INVENTORY MANAGEMENT ".center(100,'-'),end= "\n")
                user.managerMenuHeader()
                print("\t1.View Inventory\n")
                print("\t2.Search Product\n")
                print("\t3.Search Category\n")
                print("\t4.Best Selling Products\n")
                print("\t5.Restock Suggestions\n")
                print("\t6.Add New Product\n")
                print("\t7.Update Product\n")
                print("\t8.Delete Product\n")
                print("\t9.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewInventory()
                elif choice == '2':
                    user.searchProduct()
                elif choice == '3':
                    user.searchCategory()
                elif choice == '4':
                    user.bestSellingProducts()
                elif choice == '5':
                    user.restockSuggestions()
                elif choice == '6':
                    user.addProduct()
                elif choice == '7':
                    user.updateProduct()
                elif choice == '8':
                    user.deleteProduct()
                elif choice == '9':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '2':
            while True:
                clear()
                print(" EMPLOYEE MANAGEMENT ".center(100,'-'),end= "\n")
                user.managerMenuHeader()
                print("\t1.Employee List\n")
                print("\t2.Employee Performance\n")
                print("\t3.Add New Employee\n")
                print("\t4.Delete Employee\n")
                print("\t5.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewEmployee()
                elif choice == '2':
                    user.employeePerformance()
                elif choice == '3':
                    user.addEmployee()
                elif choice == '4':
                    user.deleteEmployee()
                elif choice == '5':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '3':
            while True:
                clear()
                print(" SALES MANAGEMENT ".center(100,'-'),end= "\n")
                user.managerMenuHeader()
                print("\t1.View Sales\n")
                print("\t2.Search Bill\n")
                print("\t3.Sales Breakdown\n")
                print("\t4.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewSales()
                elif choice == '2':
                    user.searchBill()
                elif choice == '3':
                    user.salesBreakdown()
                elif choice == '4':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '4':
            user.updateStoreInfo()
        elif choice == '5':
            break
        else:
            input("Please enter a valid option !\n")

def runEmployee():
    user = employee.employee()
    if not user.employeeLogin():
        return
    while True:
        clear()
        print(" EMPLOYEE MENU ".center(100,'-'),end= "\n")
        user.employeeMenuHeader()
        print("\t1.View Inventory\n")
        print("\t2.Billing\n")
        print("\t3.Account\n")
        print("\t4.LOG OUT\n")
        print("-"*100, end="\n\n")
        choice = int(input("Enter choice : "))
        if choice == 1:
            user.viewInventory()
        elif choice == 2:
            user.cart()
        elif choice == 3:
            while True:
                clear()
                print(" ACCOUNT ".center(100,'-'),end= "\n")
                user.employeeMenuHeader()
                print("\t1.My Sales\n")
                print("\t2.Change Password\n")
                print("\t3.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.mySales()
                elif choice == '2':
                    user.changeEmployeePassword()
                elif choice == '3':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == 4:
            break
        else:
            input("Please enter a valid option !\n")

while True:
    storeInfo = manager.storeInfoInitializer("storeInfoFile.txt")
    clear()
    print("-"*100)
    print(storeInfo['name'].center(100))
    print(storeInfo['city'].center(100))
    print((storeInfo['state']+" - "+storeInfo['pincode']).center(100))
    print(("Phone: "+storeInfo['phone']).center(100))
    print(end="\n")
    print(" MENU ".center(100,"-"),end="\n\n")
    print("\t1.Employee\n")
    print("\t2.Manager\n")
    print("\t3.EXIT\n")
    print("-"*100, end="\n\n")
    choice = input("Enter choice : ")
    if choice == '1':
        runEmployee()
    elif choice == '2':
        runManager()
    elif choice == '3':
        break
    else:
        input("Please enter a valid option !\n")
