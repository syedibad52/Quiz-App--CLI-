questions = {
    "Python is?": "a",
    "2+2=?": "b"
}

options = [
    ["a) Language", "b) Snake", "c) Car"],
    ["a) 3", "b) 4", "c) 5"]
]

score = 0

for i, q in enumerate(questions):
    print(q)
    for opt in options[i]:
        print(opt)
    
    ans = input("Answer: ")
    if ans == questions[q]:
        score += 1

print("Score:", score)
