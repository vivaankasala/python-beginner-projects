# Currency Converter

A simple command-line Python app that converts an amount from one currency to another using live exchange rate data from the Frankfurter API.

## Features

- Ask the user for an amount to convert
- Ask for the starting currency
- Ask for the target currency
- Convert currency codes to uppercase
- Get a live exchange rate from the Frankfurter API
- Calculate and print the converted amount
- Handle invalid currency codes or API errors

## How To Run

From the `Currency_Converter` folder, activate the virtual environment:

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

## Example

```text
Convert amount: 100
Converting from: EUR
Converting to: USD
100.0 EUR = 115.66 USD
```

The exact converted amount can change because exchange rates change over time.

## API Used

This project uses the Frankfurter API:

```text
https://api.frankfurter.dev/v2/rate/EUR/USD
```

The API returns JSON data with a rate, and the program multiplies the user's amount by that rate.

## What I Learned

This project helped me practice:

- Python functions
- User input
- `float()` conversion
- f-strings
- API requests with `requests`
- JSON responses
- HTTP status codes
- Basic error handling
- Virtual environments
- Project files like `.gitignore` and `requirements.txt`
