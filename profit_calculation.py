
from flask import Flask, render_template, request
from calculator_module import calculate_investment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(r'index.html')

@app.route('/result', methods=['POST'])
def result():
    initial_investment = float(request.form['initial_investment'])
    annual_return = float(request.form['annual_return'])
    dividend_yield = float(request.form['dividend_yield'])
    dividend_growth_rate = float(request.form['dividend_growth_rate'])
    fund_fee = float(request.form['fund_fee'])
    invest_fee = float(request.form['invest_fee'])
    investment_period = int(request.form['investment_period'])
    yearly_investment = float(request.form['yearly_investment'])

    total_profit_rate, total_original_investment, final_investment = calculate_investment(initial_investment, annual_return, dividend_yield, dividend_growth_rate, fund_fee, invest_fee, investment_period, yearly_investment)
    
    text_total_profit_rate = str("{:.0f}".format(total_profit_rate)) + "%"
    text_total_original_investment = str("{:,.0f}".format(total_original_investment)) + "원"
    text_final_investment = str("{:,.0f}".format(final_investment)) + "원"

    return render_template(r'result.html', total_profit_rate=text_total_profit_rate, total_original_investment= text_total_original_investment, final_investment=text_final_investment)

if __name__ == '__main__':
    app.run(debug=True)