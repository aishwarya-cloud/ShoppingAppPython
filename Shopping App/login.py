import uuid

class userLogin:
    def __init__(self):
        self.usersList = list()
        self.currentUser = list()
        f = open("userData.txt", "r")
        for x in f:
            x.strip()
            ls = x.split("|")
            #print(ls)
            self.usersList.append({
                'custId':ls[0],
                'userName':ls[1],
                'password':ls[2],
                'role':ls[3]
            })
        f.close()
                       
    def updateCurrentUser(self,cId,userName,password,role):
        self.currentUser.append({
                'custId':cId.strip(),
                'userName':userName.strip(),
                'password':password.strip(),
                'role':role.strip()
            })
        print(f"Welcome {userName} !! Your role is {role}")

    def getCurrentUser(self):
        return self.currentUser
        
    
    def getUserRole(self,userName,password):
        for list in self.usersList:
            if list['userName'] == userName and list['password'] == password:
                return list['role']
        return 'unknown'

    def getUsercustId(self,userName,password):
        for list in self.usersList:
            if list['userName'] == userName and list['password'] == password:
                return list['custId']
        return 'unknown'
         
    def createNewUser(self,userName,password,role):
       # for data in range(len(self.usersList)):
        for list in self.usersList:
            #print("userName : {}, password : {}, role : {}".format(list['userName'],list['password'],list['role']))
            if list['userName'] == userName and list['password'] == password:
                print("User already exists !! Please Sign in \n \n \n")
                return False
        
        else: 
            cId = str(uuid.uuid4())
            self.usersList.append({
                'custId':cId,
                'userName':userName,
                'password':password,
                'role':role
            })
            print("User Sucsessfully created \n \n \n \n")
            f = open("userData.txt", "a")
            userRecord = "\n"+cId+"|"+userName + "|"+password+"|"+role
            with open("userData.txt", "a") as myfile:
                myfile.write(userRecord)

            self.updateCurrentUser(cId,userName,password,role)
            return True

    def displayUsers(self):
        for user in self.usersList:
            print("user : {}, password : {}, role : {}".format(user['userName'],user['password'],user['role']))


"""
usr = userLogin()
usr.createNewUser('aish','123','admin')
usr.displayUsers()
"""
        