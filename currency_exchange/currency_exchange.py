import requests

def get_rates_from_api(base_code):
    url = f"http://www.floatrates.com/daily/{base_code}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

def convert_currency(target_code, amount, cache, full_rates):
    print("Checking the cache...")
    
    if target_code in cache:
        print("It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        if target_code in full_rates:
            cache[target_code] = full_rates[target_code]['rate']
    
    rate = cache.get(target_code)
    if rate:
        result = round(amount * rate, 2)
        print(f"You received {result} {target_code.upper()}.")
    else:
        print("Error: Currency rate not found.")

def main():
    base_currency = input("> ").lower()
    if not base_currency:
        return

    full_rates = get_rates_from_api(base_currency)
    
    cache = {}
    for default_curr in ['usd', 'eur']:
        if default_curr in full_rates:
            cache[default_curr] = full_rates[default_curr]['rate']

    while True:
        target_currency = input("> ").lower()
        if not target_currency:
            break
            
        try:
            amount = float(input("> "))
            convert_currency(target_currency, amount, cache, full_rates)
        except ValueError:
            print("Incorrect amount format.")
            continue

if __name__ == "__main__":
    main()
