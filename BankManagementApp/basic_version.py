                                                       # 1. Bank A/c
                                                       # 2. Deposit Money
                                                       # 3. Withdraw Money
                                                       # 4. Details
                                                       # 5. Update Details
                                                       # 6. Delete A/c

import json
import random
import string
from pathlib import Path 


class Bank:
    database = 'data.json'
    data = []
        
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file is exists")
    except Exception as err:
        print(f"Exception occur as {err}")
        
        
    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
        
    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits,k = 3)
        specialCharacters = random.choices("!@#$%^&*()_",k = 1)
        
        id = alpha + num + specialCharacters
        random.shuffle(id)
        return "".join(id)
    
        
    def CreateAccount(self):
        info = {
            "name" : input("Tell your name :- "),
            "age" : int(input('Tell your age :- ')),
            'email' : input("Tell your E-Mail :- "),
            'pin': int(input("Tell your 4 No. pin :- ")),
            'accountNo' : Bank.__accountGenerate(),
            'balance' : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, You can't created ther A/c ")
        else:
            print("Account has beem Successfully✔️")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please, Note down your A/c No ")
            
            Bank.data.append(info)
            Bank.__update()



    def depositMoney(self):
        accountNum = input("Please tewll your Account No :- ")
        pin = int(input("Please tell your Pin as well :- "))
        
        # print(Bank.data)
        userData = [i for i in Bank.data if i['accountNo'] == accountNum and i['pin'] == pin]
        
        if userData == False:
            print("Sorry, NO data found ")
        else:
            amount = int(input("How much do you want to deposit :- "))
            
            if amount > 10000 or amount < 0:
                print("Sorry, The amount is too much you can deposit below 10000/-")
            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully✔️")
                
                
                
    def withdrawMoney(self):
        accountNum = input("Please tewll your Account No :- ")
        pin = int(input("Please tell your Pin as well :- "))
        
        # print(Bank.data)
        userData = [i for i in Bank.data if i['accountNo'] == accountNum and i['pin'] == pin]
        
        if userData == False:
            print("Sorry, NO data found ")
        else:
            amount = int(input("How much do you want to withdraw :- "))
            
            if userData[0]['balance'] < amount:
                print("You don't have that much money.")
                
            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully✔️")
                
                
    def showDetails(self):
        accountNum = input("Please tewll your Account No :- ")
        pin = int(input("Please tell your Pin as well :- "))
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNum and i['pin'] == pin]
        
        print("Your Information are \n\n")
        for i in userData[0]:
            print(f"{i} : {userData[0][i]}")
            
            
    def updateDetails(self):
        accountNum = input("Please tewll your Account No :- ")
        pin = int(input("Please tell your Pin as well :- "))
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNum and i['pin'] == pin]
        
        if userData == False:
            print("No such user is found.")
        else:
            print("You can't change the age, A/c no. and balance.")
            print("Fill the details for change or leave it empty if no change.")
            
            newData = {
                'name' : input("Please tell new name and press enter"),
                'email' : input("Please tell your new email or press enter to skip."),
                'pin' : input("Enter new pin or press enter to skip.")
            }
            
            if newData['name'] == '':
                userData[0]['name'] = userData[0]['name']
            if newData['email'] == '':
                userData[0]['email'] = userData[0]['email']
            if newData['pin'] == '':
                userData[0]['pin'] = userData[0]['pin']
            
            newData['age'] = userData[0]['age']
            newData['accountNo'] = userData[0]['accountNo']
            newData['balance'] = userData[0]['balance']
            
            if type(newData['pin']) == str:
                newData['pin'] = int(newData['pin'])
                
                
            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]
                    
                    
            Bank.__update()
            print("Details updated successfully✔️")
            
            
    def deleteAcc(self):
        accountNum = input("Please tewll your Account No :- ")
        pin = int(input("Please tell your Pin as well :- "))
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNum and i['pin'] == pin]
        
        if userData == False:
            print("Sorry no search data exists.")
        else:
            check = input("Press y if you want to delete the account or press n. ")
            if check == 'y' or check == "Y" and check == 'n' or check == "N":
                print("byPassed.")
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("Account deletedd Successfully✔️")
                Bank.__update()
                
user = Bank()


print("Press 1 for creating a Account :- ")
print("Press 2 for deposit money in the bank :- ")
print("Press 3 for withdraw money from bank :- ")
print("Press 4 for details :- ")
print("Press 5 for updating the details :- ")
print("Press 6 for deleting the A/c :- ")

check = int(input("Tell your Response :- "))

if check == 1:
    user.CreateAccount()

    
if check == 2:
    user.depositMoney()

    
if check == 3:
    user.withdrawMoney()

    
if check == 4:
    user.showDetails()

    
if check == 5:
    user.updateDetails()
    
if check == 6:
    user.deleteAcc()