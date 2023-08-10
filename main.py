#1) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
listaNumeros = []
print('Informe os 5 numeros')
for i in range(5):
 listaNumeros.append(input('Numero '+ str(i+1) + ':\n'))
print(listaNumeros)

#2) Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

listaquestãodois = []
print('Informe os 10 numeros reais')
for i in range(10):
    listaquestãodois.append(float(input('Numero '+ str(i+1) + ':\n')))
listaquestãodois.reverse()
print(listaquestãodois)

#3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

listaNotas = []
media = 0
print('Informe as 4 notas')
for i in range(4):
  listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
media += listaNotas[i]
media = media/4
print(listaNotas)
print(media)

#4 Ler um vetor com 20 idades e exibir a maior e menor.
primeiro = int(input('Primeiro numero: '))
    segundo  = int(input('Segundo numero : '))
    terceiro = int(input('Terceiro numero: '))
    maior = primeiro
    if (segundo > maior):
        maior = segundo
    if (terceiro > maior):
        maior = terceiro
print('Maior: ',maior)
  menor = primeiro

    if (segundo < menor):
        menor = segundo
    if (terceiro < menor):
  menor = terceiro
print('Menor: ',menor)


