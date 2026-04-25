nome = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome}, a esta aventura!")

# Usamos .lower() em todos os inputs para o jogo não quebrar se o usuário usar letras maiúsculas
resposta = input("Você está em uma estrada de terra, ela chegou ao fim e você pode ir para a ESQUERDA ou DIREITA. Para onde você gostaria de ir? ").lower()

if resposta == "esquerda":
    resposta = input("Você chegou a um rio. Você pode caminhar ao redor dele ou atravessar nadando? (digite CAMINHAR ou NADAR): ").lower()

    if resposta == "nadar":
        print("Você tentou atravessar nadando, mas foi pego por um jacaré faminto. Você perdeu!")
    elif resposta == "caminhar":
        print("Você caminhou por muitos quilômetros, a água acabou e você não resistiu ao calor. Você perdeu!")
    else:
        print("Opção inválida. Você tropeçou e perdeu!")

elif resposta == "direita":
    resposta = input("Você chegou a uma ponte que parece bem bamba. Você quer ATRAVESSAR ou VOLTAR? ").lower()

    if resposta == "voltar":
        print("Você decidiu voltar para a segurança, mas a aventura acabou ali. Você perdeu!")
    elif resposta == "atravessar":
        resposta = input("Você atravessou a ponte com cuidado e encontrou um estranho. Você quer FALAR com ele? (sim/nao): ").lower()

        if resposta == "sim":
            print("O estranho era, na verdade, um mago bondoso! Ele te presenteou com um baú de OURO. Você VENCEU!")
        elif resposta == "nao":
            print("Você ignorou o estranho. Ele se sentiu ofendido e te transformou em uma estátua de pedra. Você perdeu!")
        else:
            print("Opção inválida. Você perdeu!")
    else:
        print("Opção inválida. Você perdeu!")

else:
        print("Opção inválida. O caminho se fechou e você perdeu!")

# DAQUI PARA BAIXO: TUDO NO CANTO ESQUERDO
print(f"\nObrigado por jogar, {nome}!")

input("\nO jogo acabou. Pressione ENTER para sair...")
