altura = float(input('Digite a altura: '))
peso = float(input('Digite o seu Peso: '))

imc = peso / (altura * altura)

print("O seu IMC: ", imc)
if imc >= 30:
    print('Acima do peso')
elif imc < 18.5:
    print('Abaixo do peso')
else:
    print('Tudo ok!')


