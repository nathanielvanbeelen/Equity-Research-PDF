import requests
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def matthew(TICKER):



    def calculate_dividend_yield(dividend, last_price):
        return dividend / last_price

    def calculate_eps(earnings, shares_outstanding):
        return earnings / shares_outstanding

    def calculate_pe_ratio(last_price, eps):
        return last_price / eps

    def calculate_roa(earnings, total_assets):
        return earnings / total_assets

    try:
        # Get stock information
        stock = yf.Ticker(TICKER)
        stock_prices = stock.history(period="10y")
        stock_info = stock.info
        stock_financials = stock.financials
        stock_balance_sheet = stock.balance_sheet

        # Extract relevant information
        last_price = stock_prices['Close'].iloc[-1]
        earnings = stock_financials.loc["Net Income"].iloc[0]
        dividend = stock_info['lastDividendValue']
        shares_outstanding = stock_info['sharesOutstanding']
        total_assets = (stock_balance_sheet.loc["Total Assets"].iloc[0] + stock_balance_sheet.loc["Total Assets"].iloc[1]) / 2

        dividend_yield = calculate_dividend_yield(dividend, last_price) * 100
        eps = calculate_eps(earnings, shares_outstanding)
        pe_ratio = calculate_pe_ratio(last_price, eps)
        roa = calculate_roa(earnings, total_assets) * 100


    except Exception as e:
        print(f"Error: {e}")

        # Plot the stock price

    
    X = plt.figure(figsize=(10,5))
    plt.plot(stock_prices['Open'])
    plt.plot(stock_prices['Close'])
    plt.title(f"{TICKER} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.savefig('stock_price.png')
    return X

matthew(input("Enter the stock ticker: "))

