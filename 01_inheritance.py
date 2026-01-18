class employee:
    company = "itc"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")



# class programmer:
#     company = "itc infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")


#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")



class programmer(employee):
    company = "itc infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")

a = employee()
b = programmer()

print(a.company, b.company)

