
from flask import Flask, render_template, request
from calculator_module import calculate_investment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    initial_investment = float(request.form['initial_investment'])
    annual_return = float(request.form['annual_return'])
    dividend_yield = float(request.form['dividend_yield'])
    fee = float(request.form['fee'])
    invest_fee = float(request.form['invest_fee'])
    investment_period = int(request.form['investment_period'])
    yearly_investment = float(request.form['yearly_investment'])

    total_profit_rate, final_investment = calculate_investment(initial_investment, annual_return, dividend_yield, fee, invest_fee, investment_period, yearly_investment)

    return render_template('result.html', total_profit_rate=total_profit_rate, final_investment=final_investment)

if __name__ == '__main__':
    app.run(debug=True)