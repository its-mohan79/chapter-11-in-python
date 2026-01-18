class employee:
    company = "itc"
    name = "default name"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.company}")


class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of all the language here is your language: {self.language}")

class programmer(employee,coder):
    company = "itc infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")

a = employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()
