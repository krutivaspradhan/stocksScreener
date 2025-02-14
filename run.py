import yfinance as yf

# Define the stock ticker symbol (Example: Apple)
ticker_symbol = "AAPL"

# Fetch stock data
stock = yf.Ticker(ticker_symbol)


# Retrieve key financial metrices
pe_ratio = stock.info.get("trailingPE") # P/E Ratio
pb_ratio = stock.info.get("priceToBook") # P/B Ratio
market_cap = stock.info.get("marketCap") # Market Capitalization
dividend_yield = stock.info.get("dividendYield") # Dividend Yield
roe = stock.info.get("returnOnEquity") # Return on Equity

# Print the retrieved data

print(f"Stock: {ticker_symbol}")
print(f"P/E Ratio: {pe_ratio}")
print(f"P/B Ratio: {pb_ratio}")
print(f"Market Cap: {market_cap}")
print(f"Dividend Yield: {dividend_yield}")
print(f"Return on Equity: {roe}")
