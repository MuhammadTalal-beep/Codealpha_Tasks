"""Minimal stock investment calculator

Scope:
  * user types a ticker and a quantity repeatedly
  * a built-in price dictionary supplies per-share values
  * total value is computed and shown
  * optionally write results to .txt or .csv

Key concepts: dictionary, input/output, arithmetic, file handling
"""

# hardcoded prices for demonstration
PRICE_DICT: dict[str, float] = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 300.0,
    "GOOG": 2700.0,
}


def main() -> None:
    holdings: dict[str, float] = {}

    print("Enter your holdings. Leave ticker blank to finish.")
    while True:
        ticker = input("Ticker: ").strip().upper()
        if not ticker:
            break
        if ticker not in PRICE_DICT:
            print("Price for that ticker is not defined. Try another or modify PRICE_DICT.")
            continue
        try:
            qty = float(input("Quantity: ").strip())
        except ValueError:
            print("Invalid number, please enter a numeric quantity.")
            continue
        if qty <= 0:
            print("Quantity must be positive.")
            continue
        holdings[ticker] = holdings.get(ticker, 0.0) + qty

    # compute total
    total = 0.0
    print("\nPortfolio summary:")
    for ticker, qty in holdings.items():
        price = PRICE_DICT[ticker]
        value = qty * price
        print(f"{ticker}: {qty} shares @ {price:.2f} -> {value:.2f}")
        total += value
    print(f"\nTotal investment value: {total:.2f}\n")

    if holdings:
        answer = input("Save results to file? (y/N): ").strip().lower()
        if answer == 'y':
            filename = input("Filename (end in .txt or .csv): ").strip()
            if filename:
                try:
                    if filename.lower().endswith('.csv'):
                        import csv
                        with open(filename, 'w', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(['Ticker','Quantity','Price','Value'])
                            for ticker, qty in holdings.items():
                                price = PRICE_DICT[ticker]
                                writer.writerow([ticker, qty, price, qty*price])
                            writer.writerow([])
                            writer.writerow(['Total','','',total])
                    else:
                        with open(filename, 'w') as f:
                            for ticker, qty in holdings.items():
                                price = PRICE_DICT[ticker]
                                f.write(f"{ticker}: {qty} shares @ {price:.2f} -> {qty*price:.2f}\n")
                            f.write(f"\nTotal investment value: {total:.2f}\n")
                    print(f"Saved to {filename}")
                except Exception as e:
                    print(f"Failed to write file: {e}")


if __name__ == '__main__':
    main()
