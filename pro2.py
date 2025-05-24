'''kbc'''
questions=[["What is the PH of H2O?","6","7","8","9",2],
["Which of the following gas is reduced in the reduction process?","Oxygen","Helium","Carbon","Hydrogen",4],
["Which of the following compound is mainly used in hand sanitizer?","Aldehyde","Acetic acid","Alcohol","Ketone",3],
["What is the S.I unit of frequency?","Diopter","Second","Hertz","Meter",3],
["Acid turns blue litmus paper into which color?","Black","Blue","Red","Orange",3]]

for question in questions:
    print (questions[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    o=int(input("enter your value 1 for a,2 for b,3 for c, 4 for d : "))
    if (question [5]==o):
        print("correct answer")
    else:
        print(f" incorect answer , the answer was {question[5]}")
    print("Better luck next time!")
    