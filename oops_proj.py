class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("Welcome to chatbook, press 1 to 5, ykw to do")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.sign_in()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        password = input("setup your password")
        self.username = email
        self.password = password
        print("you have signed up successfully")
        print("\n")
        self.menu()

    def sign_in(self):
        if self.username == '' and self.password == '':
            print("please signup first by pressing 1")
        else:
            username_entered = input("enter your email here ->")
            password_entered = input("setup your password")
            if(username_entered == self.username and password_entered == self.password):
                print("you have signed in successfully")
                print("\n")
                self.loggedin = True
            else:
                print("invalid credentials")
                print("\n")
        print("\n")
        self.menu()

obj = chatbook()

