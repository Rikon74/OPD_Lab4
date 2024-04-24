from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/', methods=['POST'])
def submit():
    choice = request.form['choice']
    try:
        if choice == 'calculate_total_amount':  # Считает конечную сумму
            interest_rate = float(request.form['interest_rate']) / 100
            starting_capital = float(request.form['starting_capital'])
            deposit_term = int(request.form['deposit_term'])
            calculated = starting_capital * (1 + interest_rate) ** deposit_term
            calculated = round(calculated, 10)
        elif choice == 'calculate_interest_rate':  # Считает ставку
            your_goal = float(request.form['your_goal'])
            starting_capital = float(request.form['starting_capital'])
            deposit_term = int(request.form['deposit_term'])
            calculated = ((your_goal / starting_capital) ** (1 / deposit_term) - 1) * 100
            calculated = round(calculated, 10)
        elif choice == 'calculate_starting_capital':  # Считает стартовый капитал
            your_goal = float(request.form['your_goal'])
            deposit_term = int(request.form['deposit_term'])
            interest_rate = float(request.form['interest_rate']) / 100
            calculated = your_goal / ((1 + interest_rate) ** deposit_term)
            calculated = round(calculated, 10)
        else:
            your_goal = float(request.form['your_goal'])  # Считает срок достижения цели
            starting_capital = float(request.form['starting_capital'])
            interest_rate = float(request.form['interest_rate']) / 100
            calculated = (math.log(your_goal / starting_capital) / math.log(1 + interest_rate))
    except:
        return render_template(f"{choice}.html", selected_option=choice)
    return render_template(f"{choice}.html", calculated=calculated, selected_option=choice )


def total_amount(starting_capital, interest_rate, deposit_term):
    total_amount = starting_capital * (1 + interest_rate/100) ** deposit_term
    return total_amount


def interest_rate(your_goal, starting_capital, deposit_term):
    interest_rate = ((your_goal/starting_capital)**(1/deposit_term) - 1) * 100
    return interest_rate


def starting_capital(your_goal, interest_rate, deposit_term):
    starting_capital = your_goal/((1 + interest_rate/100)**deposit_term)
    return starting_capital


def deposit_term(your_goal, starting_capital, interest_rate):
    deposit_term = (math.log(your_goal/starting_capital)/math.log(1+interest_rate/100))
    return deposit_term


if __name__ == '__main__':
    app.run(debug=True)