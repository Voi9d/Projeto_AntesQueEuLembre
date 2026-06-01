label irembora:
    stop music fadeout 1.0
    play music "audio/Musicas/Midnight.mp3" fadein 1.0
    hide Stella feliz2
    scene corredorexdia
    with dissolve
    k normal "{cps=40}{i}Nossa, que dia intenso... Mas foi um dia bom, eu conheci a Estella, ela é muito genil e carinhosa....{/i}{/cps}"
    if subarusangue == True:
        k normal "{cps=40}{i}Porque eu tive aquelas visões? Aquele sentimento? É como se eu realmente estivesse fazendo aquilo.{/i}{/cps}"
    else:
        k normal "{cps=40}{i}Porque o subaru vive tentando me encher o saco, desde que eu entrei na faculdade é como se ele sempre me perseguisse...{/i}{/cps}"
    scene patioescoladia2
    with dissolve
    k normal "{cps=40}{i}Caralho, que fome, que horas são...{/i}{/cps}"
    k surpreso "{cps=40}{i}Meu deus já é meio dia, eu nem percebi...{/i}{/cps}"
    k normal "{cps=40}{i}Eu preciso comer algo, será que o restaurante ja ta aberto?{/i}{/cps}"
    scene narrador
    with dissolve
    "{cps=40}Kioku, então, decide ir até o restaurante que ele casualmente vai após suas aulas da manhã, por sempre achar a comidade de lá mais barata e também melhor{/cps}"
    "{cps=40}Se passam alguns minutos, o grande relógio da cidade começa a bater, indicando ser 12:30...{/cps}"
    "{cps=40}Kioku, finalmente chega no restaurante e entra nele, novamente, o cheiro de comida o atinge, o barulho do movimento do restaurante{/cps}"
    $ renpy.music.set_volume(0.7, delay=0.5, channel='music')
    play sound "audio/SoundsEffects/TanakaRestauranteCheio.mp3"
    $ renpy.music.set_volume(0.5, delay=0.5, channel='sound')
    k feliz "{cps=40}{i}Que bom que o Restaurante do Sr. Tanaka está tão popular eu fico feliz assim{/i}{/cps}"
    scene restaurantemeiodia
    with dissolve
    k feliz "{cps=40}{i}Como sempre a melhor mesa está vazia, a mesa do canto, onde eu sempre sento...{/i}{/cps}"
    "{cps=40}Kioku, então, se senta na mesa do canto, e pega o clássico cardápio do restaurante{/cps}"
    show Kenji normal at right_pos with moveinright
    "Garçom" "{cps=40}\"Olá senhor, bem-vindo a Tanaka´s Home, a casa do Tanaka, onde você poderá se sentir em casa!\"{/cps}"
    "Garçom" "{cps=40}\"Eu sou Kenji e estarei servindo você hoje, o que deseja pedir?\"{/cps}"
    k feliz "{cps=40}\"Ah, eai Kenji, hoje você parece feliz ein?\"{/cps}"
    kj normal "{cps=40}\'Ah... Oi, Kioku, e você sempre com as mesmas piadas.\"{/cps}"
    k feliz "{cps=40}\"Hoje vai sair cedo?\"{/cps}"
    kj normal "{cps=40}\"O que você acha? Bom, eu preciso trabalhar, vai querer o mesmo de sempre?\"{/cps}"
    k normal "{cps=40}\"Sim sim, vou querer o meu clássico.\"{/cps}"
    kj normal "{cps=40}\"Okay, 15 minutos eu trago pra ti, fique a vontade e...\nBom, você sabe o resto\"{cps}"
    hide Kenji normal with moveoutright
    k normal "{cps=40}{i}Kenji sempre ta com essa cara de sono, mas ele mesmo assim é sempre gentil com todo mundo, queria eu ser assim{/cps}{/i}"
    "{cps=40}Kioku, então, espera o seu pedido chegar, e fica observando o movimento do restaurante, as pessoas conversando, os garçons correndo pra lá e pra cá...{/cps}"
    show Kenji normal at right_pos with moveinright
    kj normal "{cps=40}\"Aqui está seu pedido senhor, espero que goste.\"{/cps}"
    hide Kenji normal with moveoutright
    scene restaurantemeiodiacomida
    with dissolve
    "{cps=40}Kioku, então, começa a comer seu prato, o sabor é incrível, como sempre...{/cps}"
    "{cps=40}Ele come com calma, saboreando cada garfada, e pensando sobre o que aconteceu durante a manhã...{/cps}"
    "{cps=40}Cada garfada, é como se fosse uma eternidade, Kioku a aprecia, e ao mesmo tempo se perde em seus pensamentos....{/cps}"
    scene casakioku
    with dissolve
    stop music fadeout 1.0
    play music "audio/Musicas/Fique_comigo.mp3" fadein 1.0
    "{cps=40}{i}Esse lugar... O sentimento de nostalgia, a sensação de estar em casa...{/i}{/cps}"
    scene casakiokuentrada
    with dissolve
    "{cps=40}{i}O cheiro de comida do meio-dia... O cheiro da casa, é quase como inesquecível...{/i}{/cps}"
    "###" "{cps=40}\"Kioku? Meu anjo? Mamãe ta aqui na cozinha\"{/cps}"
    menu:
        "Ir para o Corredor":
            scene casakiokucorredor
            with dissolve
    "{cps=40}{i}Esse sentimento.... de conforto e amor....{/i}{/cps}"
    "{cps=40}{i}Quando foi que eu me senti assim antes?{/i}{/cps}"
    menu:
        "Ir para o Quarto":
            scene casakiokuquarto
            with dissolve
            "{cps=40}{i}Essa cama... O conforto... O sentimento de segurança...{/i}{/cps}"
            "{cps=40}{i}Meu antigo computador e refúgio para se sentir fora da realidade...{/i}{/cps}"
            "{cps=40}{i}Meus livros e mangás, suas paixões...{/i}{/cps}"
            "{cps=40}{i}\'Senhor Polvicio\' meu amigo de pelúcia....{/i}{/cps}"
            "{cps=40}{i}Porquê.... Porque eu me sinto assim? Porque eu sinto essa nostalgia, esse conforto, esse amor?{/i}{/cps}"
    menu:
        "Ir para o Quarto da ###":
            scene casakiokuquartomae
            with dissolve
            "{cps=40}{i}O quarto da ###... Esse cheiro de perfume... Aqui era onde eu me sentia seguro.{/i}{/cps}"
            "{cps=40}{i}Aqui era onde eu me sentia amado... Onde eu me sentia protegido...{/i}{/cps}"
    menu:
        "Ir para a Cozinha":
            scene casakiokucozinha
            with dissolve
            "{cps=40}{i}A cozinha... O cheiro de comida... O conforto... O sentimento de estar em casa...{/i}{/cps}"
            "{cps=40}{i}E....{/i}{/cps}"
            show Phiona feliz
            with dissolve
            "###" "{cps=40}\"Oi meu amor, que bom que você chegou, como foi a aula?\"{/cps}"
            "{cps=40}{i}A voz dela.... É tão suave e.... acolhedora...{/i}{/cps}"
            hide Phiona feliz
            show Phiona feliz2
            "###" "{cps=40}\"Fiz sua comida favorita, espero que goste!\"{/cps}"
            "{cps=40}{i}O cheiro da comida, o conforto, a sensação de estar em casa... O amor dela... Tudo isso me atinge como uma onda de choque...{/i}{/cps}"
            hide Phiona feliz2
            show Phiona normal
            "###" "{cps=40}\"Kioku??? Ei...\"{/cps}"
            hide Phiona normal
            with dissolve
    scene restaurantetarde
    with dissolve 
    pause 0.5
    stop music fadeout 1.0
    play music "audio/Musicas/Midnight.mp3" fadein 1.0
    show Kenji normal
    with dissolve
    kj normal "{cps=40}\"Kioku? Acorda, o restaurante ta fechando ja...\"{/cps}"
    k normal "{cps=40}\"Nossa.... Desculpa Kenji, desculpa por ter dormido.\"{/cps}"
    kj normal "{cps=40}\"Não tem problema, senhor Tanaka gosta de você, ele não se importa.\"{/cps}"
    kj normal "{cps=40}\"Apenas se agilize, ja estamos preste a fechar\"{/cps}"
    hide Kenji normal with moveoutright
    k normal "{cps=40}{i}Merda, dormi muito aqui, e que sonho estranho foi esse?{/i}{/cps}"
    scene ruanoiteverao
    with dissolve
    k normal "{cps=40}{i}Eu preciso ir pra casa, Mingau deve estar me esperando...{/i}{/cps}"
    k normal "{cps=40}{i}Merda, a estação ja ta fechada, vou ter que pegar o busão.{/i}{/cps}"
    scene estacaoonibusnoite
    with dissolve
    k normal "{cps=40}{i}O próximo ônibus só passa daqui a 20 minutos... Bom não tem muito o que eu fazer, vou esperar aqui...{/i}{/cps}"
    k normal "{cps=40}{i}Merda, meu 4g tava desligado, nossa, a Jinsei vai me matar{/i}{/cps}"
    $ receive_message("Jinsei", "Oiiii, cade você? Foi almoçar aonde?", time="12:45")
    pause 0.5
    $ receive_message("Jinsei", "Kioku, você foi almoçar no Tanaka?", time="12:50")
    pause 0.5
    $ receive_message("Jinsei", "O senhor está me ignorandooooo???? 😠😠", time="13:10")
    pause 0.5
    $ receive_message("Jinsei", "Você ta em casa pelo menos?", time="14:00")
    pause 0.5
    $ receive_message("Jinsei", "Manda mensagem pelo menos quando puder, por favor!", time="14:31")
    $ set_pending_choice("Jinsei", "jinsei_preocupada")
    if consequência_ativada["respondeu_jinseipreocupada"] == True:
        k normal "{cps=40}{i}Merda, Jinsei ja deve ter ido dormir, espero que ela fique aliviada quando ver as mensagens...{/i}{/cps}"
        jump chegandoemcasa
    else:
        jump chegandoemcasa

label chegandoemcasa:
    stop music fadeout 1.0
    play music "audio/Musicas/NoitedeVerão.mp3" fadein 1.0
    scene narrador
    with dissolve
    "{cps=40}Se passa os 20 minutos, até que o ônibus chega, Kioku entra nele, senta em um dos assentos e fica olhando pela janela, pensando sobre o que aconteceu durante o dia...{/cps}"
    "{cps=40}Se passam 3 horas, até que finalmente a parada de Kioku é avistada, ele, então, desce do ônibus, e caminha até o seu apartamento...{/cps}"
    scene apartamentoexternonoite
    with dissolve
    k normal "{cps=40}{i}Caralho, eu ainda to muito cansado{/i}{/cps}"
    k normal "{cps=40}{i}Eu preciso entrar, o Mingau deve estar me esperando...{/i}{/cps}"
    scene narrador
    with dissolve
    play sound "audio/SoundsEffects/abrindoporta.mp3"
    scene salaanoite
    with dissolve
    pause 0.5
    play sound "audio/SoundsEffects/fechandoporta.mp3"
    "{cps=40}Kioku, então, entra no seu apartamento, e fecha a porta atrás de si...{/cps}"
    "{cps=40}Começa a procurar pelo seu querido gato Mingau, e o encontra dormindo no sofá...{/cps}"
    show mingaudormindo
    with dissolve
    play sound "audio/Mingau/minguauronronando.mp3"
    k feliz "{cps=40}{i}Mingau... Meu amorzinho... Que bom que você ta bem...{/i}{/cps}"
    k feliz "{cps=40}{i}Vou deixar sua ração aqui pra se você precisar durante a noite...{/i}{/cps}"
    hide mingaudormindo
    with dissolve
    scene Quarto2
    with dissolve
    k normal "{cps=40}{i}Nossa, eu to realmente exausto, acho que vou só me deitar e capotar na cama...{/i}{/cps}"
    scene narrador
    with dissolve
    "{cps=40}Kioku, então, se deita na cama, e fecha os olhos...{/cps}"
    "{cps=40}Sente seu corpo relaxar, depois de um dia intenso, e começa a se sentir sonolento...{/cps}"
    "{cps=40}E então, ele finalmente adormece...{/cps}"
    jump finaldemo



            