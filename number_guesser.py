import random

# Título do jogo
print("--- BEM-VINDO AO ADIVINHE O NÚMERO ---")

numero_teto = input("Digite o número limite para o jogo (ex: 10, 50, 100): ")

if numero_teto.isdigit():
    numero_teto = int(numero_teto)

    if numero_teto <= 0:
        print('Por favor, digite um número maior que 0 na próxima vez.')
        quit()
else:
    print('Por favor, digite um número válido.')
    quit()

# O randint garante que o número limite que você digitou TAMBÉM possa ser o sorteado
numero_aleatorio = random.randint(0, numero_teto)
tentativas = 0

while True:
    tentativas += 1
    palpite_usuario = input("Qual o seu palpite? ")
    
    if palpite_usuario.isdigit():
        palpite_usuario = int(palpite_usuario)
    else:
        print('Isso não é um número! Tente digitar um algarismo.')
        continue

    if palpite_usuario == numero_aleatorio:
        print("🎉 PARABÉNS! Você acertou!")
        break
    elif palpite_usuario > numero_aleatorio:
        print("Você chutou ACIMA do número secreto.")
    else:
        print("Você chutou ABAIXO do número secreto.")

print(f"Você precisou de {tentativas} tentativas para vencer!")