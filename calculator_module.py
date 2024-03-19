def calculate_investment(initial_investment, annual_return, dividend_yield, dividend_growthrate, fee, invest_fee, investment_period, yearly_investment):
  """
  투자 수익률 및 투자금 계산

  Args:
    initial_investment: 초기 투자금액
    annual_return: 연간 수익률
    dividend_yield: 배당률
    dividend_growthrate : 배당 성장률
    fee: 수수료
    investment_period: 투자 기간
    yearly_investment: 매년 추가 투자금액

  Returns:
    투자 수익률, 투자금
  """

  total_profit = 0
  final_investment = initial_investment
  original_investment = initial_investment

  for year in range(investment_period):
    
    # 연간 투자금 계산
    annual_investment = original_investment

    investing_fee = yearly_investment * invest_fee

    # 연간 수익 계산
    annual_profit = annual_investment * (annual_return + dividend_yield - fee) - investing_fee

    # # 총 투자 수익 계산
    # total_profit += annual_profit

    # 투자금 계산
    final_investment = original_investment + annual_profit

    # 투자금
    original_investment = final_investment + yearly_investment

    # 배당 성장
    dividend_yield = dividend_yield + dividend_yield*dividend_growthrate
  
  total_original_investment = initial_investment + (yearly_investment*(investment_period-1))

  return ((final_investment-total_original_investment) / (total_original_investment))*100.0, total_original_investment, final_investment


# def main():
#   """
#   사용자 입력 처리 및 결과 출력
#   """

#   # 사용자 입력
#   initial_investment = float(input("초기 투자금액 입력: "))
#   annual_return = float(input("연간 수익률 입력 (예: 0.05): "))
#   dividend_yield = float(input("배당률 입력 (예: 0.03): "))
#   fee = float(input("펀드 보수 수수료 입력 (예: 0.001): "))
#   invest_fee = float((input("매수 수수료 입력(0.000213): "))) #0.000213 vs 0.0025
#   investment_period = int(input("투자 기간 입력: "))
#   yearly_investment = float(input("매년 추가 투자금액 입력: "))

#   # 투자 수익률 및 투자금 계산
#   total_profit_rate, final_investment = calculate_investment(initial_investment, annual_return, dividend_yield, fee, invest_fee, investment_period, yearly_investment)

#   # 결과 출력
#   print(f"투자 수익률: {total_profit_rate:.2%}")
#   print(f"투자금: {final_investment:,}")

# if __name__ == "__main__":
#   main()