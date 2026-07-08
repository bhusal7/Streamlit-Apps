import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    @classmethod
    def load_data(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database) as fs:
                    cls.data = json.loads(fs.read())
            else:
                cls.data = []
        except Exception as err:
            print(f"Exception occurred: {err}")
            cls.data = []

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data, indent=4))

    @staticmethod
    def __account_generate():
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        special = random.choices("!@#$%^&*()_", k=1)
        acct_id = alpha + num + special
        random.shuffle(acct_id)
        return ''.join(acct_id)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return {"success": False, "message": "You must be at least 18 and use a 4-digit PIN."}
        
        new_account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": cls.__account_generate(),
            "balance": 0
        }
        cls.data.append(new_account)
        cls.__update()
        return {"success": True, "account": new_account}

    @classmethod
    def find_user(cls, account_no, pin):
        return next((user for user in cls.data if user['accountNo'] == account_no and user['pin'] == pin), None)

    @classmethod
    def deposit(cls, account_no, pin, amount):
        user = cls.find_user(account_no, pin)
        if not user:
            return {"success": False, "message": "User not found."}
        if not (0 < amount <= 10000):
            return {"success": False, "message": "Amount must be between 1 and 10,000."}
        user['balance'] += amount
        cls.__update()
        return {"success": True, "balance": user['balance']}

    @classmethod
    def withdraw(cls, account_no, pin, amount):
        user = cls.find_user(account_no, pin)
        if not user:
            return {"success": False, "message": "User not found."}
        if user['balance'] < amount:
            return {"success": False, "message": "Insufficient funds."}
        user['balance'] -= amount
        cls.__update()
        return {"success": True, "balance": user['balance']}

    @classmethod
    def get_details(cls, account_no, pin):
        user = cls.find_user(account_no, pin)
        return {"success": bool(user), "details": user} if user else {"success": False, "message": "User not found."}

    @classmethod
    def update_details(cls, account_no, pin, name=None, email=None, new_pin=None):
        user = cls.find_user(account_no, pin)
        if not user:
            return {"success": False, "message": "User not found."}
        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            user['pin'] = new_pin
        cls.__update()
        return {"success": True, "message": "Updated successfully."}

    @classmethod
    def delete_account(cls, account_no, pin):
        user = cls.find_user(account_no, pin)
        if not user:
            return {"success": False, "message": "User not found."}
        cls.data.remove(user)
        cls.__update()
        return {"success": True, "message": "Account deleted."}

# Load data at start
Bank.load_data()
