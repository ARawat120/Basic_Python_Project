# quiz game

questions = ["Is your age is  equal or above 10??(Yes,No)",
             "What is the Capital of India??",
             "Which city is called pink city in Rajasthan??",
             "Who is the first president of India??",
             "What is the answer of : 596*56??",
             "what are the 7 continent of India??(online input with space separation)"]
Answers = ["Yes",
           "Delhi",
           "Jaipur",
           "Dr.rajender prasad",
           "33376",
           ["chandigarh",
            "Delhi",
            "Daman-Diu",
            "Dadra-and-Nagar-Haveli",
            "Puducherry",
            "Jammu-and-Kashmir",
            "lakshadweep",
            "Andaman-and-Nicobar-Islands"]]
i = 1
print(questions[0])
User_Answer = input().lower()

if User_Answer.capitalize() == Answers[0] :
    while i<len(questions):

        if i==len(questions)-1:
            print(questions[i])
            User_Answer = list(map(str,input().split()))
            for Answer in User_Answer:
                if Answer in Answers[len(Answers)-1] or len(User_Answer) == 7:
                    continue
                else:
                    print(f"Invalid Answer : {Answer}")
            print("Answer is Correct")
        else:
            print(questions[i])
            User_Answer = input().lower()
            if User_Answer.capitalize() == Answers[i]:
                print("Answer is Correct")
            else:
                print(f"Invalid Answer : {Answers[i]}")
        i += 1
else:
    print("Sorry !! You Are not Eligible")