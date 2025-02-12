def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def classificar_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif 18.5 <=imc < 25:
        return "peso adequado"
    elif 25 <= imc < 30:
        return "sobrepeso"
    elif 30 <= imc < 35:
        return "obesidade grau 1"
    elif 35 <= imc < 40:
        return "obesidade grau 2"
    else:
        return "obesidade grau 3"
    
    def main():
        print ("calculadora de IMC")
        Peso = float (input("digite seu peso (kg): "))
        altura = float (input("digite sua altura (m) "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"seu IMC É {imc:.2f} - clssificação: {classificacao}")

if __name__ == "__main__":
    main()
    