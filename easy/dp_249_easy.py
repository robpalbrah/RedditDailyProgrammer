"""
[2016-01-11] Challenge #249 [Easy] Playing the Stock Market
https://tinyurl.com/dp-249-easy
"""
#Status: Done

# It would be interesting to make a script that calculates 
# maximum possible daily profit and see the trading 
# behaviour that will result from it. 
stock_prices = """9.20 8.03 10.02 8.08 8.14 8.10 8.31 8.28
8.35 8.34 8.39 8.45 8.38 8.38 8.32 8.36 8.28 8.28 8.38 8.48 
8.49 8.54 8.73 8.72 8.76 8.74 8.87 8.82 8.81 8.82 8.85 8.85 
8.86 8.63 8.70 8.68 8.72 8.77 8.69 8.65 8.70 8.98 8.98 8.87 
8.71 9.17 9.34 9.28 8.98 9.02 9.16 9.15 9.07 9.14 9.13 9.10 
9.16 9.06 9.10 9.15 9.11 8.72 8.86 8.83 8.70 8.69 8.73 8.73 
8.67 8.70 8.69 8.81 8.82 8.83 8.91 8.80 8.97 8.86 8.81 8.87 
8.82 8.78 8.82 8.77 8.54 8.32 8.33 8.32 8.51 8.53 8.52 8.41 
8.55 8.31 8.38 8.34 8.34 8.19 8.17 8.16"""

stock_prices = [float(stock) for stock in stock_prices.split()]

stock_prices_len = len(stock_prices)

max_profit = 0

for (i, stock) in enumerate(stock_prices):
    for index in range(i + 2, stock_prices_len):
        profit = stock_prices[index] - stock
        
        if profit > max_profit:
            max_profit = profit
            print(max_profit)
            max_profit_buy = stock
            max_profit_sell = stock_prices[index]
            
print(max_profit_buy, max_profit_sell)
