class chatbook:

    __user_id = 1

    def __init__(self):
        # print(id(self)) # this will print memory address
        self.id = chatbook.__user_id #class access
        chatbook.__user_id += 1
        self.__name = "default"
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()


    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("Welcome to chatbook, press 1 to 5, ykw to do")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.sign_in()
        elif user_input == "3":
            self.posting()
        elif user_input == "4":
            self.sendmsg()
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
        self.menu()

    def posting(self):
        if self.loggedin:
            txt = input("enter your text here ->")
            print(f"your text message has been posted successfully, the message is {txt}")
        else:
            print("please sign in first by pressing 2")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin:
            txt_msg = input("enter your text here ->")
            friend = input("enter your friend name here ->")
            print(f"your text message has been sent to {friend}")
        else:
            print("please sign in first by pressing 2")
        print("\n")
        self.menu()

#obj = chatbook()

