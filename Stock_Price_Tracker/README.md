# Stock Price Tracker

A simple command-line Python app that gets stock quote data from the Alpha Vantage API and prints a clean stock summary.

## Features

- Ask the user for a stock symbol
- Request quote data from the Alpha Vantage `GLOBAL_QUOTE` endpoint
- Save the full API response to `stock_data.json`
- Print the stock symbol
- Print the latest price
- Print the price change
- Print the change percentage
- Print the latest trading day

## How To Run

From the `Stock_Price_Tracker` folder, activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python main.py
```

## API Key Setup

This project uses a `config.py` file to keep the Alpha Vantage API key out of GitHub.

Create a file named `config.py` in the `Stock_Price_Tracker` folder:

```python
api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
```

The `.gitignore` file ignores `config.py`, so your real API key stays private.

## Example

```text
Enter Stock Symbol: AAPL
AAPL Stock Info
Price: $198.42
Change: 1.23
Change Percent: 0.62%
Latest Trading Day: 2026-06-18
```

Exact values can change depending on the API response and market data timing.

## What I Learned

This project helped me practice:

- API requests with `requests`
- API keys
- JSON responses
- Nested dictionaries
- Saving data to JSON
- f-strings
- Formatting prices
- Keeping secrets out of GitHub

## Notes

This project is for learning purposes only and is not financial advice. Free stock API data may be delayed or rate-limited.
