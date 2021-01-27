# Stock & Billing Software for Super Markets 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)   
A **command line interface** program to perform billing and inventory management for super markets and other retail stores. 

>**This program was developed as a team for our second year college microproject based on python.**  
>**Note:** This is **not** an industry standard program. This program merely depicts some of the functionalities found in production software used in retail stores for billing and  managing inventory.

## Files
Source code:
- **main.py** - main program containing all the menus and executable code. **Run this file to execute the program.**
- **manager.py** - contains the manager class and its associated functions.
- **employee.py** - contains the employee class and its associated functions.

Upon successful usage of the program, the following binary data files may be generated:
- employeeFile.txt - contains the details of all the employees.
- billGeneratorFile.txt - to keep track of the bill number.
- productFile.txt - contains the details of all products in the inventory.
- salesFile.txt - stores all the sales related data.
- storeInfoFile.txt - contains the name and other information about the store.

## Packages/Libraries used

- **pickle**
- **os**
- **difflib**
- **datetime**
- **textwrap**

All the above are standard built-in python modules.
## Scope

- **Manager** :  has access to the following functionalities
  - Inventory management
    - View inventory: Returns details of all the products available .
    - Search product: Returns details of a particular product.
    - Best Selling Products: lists the names of the best selling products.
    - Restock Suggestions: Alerts the user  when they are low on specific products. 
    - Add new product: Adds a new product to the inventory.
    - Update product:  Updates the price and quantity of a product in the inventory.
    - Delete product: Deletes a product from the inventory.
    - Search category: Displays products belonging  to a specific category.
    
  - Employee Management
    - Employee list: Returns details of all the employees.
    - Delete employee: Deletes an employee from the file.
    - Add new employee: Adds a new employee to the file.
    - Employee performance: Displays performance of each employee.
  - Sales Management
    - View sales: Returns details of all the sales done.
    - Search bill: Returns  the details of a particular bill.
    - Sales Breakdown: Displays the sales made by each employee on a specific date.
  - Update Store Information: updates/changes the details of the store such as name, address, etc.
 
- **Employee** : has access to the following functionalities
  - View inventory: Returns details of all the products available. 
  
  - Billing
    -  Add item:  Adds an item to the cart.
    - Update item: Updates the quantity of an  item in the  cart.
    - Delete item: Deletes an item from the cart.
    - Generate Bill:  Generates a bill for the customer.
  - Account
    - My sales: Returns  details of the sales done by the logged in employee.
    - Change Password: To change the password of the logged in employee. 
   
 >**Note:** the password for manager login is  "**admin**"
 
 ## Team Members
-  Alan Benny
-  Antony Kollannur
-  Hafis K
-  Roshin Rajesh
-  Sidharth Anilkumar
-  Simon Alexander
-  Thomas Manoj
-  Thomas Philip

## Copyright License [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
**This project is licensed under the Apache License, Version 2.0**
