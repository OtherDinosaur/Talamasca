# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e5 = Character("Eileen", what_outlines=[( 1, "#008000", 0, 0 )] )

e5 "The what_outlines property puts an outline around the text."

e5 "It's a little complicated since it takes a list with a tuple in it, with the tuple being four things in parenthesis, and the list the square brackets around them."

e5 "The first number is the size of the outline, in pixels. That's followed by a string giving the hex-code of the color of the outline, and the x and y offsets."
 

define l = Character("Sr. Lobo", who_color="#000000ff",who_outlines=[( 1, "#ffffff", 0, 0 )],what_color="#000000ff")
define sn = Character("Você",who_color="#ffffffff",who_outlines=[( 1, "#000000", 0, 0 )],what_color="#000000ff",what_outlines=[( 0, "#808080", 2, 2 )])
define nar = Character("Você",kind=sn,what_italic=True)
define nvll = Character(what_italic=True, what_layout='subtitle', kind=nvl)

transform halfsize:
    zoom 0.6
    xalign 0.5
    yalign 1.0

define dissolve1 = Dissolve(3.0)
define fade1 = Fade(1.5, 0.5, 1.0)
define fade2 = Fade(0.5, 0.2, 0.5, color="#cdf00aff")
define fade3 = Fade(0.2, 0.0, 0.8, color='#f70f0f')

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

    nar "..."

    sn "Olá?"

    scene room with fade1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    sn "Tem alguém aí?"

    menu:
        "Gritar":
            sn "Socorrooooo!!!"

    "..."

    menu:
        "Gritar novamente":
            sn "Alguém aí tá me ouvindo? Eu não consido sair!"

    "..."

    menu:
        "Gritar mais uma vez":
            sn "ALGUÉM ME AJUDAAAAAA!!"

    

    show sr lobo at halfsize 
    with dissolve1
    play music "Childishly_fresh_eyes.mp3" fadein 5.0
    $ renpy.music.set_volume(0.3, channel='music')


    # These display lines of dialogue.

    sn "O que tá acontecendo? Quem é você?"

    sn "Como eu vim parar aqui?"

    sn "Por favor, me ajuda!"

    nar "{cps=1}...{/cps}"

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
            with fade3
 
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
    


    # Define the set to track clicks
    default escolhida = set()

    label quarto:
        scene quarto
        with fade1

        # Optional: Logic to play narration only once
        if len(escolhida) == 0:
            nar "Posso explorar o ambiente..."

    # --- THE MAIN LOOP ---
    label quarto_loop:
        # This calls the screen and waits for the player to click
        call screen quarto_point_and_click


    # --- OBJECT LOGIC BELOW ---

    label quarto_janela:
        nar "Tem uma janela ali..."
        
        menu:
            "Pular":
                stop music fadeout 2.0
                nar "Essa é minha chance, qualquer lugar é melhor que aqui"
                
                play sound "rack.mp3"
                play sound "slash.mp3"
                with fade3
                pause 2.0
                
                sn "AAAAAAAAARRRHHHHGGG!!"
                sn "Uma armadilha de urso!"

                show sr lobo at halfsize with dissolve
                l "Lamentável."
                l "Você falhou no teste mais ridículo."
                hide sr lobo with dissolve1

                play music "Childishly_fresh_eyes.mp3" fadein 5.0
                scene black with fade1

                nvll """Você não possui valor algum.


                O lobo achará outra presa,


                alguém mais digno.


                O culto continuará sem você.


                Mais sequestros, mais mortes, mais impunidade.


                Você poderia ter mudado isso,


                mas não fez as escolhas certas."""

                jump end_credits

            "Não arriscar":
                $ escolhida.add("Janela")
                # We return to the click loop
                jump quarto_loop


    label quarto_porta:
        nar "Trancada. Que surpresa."
        $ escolhida.add("Porta")
        jump quarto_loop


    label quarto_quadro:
        stop music fadeout 2.0
        nar "Que figura psicodélica curiosa..."
        play sound "creepy.mp3"
        nar "..."
        nar "Tá, não tô me sentindo bem... É melhor parar."
        
        play music "Childishly_fresh_eyes.mp3" fadein 5.0
        $ stress = stress-1
        $ escolhida.add("Quadro")
        jump quarto_loop


    label quarto_caixas:
        play sound "caindo.mp3"
        pause 2.0
        nar "Esse barulho todo, só por roupas de cama velhas e ensanguentadas."
        stop music fadeout 0.5

        show sr lobo at halfsize with dissolve1
        l "Eu disse{p} Nada{w} de{w} barulho!!"

        with vpunch
        play sound "punch.mp3"
        with fade3

        $ stress = stress-2
        play music "Childishly_fresh_eyes.mp3" fadein 5.0

        l "Este é meu último aviso."
        l "Não serei tão educado da próxima vez."
        hide sr lobo with dissolve

        # We add this to 'escolhida' so the button disappears in the screen logic
        $ escolhida.add("Caixas") 
        jump quarto_loop


    label quarto_cama:
        nar "Acho que só me resta dormir mesmo."
        jump Cenario2
        return





    # This ends the game.

    label end_credits:

    scene black
    with fade1
    play music "ending.mp3" fadeout 3.0
    show screen credits
    pause 60  # Adjust duration as needed
    hide screen credits
    return

screen credits:
    frame at credits_scroll(65.0):
        background None
        xalign 0.5
        vbox:
            label "Arte" xalign 0.5
            null height 50
            text "Alby_kun"
            null height 50
            label "Programação" xalign 0.5
            null height 50
            text "doriandayvid"
            null height 20
            text "Daniloxls"
            null height 20
            text "Pedro Guilerme"
            null height 50
            label "Roteiro e Narrativa" xalign 0.5
            null height 50
            text "Enola"
            null height 20
            text "doriandayvid"
            null height 150
           

transform credits_scroll(speed):
    ypos 1000
    linear speed ypos -2600


screen quarto_point_and_click():
    modal True 

    # 1. WINDOW BUTTON
    imagebutton:
        idle "janela_idle.png"    # Your image for the window
        hover "janela_hover.png"  # Image when mouse is over it (optional)
        xpos 0 ypos 0         # CHANGE THESE COORDINATES
        focus_mask True           # Ignores transparent parts of the image
        action Jump("quarto_janela")

    

    # 3. PAINTING BUTTON
    imagebutton:
        idle "quadro_idle.png"
        hover "quadro_hover.png"
        xpos 0 ypos 0
        focus_mask True
        action Jump("quarto_quadro")

    # 4. BOXES BUTTON
    # We use 'if' so the button disappears after the boxes fall!
    if "Caixas" not in escolhida:
        imagebutton:
            idle "caixas_idle.png"
            hover "caixas_hover.png"
            xpos 0 ypos 0
            focus_mask True
            action Jump("quarto_caixas")

    # 2. DOOR BUTTON
    imagebutton:
        idle "porta_idle.png"
        hover "porta_hover.png"
        xpos 0 ypos 0
        focus_mask True
        action Jump("quarto_porta")

    # 5. BED BUTTON (To finish the scene)
    imagebutton:
        idle "cama_idle.png"
        hover "cama_hover.png"
        xpos 0 ypos 0
        focus_mask True
        action Jump("quarto_cama")