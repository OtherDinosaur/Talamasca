

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



        
        "Se levantar":

            nar "Ali está, meu \"anfitrião\"..."



    l "Parece que a transição funcionou"

    show sr lobo at halfsize
    with dissolve1

    l "Genial"