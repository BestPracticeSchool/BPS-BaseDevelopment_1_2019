skobochki = {')':'(', ']':'[', '}':'{'}
 
def tak(s):
    steck = []
    for ch in s:
        if ch in skobochki.values():
            steck.append(ch)
        elif ch in skobochki.keys():
            if not (steck and skobochki[ch] == steck.pop()):
                return False
    return True

n = int(input())
for i in range(0,n): 
     s = input() 
     if (tak(s) == True): 
          print("yes")
     else: 
          print("no")