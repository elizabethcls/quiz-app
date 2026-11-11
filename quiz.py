import random
questions = [
    {"q": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
    {"q": "What is the largest planet in our solar system?", "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"], "answer": "B"},
    {"q": "What is the chemical symbol for water?", "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"], "answer": "A"},
]
random.shuffle(questions)
score = 0

for item in questions:
    print("\n" + item["q"])
    for option in item["options"]:
        print(option)

    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in["A","B","C","D"]:
            break
        print("Invalid input.Please type A,B,C .")

    if user_answer == item["answer"]:
         print("Correct!")
         score += 1

    else :
        print(f"Wrong! The correct answer is {item['answer']}.")

print(f"\nScore:{score}/{len(questions)}")