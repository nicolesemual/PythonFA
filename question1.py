# NICOLE SUE IDORA ANAK SEMUAL
# 20DDT21F1041


nf=open('password.txt','w')
nf.write('1903_matjan')
nf.write('\nfaizal13')
nf.write('\nhaha@faizal213HAHA')
nf.write('\njaja')
nf.write('\nlalalalal')
nf.write('\n1903_Faizal')
nf.close()


class PasswordManager:
    def __init__(self,password,entered_password):
        self.password=password
        self.entered_password=entered_password

    def old_passwords(self):
        pass_lama = self.password[-1]
        return pass_lama


    def get_password(self):
        print(f"{self.entered_password} is not your current password.")
        if self.entered_password not in self.password:
            print("Your password is wrong")
        else:
            print("Please enter your new password")

    def set_password(self):
        print(f"{self.entered_password} is not your current password.")
        if self.entered_password not in self.password:
            ans = input(f"Are you sure want to insert {self.entered_password} in password.txt ? (Yes,No): ")
            if ans =="Yes":
                nm=open('password.txt','a')
                nm.write("\n" +self.entered_password)
                nm.close()
                print("Your New Password have been entered. Thankyou.")
            elif ans == 'No':
                print('Thankyou. Have a nice day')
        else:
            print(f'{self.entered_password} is already in list.')

    def is_correct(self):
        print("your password is wrong")
        if self.entered_password == object1.get_password():
            print("You have entered current password.")
        else:
            object.set_password()


list_of_password = open('password.txt').read()
make_as_list=list_of_password.split()
password = input("Please enter your password to reset: ")
object1 = PasswordManager(make_as_list,password)
object1.is_correct()




