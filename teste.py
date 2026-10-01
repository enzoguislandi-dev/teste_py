print("Olá, bem vindo ao Next!")
nome = input("Digite seu nome?: ")

if nome == "Guilherme Reiche":
    print("Olá, bem vindo ao next, vc é da Tríplice ne?")
    resposta = input("Você é da Tríplice?: ")
    if resposta in ("sim", "SIM", "s", "Sim", "ss", "yes", "sou sim"):
        print("VAMOOOOOOOOOOOOO, RUMO AO NEXT!")
    elif resposta in ("não", "nao", "nn", "not", "no", "n"):
        print("Oxi tá maluco porra? então sai daí impostor do caralho, Reiche JAMAIS falaria isso")
elif nome == "Enzo Guislandi":
    print("Bem vindo ao Next, boss! E boa sorte!")
else:
    print(f"Olá {nome}, seu usuário não foi encontrado aqui no next! ACESSO NEGADO, DA 1CCPG só se for da TRÍPLICE!!!")