"""
Datheon Python Programming Internship
Task 2: Stock Portfolio Performance Tracker

This program calculates the current value and profit/loss
of a stock portfolio based on the number of shares,
purchase price, and current price.
"""


def calculate_stock_value(shares, price):
    """Calculate the value of a stock holding."""
    return shares * price


def calculate_profit_loss(shares, purchase_price, current_price):
    """Calculate profit or loss for a stock holding."""
    return shares * (current_price - purchase_price)


def display_portfolio(portfolio):
    """Display portfolio details and calculate totals."""
    print("\n" + "=" * 75)
    print("             STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 75)

    print(
        f"{'Stock':<12}"
        f"{'Shares':>10}"
        f"{'Buy Price':>14}"
        f"{'Current Price':>16}"
        f"{'Value':>13}"
        f"{'P/L':>10}"
    )

    print("-" * 75)

    total_investment = 0
    total_current_value = 0
    total_profit_loss = 0

    for stock in portfolio:
        investment = calculate_stock_value(
            stock["shares"], stock["purchase_price"]
        )

        current_value = calculate_stock_value(
            stock["shares"], stock["current_price"]
        )

        profit_loss = calculate_profit_loss(
            stock["shares"],
            stock["purchase_price"],
            stock["current_price"]
        )

        total_investment += investment
        total_current_value += current_value
        total_profit_loss += profit_loss

        print(
            f"{stock['symbol']:<12}"
            f"{stock['shares']:>10}"
            f"{stock['purchase_price']:>14.2f}"
            f"{stock['current_price']:>16.2f}"
            f"{current_value:>13.2f}"
            f"{profit_loss:>10.2f}"
        )

    print("-" * 75)

    print(f"Total Investment : ₹{total_investment:,.2f}")
    print(f"Current Value    : ₹{total_current_value:,.2f}")

    if total_profit_loss > 0:
        print(f"Total Profit     : ₹{total_profit_loss:,.2f}")
    elif total_profit_loss < 0:
        print(f"Total Loss       : ₹{abs(total_profit_loss):,.2f}")
    else:
        print("Total Profit/Loss: ₹0.00")

    if total_investment > 0:
        percentage = (total_profit_loss / total_investment) * 100
        print(f"Overall Return   : {percentage:.2f}%")

    print("=" * 75)


def get_number(prompt):
    """Get a positive number from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a value greater than 0.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def add_stock():
    """Collect stock information from the user."""
    print("\n--- Add Stock ---")

    symbol = input("Enter stock symbol: ").strip().upper()

    while not symbol:
        print("Stock symbol cannot be empty.")
        symbol = input("Enter stock symbol: ").strip().upper()

    shares = get_number("Enter number of shares: ")
    purchase_price = get_number("Enter purchase price per share: ")
    current_price = get_number("Enter current price per share: ")

    return {
        "symbol": symbol,
        "shares": shares,
        "purchase_price": purchase_price,
        "current_price": current_price
    }


def main():
    """Run the portfolio tracker."""
    print("=" * 75)
    print("        WELCOME TO STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 75)

    portfolio = []

    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. View portfolio")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            stock = add_stock()
            portfolio.append(stock)
            print(f"{stock['symbol']} added successfully.")

        elif choice == "2":
            if not portfolio:
                print("\nYour portfolio is empty.")
                print("Please add at least one stock first.")
            else:
                display_portfolio(portfolio)

        elif choice == "3":
            print("\nThank you for using the Stock Portfolio Performance Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()