define flash = Fade(0.05, 0.1, 0.3, color="#ffffff")
define slow_dissolve = Dissolve(2.0)
define quick_flash = Fade(0.03, 0.05, 0.2, color="#ffffff")

label cena_final_aceitacao:

    scene Quarto2
    with fade

    pause 2.0

    "{cps=40}As memórias finalmente voltam.{/cps}"

    pause 1.0

    "{cps=40}Uma após a outra.{/cps}"

    pause 1.0

    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    show maekioku
    with flash

    pause 0.2

    hide maekioku

    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    show harutachi
    with flash

    pause 0.2

    hide harutachi
    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    show hospital
    with flash

    pause 0.2

    hide hospital
    scene Quarto2
    with fade

    stop sound

    pause 2.0

    "{cps=40}A voz de Haru.{/cps}"

    pause 0.8

    "{cps=40}O som da chuva.{/cps}"

    pause 0.8

    "{cps=40}A queda.{/cps}"

    pause 1.5

    k triste "{cps=18}...{/cps}"

    pause 2.0

    k triste "{cps=18}Então foi isso...{/cps}"

    pause 1.5

    k triste "{cps=18}Eu realmente...{/cps}"

    pause 2.0

    k triste "{cps=18}Lembrei.{/cps}"

    pause 3.0

    "{cps=40}Durante dez anos, Kioku acreditou que esquecer era seguir em frente.{/cps}"

    pause 1.0

    "{cps=40}Mas algumas memórias não desaparecem.{/cps}"

    pause 1.0

    "{cps=40}Elas apenas esperam.{/cps}"

    pause 2.0

    scene cemiterio
    with fade

    pause 3.0

    k triste "{cps=18}Oi, Haru...{/cps}"

    pause 1.5

    window hide

    pause 1.0

    show screen final_text_screen

    pause 6.0

    hide screen final_text_screen
    with dissolve

    pause 2.0

    scene black
    with slow_dissolve

    pause 3.0

    return