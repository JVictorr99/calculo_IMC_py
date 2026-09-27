    # queria usar apenas a função do sleep 

from time import sleep   
print("="*60)

    # queria definir a função sleep sem precisar chamar toda vez
def imprimir (texto, tempo = 2):
    print(texto)
    sleep(tempo)
    
imprimir("Óla bem-vindo!")
print("="*60)
nome = input("Como devo te chamar? ")
nome = "\033[1;32m" + nome + "\033[0m" # transformei a variavel em cor para o terminal
imprimir(f"Prazer em te conhecer {nome}!")

print("="*60)
imprimir("Vamos começar a calcula seu IMC irrei precisar de algumas informações; ")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


if peso <= 0 or altura <= 0:    # Aqui eu estou verificando se o usuario digitou 0 na altura ou peso evitando algum erro
    print("Peso ou altura inválidos!")
    
elif peso > 300:                # Segunda segurança Evitar que o digita o peso alem do considerado Normal
    print("valor do peso Inválido")
else:
    if altura > 3:
        altura = altura / 100      # terceira segurança evitar que usuario digite sua altura sem usar , ou . ( exemplo 171 )
    
    imc = peso / (altura * altura)
   
    if imc < 18.5:              # Aqui denpendendo do calculo feito o prrograma iria guarda a variavel resultado
        resultado = "Abaixo do peso!"
    elif  18.5 < imc <= 24.90:
        resultado = "Peso Normal!"
    elif 25.0 <= imc <= 29.90:
        resultado = "Sobre peso!"
    elif 30.0 <= imc < 34.90:
        resultado = "Obesidade grau 1!"
    elif  35.0 <= imc <= 39.90:
        resultado = "Obessidade grau 2!"
    elif 40.0 <= imc <= 70:
        resultado = "Obessidade grau 3! Alto risco de morte."

resultado = "\033[1;32m" + resultado + "\033[0m"

imprimir(f"{nome} seu Resultado Deu {resultado} Valor do seu IMC \033[1;32m{imc:.2f}\033[0m")    
print("="*60)
    
print("Fim do algoritimo!")