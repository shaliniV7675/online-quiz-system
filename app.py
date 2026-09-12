from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "Which language is used to structure a webpage?",
        "options": ["CSS", "HTML", "JavaScript", "Python"],
        "answer": "HTML"
    },
    {
        "question": "Who is Chief Minister of Andhra Pradesh (2024)?",
        "options": ["Chandra Babu Naidu", "Pavan Kalyan", "Nara Lokesh", "Modi"],
        "answer": "Chandra Babu Naidu"
    },
    {
        "question": "Which language is used to style a webpage?",
        "options": ["CSS", "HTML", "JavaScript", "Python"],
        "answer": "CSS"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Mark Up Language",
            "Hyper Text Miled Language",
            "Hyper Transfer Mark Up Line",
            "Hyper Text Micro Language"
        ],
        "answer": "Hyper Text Mark Up Language"
    },
    {
        "question": "Which HTTP method is used to send data to a server?",
        "options": ["POST", "GET", "UPDATE", "DELETE"],
        "answer": "POST"
    },
    {
        "question": "Which framework is used in this project?",
        "options": ["Django", "Node.js", "Express.js", "Flask"],
        "answer": "Flask"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f"question{i}")
        if user_answer == q["answer"]:
            score += 1
    total = len(questions)
    percentage = round((score / total) * 100, 1)
    return render_template("result.html", score=score, total=total, percentage=percentage)


if __name__ == "__main__":
    app.run(debug=True)
