import login
import ProductCatalog
import uuid
import os

a = 1
usr = login.userLogin()
while(a == 1):
    print(""" Welcome to Shooping App !!
            To create new user : Select 1
            To login existing user: Select 2
            to exit : Select 3  """)
    x = int(input())
    #if x!= 1 or x != 2 or x!= 3:
     #   print("Please select 1 or 2 or 3 only \n")
      #  continue

    y = int(x)
    #print(f"You selected {x} \n")
    #usr = login.userLogin()

    if(y == 1):
        os.system("cls")
        userName = str(input("Ener User Name: " ))
        password = str(input("Ener User Password: " ))
        role = int(input("Enter 1 for customer and 2 for admin role : "))
        if usr.createNewUser(userName,password,'Customer' if role == 1 else 'Admin') == False:
            continue
        else:
            break
        
    elif y == 2:
        #pass
        userName = str(input("Ener User Name: "))
        password = str(input("Ener User Password: "))
        role = usr.getUserRole(userName,password)
        if role == "unknown":
            print("User Not available\n\n\n")
            continue
        else:
            #usr.updateCurrentUser(str(uuid.uuid4()),userName,password,role)
            usr.updateCurrentUser(usr.getUsercustId(userName,password),userName,password,role)
            break

    else:
        print("user selected 3 Good Bye")
        #break
        exit()

cUser = list()
cUser = usr.getCurrentUser()
#print(f"Current logged user **** {cUser}")
for z in cUser:
     pass
#    print(f"Current logged user &&& {z['role']} and id = {z['custId']}")

if z['role'] == "Admin":
    pc = ProductCatalog.adminUser()
    print("Select 1 - To update product category\n")
    print("Select 2 - To update product catalogue \n")
    opt = input()
    if(opt == 1 or opt == "1"):
        print("Updating Product cataegory")
        pc.displayProductCatagory()
        cat = input(f"Enter Product Category Name :- ")
        pc.addNewProductCategory(cat)

    elif(opt == 2 or opt == "2"):
        print("Updating Product catalogue")
        pc.displayProductCatagory()
        print("Select Category Number")
        cat = int(input())
        pname = input(f"Enter Product Name for {cat}:- ")
        pprice = input(f"Enter Product Price for {cat}:- ")
        pid = str(uuid.uuid4())
        pc.addNewProduct(cat,"categoryId",pid,pname,pprice)
        
elif z['role'] == "Customer":
    while 1:
        pc2= ProductCatalog.customerUser()
        print("Customer")
        pc2.displayProductCatagory()
        print(f"Select Category Number {z['userName']}")
        print("\n Press -2 to exit application")
        exit = 0
        cat = int(input())
        if cat == -2:
            break;
        pc2.displayProductCatalog(cat)
        print("\n Press -1 for Catgory list")
        print("\n Press -3 for Cleck Out")
        print("\n Press -2 to exit application")
        while 1:
            prd = int(input())
            if prd == -1:
                print('Back to Categories ..')
                break;

            if prd == -2:
                print('Exiting ..')
                exit = 1
                break;
                
            if prd == -3:
                print('Proceeding to Check out ..')
                if (pc2.checkOut(z['custId']) == True):
                    pc2.updateCart()
                break;
                
            if pc2.addToCart(cat,prd,z['userName'],z['custId']) == True:
                continue
                #break
            else:
                print('Product not found')

        if exit == 1:
            break;

"""
elif z['role'] == "Customer":
    pc2= ProductCatalog.customerUser()
    print("Customer")
    pc2.displayProductCatagory()
    print(f"Select Category Number {z['userName']}")
    cat = int(input())
    pc2.displayProductCatalog(cat)
    while 1:
        prd = int(input())
        if prd == -1:
            print('Exiting ..')
            break;
            
        if pc2.addToCart(cat,prd,z['userName'],z['custId']) == True:
            continue
            #break
        else:
            print('Product not found')
        
"""
    


