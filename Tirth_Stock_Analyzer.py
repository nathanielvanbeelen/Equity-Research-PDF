import yfinance as yf
from openai import OpenAI


def stock_analysis(TICKER):
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key='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')

    TICKER = TICKER.upper()

    try:
        # Retrieve stock data using yfinance
        stock = yf.Ticker(TICKER)
        stock_prices = stock.history(period="10y")
        stock_info = stock.info
        stock_financials = stock.financials
        stock_balance_sheet = stock.balance_sheet

        # Extract relevant financial information
        last_price = stock_prices['Close'].iloc[-1]
        earnings = stock_financials.loc["Net Income"].iloc[0]
        dividend = stock_info.get('lastDividendValue', 0)
        shares_outstanding = stock_info['sharesOutstanding']

        # Use the first available Total Assets value if it exists
        if "Total Assets" in stock_balance_sheet.index:
            total_assets = stock_balance_sheet.loc["Total Assets"].iloc[0]
        else:
            total_assets = 0

        # Calculate financial metrics
        dividend_yield = (dividend / last_price) * 100
        eps = earnings / shares_outstanding
        pe_ratio = last_price / eps
        roa = (earnings / total_assets) * 100 if total_assets else None

    except Exception as e:
        print(f"Error retrieving stock data: {e}")
        return

    # Prepare the financial data summary and prompt for the OpenAI API
    data_summary = f"""
Stock: {TICKER}
Last Share Price: {last_price:.2f}
PE Ratio: {pe_ratio:.2f}
Dividend Yield: {dividend_yield:.2f}%
EPS: {eps:.2f}
ROA: {f"{roa:.2f}%" if roa is not None else "Data not available"}
"""

    prompt = (
        f"Using the following financial data for a stock, write a concise one-paragraph summary that highlights "
        f"its key financial metrics and overall performance:\n{data_summary}"
    )

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",  # Ensure the model name is correct
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating AI summary: {e}"
