# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Sr. Lobo", ) #window_background= , who_color= , 
define sn = Character("Você")

transform halfsize:
    zoom 0.6
    xalign 0.5
    yalign 1.0

define dissolve1 = Dissolve(3.0)
define fade1 = Fade(1.5, 0.5, 1.0)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "..."

    "Olá?"

    scene bg room with fade1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Tem alguém aí?"

    menu:
        "Gritar":
            "Socorrooooo!!!"

    "..."

    menu:
        "Gritar novamente":
            "Alguém aí tá me ouvindo? Eu não consido sair!"

    "..."

    menu:
        "Gritar mais uma vez":
            "ALGUÉM ME AJUDAAAAAA!!"

    

    show sr lobo at halfsize 
    with fade1
        


    # These display lines of dialogue.

    "O que tá acontecendo? Quem é você?"

    "Como eu vim parar aqui?"

    "Por favor, me ajuda!"

    "{cps=1}...{/cps}"

    l "Pobre alma perdida."

    l "Não se apavore mais, não há com o que se preocupar."

    l "Você está no lugar certo agora."

    sn "O que você ...{nw}"

    play sound "lobo.mp3"

    l "{cps=95}Não me interrompa!{/cps}"

    l "Não gosto quando me interrompem"

    l "E também não fique gritando. Odeio visitas mal educadas"

    l "Você entende, não é?"

    sn "..."

    l "Eu lhe fiz uma {b}PERGUNTA{/b}."

    sn "E-eu entendo."

    l "Ótimo."

    l "Eu sou o Senhor Lobo, e esta é minha casa."

    l "Você ficará bem, contanto que não faça algo deselegante."

    l "Para facilitar, deixarei algumas coisas claras:"

    l "{b}Nunca{/b} entre no meu quarto."

    l "Não tente ir embora antes que eu permita."

    l "Não faça barulho.{w} Não fale com outras pessoas."

    l "Limpeza é essencial,{w} assim como a obediência."

    l "Se seguir essas regrinhas, nossa convivência será agradável"





    
    
    
    
    
    
    
    
    
    # hide sr lobo


    # jump Cenario2





    # This ends the game.

    return
