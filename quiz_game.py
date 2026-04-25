print("--- BEM-VINDO AO QUIZ DE TECNOLOGIA ---")

jogar = input("Você quer iniciar o jogo? (sim/nao): ").lower()

if jogar != "sim":
    print("Fica para a próxima! Tchau.")
    quit()

print("Ótimo! Vamos começar...")
pontuacao = 0

# Pergunta 1
resposta = input("\n1. O que significa a sigla CPU? ").lower()
if resposta == "unidade central de processamento" or resposta == "central processing unit":
    print("Correto! ✅")
    pontuacao += 1
else:
    print("Incorreto! ❌")

# Pergunta 2
resposta = input("2. O que significa a sigla RAM? ").lower()
if resposta == "memoria de acesso aleatorio" or resposta == "random access memory":
    print("Correto! ✅")
    pontuacao += 1
else:
    print("Incorreto! ❌")

# Pergunta 3
resposta = input("3. Qual a linguagem de programação que usa a logo de uma cobra? ").lower()
if resposta == "python":
    print("Correto! ✅")
    pontuacao += 1
else:
    print("Incorreto! ❌")

print(f"\nFim do Quiz! Você acertou {pontuacao} perguntas.")
print(f"Sua porcentagem de acerto foi de {(pontuacao / 3) * 100:.2f}%.")

input("\nO jogo acabou. Pressione ENTER para sair...")