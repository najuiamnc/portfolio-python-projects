import random

vitorias_usuario = 0
vitorias_computador = 0

opcoes = ["pedra", "papel", "tesoura"]

print("--- BEM-VINDO AO PEDRA, PAPEL E TESOURA ---")

while True:
    usuario_escolha = input("\nEscolha Pedra, Papel, Tesoura ou 'Q' para sair: ").lower()
    
    if usuario_escolha == "q":
        break # Só sai do jogo se você digitar Q

    if usuario_escolha not in opcoes:
        print("Opção inválida! Escreva Pedra, Papel ou Tesoura.")
        continue

    numero_aleatorio = random.randint(0, 2)
    computador_escolha = opcoes[numero_aleatorio]
    
    print(f"O computador escolheu: {computador_escolha}.")

    if usuario_escolha == "pedra" and computador_escolha == "tesoura":
        print("Você venceu! 🎉")
        vitorias_usuario += 1
    elif usuario_escolha == "papel" and computador_escolha == "pedra":
        print("Você venceu! 🎉")
        vitorias_usuario += 1
    elif usuario_escolha == "tesoura" and computador_escolha == "papel":
        print("Você venceu! 🎉")
        vitorias_usuario += 1
    elif usuario_escolha == computador_escolha:
        print("Empate! 🤝")
    else:
        print("Você perdeu! 💀")
        vitorias_computador += 1
    
    # O jogo volta para o início do 'while' automaticamente aqui

# --- FINAL DO SCRIPT (FORA DO WHILE) ---
# Essas linhas abaixo só rodam quando você digita 'Q'
print("-" * 30)
print(f"PLACAR FINAL -> Você: {vitorias_usuario} | Computador: {vitorias_computador}")
print("Obrigado por jogar!")

input("\nO jogo acabou. Pressione ENTER para fechar a janela...")