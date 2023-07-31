playing = str(input("do you wanna play? (y/n) "))
if playing != "y":
    quit()

print("ok! Let's play")
correctanswers=0

answer1= input("what has a head and a tail but not body? ")
if answer1== "coin":
    print("correct")
    print("hint letter-J")
    correctanswers=correctanswers+1
else:
    print("incorrect")

answer2=int(input("what is the correct answer to 10*a+b ? 5a+3b=65,3a+4b=50 "))
if answer2==105:
    print("correct")
    print("hint letter-")
    correctanswers=correctanswers+1
else:
    print("incorrect")

answer3=int(input("what is the binary epresentation to decimal 69? "))
if answer3==1000101:
    print("correct")
    print("hint letter-A")
else:
    print("incorrect")

answer4=input("if xyz=def, what is the word form hint letters ")
if answer4=="cat":
    print("correct")
