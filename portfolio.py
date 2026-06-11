import os

# 1. Hardcoded dictionary to define stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "AMZN": 175,
    "GOOG": 150
}

def main():
    print("=== Welcome to Stock Portfolio Tracker ===")
    print("Available stocks in our system:", list(STOCK_PRICES.keys()))
    print("-" * 40)
    
    portfolio = {}
    
    # 2. Taking user input for stocks and quantity
    while True:
        stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper().strip()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in STOCK_PRICES:
            print(f"Sorry, '{stock_name}' is not in our system. Please try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of shares for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number for quantity.")
            continue
            
        # Add or update stock in portfolio
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    if not portfolio:
        print("\nYour portfolio is empty. Exiting...")
        return

    # 3. Calculating total investment value
    print("\n" + "="*30)
    print("       YOUR INVESTMENT SUMMARY      ")
    print("="*30)
    
    report_lines = []
    report_lines.append("=== STOCK PORTFOLIO REPORT ===")
    
    total_portfolio_value = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        total_value = qty * price
        total_portfolio_value += total_value
        
        line = f"Stock: {stock} | Shares: {qty} | Price per Share: ${price} | Total Value: ${total_value}"
        print(line)
        report_lines.append(line)
        
    summary_line = f"\nTotal Portfolio Value: ${total_portfolio_value}"
    print("-" * 40)
    print(summary_line)
    report_lines.append(summary_line)
    
    # 4. File Handling: Saving the result in a .txt file
    file_name = "portfolio_report.txt"
    with open(file_name, "w") as file:
        for line in report_lines:
            file.write(line + "\n")
            
    print(f"\n[Success] Portfolio details saved to '{file_name}' successfully!")

if __name__ == "__main__":
    main()