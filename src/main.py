import calculator
def main():
    while True:
        option = input("1 - Cargar una inversion\n2 - Calcular profit\n")

        if option == "1":
            load_investment()
        elif option == "2":
            calculate_profit()
        else:
            break

def load_investment():
    ticker = input("Ingresa el nombre del ticker de la accion: ")
    amount = input("Ingresa el monto en pesos a invertir: ")
    calculator.load_investment(ticker, float(amount))

def calculate_profit():
    total = input("Inserta el total del portafolio en pesos: ")
    difference = calculator.calculate_profit(float(total))
    print(f'La diferencia entre haber invertido y tenerlo siempre al dolar mas barato es de: {difference} dolares')
main()