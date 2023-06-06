from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html', current_year=current_year)

@app.route('/calculate', methods=['POST'])
def calculate():
    day = int(request.form['day'])
    month = int(request.form['month'])
    year = int(request.form['year'])

    today = datetime.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    age_year = current_year - year
    age_month = current_month - month
    age_day = current_day - day

    if age_day < 0:
        age_month -= 1
        days_in_previous_month = 31 if current_month > 1 else 0
        age_day += days_in_previous_month

    if age_month < 0:
        age_year -= 1
        age_month += 12

    return render_template('result.html', age_year=age_year, age_month=age_month, age_day=age_day)

if __name__ == '__main__':
    app.run(debug=True)
