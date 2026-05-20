from flask import Flask, request
from questions import questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():

    score = 0

    if request.method == "POST":

        for i, q in enumerate(questions):

            user_answer = request.form.get(f"q{i}")

            if user_answer == q["answer"]:
                score += 1

        percentage = (score / len(questions)) * 100

        return f"""
        <html>

        <head>
            <title>Quiz Result</title>
        </head>

        <body style="
            font-family: Arial;
            background-color: #f2f2f2;
            text-align: center;
            padding-top: 100px;
        ">

            <h1>Quiz Completed!</h1>

            <h2>Your Score: {score}/{len(questions)}</h2>

            <h2>Percentage: {percentage}%</h2>

            <a href="/" style="
                text-decoration: none;
                background-color: blue;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
            ">
                Play Again
            </a>

        </body>
        </html>
        """

    html = """

    <html>

    <head>

        <title>Python Quiz</title>

        <style>

            body{
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 30px;
            }

            .quiz-box{
                background: white;
                padding: 20px;
                border-radius: 10px;
                max-width: 800px;
                margin: auto;
            }

            h1{
                text-align: center;
                color: darkblue;
            }

            .question{
                margin-bottom: 25px;
            }

            #timer{
                text-align: center;
                color: red;
                font-size: 25px;
            }

            button{
                background-color: blue;
                color: white;
                border: none;
                padding: 12px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }

        </style>

    </head>

    <body>

        <div class="quiz-box">

        <h1>Python Quiz</h1>

        <h2 id="timer">Time Left: 150 seconds</h2>

        <form method="POST" id="quizForm">
    """

    for i, q in enumerate(questions):

        html += f"""
        <div class="question">

        <h3>Q{i+1}. {q['question']}</h3>
        """

        for option in q["options"]:

            option_letter = option[0]

            html += f"""
            <input type="radio" name="q{i}" value="{option_letter}" required>
            {option}
            <br><br>
            """

        html += "</div>"

    html += """

        <center>
            <button type="submit">Submit Quiz</button>
        </center>

        </form>

        </div>

        <script>

            let timeLeft = 150;

            const timer = document.getElementById("timer");

            const countdown = setInterval(() => {

                timeLeft--;

                timer.innerHTML = "Time Left: " + timeLeft + " seconds";

                if(timeLeft <= 0){

                    clearInterval(countdown);

                    alert("Time Up! Quiz Submitted");

                    document.getElementById("quizForm").submit();
                }

            }, 1000);

        </script>

    </body>

    </html>
    """

    return html

if __name__ == "__main__":
    app.run(debug=True)