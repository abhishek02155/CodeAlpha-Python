# """
# CodeAlpha - Python Programming Internship
# Task 2: Stock Portfolio Tracker
# A simple stock tracker that calculates 
# total investment based on manually defined stock prices.
# Results can optionally be saved to a .txt or .csv file.
# """

# import csv


# # Hardcoded dictionary of stock prices
# STOCK_PRICES = {
#     "AAPL": 180,
#     "TSLA": 250,
#     "GOOGL": 140,
#     "MSFT": 320,
#     "AMZN": 130,
#     "META": 300,
#     "NFLX": 450,
# }

# def display_available_stocks():
#     print("\nAvailable stocks and prices (per share):")
#     for stock, price in STOCK_PRICES.items():
#         print(f"  {stock}: ${price}")

# def get_portfolio_input():
#     """Collect stock names and quantities from the user."""
#     portfolio = {}
#     while True:
#         stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
#         if stock == "DONE":
#             break
#         if stock not in STOCK_PRICES:
#             print(f"'{stock}' is not in the price list. Please choose from the available stocks.")
#             continue
#         try:
#             quantity = int(input(f"Enter quantity of {stock}: "))
#             if quantity < 0:
#                 print("Quantity cannot be negative.")
#                 continue
#         except ValueError:
#             print("Please enter a valid whole number for quantity.")
#             continue
#         # Add to existing quantity if stock already entered
#         portfolio[stock] = portfolio.get(stock, 0) + quantity
#     return portfolio

# def calculate_investment(portfolio):
#     """Calculate the total investment value and a breakdown per stock."""
#     breakdown = []
#     total = 0
#     for stock, quantity in portfolio.items():
#         price = STOCK_PRICES[stock]
#         value = price * quantity
#         total += value
#         breakdown.append((stock, quantity, price, value))
#     return breakdown, total

# def display_summary(breakdown, total):
#     print("\n" + "=" * 45)
#     print("PORTFOLIO SUMMARY")
#     print("=" * 45)
#     print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
#     print("-" * 45)
#     for stock, quantity, price, value in breakdown:
#         print(f"{stock:<8}{quantity:<8}${price:<9}${value:<9}")
#     print("-" * 45)
#     print(f"Total Investment Value: ${total}")
#     print("=" * 45)

# def save_to_file(breakdown, total):
#     """Save the portfolio summary to a .txt or .csv file based on user choice."""
#     choice = input("\nSave results to a file? (txt/csv/no): ").lower().strip()
#     if choice == "txt":
#         filename = "portfolio_summary.txt"
#         with open(filename, "w") as f:
#             f.write("PORTFOLIO SUMMARY\n")
#             f.write("=" * 45 + "\n")
#             f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
#             f.write("-" * 45 + "\n")
#             for stock, quantity, price, value in breakdown:
#                 f.write(f"{stock:<8}{quantity:<8}${price:<9}${value:<9}\n")
#             f.write("-" * 45 + "\n")
#             f.write(f"Total Investment Value: ${total}\n")
#         print(f"Saved to {filename}")
#     elif choice == "csv":
#         filename = "portfolio_summary.csv"
#         with open(filename, "w", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow(["Stock", "Quantity", "Price", "Value"])
#             for stock, quantity, price, value in breakdown:
#                 writer.writerow([stock, quantity, price, value])
#             writer.writerow([])
#             writer.writerow(["Total Investment Value", "", "", total])
#         print(f"Saved to {filename}")
#     else:
#         print("Results not saved.")

# def main():
#     print("=" * 45)
#     print("STOCK PORTFOLIO TRACKER")
#     print("=" * 45)
#     display_available_stocks()
#     portfolio = get_portfolio_input()
#     if not portfolio:
#         print("\nNo stocks entered. Exiting.")
#         return
#     breakdown, total = calculate_investment(portfolio)
#     display_summary(breakdown, total)
#     save_to_file(breakdown, total)

# if __name__ == "__main__":
#     main()

import yfinance as yf
import csv

def get_live_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    if not data.empty:
        return round(data['Close'].iloc[-1], 2)
    else:
        return None

def calculate_investment(portfolio):
    breakdown = []
    total = 0
    for stock, quantity in portfolio.items():
        price = get_live_price(stock)
        if price is None:
            print(f"⚠️ Could not fetch price for {stock}, skipping.")
            continue
        value = price * quantity
        total += value
        breakdown.append((stock, quantity, price, value))
    return breakdown, total
