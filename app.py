from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv("career_data.csv")

def get_career_response(user_input):
    user_input = user_input.lower()

    for _, row in data.iterrows():
        if row['career'].lower() in user_input:
            return f"{row['career']}:\nStream: {row['stream']}\nSubjects: {row['subjects']}\nExam: {row['entrance_exam']}\nSkills: {row['skills']}\nAvg Salary: {row['avg_salary']}"

    if "science" in user_input:
        return "In science stream, you can become a doctor, engineer, scientist, or pilot."
    elif "commerce" in user_input:
        return "In commerce, you can become a CA, accountant, banker, or business manager."
    elif "arts" in user_input:
        return "Arts offers careers like lawyer, journalist, psychologist, or civil servant."

    return "Please ask about a specific career or stream."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_career_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
