n=int(input())
if n<=0:
    print("Invalid Input")
else:
    arr=list(map(int,input().split()))
    k=int(input())
    if k>n:
        print("invalid Input")
    else:
        first=arr[:n-k]
        last=arr[n-k:]
        res=last+first
        print(res)


class UserClass:
    full_name = ""
    email = ""
    __password = ""
    mobile_number = ""

    def _init_(self, name, email, password):
        self.full_name = name
        self.email = email
        self.__password = password

    def update_name(self, new_name):
        self.full_name = new_name

    def get_name(self):
        return self.full_name

    """ setter method for private variable password """

    def update_password(self, new_password):
        self.__password = new_password

    def update_mobile_number(self, new_number):
        self.mobile_number = new_number

    """ getter method for private variable password """

    def get_user_password(self):
        return self.__password


import UserClass


class Login:
    __db = []

    def _init_(self):
        self.print_menu()

    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    def create_user(self, name, email, password):
        new_user = UserClass(name, email, password)
        self.__db.append(new_user)
        print(self.__db)
        return True

    def validate_user(self, email, password):
        temp = self.__db.copy()

    for user_obj in temp:
        if email ==


obj = Login()
while True:
    option = input("Enter your choice: ")
    if option == '1':
        name = input("Enter your full name: ")
        email = input("Enter Email: ")
        password = input("create new password: ")
    res = obj.create_user(name, email, password)
    if res == True:
        print("User created successfully")
elif option == '2':

pass
elif option == '3':
break
else:
print("Invalid Input")