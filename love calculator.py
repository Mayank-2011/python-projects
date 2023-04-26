print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

complete_name = str(name1+name2).lower()
T = complete_name.count("t")
R = complete_name.count("r")
U = complete_name.count("u")
E = complete_name.count("e")

true = T+R+U+E

L = complete_name.count("l")
O = complete_name.count("o")
V = complete_name.count("v")
E = complete_name.count("e") 

love = L+O+V+E

score = int(str(true) + str(love))
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<=score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
