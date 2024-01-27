from api import dolarapi
FILE = "investments.txt"

def load_investment(ticker, amount):
    dolar_mep = dolarapi.get_mep()
    dolar_blue = dolarapi.get_blue()
    amount_mep = amount/dolar_mep
    amount_blue = amount/dolar_blue
    with open(FILE, 'a') as file:
        file.write(",".join([ticker, str(amount), str(amount_mep), str(amount_blue)]))
        file.write('\n')

def calculate_profit(total):
    sum_dolares = 0
    dolar_mep = dolarapi.get_mep()
    dolar_blue = dolarapi.get_blue()
    mayor_venta = min(dolar_mep, dolar_blue)
    # Calculate the amount of dollars those could've been
    with open(FILE, 'r') as file:
        for line in file:
            investment = line.rstrip().split(",")
            sum_dolares += max(float(investment[2]), float(investment[3]))
    return total/mayor_venta - sum_dolares
