#User Data Validation
user_data_container = []
while True:
        first_name = input("Enter First name: ")
        last_name = input("Enter Last name: ")
        e_mail = input("Enter E-mail: ")
        names = (first_name + ' ' + last_name)
        import random
        import string
        random_strings = ""
        for i in range(5):
                 random_strings += (random.choice(string.ascii_lowercase))
        password = (names[0:2]+names[-2:]+random_strings)
        user = {'Name':names,
                 'E-mail':e_mail,
                 'password':password
                 }
        response = input(f'Your password is: {password}, do you like it?(yes/no): ') 
        if response == 'yes':
                pass
        elif response == 'no':
            personal_password = input('Please enter your own password: ')
            user['password'] = personal_password
            if len(personal_password) < 7:
                while len(personal_password) < 7:
                        personal_password = input("password can't be less than 7 characters, please re-enter password: \n")
                else:
                        user['password'] = personal_password
        user_data_container.append(user)
        print(user)
        another_user = input('Any other user? (yes/no): ')
        if another_user == 'yes':
                continue
        else:
                m = 0
                for item in user_data_container:
                        m += 1
                        print(f'User{m}: {item}')
                break
    

