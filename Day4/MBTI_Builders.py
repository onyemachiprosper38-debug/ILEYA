questionA = [

    "expand energy, enjoy groups",
    "interpret literally",
    "logical, thinking, questioning",
    "organized, orderly",
    "more outgoing, think out loud",

    "practical, realistic",
    "candid, straight forward, frank",
    "plan schedule",
    "seek many task",
    "standard, usual, conventional",
    
    "firm, tend to criticize",
    "regulated, structured",
    "external, communicative",
    "focus on here-and-now",
    "tough-minded, just",

    "preparation, plan ahead",
    "active, initiate",
    "facts, things, what is",
    "matter of fact",
    "control, govern"
  ]

questionB = [

    "conserve energy, enjoy one-on-one",
    "look for meaning and posibilities",
    "empathetic, feeling, accommodating",
    "flexible, adaptable",
    "more reserved, think to yourself",

    "imaginative, innovative",
    "tactful, kind, encouraging",
    "unplanned, spontaneous",
    "seek private, solitary activities",
    "different, novel, unique",

    "gentle, tend to appriciate",
    "easy-going, live and let live",
    "internal, retcent",
    "look to the future, big picture",
    "tender-hearted, merciful",

    "go with the flow",
    "reflective, deliberate",
    "ideas, dreams, what could be",
    "sensitive, people-oriented",
    "latitude, freedom",
 ]

e = 0
i = 0

s = 0
n = 0

t = 0
f = 0

j = 0
p = 0

responses = []

name = input("what is your name ?")

for count in range (20):
    print("\nQuestion ", (count + 1))
    print("A " + questionA[count])
    print("B " + questionB[count])

    answer = input("Chose A or B: ")
    answer = answer.upper()

    while answer != "A" and answer != "B":

        print("Expected A or B as Response")
        print("I know this is an error, please retry again")

        answer = input("Choose A or B")
        answer = answer.upper()
   
    responses.append(answer)

    if count == 0 or count == 4 or count == 8 or count == 12 or count == 16:
        if answer == "A": 
            e = e + 1; 
        
        else :
            i = i + 1;
        
    
    elif count == 1 or count == 5 or count == 9 or count == 13 or count == 17:
        if answer == "A":
            s = s + 1;
        
        else :
            n = n + 1;    
        
    
    elif count == 2 or count == 6 or count == 10 or count == 14 or count == 18:
        if answer == "A":
            t = t + 1;    
       
        else: 
            f = f + 1;
       
    
    elif count == 3 or count == 7 or count == 11 or count == 15 or count == 19:
        if answer == "A":
            j = j + 1    
       
        else: 
            p = p + 1
       
       


personality = ""

if e > i:
    personality = personality + "E"

else:
    personality = personality + "I"


if s > n:
    personality = personality + "S"

else :
    personality = personality + "N"


if t > f:
    personality = personality + "T"

else:
    personality = personality + "F"


if j < p:
    personality = personality + "J"

else :
    personality = personality + "P"


print("\nYour Responses")
for answer in responses:
    print(answer)


print("\nHello " + name);
print("Your personality Type is: " + personality)
print("\nPersonality meaning ")

if personality == "INFP":
    print("INFP people are caring and imaginative.")


elif personality == "INTJ":
    print("INTJ people are strategic and independent.")


elif personality == "ENTJ":
    print("ENTJ People are confident leaders.")


elif personality == "ESFP":
    print("ESFP People are energetic and fun.")


else:
    print("You have a unique personality.")



