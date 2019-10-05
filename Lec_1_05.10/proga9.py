class Film:
    def __init__(self, *args):
        self.title = args[0]
        self.stars = args[1]
        self.rating = args[2]

    
    def predict(self):
        return self.stars*self.rating*99000



f = Film("Iron man", 5, 9.21)

class Serial(Film): #, Film1, str, dict, tuple, Film2):
    pass

s = Serial("Friends", 10, 9.99)
print(s.title,  s.stars, s.rating)

print(2 + 3)
print("kek"+"lol")


