# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Sr. Lobo", who_color="#000000ff")
define sn = Character("Você")
define nar = Character("você", what_italic=True)

transform halfsize:
    zoom 0.6
    xalign 0.5
    yalign 1.0

define dissolve1 = Dissolve(3.0)
define fade1 = Fade(1.5, 0.5, 1.0)
define fade2 = Fade(0.5, 0.2, 0.5, color="#cdf00aff")

screen stress():
    frame:
        xalign 0.0 
        yalign 0.0
        hbox:
            text "Stress: [stress]"
 

# The game starts here.

label start:

    hide quick_menu
    $ stress = 10
    show screen stress()
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "..."

    "Olá?"

    scene room with fade1

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
    play music "Childishly_fresh_eyes.mp3" fadein 5.0


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

    l """Ótimo.

    Eu sou o Senhor Lobo, e esta é minha casa.

    Você ficará bem, contanto que não faça algo deselegante.

    Para facilitar, deixarei algumas coisas claras:

    {b}Nunca{/b} entre no meu quarto.

    Não tente ir embora antes que eu permita.

    Não faça barulho.{w} Não fale com outras pessoas.

    Limpeza é essencial,{w} assim como a obediência.

    Se seguir essas regrinhas, nossa convivência será agradável."""

    sn "{i}A tensão é muito alta, não consigo responder nada{/i}"

    l "Vamos jantar."

    l "Hoje o jantar será especial em sua honra."
    
    menu:
        l "Escolha o que gostaria de desfrutar."

        "Sopa":
            l "Então venha comigo.{w=2}"

            pause 2.0
            
            nar "Não acredito que estou aproveitando esse jantar"

            nar "Só sei que o pânico não me deixa pensar direito"
        
        "Filé":
            l "Então venha comigo.{w=2}"

            pause 2.0

            nar "Que carne dura, e que gosto estranho..."

            l "Fico feliz que tenha gostado da carne,"

            stop music fadeout 2.0
            
            l "ao menos um bom uso para aquele imprestável que tentou sair sem permissão."

            play sound "creep.mp3"
            with Fade(0.2, 0.0, 0.8, color='#f70f0f')
 
            $ stress = stress-2

            nar "Eu acho que vou no banheiro vomitar"
            
            with fade2
            play sound "estomago.mp3"

            l "Parece que ele ainda tenta fugir de seu dever. Deprimente."

            play music "Childishly_fresh_eyes.mp3" fadein 5.0

            l "Espero que você não me dê tanta dor de cabeça assim."

        "Salada":
            l "Então venha comigo."

            pause 2.0

            nar "Parece uma salada normal e decente."

            nar "Mas a cada garfada fica mais amarga e azeda."

            nar "Deve ser o gosto que tem o cativeiro."


    l "Vou lhe mostrar seus aposentos agora."

    l "Espero que estejam de seu agrado."

    nar "Parece que não há outra escolha."

    l "Lembre-se do que eu falei anteriormente."

    l "Não{w} me decepcione."

    hide sr lobo
    with dissolve

    scene quarto
    with fade1
    jump quarto


    default escolhida = set()
    
   
    label quarto:
        
        
    
        menu:
            set escolhida
            nar "Posso explorar o ambiente..."
            
            "Janela":
                menu:
                    nar "Tem uma janela ali..."
                    
                    "Pular":
                        nar "Essa é minha chance, qualquer lugar é melhor que aqui"

                        sn "AAAAAAAAARRRHHHHGGG!!"

                        sn "Uma armadilha de urso!"

                        show sr lobo at halfsize
                        with dissolve

                        l "Lamentável."

                        l "Você falhou no teste mais ridículo."

                        hide sr lobo

                        return

                    "Não arriscar":
                        $ escolhida.add("Janela")
                        jump quarto
            
            "Porta":

                nar "Trancada. Que surpresa."
                $ escolhida.add("Porta")
                jump quarto

            "Quadro":

                nar "Que figura psicodélica curiosa..."

                nar "..."

                nar "Tá, não tô me sentindo bem... É melhor parar."
                $ stress = stress-1

                $ escolhida.add("Quadro")
                jump quarto
            
            "Caixas acima do guarda-roupa":

                play sound "caindo.mp3"

                pause 2.0

                nar "Esse barulho todo, só por roupas de cama velhas e ensanguentadas."

                show sr lobo at halfsize
                with dissolve1

                l "Eu disse{p} Nada{w} de{w} barulho!!"

                with vpunch
                play sound "punch.mp3"
                with Fade(0.2, 0.0, 0.8, color='#f70f0f')

                $ stress = stress-2

                l "Este é meu último aviso."

                l "Não serei tão educado da próxima vez."

                hide sr lobo
                with dissolve

                $ escolhida.add("Caixas acima do guarda-roupa")
                jump quarto

            "cama":

                nar "Acho que só me resta dormir mesmo."


          
      



    jump Cenario2





    # This ends the game.

    return
