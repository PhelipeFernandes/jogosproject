def jogar():

    print('********************************')
    print('***Bem vindo ao jogo de forca***')
    print('********************************')

    enforcou = False
    acertou = False

    palavra_secreta = "catapimbas"
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_"]
    while(not enforcou and not acertou):

         chute = input("Qual letra? ")
         chute = chute.strip()
         index = 0
         for letra in palavra_secreta:
             if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
             index = index + 1

    print("Jogando...")

if(__name__=="__main__"):
    jogar()