from config import api_key
import requests
import json

def get_stock_data(symbol):
    url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response=requests.get(url)
    data=response.json()
    with open("stock_data.json","w") as file:
        json.dump(data,file)
    return data
def stock_info(data):
    print(f"{data['01. symbol']} Stock Info")
    price=float(data["05. price"])
    print(f"Price: ${price:.2f}")
    change=float(data["09. change"])
    print(f"Change: {change:.2f}")
    print(f"Change Percent: {data['10. change percent']}")
    print(f"Latest Trading Day: {data['07. latest trading day']}")
    
def main():
    symbol=input("Enter Stock Symbol: ")
    stock_data=get_stock_data(symbol)
    stock_info(stock_data["Global Quote"])

    

main()