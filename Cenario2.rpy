

label Cenario2:

    play music "transient.mp3" fadein 5.0
    scene quarto
    with fade1

    nar "Essa noite foi muito longa e tensa..."

    menu:
        nar "Ele tá ali! Acho que não percebeu que eu acordei."

        "Fingir dormir por mais um tempo":

            nar "Isso é só um sonho ruim, eu vou acordar daqui a pouco."

            "{i}Passos se aproximam de você.{/i}"

            stop music fadeout 2.0

            "{i}Um travesseiro aparece em seu rosto.{/i}"
            
            play sound "coration.mp3"
            scene black
            with fade1
            play sound "suspense.mp3"

            "{i}Você escuta entre seus gritos abafados.{/i}"

            l "É rude deixar seu anfitrião tanto tempo lhe esperando."

            l "Não tente me fazer de bobo novamente"

            "{i}A escuridão está perto...{/i}"

            $ stress = stress-2

            scene quarto
            with Fade(0.2, 0.0, 0.8, color='#ffffff')

            "{i} O travesseiro saiu da sua cara, no último momento.{/i}"

            show sr lobo at halfsize
            with dissolve

            play music "transient.mp3" fadein 2.0

        
        "Se levantar":

            nar "Ali está, meu \"anfitrião\"..."

            show sr lobo at halfsize
            with dissolve

            nar "Minha cabeça e minhas costas doem."

            nar "É como se eu estivesse de pé a noite toda."

            nar "Vamos ver qual será meu destino hoje"

    
    l "Limpe-se, vista-se e venha comer."

    l "Teremos um evento hoje, um importante compromisso."

    l "Passarei mais detalhes depois."

    scene room
    with fade1
    
    show sr lobo at halfsize
    with dissolve

    l """Hoje nós vamos para uma festa do chá com meus Confrades,

    por favor não me desaponte e não me envergonhe na frente deles."""

    $ primeira = True

    label regras:
        
        l """Tenha educação.

        Você terá que se comportar à mesa, não falar a não ser que seja pedido,

        e especialmente,{w} não fale com o Senhor Bode.

        Tenha em mente sempre a obediência a mim, e esteja com a higiene e a vestimenta impecáveis.

        Não fale com os outros acompanhantes, mesmo que eles queiram falar com você.

        Não tente nehuma estupidez.{w} Lembre-se:

        {b}Estarei de olho em você o tempo todo.{/b}"""

        nar "Parece que ele tem receio de que as coisas saiam errado nessa festa do chá"

        sn "Por que esse evento é tão importante?"

        l "Será um momento de interagir com velhos amigos, e aproveitar um bom chá."

        l "Espero que se comporte."

        jump men

        label men:
            menu:
            
                
                l "Você entendeu as regras, ou preciso repeti-las?"


                "Eu entendi":

                    nar "Mas não gostei..."
                    
            

                "Não entendi, poderia repetir?":

                    if primeira:
                        $ primeira = False

                        l "Não me faça repetir mais uma vez."

                        jump regras
                    else:
                        stop music fadeout 1.0
                        pause 2.0

                        l "Acho que eu deveria tirar uma de suas orelhas, já que não está usando elas"

                        play sound "rack.mp3"
                        play sound "slash.mp3"
                        with fade3
                        pause 2.0
                        play music "transient.mp3" fadein 5.0
                        $ stress = stress-2

                        l "Agora se limpe novamente, e não suje mais minha casa."
                        
    
    pause 2.0

    l """Termine de comer e se prepare para aprender a se portar à mesa.

    Atitudes errôneas podem incomodar a todos.

    Não se sirva antes do anfitrião.

    Use a faca apenas para cortar carnes duras.{p} Outros pratos devem ser cortados com o garfo.

    Mastigue com a boca fechada.{w} Não faça barulho.

    Vai ser o suficiente por agora.

    Vamos nos preparar para a festa do chá."""

    hide sr lobo
    with fade
    
    nar "Ele está muito preocupado com algo"

    nar "Talvez eu possa encontrar algo de útil nesse evento"

    nar "Quero minha liberdade de volta...{w} Soa até como crime agora."

    play sound "porta.mp3"
    show sr lobo at halfsize
    with dissolve

    l "Tudo pronto. Vamos agora mesmo."

    hide sr lobo
    with fade

    nar "Não tenho condições de estar em uma festa, nem em uma fuga."

    nar "E eu sei que um erro pode custar minha vida."

    jump Cenario3







    















    l "Parece que a transição funcionou"

    show sr lobo at halfsize
    with dissolve1

    l "Genial"