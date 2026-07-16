questions = (
    "What is the process plants use to make their own food?",
    "What force keeps us on the ground?",
    "What is the center of an atom called?",
    "What is the largest organ in the human body?",
    "How long does it take for the Earth to revolve around the Sun?"
)

choices = (
    ("A. Respiration", "B. Photosynthesis", "C. Fermentation", "D. Transpiration"),
    ("A. Magnetism"  , "B. Friction"      , "C. Gravity"     , "D. Inertia"      ),
    ("A. Electron"   , "B. Nucleus"       , "C. Proton"      , "D. Molecule"     ),
    ("A. Liver"      , "B. Brain"         , "C. Skin"        , "D. Heart"        ),
    ("A. 24 Hours"   , "B. 30 Days"       , "C. 365.35 Days" , "D. 12 Months"    ),
    )

answers = ('B', 'C', 'B', 'C', 'C')

score = 0
print("---- Science Quiz Game ----")

for i in range(len(questions)):
    print(f"{i+1}. {questions[i]}")
    for choice in choices[i]:
        print(choice)
    answer = input("Answer : ")
    answer = answer.upper()
    while not answer in "ABCD":
        answer = input("Invalid answer, please try again : ")
    if answer == answers[i]:
        print("Correct!")
        score +=1
    else:
        print("Wrong Answer 😝")
    print()

print(f"{score} / 5")

    