class productCatalog:
    def __init__(self):
        self.productCataloglist = list()
        self.refreshList()
        """
        tempList = list()
        f = open("productCatalog.txt", "r")
        for x in f:
            #print(f"productCatalog here= {x}")
            catalog = str(x.strip()+".txt")
            f2 = open(catalog, "r")
            for y in f2:
                #print(f"data = {y}")
                ls = y.split("|")
                #tempList.append(ls[2].strip())
                tempList.append({
                'categoryId':ls[0].strip(),
                'productId':ls[1].strip(),
                'productName':ls[2].strip(),
                'productPrice':ls[3].strip()
            })
            
            f2.close()
            self.productCataloglist.append({
                'category':x,
                'data':tempList
            })
                           
        f.close()
        """

    def refreshList(self):
        self.productCataloglist.clear()
        tempList = list()
        f = open("productCatalog.txt", "r")
        for x in f:
            #print(f"productCatalog here= {x}")
            catalog = str(x.strip()+".txt")
            f2 = open(catalog, "r")
            for y in f2:
                #print(f"data = {y}")
                if (len(y) > 1):
                    #print(f"Catalog data available - {len(y)}")
                    ls = y.split("|")
                    #tempList.append(ls[2].strip())
                    tempList.append({
                    'categoryId':ls[0].strip(),
                    'productId':ls[1].strip(),
                    'productName':ls[2].strip(),
                    'productPrice':ls[3].strip()
                    })
                else:
                     pass
                #    print ("Catalog file empty")
            
            f2.close()
            self.productCataloglist.append({
                'category':x,
                'data':tempList
            })
                           
        f.close()
        

    def displayProductCatagory(self):
        temp = 1;
        for list in self.productCataloglist:
            #pass
            print("No : {} ,category : {} \n".format(temp,list['category']))
            temp+= 1
             
    def displayProductCatalog(self,id):
        temp = 1;
        for list in self.productCataloglist:
            if temp == id:
                cat = list['category'].strip()
                fname = list['category'].strip()+".txt"
                print("No : {} ,category : {} \n".format(temp,list['category']))
            temp+= 1;
        #print (f"fname = {fname}")
        f2 = open(fname, "r")
        var = 1
        for y in f2:
            if(len(y) > 1):
                ls = y.split("|")
                print(f"No:{var} \t Product: {ls[2].strip()} \t Price: {ls[3].strip()}\n")
            var += 1
        f2.close()

class adminUser(productCatalog):
    def addNewProductCategory(self,cat):
        with open("ProductCatalog.txt", "a") as myfile:
            myfile.write("\n"+cat)
        fname = cat + ".txt"
        open(fname, "w")
        
    def addNewProduct(self,pno,categoryId,productId,productName,productPrice):
        #print("Inside add new product")
        temp = 1;
        for list in self.productCataloglist:
            if temp == pno:
                cat = list['category'].strip()
                fname = list['category'].strip()+".txt"
                print("No : {} ,category : {} \n".format(temp,list['category']))
            temp+= 1;
        #print (f"fname = {fname}")
        userRecord = cat + "|"+productId+"|"+productName+"|"+productPrice+"\n"
        with open(fname, "a") as myfile:
            myfile.write(userRecord)
        self.refreshList()
        #self.displayProductCatalog()
                
class customerUser(productCatalog):
    def addToCart(self,cat,prd,usrName,custId):
        temp = 1;
        catnm = 'unknown'
        for list in self.productCataloglist:
            if temp == cat:
                catnm = list['category'].strip()
                fname = list['category'].strip()+".txt"
                #print("No : {} ,category : {} \n".format(temp,list['category']))
            temp+= 1;
        #print (f"fname = {fname}")
        f2 = open(fname, "r")
        var = 1
        for y in f2:
            if var == prd:
                ls = y.split("|")
                print(f"No:{var} \t CustId: {custId} \t user: {usrName} \t Categoty: {catnm} \t Product: {ls[2].strip()} \t Price: {ls[3].strip()}\n")
                cart = custId + "|"+usrName+"|"+ls[2].strip()+"|"+ls[3].strip()+"|"+"NoPayment"+"\n"
                with open("cart.txt", "a") as myfile:
                    myfile.write(cart)
                return True
            var += 1
        f2.close()
        return False

    def checkOut(self,custId):
       print (f"custId = {custId} ")
       f = open("cart.txt", "r")
       totalAmount = 0 
       for x in f:
           ls = x.split("|")
           #print(f" categoryId: {ls[0]} \t user name: {ls[1]} \t product : {ls[2]} \t price: {ls[3]} \t paid ? :{ls[4]}  \n")
           #print (f"no payment stst = {ls[4]} ")
           if (ls[0] == custId):
               #print(f" paymet sys = {ls[4]}")
               p = ls[4]
               if(p.strip() == "NoPayment"):
                   #print("No payment match %%%%%%%")
                   totalAmount += int(ls[3])
                   print(f" categoryId: {ls[0]} \t user name: {ls[1]} \t product : {ls[2]} \t price: {ls[3]} \t total: {totalAmount} \n")

       print(f"Your total amount is = {totalAmount}")
       if (totalAmount == 0):
           print("Cart is empty")
           return False
       f.close() 
       #print("\n Select Payment option") 
       f = open("paymentOptions.txt", "r")
       no = 0 
       for x in f: 
           print(f"No : {no} \t Payment option : {x}")
           no += 1
       pOption = int(input("\n Enter number for payment option: ")) 
       no = no -1 
       if (pOption >= 1 and pOption <= no ): 
           print("Transaction Successful")
           return True
       else:
           print("Invalid payment option") 
           return False
       f.close()

    def updateCart(self):
        f = open("cart.txt", "r+")
        f.truncate(0)
        print("Cart truncated")
        f.close()
    
    def updateCart2(self,custId):
        # Python program to replace text in a file
        x = input("enter text to be replaced:")
        y = input("enter text that will replace:")

        # file.txt should be replaced with
        # the actual text file name
        f = open("cart.txt", "r+")

        # each sentence becomes an element in the list l
        l = f.readlines()

        # acts as a counter to know the
        # index of the element to be replaced
        c = 0
        for i in l:
            if x in i:
                # Replacement carries the value
                # of the text to be replaced
                Replacement = i.replace(x, y)

                # changes are made in the list
                l[c] = Replacement
                
            c += 1

        # The pre existing text in the file is erased
        f.truncate(0)

        # the modified list is written into
        # the file thereby replacing the old text
        print(f"new str = {l}")
        f.writelines(l)
        f.close()
        print("Text successfully replaced")

   




