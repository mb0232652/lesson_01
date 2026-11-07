class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayfirst_name(self):
                  print(self.first_name)
    def saylast_name(self):
                  print(self.last_name)
    def get_info(self):
        print (f"{self.first_name} {self.last_name}")
# User1 = User("Марк", "Марков")

# User1.sayfirst_name()
# User1.saylast_name()
# print (User1. get_info())
