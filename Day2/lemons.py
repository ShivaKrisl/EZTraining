lemons = eval(input("Enter no.of lemons you have = "))
def find(lemons):
    try:
        return  "Invalid Input" if  lemons<0 or type(lemons)!=int else f"need {21-lemons}" if 21-lemons>=0 else f"extra {lemons-21}" 
    except Exception:
        return("Invalid input of string type")
print(find(lemons))