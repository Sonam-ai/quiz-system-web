from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_quiz_data(filename='quiz_data.json'):
    with open(filename, 'r') as file:
        return json.load(file)

questions = load_quiz_data()
total_questions = len(questions)

@app.route('/')
def index():
    # Prepare enumerated questions for the template
    questions_with_index = list(enumerate(questions))
    return render_template('index.html', questions_with_index=questions_with_index, total=total_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    for i, q in enumerate(questions):
        user_answer = request.form.get(f'question_{i}')
        correct = q['options'][q['answer']]
        if user_answer == correct:
            score += 1
            results.append((q['question'], user_answer, correct, True))
        else:
            results.append((q['question'], user_answer, correct, False))
    return render_template('result.html', score=score, total=total_questions, results=results)

if __name__ == '__main__':
    app.run(debug=True)