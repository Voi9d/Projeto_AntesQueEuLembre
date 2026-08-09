label Capítulo_1:
    jump dia2
    stop music fadeout 1.0
    play music "audio/Musicas/frozen_winter.mp3" fadein 1.0
    
    scene Ato1
    with dissolve

    # These display lines of dialogue.



    "Voz Feminina" "{cps=40}\"Eai Kioku, você quer?{/cps}\""
    "Kioku Aida" "{cps=40}\"Ah... Não sei, não sei se quero...{/cps}\""
    "Voz Feminina" "{cps=40}\"Vamos, você precisa espairecer a cabeça depois de tudo, vai estar todo mundo, vai ser divertido...{/cps}\""
    "Kioku Aida" "{cps=40}\"Hmm...... Tá bom, acho que vou...{/cps}\""
    "Voz Feminina" "{cps=40}\"Ah que bom, vai ser divertido, eu prometo...{/cps}\""
    $ unlock_achievement('first_ach')
    pause 1.0
    k "{cps=40}{i}Mesmo passando tanto tempo, eu as vezes penso sobre...{/i}{/cps}"
    
    # Diminui o volume da música para 30% quando o alarme tocar
    $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
    play sound "audio/SoundsEffects/alarme.mp3" fadein 0.5
    pause 0.25

    scene Quarto1
    with pixellate


    
    # Restaura o volume da música para 100%
        
    
    pause 1.0

    stop sound fadeout 0.25
    
    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')

    k normal "{cps=40}\"Que saco esse despertador, eu tenho que desativar ele se quiser dormir mais.\"{/cps}"

    play audio "SoundsEffects/celularvibrando.mp3"
    pause 1.0
    

    k normal "{cps=40}\"Quem ta me ligando as 8 da manhã....\"{/cps}"
    stop audio fadeout 0.5
    k normal "{cps=40}\"Porque a Jinsei ta me ligando essa hora, meu deus do céu.\"{/cps}"
    k normal "{cps=20}\"Oi Jinsei c{nw}"
    pause 0.5
    j sorisso "{cps=40}\"Boooooooom diaaaaaaaa Kioku...\"{/cps}"
    j encantadaf "{cps=40}\"Como você tá Kiokuzinho? Dormiu bem?\"{/cps}"
    $ desbloquear_Personagem("jinsei")

    menu:
        "O mesmo de sempre sabe como é":
            jump omesmodesempre
        "To bem, fui acordado pelo despertador de novo":
            jump acordadodespertador
        "Ficar em Silêncio":
            jump silencio

label omesmodesempre:

    k normal "{cps=40}\"Ah... sabe como é, o mesmo de sempre...{/cps}\""
    j sorisso "{cps=40}\"Ah me conta mais vai, se parece que acordou meio mal.{/cps}\""
    jump contar_verdade

label acordadodespertador:

    k normal "{cps=40}\"Ah... To bem, única coisa é que fui acordado pelo despertador.... de novo.\"{/cps}"
    j encantadaf "{cps=40}\"Bom pelo menos alguém consegue te acordar hahahahaha.{/cps}\""
    k divertindo "{cps=40}\"Hahahaha, tem razão, mas sei la, hoje queria dormir mais.{/cps}\""
    j normal "{cps=40}\"Mas, pela sua voz, você parece meio mal.{/cps}\""
    k normal "{cps=40}\"Ah não é nada de mais, não precisa se preocupar com isso.{/cps}\""
    j surpresa "{cps=40}\"Pode confiar em mim Kioku, o que aconteceu?{/cps}\""
    jump contar_verdade

return

label silencio:

    k normal "{cps=40}\"....{/cps}\""
    j choro "{cps=40}\"Sonhou com aquilo de novo né?{/cps}\""
    k triste "{cps=40}\"....{/cps}\""
    k "{cps=40}{i}Aquele silêncio parece ter durado um século, porque sempre que toca nesse assunto é assim.{/i}{/cps}"
    jump contar_verdade

label contar_verdade:
    menu:
        "Contar a verdade":
            $ amizade_add("jinsei", 3)
            k normal "{cps=40}\"Na verdade Jinsei, to meio mal... não sei explicar direito...{/cps}\""
            j choro "{cps=40}\"Ah... quer conversar sobre isso?{/cps}\""
            k normal "{cps=40}\"Não sei se quero falar sobre isso... são coisas complicadas...{/cps}\""
            j choro "{cps=40}\"Tudo bem Kioku, se quiser conversar sobre isso, eu to aqui.{/cps}\""
            k "{cps=40}{i}Eu sinto que a Jinsei é a única pessoa que eu posso confiar hoje em dia, não devo esconder isso a ela, vou contar o que sonhei.{/i}{/cps}"
            k normal "{cps=40}\"Na verdade eu sonhei com aquele garoto de novo... eu de 10 anos atrás...{/cps}\""
            j surpresa "{cps=40}\"Sério? E o que aconteceu?{/cps}\""
            k normal "{cps=40}\"Nada de mais, eu conversando com uma outra pessoa, ela estava me convidando para alguma coisa{/cps}\""
            j surpresa "{cps=40}\"Ah... e você lembra quem era essa pessoa?{/cps}\""
            k normal "{cps=40}\"Não sei, não lembro o rosto dela direito... mas eu lembro que ela tinha uma voz muito suave e animada...{/cps}\""
            k normal "{cps=40}\"E... foi isso, depois eu acordei{/cps}\""
            j sorisso "{cps=40}\"Entendi, bom, pelo menos não foi pesadelo, né?{/cps}\""
            $ show_consequence("Jinsei se lembrará disso", 1.5)
            $ consequência_ativada["jinsei_verdade_sonho"] = True
            j sorisso "{cps=40}\"Ei, mudando de assunto...{/cps}\""

            jump prova

        "Arrumar uma desculpa":
            call rolar_d20_base(dc=12, atributo='labia', titulo="Teste de Lábia: Arrume uma Desculpa")
            $ resultado = _return
            if resultado:
                $ amizade_add("jinsei", -1)
                k normal "{cps=40}\"Ah... é que to meio cansado sabe, ando tendo uns sonhos estranhos...{/cps}\""
                j choro "{cps=40}\"Sonhos estranhos? Que tipo de sonhos?{/cps}\""
                k normal "{cps=40}\"Ah... é melhor nem falar sobre isso...{/cps}\""
                j choro "{cps=40}\"Ah... se quiser conversar sobre isso, eu to aqui.{/cps}\""
                k normal "{cps=40}\"Obrigado Jinsei... mas é melhor eu não falar sobre isso...{/cps}\""
                j sorisso "{cps=40}\"Tudo bem Kioku, se quiser conversar sobre...{/cps}\""
                $ show_consequence("Jinsei se lembrará disso", 1.5)
                $ consequência_ativada["jinsei_mentira_sonho"] = True
                k "{cps=40}{i}Eu não quero envolver a Jinsei nisso, é melhor eu não contar nada pra ela.{/i}{/cps}"
                j sorisso "{cps=40}\"Ei, mudando de assunto...{/cps}\""
                jump prova
            else:
                $ amizade_add("jinsei", -3)
                k normal "{cps=40}\"Ah... é que to meio cansado sabe, mas não é nada de mais.{/cps}\""
                j choro "{cps=40}\"Cansado? Você tem dormido bem?{/cps}\""
                k normal "{cps=40}\"Ah... até que sim, mas é uns sonhos nada a ver sabe?{/cps}\""
                j choro "{cps=40}\"Não sei... mas tudo bem se você diz que não é nada de mais...{/cps}\""
                k normal "{cps=40}\"Obrigado Jinsei... mas é melhor eu não falar sobre isso...{/cps}\""
                j sorisso "{cps=40}\"Tudo bem Kioku, se quiser conversar sobre...{/cps}\""
                $ show_consequence("Jinsei se lembrará disso", 1.5)
                $ consequência_ativada["jinsei_mentira_sonho"] = True
                j sorisso "{cps=40}\"Ei, mudando de assunto...{/cps}\""
                jump prova

return

label prova:
    j sorisso "{cps=40}\"Estudou para prova de hoje?{/cps}\""
    k surpreso "{cps=40}\"Era hoje?{/cps}\""
    j surpresa "{cps=40}\"Sim, era hoje.{/cps}\""
    j seachando "{cps=40}\"Meu deus do céu Kioku...{/cps}\""
    pause 0.5
    k divertindo "{cps=40}\"Você devia ter visto sua cara hahaha.{/cps}\""
    j bravanime "..."
    k superfeliz "{cps=40}\"Aiai, me tirou boas risadas..{/cps}\""
    k feliz "{cps=40}\"Estudei sim Jinsei, pode ficar tranquila.{/cps}\""
    j sorisso "..."
    j encantada "{cps=40}\"Você tem um lindo sorriso, sabia Kioku.{/cps}\""
    k normal "..."
    j bravanime "{cps=40}\"Af... você tava melhor sorrindo Kioku, você tem que sorrir mais.{/cps}\""
    k normal "{cps=40}\"Não sei não, to bem assim do jeito que sou...{/cps}\""
    j sorisso "{cps=40}\"Bem, eu vou tomar um banho, tomar café, e ir pra escola, beijinhos.{/cps}\""
    j encantadaf "{cps=40}\"Não vai se atrasar ein Kioku.{/cps}\""

    k "{cps=40}{i}Graças a Deus eu estudei pra essa prova, última prova desse semestre, depois posso ficar livre da faculdade.{/i}{/cps}"
    k "{cps=40}{i}Ta não vamo enrolar, já é 8:15, o trem chega as 8:40, tenho 15 minutos pra sair de casa.{/i}{/cps}"
    k "{cps=40}{i}Eu posso fazer duas coisas só, e agora o que eu faço velho, me perdi no tempo conversando com a Jinsei.{/i}{/cps}"

    show screen phone_button
    show screen phone_notification
    show screen phone_system

    $ receive_message("Jinsei", "Ei, só pra te lembrar, o professor Yuki não gosta de atrasos, então não se atrasa!!!!!!!", time="08:15")
    $ set_pending_choice("Jinsei", "jinsei_yuki_atraso")

    menu:
        "Escovar os Dentes":
            $ dentesprimeiro = True
            jump escovardente
        "Tomar banho":
            $ banhoprimeiro = True
            jump tomarbanho
        "Tomar café":
            $ tomarcafeprimeiro = True
            jump cafemanha
        "Alimentar o Mingau":
            $ mingaualimentadoprimeiro = True
            jump alimentarmingau

label escovardente:
    $ consequência_ativada["pasta_nova"] = True 
    scene banheiroap
    with pixellate
    k normal "{cps=40}{i}Ok, vou escovar meus dentes rapidinho.{/i}{/cps}"
    k bravo "{cps=40}\"Mas que merda cara, que dificuldade de tirar a pasta velho, ja dobrei toda a bisnaga e nada de sair essa porra.{/cps}\""

    # Inicia o minigame (20 cliques em 5s)
    $ pasta_clicks = 0
    $ pasta_time_left = 5
    call screen minigame_pasta
    if _return:
        k feliz "{cps=40}{i}Finalmente! Consegui tirar a pasta meu deus. Nossa doeu minha mãe fazendo isso, depois da faculdade vou comprar uma pasta nova.{/i}{/cps}"
        scene narrador
        with dissolve
        play audio "audio/escovardente.mp3"
        pause 5.0
        scene banheiroap
        with dissolve
    else:
        k bravo "{cps=40}{i}Que merda... não consegui tirar a pasta. Que saco, assim vou me atrasar, depois escovo os dentes{/i}{/cps}"

    if dentesprimeiro == True:
        if pasta_clicks >= 20:
            k feliz "{cps=40}{i}Agora que escovei meus dentes, eu ainda posso fazer mais uma coisa antes de sair.{/i}{/cps}"
            menu:
                "Tomar banho":
                    $ banhosegundo = True
                    jump tomarbanho
                "Tomar café":
                    $ tomarcafesegundo = True
                    jump cafemanha
                "Alimentar o Mingau":
                    $ mingaualimentadosegundo = True
                    jump alimentarmingau
        else:
            k "{cps=40}{i}Mesmo não tendo escovado os dentes, eu ainda posso fazer mais uma coisa antes de sair.{/i}{/cps}"
            menu:
                "Tomar banho":
                    $ banhosegundo = True 
                    jump tomarbanho
                "Tomar café":
                    $ tomarcafesegundo = True
                    jump cafemanha
                "Alimentar o Mingau":
                    $ mingaualimentadosegundo = True
                    jump alimentarmingau
    elif dentesegundo == True and (banhoprimeiro == True or tomarcafeprimeiro == True or mingaualimentadoprimeiro == True):
        k "{cps=40}{i}Agora sim, estou pronto pra sair de casa.{/i}{/cps}"
        jump sairdecasa

label tomarbanho:
    scene banheiroap
    with pixellate
    k normal "{cps=40}{i}Ok, vou tomar um banho rápido, pra não me atrasar.{/i}{/cps}"
    scene narrador
    with dissolve
    play audio "audio/SoundsEffects/tomarbanho.mp3"
    k feliz "{cps=40}{i}Ahhh... que delícia, água morna... isso é vida.{/i}{/cps}"
    scene banheiroapbanho
    stop audio fadeout 0.5
    with dissolve

    if banhoprimeiro == True:
        k "{cps=40}{i}Agora que tomei banho, eu ainda posso fazer mais uma coisa antes de sair.{/i}{/cps}"
        menu:
            "Escovar os Dentes":
                $ dentesegundo = True
                jump escovardente
            "Tomar café":
                $ tomarcafesegundo = True
                jump cafemanha
            "Alimentar o Mingau":
                $ mingaualimentadosegundo = True
                jump alimentarmingau
    elif banhosegundo == True and (dentesprimeiro == True or tomarcafeprimeiro == True or mingaualimentadoprimeiro == True):
        k "{cps=40}{i}Agora sim, estou pronto pra sair de casa.{/i}{/cps}"
        jump sairdecasa

label cafemanha:
    scene cozinhaap
    with pixellate
    k feliz "{cps=40}{i}Ok, vou tomar um café rápido, pra não me atrasar, cafézin preto com aquele sanduba de pão de forma....{/i}{/cps}"
    k normal "{cps=40}\"Mano.... Cade o pão?{/cps}\""
    call rolar_d20_base(dc=10, atributo='sorte', titulo="Tente a Sorte: Eu comprei Pão?")
    $ resultado = _return
    if resultado:
        k feliz "{cps=40}{i}Ahhh, graças a deus, eu comprei, não vou passar fome.{/i}{/cps}"
    else:
        $ consequência_ativada["esqueceu_pao"] = True
        k bravo "{cps=40}{i}Merda, eu esqueci de comprar pão ontem...{/i}{/cps}"
        k normal "{cps=40}{i}Depois da faculdade eu compro{/i}{/cps}"
    

    if tomarcafeprimeiro == True:
        if resultado:
            k "{cps=40}{i}Agora que tomei meu café, eu ainda posso fazer mais uma coisa antes de sair.{/i}{/cps}"
            menu:
                "Escovar os Dentes":
                    $ dentesegundo = True
                    jump escovardente
                "Tomar banho":
                    $ banhosegundo = True
                    jump tomarbanho
                "Alimentar o Mingau":
                    $ mingaualimentadosegundo = True
                    jump alimentarmingau
        else:
            k "{cps=40}{i}Vou tomar só um café mesmo não preciso do pão.{/i}{/cps}"
            k "{cps=40}{i}Eu ainda posso fazer mais uma coisa antes de sair.{/i}{/cps}"
            menu:
                "Escovar os Dentes":
                    $ dentesegundo = True
                    jump escovardente
                "Tomar banho":
                    $ banhosegundo = True
                    jump tomarbanho
                "Alimentar o Mingau":
                    $ mingaualimentadosegundo = True
                    jump alimentarmingau
    elif tomarcafesegundo == True and (dentesprimeiro == True or banhoprimeiro == True or mingaualimentadoprimeiro == True):
        k "{cps=40}{i}Agora sim, estou pronto pra sair de casa.{/i}{/cps}"
        jump sairdecasa
    



label alimentarmingau:
    scene sala
    with pixellate
    play audio "audio/Mingau/minguauronronando.mp3" 
    show mingaudormindo at center:
        zoom 0.5
    k feliz "{cps=40}{i}O Mingau é tão bonito dormindo, você é a unica coisa que ainda me faz sorrir nesse mundo amigão.{/i}{/cps}"
    k feliz "{cps=40}{i}Vou alimentar você antes de sair, espera aí.{/i}{/cps}"
    stop audio fadeout 0.5
    hide mingaudormindo
    $ unlock_achievement('mingau')
    play audio "audio/Mingau/mingaumiando.mp3" fadeout 0.5
    show minguaufeliz
    with dissolve
    k feliz "{cps=40}\"Bom dia amigão, coloquei sua comida no pote, pode ir comer.{/cps}\""
    k feliz "{cps=40}\"Eu vou sair agora pra ir pra faculdade, mas não se preocupa que eu volto mais tarde.{/cps}\""
    k superfeliz "{cps=40}\"Tenta não fazer bagunça por aí ok?{/cps}\""
    play audio "audio/Mingau/mingauresponde.mp3"
    k feliz "{cps=40}\"Eu te amo mingau, te vejo mais tarde amigão.{/cps}\""
    play audio "audio/Mingau/mingauvaicomer.mp3"
    hide minguaufeliz
    with dissolve

    if mingaualimentadoprimeiro == True:
        k "{cps=40}{i}Okay, agora que alimentei o Mingau, eu ainda posso fazer mais uma coisa antes de sair.{/i}{/cps}"
        menu:
            "Escovar os Dentes":
                $ dentesegundo = True
                jump escovardente
            "Tomar banho":
                $ banhosegundo = True
                jump tomarbanho
            "Tomar café":
                $ tomarcafesegundo = True
                jump cafemanha
    elif mingaualimentadosegundo == True and (dentesprimeiro == True or banhoprimeiro == True or tomarcafeprimeiro == True):
        k "{cps=40}{i}Agora sim, estou pronto pra sair de casa.{/i}{/cps}"
        jump sairdecasa      

label sairdecasa:
    $ cancel_pending_choice("Jinsei", "jinsei_yuki_atraso")
    scene narrador
    with dissolve
    play sound "audio/SoundsEffects/abrindoporta.mp3"
    pause 1.0
    play sound "audio/SoundsEffects/fechandoporta.mp3"
    scene apartamentoexterno
    with pixellate
    k "{cps=40}{i}Finalmente estou fora de casa, agora é só pegar o trem e ir pra faculdade.{/i}{/cps}"
    play audio "audio/SoundsEffects/batendonaporta.mp3"
    pause 1.0
    k "{cps=40}{i}Que barulho é esse?{/cps}{/i}"
    k "{cps=40}{i}Parece que vem lá da lavanderia do prédio...{/i}{/cps}"
    menu:
        "Investigar o barulho":
            jump investigarbarulho
        "Ignorar o barulho e seguir para a estação de trem":
            jump tremestacao


label investigarbarulho:
    $ unlock_achievement('estella')
    $ trematraso = True
    $ consequência_ativada["conhecer_estella"] = True
    $ consequência_ativada["conheceu_estella_apartamento"] = True
    k "{cps=40}{i}Vou ver o que está acontecendo lá na lavanderia.{/i}{/cps}"
    scene escadalavanderia
    with pixellate
    stop music fadeout 1.0
    play music "audio/Musicas/Quandoaencontrei.ogg" fadein 1.0
    $ renpy.music.set_volume(0.5, delay=0.5, channel='music')
    k normal "{cps=40}\"Quem está aí? Precisa de ajuda?{/cps}\""
    show Stella envergonhada
    with dissolve
    "???" "{cps=40}\"Ai meu deus, me ajuda por favor... a porta ta emperrada eu acho...{/cps}\""
    hide Stella envergonhada
    show Stella feliz
    k normal "{cps=40}\"Emperrada?...{/cps}\""
    hide Stella feliz
    show Stella envergonhada
    "???" "{cps=40}\"Sim, eu acho que a maçaneta quebrou... você pode me ajudar?{/cps}\""
    hide Stella envergonhada
    show Stella feliz
    k normal "{cps=40}\"Claro, espera aí que eu vou tentar abrir pra você{/cps}\""
    hide Stella feliz
    scene narrador
    with pixellate
    k normal "{cps=40}{i}Deixa eu tentar abrir esta porta...{/i}{/cps}"
    k surpreso "{cps=40}{i}Calma ai.... essa porta tá trancada.{/cps}{/i}"
    k normal "{cps=40}{i}Será que ela usou a chave que todos tem da lavanderia?{/i}{/cps}"
    k normal "{cps=40}{i}Deixa eu tentar usar a chave...{/i}{/cps}"
    k surpreso "{cps=40}{i}Consegui abrir a porta...{/cps}{/i}"
    k normal "{cps=40}{i}Espera ai, ela não tentou usar a chave?{/i}{/cps}"
    k normal "{cps=40}\"Pronto, a porta está aberta agora.{/cps}\""
    scene escadalavanderia
    with pixellate
    show Stella feliz2
    with dissolve
    "???" "{cps=40}\"Ai meu deus, muito obrigada... eu estava aqui presa a um tempão tentando abrir a porta pra lavar minhas roupas.{/cps}\""
    hide Stella feliz2
    show Stella feliz
    k normal "{cps=40}\"Imagina, que bom que consegui ajudar.{/cps}\""
    k normal "{cps=40}\"Você não recebeu uma dessas chaves quando se mudou pra cá?{/cps}\""
    hide Stella feliz
    show Stella envergonhada
    "???" "{cps=40}\"Ah... eu acho que sim... eu devo ter perdido ela... em algum lugar..... do prédio{/cps}\""
    hide Stella envergonhada
    show Stella feliz
    k feliz "{cps=40}\"Ah sim, entendo, inclusive, muito prazer sou Kioku Aida{/cps}\""
    hide Stella feliz
    show Stella feliz2
    s feliz2 "{cps=40}\"Muito prazer Kioku, eu sou Estella Nascimento, acabei de me mudar pra cá faz pouco tempo{/cps}\""
    $ desbloquear_Personagem("estella")
    hide Stella feliz2
    show Stella feliz
    k feliz "{cps=40}\"Que legal, seja bem vinda ao prédio então{/cps}\""
    hide Stella feliz
    show Stella feliz2
    s feliz2 "{cps=40}\"Obrigada Kioku, eu espero me dar bem com todos aqui{/cps}\""
    menu:
        "Perguntar sobre o nome":
            k normal "{cps=40}\"Estella, que nome bonito... de onde é esse nome?{/cps}\""
            hide Stella feliz2
            show Stella happy1
            s happy1 "{cps=40}\"Ah obrigada Kioku, na verdade é um nome português, meus pais são do Brasil.{/cps}\""
            k feliz "{cps=40}\"Nossa que legal, eu sempre quis conhecer o Brasil.{/cps}\""
            hide Stella happy1
            show Stella happy2
            s happy2 "{cps=40}\"Você deveria mesmo Kioku, é um país lindo, cheio de praias, as comidas de lá são incriveis, as pessoas são gentis...{/cps}\""
            k feliz "{cps=40}\"Quem sabe um dia eu consiga ir lá visitar.{/cps}\""
            hide Stella happy2
            show Stella feliz3
            s feliz3 "{cps=40}\"Com certeza Kioku, quando tu for eu levo você pra conhecer Porto Alegre.{/cps}\""
            hide Stella feliz3
            show Stella feliz
            k divertindo "{cps=40}\"Tudo bem, prometido então haha.{/cps}\""
            hide Stella feliz
            show Stella feliz2
            s feliz2 "{cps=40}\"Você vai adorar o Brasil!!!{/cps}\""
            hide Stella feliz2
            show Stella feliz
            menu:
                "Ajudar a procurar a chave":
                    $ consequência_ativada["ajudar_estella_chave"] = True
                    k normal "{cps=40}\"Você falou que tinha perdido a sua chave né?{/cps}\""
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Sim, eu não faço ideia de onde eu perdi...{/cps}\""
                    hide Stella feliz2
                    show Stella feliz
                    k feliz "{cps=40}\"Ah, eu posso te ajudar depois que eu voltar da faculdade.{/cps}\""
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Sério mesmo?{/cps}\""
                    hide Stella feliz2
                    show Stella feliz
                    k feliz "{cps=40}\"Claro, eu não tenho nada pra fazer hoje a tarde mesmo, posso te ajudar a procurar.{/cps}\""
                    hide Stella feliz
                    show Stella happy2
                    s happy2 "{cps=40}\"Nossa, muito obrigada Kioku...{/cps}\""
                    hide Stella happy2
                    show Stella envergonhada
                    s envergonhada "{cps=40}\"Me sinto mal por ter perdido, acabei de chegar e ja fiz merda hahaha.{/cps}\""
                    hide Stella envergonhada
                    show Stella feliz
                    k feliz "{cps=40}\"Não se preocupa com isso, acontece, eu mesmo já perdi chaves antes...{/cps}\""
                    hide Stella feliz
                    show Stella envergonhada
                    s envergonhada "{cps=40}\"Tem razão hahaha{/cps}\""
                    hide Stella envergonhada
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Então tá combinado...{/cps}\""
                    s feliz2 "{cps=40}\"Mas pera, como vou te chamar quando você chegar em casa?{/cps}\""
                    hide Stella feliz2
                    show Stella feliz
                    k normal "{cps=40}\"Eu posso te dar o meu número de celular, ai quando eu chegar em casa eu te dou um toque\"{/cps}"
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Ah sim, pode ser assim então...{/cps}\""
                    hide Stella feliz2
                    show Stella feliz
                    k normal "{cps=40}\"Então tá, meu número é 1724-1021, me manda uma mensagem mais tarde...{/cps}\""
                    $ consequência_ativada["celular_estella"] = True
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Okay, pode deixar, no final da tarde eu te mando mensagem...{/cps}\""
                    hide Stella feliz2
                    show Stella feliz
                    k feliz "{cps=40}\"Bom, agora eu tenho que ir, se não eu perco o Trem haha{/cps}\""
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Claro, foi um prazer te conhecer Kioku{/cps}\""
                    hide Stella feliz2
                    show Stella feliz3
                    k feliz "{cps=40}\"Igualmente Estella, até mais.{/cps}\""
                    hide Stella feliz3
                    jump tremestacao
                "Se despedir":
                    $ trematraso = False
                    hide Stella feliz2
                    show Stella feliz
                    k normal "{cps=40}\"Bom, agora eu tenho que ir, se não eu perco o Trem{/cps}\""
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Claro, foi um prazer te conhecer Kioku{/cps}\""
                    k feliz "{cps=40}\"Igualmente Estella, até mais.{/cps}\""
                    hide Stella feliz2
                    with dissolve
                    jump tremestacao          
        "Ajudar a procurar a chave":
            hide Stella feliz2
            show Stella feliz
            $ consequência_ativada["ajudar_estella_chave"] = True
            k normal "{cps=40}\"Você falou que tinha perdido a sua chave né?{/cps}\""
            hide Stella feliz
            show Stella feliz2
            s feliz2 "{cps=40}\"Sim, eu não faço ideia de onde eu perdi...{/cps}\""
            hide Stella feliz2
            show Stella feliz
            k feliz "{cps=40}\"Ah, eu posso te ajudar depois que eu voltar da faculdade.{/cps}\""
            hide Stella feliz
            show Stella feliz2
            s feliz2 "{cps=40}\"Sério mesmo?{/cps}\""
            hide Stella feliz2
            show Stella feliz
            k feliz "{cps=40}\"Claro, eu não tenho nada pra fazer hoje a tarde mesmo, posso te ajudar a procurar.{/cps}\""
            hide Stella feliz
            show Stella happy2
            s happy2 "{cps=40}\"Nossa, muito obrigada Kioku...{/cps}\""
            hide Stella happy2
            show Stella envergonhada
            s envergonhada "{cps=40}\"Me sinto mal por ter perdido, acabei de chegar e ja fiz merda hahaha.{/cps}\""
            hide Stella envergonhada
            show Stella feliz
            k feliz "{cps=40}\"Não se preocupa com isso, acontece, eu mesmo já perdi chaves antes...{/cps}\""
            hide Stella feliz
            show Stella envergonhada
            s envergonhada "{cps=40}\"Tem razão hahaha{/cps}\""
            hide Stella envergonhada
            show Stella feliz2
            s feliz2 "{cps=40}\"Então tá combinado...{/cps}\""
            s feliz2 "{cps=40}\"Mas pera, como vou te chamar quando você chegar em casa?{/cps}\""
            hide Stella feliz2
            show Stella feliz
            k normal "{cps=40}\"Eu posso te dar o meu número de celular, ai quando eu chegar em casa eu te dou um toque\"{/cps}"
            hide Stella feliz
            show Stella feliz2
            s feliz2 "{cps=40}\"Ah sim, pode ser assim então...{/cps}\""
            hide Stella feliz2
            show Stella feliz
            k normal "{cps=40}\"Então tá, meu número é 1724-1021, me manda uma mensagem mais tarde...{/cps}\""
            $ consequência_ativada["celular_estella"] = True
            hide Stella feliz
            show Stella feliz2
            s feliz2 "{cps=40}\"Okay, pode deixar, no final da tarde eu te mando mensagem...{/cps}\""
            hide Stella feliz2
            show Stella feliz
            menu:
                "Perguntar sobre o nome":
                    k normal "{cps=40}\"Estella, que nome bonito... de onde é esse nome?{/cps}\""
                    hide Stella feliz2
                    show Stella happy1
                    s happy1 "{cps=40}\"Ah obrigada Kioku, na verdade é um nome português, meus pais são do Brasil.{/cps}\""
                    k feliz "{cps=40}\"Nossa que legal, eu sempre quis conhecer o Brasil.{/cps}\""
                    hide Stella happy1
                    show Stella happy2
                    s happy2 "{cps=40}\"Você deveria mesmo Kioku, é um país lindo, cheio de praias, as comidas de lá são incriveis, as pessoas são gentis...{/cps}\""
                    k feliz "{cps=40}\"Quem sabe um dia eu consiga ir lá visitar.{/cps}\""
                    hide Stella happy2
                    show Stella feliz3
                    s feliz3 "{cps=40}\"Com certeza Kioku, quando tu for eu levo você pra conhecer Porto Alegre, e conhecer o maior do Sul.{/cps}\""
                    k divertindo "{cps=40}\"Fechado então, não sei o que você quis dizer com 'maior do Sul' mas é isso hahaha.{/cps}\""
                    hide Stella feliz3
                    show Stella happy2
                    s happy2 "{cps=40}\"Hahaha, é um time de futebol, o Grêmio, o time que eu torço.{/cps}\""
                    hide Stella happy2
                    show Stella feliz
                    k surpreso "{cps=40}\"Ah sim, eu não entendo muito de futebol, mas quem sabe você me ensina um dia.{/cps}\""
                    hide Stella happy2
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Com certeza Kioku, e de brinde eu vou te levar pra assistir um jogo haha.{/cps}\""
                    hide Stella feliz2
                    show Stella feliz
                    k divertindo "{cps=40}\"Fechado haha.{/cps}\""
                    jump tremestacao
                "Se despedir":
                    $ trematraso = False
                    hide Stella feliz2
                    show Stella feliz
                    k normal "{cps=40}\"Bom, agora eu tenho que ir, se não eu perco o Trem{/cps}\""
                    hide Stella feliz
                    show Stella feliz2
                    s feliz2 "{cps=40}\"Claro, foi um prazer te conhecer Kioku{/cps}\""
                    k feliz "{cps=40}\"Igualmente Estella, até mais.{/cps}\""
                    hide Stella feliz2
                    with dissolve
                    jump tremestacao
        "Se despedir":
            $ trematraso = False
            hide Stella feliz2
            show Stella feliz
            k normal "{cps=40}\"Bom, agora eu tenho que ir, se não eu perco o Trem{/cps}\""
            hide Stella feliz
            show Stella feliz2
            s feliz2 "{cps=40}\"Claro, foi um prazer te conhecer Kioku{/cps}\""
            k feliz "{cps=40}\"Igualmente Estella, até mais.{/cps}\""
            hide Stella feliz2
            with dissolve
            jump tremestacao
            
label fimdemosecreto:
    stop music fadeout 1.0
    play music "audio/Musicas/finaldemo.mp3" fadein 1.0
    scene narrador
    with dissolve
    "{cps=40}Kioku volta ao seu apartamento, e ao chegar lá, ele vê uma carta em cima da mesa{/cps}"
    "{cps=40}Ele então pega a carta, e começa a ler{/cps}"
    "{cps=40}{i}Kioku\nSe você está lendo isso, significa que você voltou para casa sem fazer perguntas demais. Isso é bom.{/i}{/cps}"
    "{cps=40}{i}Você sempre faz isso.\nEu pensei em não escrever. Em deixar que o tempo fizesse o que ele sempre faz com você: apagar. Mas algumas coisas não desaparecem sozinhas. Elas apenas esperam.{/i}{/cps}"
    "{cps=40}{i}Você não perdeu sua memória.\nVocê escondeu ela.{/cps}{/i}"

    "{cps=40}{i}Não foi um acidente.\nNão foi uma doença.\nNão foi culpa de nínguem além de você.{/i}{/cps}"

    "{cps=40}{i}Você fez isso para se proteger.\nPara se proteger do que você fez.\nDo que você é capaz de fazer.{/i}{/cps}"

    "{cps=40}{i}Há dez anos, você viu algo que não deveria continuar existindo dentro da sua cabeça.\nE quando percebeu o que aquilo significava… você escolheu esquecer.{/i}{/cps}"

    "{cps=40}{i}Não pense que foi covardia\nFoi sobrevivência.{/i}{/cps}"

    "{cps=40}{i}Todos nós concordamos naquela noite que seria melhor assim\nQue você não precisava carregar isso\nQue o silêncio era melhor do que a verdade.{/i}{/cps}"

    "{cps=40}{i}Alguns de nós mantiveram essa promessa\nOutros... não conseguiram.{/i}{/cps}"

    "{cps=40}{i}Se as memórias estão voltando, significa que o pacto falhou.\nOu que você decidiu, mesmo sem perceber, quebrá-lo.{/i}{/cps}"

    "{cps=40}{i}Olhe para as pessoas ao seu redor com atenção.\nPreste atenção em quem evita certos nomes.\nEm quem muda de assunto rápido demais.\nEm quem parece aliviado quando você diz que não se lembra.{/i}{/cps}"

    "{cps=40}{i}Elas sabem o que você fez.\nE estão com medo do que você pode fazer novamente.{/i}{/cps}"

    "{cps=40}{i}Eles não estão tentando te proteger.\nEstão tentando se proteger de você lembrando.{/i}{/cps}"

    "{cps=40}{i}Não procure respostas.\nMas, se procurar...\nEsteja preparado para perder mais do que esqueceu.{/i}{/cps}"

    "{cps=40}{i}Algumas verdades não libertam.\nElas cobram.{/i}{/cps}"

    "{cps=40}{i}Com pesar — alguém que lembra tudo.{/i}{/cps}"
    "{cps=40}{i}{b}Final 3 de 4 da Demo feita{/i}{/b}{/cps}"
    "{cps=40}{i}{b}E bem assim termina nossa história... Pelo menos por enquanto{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Talvez tenha ficado curta, talvez longa, tudo depende de você, jogador{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Mas o importante é que você chegou até aqui, e viu um pouco do que o \'Ainda que eu Lembre\' tem a oferecer{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Espero que tenha gostado, e que aguarde ansiosamente pelo lançamento completo do jogo{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Qualquer feedback, negativo ou positivo, que você queira dizer ou falar, por favor entre no {a=https://discord.gg/wp3UTT7q8t}Discord{/a} do jogo{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Lá, além de poder dar feedbacks, vocês poderão acompanhar atualizações, dar sugestões, e até apoiar o meu trabalho{/i}{/b}{/cps}"
    "{cps=40}{i}{b}No momento em que estou terminando esta demo, não possuo ainda um catarse.me ou um patron, ou qualquer coisa, então caso, você realmente gostou da minha demo, e realmente quer apoiar meu projeto{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Basta entrar no servidor do Discord, divulgar o jogo, para que ele cresça, mesmo não sendo financeiramente, ainda assim, você estaria ajudando demais a produção{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Por conta de apenas eu estar com toda a produção(Programação, musicas, personagens e afins) é necessário mais tempo para produzir algo bom o suficiente para toda e qualquer pessoa{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Com isso dito, espero que entendam caso atualizações futuras, demorem mais para sair, visto que apenas eu estou encarregado de toda a produção{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Bem, acho que era isso que eu tinha, novamente, muito obrigado por jogar até o final, e se você chegou até aqui, quer dizer que pegou 1 dos 3 finais dessa demo{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Se você quiser voltar ao início, tem um final secreto(que já dando uma dica, é bem fácil de conseguir, e provavelmente no jogo final vai sumir..... Ou não){/i}{/b}{/cps}"
    "{cps=40}{i}{b}E bem, se você esta lendo isso, quer dizer que você chegou no final secreto, viu e descobriu um pouco mais sobre talvez o passado de Kioku{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Quem será a pessoa por trás da carta? O que aconteceu em 25 de Julho de 2015? Talvez... essas sejam as perguntas erradas a se fazer{/i}{/b}{/cps}"
    "{cps=40}{i}{b}As vezes, desenterrar o passado, não é o caminho certo, pois memórias são feitas para lembrar, e o que foi perdida, deve-se continuar assim....{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Enfim, muito obrigado de coração, e nos vemos nas futuras atualizações de \'Antes que eu Lembre\', até mais <3{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Quase ia esquecendo(olha o processinho ai), agradeçimentos a Noraneko Games que disponibilizou gratuitamente os assets de personagens e alguns planos de fundos utilizados{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Muito obrigado, sem o trabalho de vocês esse jogo seria três vezes mais difícil de ser produzido{/i}{/b}{/cps}"
    "{cps=40}{i}{b}Nos vemos em breve.....{/i}{/b}{/cps}"
    return




