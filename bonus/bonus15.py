# a = [
#     {
#         "question_text": "What are dolphins?",
#         "alternatives": ["Amphibians", "Fish", "Mammals", "Birds"],
#         "correct_answer": 3
#     },
#     {
#         "question text": "What occupies most of the Earth's surface?",
#         "alternatives": ["Land", "Water"],
#         "correct_answer": 2
#     }
# ]

# print(a)
#
#


#
#
#
import json

with open('questions.json', 'r') as file:
    content = file.read()

# print('content: ', content)  # output is as same as json file
# print('type: ', type(content))  # <class 'str'>
data = json.loads(content)
# print('data: ', data)

# [{'question_text': 'What are dolphins?', 'alternatives': ['Amphibians', 'Fish', 'Mammals', 'Birds'],
# 'correct_answer': 3}, {'question text': "What occupies most of the Earth's surface?", 'alternatives': ['Land',
# 'Water'], 'correct_answer': 2}]

# print('type: ', type(data))  # <class 'list'>

# score = 0

for question_no, question in enumerate(data):
    print("Question No", question_no + 1, ".", question["question_text"])
    for index, alternative in enumerate(question["alternative"]):
        print(index + 1, ".", alternative)

    user_choice = int(input("Enter your answer: "))

    # if user_choice == question["correct_answer"]:
    #     print("Answer is correct")
    # else:
    #     print("Wrong answer")

    question["user_choice"] = user_choice
    # if question["user_choice"] == question["correct_answer"]:
    #     score = score + 1
    #     # print(score)
    #     print("Answer is correct")
    # else:
    #     score = score
    #     # print(score)
    #     print("Wrong answer")
    #     print("The correct answer is: ", question["correct_answer"])

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
        # print(score)
        # print("Answer is correct")
    else:
        # score = score
        result = "Wrong answer"
        # print(score)
        # print("Wrong answer")
        # print("The correct answer is: ", question["correct_answer"])

    message = f"{index + 1}. {result}; Your answer: {question['user_choice']},Correct answer is {question['correct_answer']}"
    print(message)

# print(data)

# [{'question_text': 'What are dolphins?', 'alternative': ['Amphibians', 'Fish', 'Mammals', 'Birds'],
# 'correct_answer': 3, 'user_choice': 1}, {'question_text': "What occupies most of the Earth's surface?",
# 'alternative': ['Land', 'Water'], 'correct_answer': 2, 'user_choice': 2}]
print("Total Score: ", score, "/", len(data))
