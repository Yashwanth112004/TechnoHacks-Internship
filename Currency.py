from forex_python.converter import CurrencyRates
all_currency_codes = [
    "EUR","INR","IDR","BGN","USD","ILS","GBP","DKK","CAD","JPY","HUF","RON","MYR",
    "SEK","SGD","AUD","HKD","CHF","KRW","CNY","TRY","HRK","NZD","THB","NOK","RUB",
    "MXN","CZK","BRL","PLN","PHP","ZAR"
    ]
print("All Currency Codes:  ", end=" ")
print(" ".join(all_currency_codes))
print("Enter the Currency Codes from Above Codes")
while(1):
    print("----------------------------------------------------------")
    a=float(input("Enter the Amount: "))
    f = input("Enter the source currency code : ").upper()
    t = input("Enter the target currency code : ").upper()
    c = CurrencyRates()
    ert=c.get_rate(f,t)
    crt=a*ert
    print(crt)
    
