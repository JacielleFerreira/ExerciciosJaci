valor = float(input('Digite o valor da prestação: '))
taxa = int(input('Digite a taxa da prestação: '))
tempo = int(input('Digite o tempo da prestação: '))

prestaçao = valor + (valor * (taxa / 100) * tempo)

print ('O valor da prestação em atraso é:',prestaçao)

