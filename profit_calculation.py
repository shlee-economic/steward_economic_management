
from flask import Flask, render_template, request
from calculator_module import calculate_investment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    initial_investment = float(request.form['초기 투자금 (initial_investment)'])
    annual_return = float(request.form['연간 수익률 (annual_return)'])
    dividend_yield = float(request.form['연간 배당률 (dividend_yield)'])
    dividend_growthrate = float(request.form['배당 성장률 (dividend_growth_rate)'])
    fee = float(request.form['펀드 수수료 (fund fee)'])
    invest_fee = float(request.form['매수 수수료 (invest_fee)'])
    investment_period = int(request.form['투자 기간 (investment_period)'])
    yearly_investment = float(request.form['연간 추가 투자금 (yearly_investment)'])

    total_profit_rate, total_original_investment, final_investment = calculate_investment(initial_investment, annual_return, dividend_yield, dividend_growthrate, fee, invest_fee, investment_period, yearly_investment)
    
    text_total_profit_rate = str("{:.0f}".format(total_profit_rate)) + "%"
    text_total_original_investment = str("{:,.0f}".format(total_original_investment)) + "원"
    text_final_investment = str("{:,.0f}".format(final_investment)) + "원"

    return render_template('result.html', total_profit_rate=text_total_profit_rate, total_original_investment= text_total_original_investment, final_investment=text_final_investment)

if __name__ == '__main__':
    app.run(debug=True)