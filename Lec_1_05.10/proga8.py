class MyClass:
    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
    
    def get_name(self):
        return self.name + " WOWOWOWOWOWOWOW"

mc = MyClass("Suzan", "Snow")
print(mc.name, mc.surname)
print(mc.get_name())

print(dir(mc.get_name))