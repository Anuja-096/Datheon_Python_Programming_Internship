"""
Datheon Python Programming Internship
Task 2: Stock Portfolio Performance Tracker

This program allows users to add, view, and remove stocks
from a portfolio and calculates investment, current value,
profit/loss, and percentage return.
"""


def calculate_investment(shares, purchase_price):
    """Calculate the amount invested in a stock."""
    return shares * purchase_price


def calculate_current_value(shares, current_price):
    """Calculate the current value of a stock."""
    return shares * current_price


def calculate_profit_loss(investment, current_value):
    """Calculate profit or loss."""
    return current_value - investment


def calculate_return(investment, profit_loss):
    """Calculate percentage return."""
    if investment == 0:
        return 0
    return (profit_loss / investment) * 100


def get_positive_number(prompt):
    """Get a positive number from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_stock_symbol():
    """Get a valid stock symbol from the user."""
    while True:
        symbol = input("Enter stock symbol: ").strip().upper()

        if symbol:
            return symbol

        print("Stock symbol cannot be empty.")


def add_stock(portfolio):
    """Add a new stock to the portfolio."""
    print("\n" + "-" * 60)
    print("ADD STOCK")
    print("-" * 60)

    symbol = get_stock_symbol()

    # Prevent duplicate stock entries
    for stock in portfolio:
        if stock["symbol"] == symbol:
            print(f"{symbol} is already present in your portfolio.")
            print("Please use the existing entry or remove it first.")
            return

    shares = get_positive_number("Enter number of shares: ")
    purchase_price = get_positive_number(
        "Enter purchase price per share: ₹"
    )
    current_price = get_positive_number(
        "Enter current price per share: ₹"
    )

    stock = {
        "symbol": symbol,
        "shares": shares,
        "purchase_price": purchase_price,
        "current_price": current_price
    }

    portfolio.append(stock)

    print(f"\n{symbol} added successfully!")


def view_portfolio(portfolio):
    """Display all stocks and portfolio summary."""
    if not portfolio:
        print("\nYour portfolio is empty.")
        print("Please add a stock first.")
        return

    print("\n" + "=" * 90)
    print("                 STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 90)

    print(
        f"{'Stock':<10}"
        f"{'Shares':>10}"
        f"{'Buy Price':>14}"
        f"{'Current':>14}"
        f"{'Investment':>16}"
        f"{'Current Value':>16}"
        f"{'P/L':>12}"
    )

    print("-" * 90)

    total_investment = 0
    total_current_value = 0

    for stock in portfolio:
        investment = calculate_investment(
            stock["shares"],
            stock["purchase_price"]
        )

        current_value = calculate_current_value(
            stock["shares"],
            stock["current_price"]
        )

        profit_loss = calculate_profit_loss(
            investment,
            current_value
        )

        total_investment += investment
        total_current_value += current_value

        print(
            f"{stock['symbol']:<10}"
            f"{stock['shares']:>10.2f}"
            f"{stock['purchase_price']:>14.2f}"
            f"{stock['current_price']:>14.2f}"
            f"₹{investment:>14,.2f}"
            f"₹{current_value:>14,.2f}"
            f"₹{profit_loss:>10,.2f}"
        )

    total_profit_loss = total_current_value - total_investment
    overall_return = calculate_return(
        total_investment,
        total_profit_loss
    )

    print("-" * 90)

    print(f"\nTotal Investment : ₹{total_investment:,.2f}")
    print(f"Current Value    : ₹{total_current_value:,.2f}")

    if total_profit_loss > 0:
        print(f"Total Profit     : ₹{total_profit_loss:,.2f}")
        print(f"Overall Return   : {overall_return:.2f}%")
        print("Portfolio Status : PROFIT")

    elif total_profit_loss < 0:
        print(f"Total Loss       : ₹{abs(total_profit_loss):,.2f}")
        print(f"Overall Return   : {overall_return:.2f}%")
        print("Portfolio Status : LOSS")

    else:
        print("Total Profit/Loss: ₹0.00")
        print("Overall Return   : 0.00%")
        print("Portfolio Status : NO PROFIT / NO LOSS")

    print("=" * 90)


def remove_stock(portfolio):
    """Remove a stock from the portfolio."""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n" + "-" * 60)
    print("REMOVE STOCK")
    print("-" * 60)

    print("Stocks in your portfolio:")

    for index, stock in enumerate(portfolio, start=1):
        print(f"{index}. {stock['symbol']}")

    while True:
        choice = input(
            "\nEnter stock symbol to remove (or 0 to cancel): "
        ).strip().upper()

        if choice == "0":
            print("Remove operation cancelled.")
            return

        for stock in portfolio:
            if stock["symbol"] == choice:
                portfolio.remove(stock)
                print(f"{choice} removed successfully!")
                return

        print("Stock not found. Please enter a valid stock symbol.")


def main():
    """Run the Stock Portfolio Performance Tracker."""
    portfolio = []

    print("\n" + "=" * 60)
    print("     WELCOME TO STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 60)

    while True:
        print("\nMAIN MENU")
        print("-" * 30)
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Remove Stock")
        print("4. Exit")
        print("-" * 30)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_stock(portfolio)

        elif choice == "2":
            view_portfolio(portfolio)

        elif choice == "3":
            remove_stock(portfolio)

        elif choice == "4":
            print("\nThank you for using the Stock Portfolio Performance Tracker!")
            print("Good luck with your Datheon internship! 🚀")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()