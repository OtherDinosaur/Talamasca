# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Sr. Lobo", ) #window_background= , who_color= , 
define sn = Character("Você")

transform halfsize:
    zoom 0.55
    xalign 0.5

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
    with dissolve1
        


    # These display lines of dialogue.

    "O que tá acontecendo? Quem é você?"

    l "Pobre alma perdida."

    l "Não se apavore mais, não há com o que se preocupar."

    l "Você está no lugar certo agora."





    # This ends the game.

    return
