label finaldemo:
    hide screen phone_button
    hide screen phone_notification
    hide screen phone_system  
    stop music fadeout 1.0
    play music "audio/Musicas/Porque_voce_me_deixou.mp3" fadein 1.0
    scene casakioku
    with dissolve
    "{cps=40}{i}...{/i}{/cps}"
    "{cps=40}{i}Esse lugar...{/i}{/cps}"
    "{cps=40}{i}...{/i}{/cps}"
    "{cps=40}{i}De novo esse lugar....{/i}{/cps}"
    "{cps=40}{i}Mas dessa vez.... Eu conheço{/i}{/cps}"
    scene casakiokuentrada
    with dissolve
    play sound "audio/SoundsEffects/tictackioku.mp3" fadein 1.0 loop
    $ renpy.music.set_volume(0.3, channel='sound')
    "{cps=40}{i}Eu sei onde estou...{/i}{/cps}"
    "Kioku Aida" "{cps=40}\"Mãããããããããe???\"{/cps}"
    "{cps=40}{i}Mas... o que??{/i}{/cps}"
    show Kiokujovem normal
    with dissolve
    "Kioku Aida" "{cps=40}\"Mãe? Mãe, onde você está? Eu cheguei...\"{/cps}"
    "{cps=40}{i}E-esse....\nEsse, sou eu??{/i}{/cps}"
    hide Kiokujovem normal
    with dissolve
    scene casakiokucorredor
    with dissolve
    show Kiokujovem normal
    with dissolve
    "Kioku Aida" "{cps=40}\"Mãe, você ta dormindo?\"{/cps}"
    hide Kiokujovem normal
    with dissolve
    scene casakiokuquartomae
    with dissolve
    show Kiokujovem normal
    with dissolve
    "Kioku Aida" "{cps=40}\"Mãe? Mãe, você ta ai?\"{/cps}"
    "Kioku Aida" "{cps=40}\"Ué... Ela não ta aqui, nem na cozinha....\nAh! Ela deve estar na sala.\"{/cps}"
    hide Kiokujovem normal
    with dissolve
    scene casakiokucorredor
    with dissolve
    "{cps=40}{i}Porquê.... Porquê eu tenho esse sentimento?\nPorque eu sinto que tem algo errado?{/i}{/cps}"
    "{cps=40}{i}Porquê eu não quero que ele entre na sala?{/i}{/cps}"
    scene narrador
    with dissolve
    "{cps=40}Uma porta pode ser ouvida se abrindo, e passos podem ser ouvidos entrando na sala...{/cps}"
    "Kioku Aida" "{cps=40}\"Mãe?\"{/cps}"
    stop music fadeout 1.0
    $ renpy.music.set_volume(1.5, delay=1.0, channel='sound')
    scene chegoutardekioku
    with flash
    pause 1.0
    "..."
    scene narrador
    pause 1.0
    stop sound
    "Kioku Aida" "{cps=5}\"M...ãe...?\"{/cps}"
    jump agradecimentofinaldemo

label agradecimentofinaldemo:
    play music "audio/Musicas/usaremalgummomento.mp3" fadein 1.0
    pause 1.5
    "{cps=40}{i}E bem assim termina nossa história... Pelo menos por enquanto.{/i}{/cps}"
    "{cps=40}{i}Mas o importante é que você chegou até aqui, e viu um pouco do que o \'Ainda que eu Lembre\' tem a oferecer...{/i}{/cps}"
    "{cps=40}{i}O que será que aconteceu? Porquê isso aconteceu com ####?{/i}{/cps}"
    "{cps=40}{i}Acho que para responder isso, só o tempo dirá...{/i}{/cps}"
    # "{cps=40}{i}Ou então possamos utilizar uma frase de um Senhor muito conhecido \'Essa é uma resposta que eu sei que nunca terei\'...{/i}{/cps}"
    "{cps=40}{i}Mas bem....{/i}{/cps}"
    "{cps=40}{i}Espero que tenha gostado, e que aguarde ansiosamente pelo lançamento completo do jogo{/i}{/cps}"
    "{cps=40}{i}Este projeto inteiro está sendo produzido por mim, então, cada bug, cada falha, cada erro que talvez vocês presenciaram nesta Demo, talvez não tenha sido vista pelos meus olhos.{/i}{/cps}"
    "{cps=40}{i}Qualquer feedback, negativo ou positivo, que você queira escrever ou falar, por favor entre no {a=https://discord.gg/wp3UTT7q8t}Discord{/a} do jogo{/i}{/cps}"
    "{cps=40}{i}Lá, além de poder dar feedbacks, vocês poderão acompanhar atualizações, dar sugestões, e até apoiar o meu trabalho{/i}{/cps}"
    "{cps=40}{i}Meu objetivo com esse jogo, é criar uma experiência imersiva, que possa passar uma mensagem, e ao mesmo tempo ser divertida, espero que com essa demo que você jogou, tenha pelo menos sentido um pouco do que eu senti escrevendo ela.{/i}{/cps}"
    "{cps=40}{i}Se quiser me ajudar de outras formas, basta entrar no servidor do {a=https://discord.gg/wp3UTT7q8t}Discord{/a}, divulgar o jogo, para que ele cresca, mesmo não sendo financeiramente, ainda assim, você estaria ajudando de mais a produção.{/i}{/cps}"
    "{cps=40}{i}Aliás, quero que saibam que este jogo sairá independente da quantidade de apoios, pois isso estou fazendo com o coração, e a alegria de ter mais jogos brasileiros, então conto com o apoio de você em divulgar para que mais pessoas possam chegar em \'Antes que eu Lembre\'.{/i}{/cps}"
    "{cps=40}{i}Por conta de apenas eu estar com toda a produção(Programação, musicas, personagens e afins) é necessário mais tempo para produzir algo bom o suficiente para toda e qualquer pessoa.{/i}{/cps}"
    "{cps=40}{i}Com isso dito, espero que entendam caso atualizações futuras, demorem mais para sair, visto que apenas eu estou encarregado de toda a produção.{/i}{/cps}"
    "{cps=40}{i}Bem, acho que era isso que eu tinha, novamente, muito obrigado por jogar até o final.{/i}{/cps}"
    "{cps=40}{i}Quase ia esquecendo aqui vai a lista de agradecimentos aos autores de algumas das artes/músicas/backgrounds que foram utilizadas e irão ser utilizadas.{/i}{/cps}"
    "{cps=40}{i}Disseram que não era necessário dar créditos, mas é o mínimo que posso fazer.{/cps}{/i}"
    "{cps=40}{i}Músicas:\nBell Kalengar\nPotat0Master{/i}{/cps}"
    "{cps=40}{i}Sprites:\nSutemo(Estella, Jinsei, Subaru, Kioku Criança)\nSraye(Kioku e Yuki){/i}{/cps}"
    "{cps=40}{i}Backgrounds:\nTainara-P (Todas as Imagens da Faculdade exceto Biblioteca e Terraço)\nNoraneko Games(Todas as imagens do apartamento e corredor do Kioku)\nSpiral Atlas (Casa Antiga de Kioku)\n{/i}{/cps}"
    "{cps=40}{i}House Of Imagi Studio (Biblioteca da Faculdade, Terraço da Faculdade, Academia, Parque){/i}{/cps}"
    "{cps=40}{i}Ufff.... Acho que é isso.{/i}{/cps}"
    "{cps=40}{i}Muito obrigado, sem o trabalho de vocês esse jogo seria três vezes mais difícil de ser produzido{/i}{/cps}"
    "{cps=40}{i}Bem, obrigado novamente por ter jogado, nos vemos em breve....{/i}{/cps}"
    "{cps=40}{i}Ah... quase ia esquecendo, eu não ia ir embora sem deixar nada para vocês... espero que gostem.{/cps}{/i}"
    jump teaser
    return

label teaser:
    "{cps=40}{i}Você pode largar o mouse agora, não há necessidade de clicar apartir daqui{w=1.0}{nw}{/cps}{/i}"
    pause 1.5
    stop music fadeout 1.0
    play music "audio/Musicas/Teaser.mp3"
    pause 1.0
    scene entradaapestella
    with dissolve
    pause 0.5
    show Stella feliz
    with dissolve
    s feliz "{cps=25}\"Pode entrar viu Kioku, e fica a vontade\nMi Casa, Su Casa...\"{w=1.0}{nw}{/cps}"
    pause 0.5
    hide Stella feliz
    with dissolve
    scene narrador
    with dissolve
    "???" "{cps=25}{i}Você se lembra?{w=1.0}{nw}{/cps}{/i}"
    pause 0.5
    scene salaestarapestella
    with dissolve
    show PaisEstella primeiroencontro
    with dissolve
    "Senhora Nascimento" "{cps=25}\"Olá Senhor Kioku, muito prazer em conhecer\"{w=1.5}{nw}{/cps}"
    "Senhor Nascimento" "{cps=25}\"Prazer? Você vem aqui depois de tudo?\"{w=1.5}{nw}{/cps}"
    hide PaisEstella primeiroencontro
    with dissolve
    scene narrador
    with dissolve

    pause 0.8

    "{cps=40}{i}As memórias não voltam em ordem.{/i}{w=1.2}{nw}{/cps}"

    pause 0.5

    "{cps=40}{i}Elas voltam como pedaços.{/i}{w=1.2}{nw}{/cps}"

    pause 0.5

    "{cps=40}{i}Como vozes que você jurava ter esquecido.{/i}{w=1.5}{nw}{/cps}"

    pause 0.8

    scene black
    with dissolve

    "???" "{cps=24}\"Kioku... você tá me ouvindo?\"{w=1.0}{nw}{/cps}"
    pause 0.4

    "???" "{cps=24}\"Ele não lembra de nada?\"{w=1.0}{nw}{/cps}"
    pause 0.4

    "???" "{cps=24}\"Não fala isso perto dele.\"{w=1.0}{nw}{/cps}"
    pause 0.4

    "???" "{cps=24}\"Foi um acidente.\"{w=1.0}{nw}{/cps}"
    pause 0.4

    "???" "{cps=24}\"Então por que todo mundo mentiu?\"{w=1.2}{nw}{/cps}"

    pause 0.8

    play sound "audio/SoundsEffects/coracao.mp3"

    "???" "{cps=22}\"Haru... levanta.\"{w=1.2}{nw}{/cps}"

    pause 0.6

    "???" "{cps=22}\"Levanta, por favor.\"{w=1.2}{nw}{/cps}"

    pause 0.8

    "???" "{cps=22}\"KI—\"{w=0.4}{nw}{/cps}"

    stop music fadeout 1.5
    stop sound fadeout 1.0

    pause 1.0

    scene black
    with dissolve

    pause 1.0

    "{cps=35}{i}\"Antes que eu lembre...\"{/i}{w=1.5}{nw}{/cps}"

    pause 0.5

    "{cps=35}{i}\"alguém precisa continuar mentindo.\"{/i}{w=2.0}{nw}{/cps}"

    pause 1.5

    "{cps=30}Fim.{w=2.0}{nw}{/cps}"
    $ unlock_achievement('fim')

    pause 3.0

    return



