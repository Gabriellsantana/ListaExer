# 01
n = float(input("Digite um numero: "))
print(f"O valor da quadrado do numero {n} é {n ** 2}")

# Q2
n = float(input("Digite um numero: "))
print(f"A quinata parte do numeor {n} é {n / 5}")

# Q3
n = float(input("Digite um numero: "))
print(f"A quinata parte do numeor {n} é {n / 5}")

# Q4
ase = int(input("Digite a base do triangulo: "))
alt = int(input("Digite a altura do triangulo: "))

area = (base * alt) / 2

print(f"A area de um triangulo com base {base} e altura {alt} é {area}")

# Q5
n = int(input("Digite um numro: "))

if n < 0:
    print(f"{n} é negativo")
elif n > 0:
    print(f"{n} é possotivo")
else:
    print(f"{n} é nulo")

# Q6
n = int(input("Digite um numero inteiro: "))

if n % 3 == 0:
    print(f"{n} é multiplo de 3!")
else:
    print(f"{n} não é multiplo de 3!")

# Q7
n = int(input("Digite um numero: "))

if n % 5 == 0:
    print(f"{n} é divisivel por 5")
else:
    print(f"{n} não é divisivel por 5")

# Q8
a = int(input("Digite o numero a: "))
b = int(input("Digite o numero b: "))

if a % b == 0:
    print(f"O numero a ({a}) é divisivel pelo b ({b})")

else:
    print(f"O numero a ({a}) não é divisivel pelo b ({b})")
# q9
altura = float(input('digite a sua altura: '))
sexo = str(input('digite o seu sexo m/f: '))
f = (altura * 72.7) - 58
m = (altura * 62.1) - 44.7

if sexo == 'f':
    print(f)


elif sexo == 'm':
    print(m)
# q10

# 10
a = int(input('digite um numero'))
b = int(input('digite um numero'))
c = int(input('digite um numero'))

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}')

# Q11
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

list = [a, b, c]
list.sort()
list.reverse()

print(f"A orde descrecente é: {list}")

# q12
# Elaborar um programa que apresente no final o
# somatório dos valores pares existentes na faixa de 0 até 500.
n = 0
soma = 0
while (n < 500):
    soma = soma + n
n = n + 2
print('soma %d' % soma)

# Q13
ma = None
me = None
for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
    ma = ma if ma != None and ma > altura else altura
    me = me if me != None and me < altura else altura

print(f"A maior altura é: {ma} e a menor altura é: {me}")

# q14
numero_mais_gordo = 0
peso_mais_gordo = 0
numero_mais_magro = 0
peso_mais_magro = float(
    'inf')  # Inicializado com um valor muito alto para garantir que o primeiro boi seja sempre mais magro

# Percorra os 90 bois
for i in range(1, 91):
    numero_boi = int(input(f"Digite o número de identificação do boi {i}: "))
    peso_boi = float(input(f"Digite o peso do boi {i}: "))

    # Verifique se o boi atual é o mais gordo
    if peso_boi > peso_mais_gordo:
        numero_mais_gordo = numero_boi
        peso_mais_gordo = peso_boi

    # Verifique se o boi atual é o mais magro
    if peso_boi < peso_mais_magro:
        numero_mais_magro = numero_boi
        peso_mais_magro = peso_boi

# Exiba os resultados
print("Boi mais gordo:")
print("Número:", numero_mais_gordo)
print("Peso:", peso_mais_gordo)
print("")

print("Boi mais magro:")
print("Número:", numero_mais_magro)
print("peso:", peso_mais_magro)

# Q15
abt = int(input("Quantos habitante tinham: "))
masc = 0
fem = 0
az = 0
vd = 0
cast_olho = 0
preto = 0
loiro = 0
cast_cabelo = 0
ma = None
porcent = 0

for i in range(abt):
    sexo = int(input(f"Qual o sexo do habitante {i + 1}?  1(masc) 2(fem)"))
    if sexo == 1:
        masc += 1
    else:
        fem += 1

    olhos = int(input(f"Qual a cor dos olhos do habitante {i + 1}? 1(verde) 2(azul) 3(castanho)"))

    if olhos == 1:
        vd += 1
    elif olhos == 2:
        az += 1
    else:
        cast_olho += 1

    cabelo = int(input(f"Qual a cor dos olhos do habitante {i + 1}? 1(preto) 2(loiro) 3(castanho)"))

    if cabelo == 1:
        preto += 1
    elif cabelo == 2:
        loiro += 1
    else:
        cast_cabelo += 1

    idade = int(input(f"Qual a idade do habitante {i + 1}? "))
    if sexo == 2 and olhos == 1 and cabelo == 2 and idade >= 18 and idade <= 35:
        porcent += 1
    ma = ma if ma != None and ma > idade else idade

print(f"O habitante mais velho tem {ma} anos")
b = (porcent * 100) / abt
print(
    f"A porcentagem de indivíduos do sexo feminino com idade de 18 a 35 anos que tenham olhos verdes e cabelos louros é {b}%")

# Q11
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

list = [a, b, c]
list.sort()
list.reverse()

print(f"A orde descrecente é: {list}")

# Q13
ma = None
me = None
for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
    ma = ma if ma != None and ma > altura else altura
    me = me if me != None and me < altura else altura

print(f"A maior altura é: {ma} e a menor altura é: {me}")
#q14
numero_mais_gordo = 0
peso_mais_gordo = 0
numero_mais_magro = 0
peso_mais_magro = float('inf')  # Inicializado com um valor muito alto para garantir que o primeiro boi seja sempre mais magro

# Percorra os 90 bois
for i in range(1, 91):
    numero_boi = int(input(f"Digite o número de identificação do boi {i}: "))
    peso_boi = float(input(f"Digite o peso do boi {i}: "))

    # Verifique se o boi atual é o mais gordo
    if peso_boi > peso_mais_gordo:
        numero_mais_gordo = numero_boi
        peso_mais_gordo = peso_boi

    # Verifique se o boi atual é o mais magro
    if peso_boi < peso_mais_magro:
        numero_mais_magro = numero_boi
        peso_mais_magro = peso_boi

# Exiba os resultados
print("Boi mais gordo:")
print("Número:", numero_mais_gordo)
print("Peso:", peso_mais_gordo)
print("")

print("Boi mais magro:")
print("Número:", numero_mais_magro)
print("peso:", peso_mais_magro)

# Q15
abt = int(input("Quantos habitante tinham: "))
masc = 0
fem = 0
az = 0
vd = 0
cast_olho = 0
preto = 0
loiro = 0
cast_cabelo = 0
ma = None
porcent = 0

#Q16
otal_votos = 0
votos_candidato = [0, 0, 0, 0]  # Índices 0 a 3 representam os candidatos 1 a 4
votos_nulos = 0
votos_em_branco = 0

# Receba os votos até que seja inserido o valor 0
voto = int(input("Digite o código do voto (1 a 4, 5 para voto nulo, 6 para voto em branco, ou 0 para encerrar): "))

while voto != 0:
    if voto == 1:
        votos_candidato[0] += 1
    elif voto == 2:
        votos_candidato[1] += 1
    elif voto == 3:
        votos_candidato[2] += 1
    elif voto == 4:
        votos_candidato[3] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1

    total_votos += 1
    voto = int(input("Digite o código do voto (1 a 4, 5 para voto nulo, 6 para voto em branco, ou 0 para encerrar): "))

# Calcule e exiba os resultados
print("Resultado da eleição:")
print("")

# Resultado para cada candidato
for i in range(4):
    candidato = i + 1
    percentual = (votos_candidato[i] / total_votos) * 100
    print("Candidato", candidato, ":")
    print("Total de votos:", votos_candidato[i])
    print("Percentual:", percentual, "%")
    print("")

# Resultado para votos nulos
percentual_nulos = (votos_nulos / total_votos) * 100
print("Votos nulos:")
print("Total de votos:", votos_nulos)
print("Percentual:", percentual_nulos, "%")
print("")

# Resultado para votos em branco
percentual_em_branco = (votos_em_branco / total_votos) * 100
print("Votos em branco:")
print("Total de votos:", votos_em_branco)
print("Percentual:", percentual_em_branco, "%")

for i in range(abt):
    sexo = int(input(f"Qual o sexo do habitante {i + 1}?  1(masc) 2(fem)"))
    if sexo == 1:
        masc += 1
    else:
        fem += 1

    olhos = int(input(f"Qual a cor dos olhos do habitante {i + 1}? 1(verde) 2(azul) 3(castanho)"))

    if olhos == 1:
        vd += 1
    elif olhos == 2:
        az += 1
    else:
        cast_olho += 1

    cabelo = int(input(f"Qual a cor dos olhos do habitante {i + 1}? 1(preto) 2(loiro) 3(castanho)"))

    if cabelo == 1:
        preto += 1
    elif cabelo == 2:
        loiro += 1
    else:
        cast_cabelo += 1

    idade = int(input(f"Qual a idade do habitante {i + 1}? "))
    if sexo == 2 and olhos == 1 and cabelo == 2 and idade >= 18 and idade <= 35:
        porcent += 1
    ma = ma if ma != None and ma > idade else idade

print(f"O habitante mais velho tem {ma} anos")
b = (porcent * 100) / abt
print(
    f"A porcentagem de indivíduos do sexo feminino com idade de 18 a 35 anos que tenham olhos verdes e cabelos louros é {b}%")

# 19 - Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

n1 = int(input("Infome primeira nota "))
n2 = int(input("Infome segunda nota "))
n3 = int(input("Infome terceira nota"))
n4 = int(input("Infome quarta  nota"))

notas =[n1,n2,n3,n4]
print(notas)

mediaf = (n1+n2+n3+n4)/4
print("A média final é",mediaf)


def maior(n1,n2,n3,n4):
   max = n1

 if n2 > max:
     max = n2
     if n3 > max:        max = n3
     if n4 > max:
     max = n4
     return max

print("Maior: ", maior(n1,n1,n3,n4))

# #21- Desenvolva um programa que altere em tempo de execução a palavra Java pela palavra Python na frase Exercícios de Java
 texto = " Execícios de java"
 texto = texto.replace("java", "Python")
 print(texto)


# #22- Faça um programa que leia um String e a imprima com todos os caracteres em MAIÚSCULO.
text =" Execícios de Python"
 print(text)
#text = text.upper()

# 23 - Faça um programa para ler uma string e contar quantas vezes um determinado caractere aparece na string. O caractere Deverá ser informado pelo usuário.
 frase = "Execícios de Python"
print(frase.count("s"))

#24
def cumsum (soma):
    soma = []
#25

#26  escreva uma função chamada is_sorted
questãovintesete = []
for g in range(5):
    questãovintesete.append(input("Informe um item da lista" + str(g + 1) + ':'))
def is_sorted (questãovintesete):
 questãovintesete = []
 for g in range(5):
    questãovintesete.append(input("Informe um item da lista"+ str(g+1) +':'))
 if is_sorted(questãovintesete) == sorted(questãovintesete):
    print("Verdadeiro")
 else:
      print("Falso")


#29 Crie um programa que leia 5 números inteiros e os armazene em uma lista
listaNumeros = []
print ('Informe um numero')
for i in range(5):
    listaNumeros.append(input('Numero '+ str(i+1) +':'))
print (sorted(listaNumeros))

#30Faça um programa que coloque em ordem 5 números quaisquer de uma lista.
questãotrintaum = []

print("informe 5 numeros")
for i in range(5):
    questãotrintaum.append(input('Numeros'+ str(i+1) +':'))
print(sorted(questãotrintaum))
#31

