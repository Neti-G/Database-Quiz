import tkinter as tk
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
falseQuestionsPath = os.path.join(dir_path, 'questions/false_ans.txt')
trueQuestionsPath = os.path.join(dir_path, 'questions/true_ans.txt')

false_list = []
with open(falseQuestionsPath, encoding="utf8") as f:
    line = f.readline()
    while line:
        false_list.append(line)
        line = f.readline()

true_list = []
with open(trueQuestionsPath, encoding="utf8") as f:
    line = f.readline()
    while line:
        true_list.append(line)
        line = f.readline()

false_map = {key: "false" for key in false_list}
true_map = {key: "true" for key in true_list}
questions = {**false_map, **true_map}


questions_list = random.sample(list(questions.keys()), len(questions.keys()))
question_index = 0


def get_question(flag):
    global questions_list
    global question_index

    if flag == 0:
        question = questions_list[0]

    elif flag == 1:
        question_index += 1
        if (question_index == len(questions_list)):
            question_index = 0
            print("All questions answered!")
        question = questions_list[question_index]

    elif question_index == 0:
        question = questions_list[0]

    else:
        question_index -= 1
        question = questions_list[question_index]

    return question


question = get_question(0)


def check_answer(answer, result_label):
    def on_click():
        global question
        if questions[question].lower() == answer.lower():
            result_label.config(text="Correct!", fg="green")
        else:
            result_label.config(text="Incorrect!", fg="red")
    return on_click


def next_question(result_label):
    def on_click():
        global question
        question = get_question(1)
        question_label.config(text=question)
        result_label.config(text="")
    return on_click


def previous_question(result_label):
    def on_click():
        global question
        question = get_question(-1)
        question_label.config(text=question)
        result_label.config(text="")
    return on_click


root = tk.Tk()
root.geometry("650x250")
root.title("Quiz")

question_frame = tk.Frame(root, width=650, height=120)
question_frame.pack_propagate(False)
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, text=question, font=("TkDefaultFont", 16), wraplength=600)
question_label.pack()

answer_frame = tk.Frame(root)
answer_frame.pack(pady=10)

result_label = tk.Label(root, text="", font=("TkDefaultFont", 14))
result_label.pack()

previous_button = tk.Button(answer_frame, text="Previous", width=10, command=previous_question(result_label))
previous_button.grid(row=0, column=0, padx=10, pady=10)

true_button = tk.Button(answer_frame, text="True", width=10, command=check_answer("true", result_label))
true_button.grid(row=0, column=1, padx=5, pady=10)

false_button = tk.Button(answer_frame, text="False", width=10, command=check_answer("false", result_label))
false_button.grid(row=0, column=2, padx=5, pady=10)

next_button = tk.Button(answer_frame, text="Next", width=10, command=next_question(result_label))
next_button.grid(row=0, column=3, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("TkDefaultFont", 16))
result_label.pack()

root.mainloop()
