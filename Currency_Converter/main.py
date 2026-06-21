import requests


def conversion(amount,api_data):
    converted_amount=float(amount*api_data["rate"])
    return converted_amount
def conversion_api(currency1,currency2):
    api_url= f"https://api.frankfurter.dev/v2/rate/{currency1}/{currency2}"
    response=requests.get(api_url)
    data=response.json()
    if response.status_code != 200:
        print(print("Invalid currency code or API error."))
        return None
    return data
def main():
    convert_amount=float(input("Convert amount: "))
    first_currency=input("Converting from: ").upper()
    second_currency=input("Converting to: ").upper()
    api_data=conversion_api(first_currency,second_currency)
    if api_data is None:
        return
    converted=conversion(convert_amount,api_data)
    print(f"{convert_amount} {first_currency} = {converted} {second_currency}")




main()