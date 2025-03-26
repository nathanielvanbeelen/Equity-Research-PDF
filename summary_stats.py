# Function to calculate the P/E ratio of a stock
def calculate_pe_ratio(price, earnings):
    return price / earnings


# Function to calculate the dividend yield of a stock
def calculate_dividend_yield(dividend, price):
    return dividend / price


# Function to calculate the earnings per share of a stock
def calculate_eps(net_income, shares_outstanding):
    return net_income / shares_outstanding


# Function to calculate ROA of a stock
def calculate_roa(net_income, total_assets):
    return net_income / total_assets

import yfinance as yf

# Take user input for ticker
TICKER = input('Enter a stock ticker (e.g. BHP.AX): ').upper()