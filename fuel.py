'''
Run your program with python fuel.py. Type 3/4 and press Enter. Your program should output:
75% 
Run your program with python fuel.py. Type 1/4 and press Enter. Your program should output:
25%
Run your program with python fuel.py. Type 4/4 and press Enter. Your program should output:
F
Run your program with python fuel.py. Type 0/4 and press Enter. Your program should output:
E
Run your program with python fuel.py. Type 4/0 and press Enter. Your program should handle a ZeroDivisionError and prompt the user again.
Run your program with python fuel.py. Type three/four and press Enter. Your program should handle a ValueError and prompt the user again.
Run your program with python fuel.py. Type 1.5/3 and press Enter. Your program should handle a ValueError and prompt the user again.
Run your program with python fuel.py. Type 5/4 and press Enter. Your program should prompt the user again.
'''
while True:
    try:
        Fraction = input("Fraction: ")
        Fraction = Fraction.split("/")
        percent = int((int(Fraction[0]) / int(Fraction [1])) * 100) #formul for calculating
        if percent <= 1:
            print("E") #for E
        elif 100 >= percent >= 99 :
            print("F")              #for F
        elif percent > 100:
            continue              #for more than 100
    except (ValueError, ZeroDivisionError): #catch except
        continue    
    else:
        print(f"{percent}%")    
        break