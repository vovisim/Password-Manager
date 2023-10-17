from generation_passord import GenerationPass
class Password:
    Login = ""
    Password = ""
    Name = ""



    def __init__(self, name):
        self.Name = name

    def ViborFunction(self, what_do, login, password):
        if what_do == "Set":
            self.SetPassword(login, password)
        elif what_do == "See":
            self.SeePassword()
    def SetPassword(self, Login, Pass):
        self.Login = Login
        self.Password = Pass
        with open("pass.txt", "w") as filepass:
            filepass.write(Login, Pass )




    def SeePassword(self):
        print(f"Название сервиса: {self.Name}")
        print(f"Логин: {self.Login}")
        print(f"Пароль: {self.Password}")



passjhournal = Password(name="Journal")
passjhournal.SetPassword("wova53209@ayndex.ru", "fsdgsgsghs")
passjhournal.SeePassword()










print("Что вы хотите сделать\n 1.Добавить пароль\n 2.Посмотреть пароль\n 3.Удалить пароль\n")
vibor_deistvia = int(input())
if vibor_deistvia == 1:
    imaparola = input()

