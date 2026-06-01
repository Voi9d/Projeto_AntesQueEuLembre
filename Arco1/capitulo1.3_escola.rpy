label escola:
    stop music fadeout 2.0
    play music "audio/Musicas/school.mp3" fadein 2.0
    scene narrador
    with dissolve
    show Cap1 at center
    with dissolve 
    pause 2.0
    scene entradaescoladia
    with pixellate
    if trematraso == True:
        jump discussaoatraso
    else:
        k normal "{cps=40}{i}Cheguei a tempo, que bom, não preciso me preocupar em ter me atrasado.{/i}{/cps}"
        k normal "{cps=40}{i}Vou estudar mais um pouco para poder ir bem na prova.{/i}{/cps}"
        scene biblioteca1
        with pixellate
        k normal "{cps=40}{i}Ah, único lugar onde posso ter paz, essa hora ninguém aparece aqui, então posso estudar mais, bom, vamo lá.{/cps}"
        scene narrador
        with dissolve
        "{cps=40}Kioku começa a estudar, revisa cada conteúdo que irá cair na sua prova, cada centímetro, porque ele sabe, mesmo que precise de pouca nota, que a prova final de seu professor, é sempre a mais díficil.{/cps}"
        "{cps=40}Se passam alguns minutos, e durante os estudos Kioku acaba dormindo no meio.{/cps}"
        scene biblioteca2
        with pixellate
        "???" "\"{cps=40}Vamos acordar bela adormecida....\"{/cps}"
        k normal "{cps=40}\"Hã? Quem? Onde?{/cps}\""
        show Subaru sorisso
        with dissolve
        "???" "\"{cps=40}O que foi Kioku? Perdeu alguma coisa?\"{/cps}"
        k normal "{cps=40}\"Só me faltava essa, o que você quer Subaru.{/cps}\""
        jump discussao

label discussao:
    hide Subaru sorisso
    show Subaru sorisso
    si sorisso "{cps=40}\"Ei, relaxa mano, só vim acordar você.... Além do mais, você tem uma prova a fazer não?\"{/cps}"
    k bravo "{cps=40}\"Merda.... dormi demais, sai da minha frente Subaru...{/cps}\""
    si sorisso "{cps=40}\"Ainda continua educado igual antigamente, né Kioku?{/cps}\""
    k bravo "{cps=40}\"Antigamente? Você sempre foi um idiota comigo, como quer que eu seja educado?.\"{/cps}"
    k bravo "{cps=40}\"Por favor, eu to atrasado pra prova final, eu não tenho tempo pra perder contigo hoje, sai fora.{/cps}\""
    hide Subaru sorisso
    show Subaru bravo1
    si bravo1 "{cps=40}\"Você sempre tenta fugir quando alguém toca em assuntos desconfortáveis?{/cps}\""
    hide Subaru bravo1
    menu:
        "Confrontar Subaru":
            $ provaatraso = True
            $ subarusangue = True
            k irritado "{cps=40}\"Subaru, eu não quero discutir contigo hoje... só sai da minha frente.{/cps}\""
            hide Subaru bravo1
            show Subaru bravo2
            si bravo2 "{cps=40}\"Engraçado... você continua reagindo exatamente igual naquela época, sempre fugindo do real problema.{/cps}\""
            k irritado "{cps=40}\"Real problema? O único real problema aqui é você que está me fazendo atrasar para a prova, agora sai da frente!{/cps}\""
            hide Subaru bravo2
            show Subaru irritado
            si irritado "{cps=40}\"Você pode esquecer o passado o quanto quiser, Kioku... mas ele ainda tá aí. Eu não vou sair daqui até a gente resolver isso.{/cps}\""
            menu:
                "{b}{i}SoCaR A PoRrA dO SuBuRu{/i}{/b}":
                    stop music fadeout 1.0
                    play music "audio/Musicas/KiokuI.mp3" fadein 1.0
                    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                    scene narrador
                    with dissolve
                    "???" "{cps=40}{i}Kioku, você sabe o que fazer....{/i}{/cps}"
                    "???" "{cps=40}{i}Ele merece conhecer o verdadeiro Kioku Aida, mostre a ele quem você é.{/i}{/cps}"
                    "???" "{cps=40}{i}Ele merece a morte.... E você é ELA, mostre que não se deve mexer com a morte.{/i}{/cps}"
                    "{cps=40}Kioku cerra os punhos, encara Subaru nos fundos dos olhos, com aquele sorriso debochado, e então, Kioku pega Subaru pelo pescoço.{/cps}"
                    "{cps=40}Ele o ergue do chão, Subaru começa a se debater, tentando se soltar, mas Kioku o segura firme, como se fosse nada....{/cps}"
                    "{cps=40}E então, com sua mão, ele começa....{/cps}"
                    "1"
                    "2"
                    "3"
                    "4"
                    "5"
                    "6"
                    "{cps=40}Naquele momento Kioku perdeu as contas de quantos socos ele deu em Subaru, era como se tudo ao redor tivesse parado, a sua mente apenas pensava em sangue, e a única coisa que existia era ele e Subaru....{/cps}"
                    "{cps=40}Kioku não sentia dor, não sentia cansaço, tudo que ele sentia era uma raiva incontrolável, uma vontade de fazer Subaru pagar por tudo que ele fez....{/cps}"
                    "{cps=40}E assim, Kioku continua.{/cps}"
                    "{cps=40}Kioku finalmente para, ele não sabe por quanto tempo bateu no rosto de Subaru, ele só sabe que antes era uma pessoa que se debatia em seu braço....{/cps}"
                    "{cps=40}Agora era um corpo sendo segurado como se fosse carne, onde era para ser seu rosto, apenas um buraco afundado irreconhecível.{/cps}"
                    "{cps=40}Kioku larga o que um dia era o corpo de Subaru, seus punhos pingando sangue, suas falanges completamente enroxadas, ele olha para frente.{/cps}"
                    "{cps=40}E um grande sorisso toma conta de seu rosto, aquele sangue nas suas mãos, lhe fazia bem, {i}\"ele recebeu o que merecia\"{/i}.{/cps}"
                    "{cps=40}Por um segundo, então, Kioku fecha os olhos e respira fundo.{/cps}"
                    $ unlock_achievement('killerpassager')
                    jump oquerealmenteaconteceu2
                "{b}{i}SoCaR SuBuRu{/i}{/b}":
                    stop music fadeout 1.0
                    play music "audio/Musicas/KiokuI.mp3" fadein 1.0
                    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                    scene narrador
                    with dissolve
                    "{cps=40}Kioku fecha seus punhos, é como se tudo ao redor ficasse lento, vendo Subaru Ichida na sua frente, rindo dele, e de sua situação....{/cps}"
                    "???" "{cps=40}{i}Ele ri de você Kioku, como se você fosse ninguém, ele ri da sua situação, você vai mesmo deixar ele te tratar dessa forma?{/i}{/cps}"
                    "???" "{cps=40}{i}Não..... você não vai deixar isso acontecer.... VOCÊ NÃO PODE DEIXAR ISSO ACONTECER.{/i}{/cps}"
                    "???" "{cps=40}{i}ELE RI DE VOCÊ.... ELE ZOA DA SUA SITUAÇÃO..... ELE RI DA SUA FAMILIA, AMIGOS E DE TODO MUNDO....{/i}{/cps}"
                    "???" "{cps=40}{i}{size=+10}ELE{/size} {size=+15}TEM{/size} {size=+20}QUE{/size} {size=+25}PAGAR....{/size}{/i}{/cps}"
                    "{cps=40}Tudo ficou escuro na visão de Kioku, unica coisa que ele conseguia ouvir era....{/cps}"
                    "{cps=40}De novo....{/cps}"
                    "{cps=40}De novo....{/cps}"
                    "{cps=40}De novo....{/cps}"
                    "{cps=40}E de novo...{/cps}"
                    "{cps=40}Até que.....{/cps}"
                    pause 1.0
                    "{cps=40}Kioku para de bater.... suas mãos encharcadas de sangue....{/cps}"
                    "???" "{cps=40}{i}É bom né Kioku, esse sentimento.... de prazer ao ver alguêm {size=+10}DESPREZIVEL{/sizel} como ele no chão...{/i}{/cps}"
                    "???" "{cps=40}{i}Olha para ele.... no chão..... seu rosto todo sangrento, ele não fica bem assim? Esse é o lugar que ele merece ficar....{/i}{/cps}"
                    "???" "{cps=40}{i}Agora pega a cabeça dele, mostra pra ele quem manda aqui Kioku, finaliza ele assim como você fez no passado.... Eu sei que você quer....{/i}{/cps}"
                    "???" "{cps=40}{i}Porque você ta parado Kioku? Vamos, eu sei que você queria ele bem pior do que ja está, e eu sei.... Que você consegue fazer ele ficar pior.{/i}{/cps}"
                    "???" "{cps=40}{i}{size=+25}VAMOS KIOKU, MOSTRE PARA ELE COM QUEM ELE TA MECHENDO, MOSTRA PRA ELE QUEM É KIOKU AIDA{/size}{/i}{/cps}"
                    menu:
                        "{b}{i}FiNaLiZaR O SuBuRu{/i}{/b}":
                            "{cps=40}Kioku pega Subaru pelo cabelo, como se não fosse nada, apenas uma carne que retirou do freezer....{/cps}"
                            "{cps=40}Olha para ele, ainda consciente, seus olhos marejados de dor, pedindo por qualquer perdão.....{/cps}"
                            "{cps=40}Mas Kioku não queria saber sobre perdoa-lo....{/cps}"
                            "{cps=40}Única coisa que passava pela cabeça de Kioku era que Subaru não sofreu o suficiente.{/cps}"
                            "{cps=40}Kioku então, joga Subaru no chão que grita de dor pelo impacto, o mesmo começa a gritar por socorro, com sua voz fraca por estar se engasgando com seu próprio sangue....{/cps}"
                            "{cps=40}Kioku olha para Subaru, seus olhos que agora eram olhos vazios, completamente pretos....{/cps}"
                            k morte "{cps=40}Odeio gente barulhenta...{/cps}"
                            play audio "audio/headbreak.mp3"
                            "{cps=40}Kioku esmaga a cabeça de Subaru contra o chão, o som da cabeça rompendo, seus ossos quebrando, aquele não era mais o Kioku....{/cps}"
                            $ unlock_achievement('killerpassager')
                            jump oquerealmenteaconteceu2
                        "{b}{i}FiNaLiZaR SuBuRu{/i}{/b}":
                            "{cps=40}Kioku pega Subaru pelo cabelo, como se não fosse nada, apenas uma carne que retirou do freezer....{/cps}"
                            "{cps=40}Olha para ele, ainda consciente, seu rosto parecia distorcido, seus olhos marejados de dor, rindo e pedindo por mais.....{/cps}"
                            "{cps=40}Kioku sabia que aquele não era o Subaru, mas ele não reclamava, porque ele queria realmente fazer Subaru sofrer mais...{/cps}"
                            "{cps=40}Kioku olha nos fundos dos olhos de Subaru, o joga no chão com toda sua força, e se ajoelha por cima dele.{/cps}"
                            "{cps=40}Cerra seus punhos, prontos para mais um round.... e então, Kioku começa...{/cps}"
                            "1"
                            "2"
                            "3"
                            "4"
                            "5"
                            "6"
                            "7"
                            "{cps=40}....{/cps}"
                            "{cps=40}Kioku ja perdeu as contas, apenas continuava, até ele não poder mais....{/cps}"
                            "{cps=40}Então, ele continua, de novo...{/cps}"
                            "{cps=40}De novo....{/cps}"
                            "{cps=40}De novo....{/cps}"
                            "{cps=40}E de novo...{/cps}"
                            "{cps=40}Kioku da o seu último soco, com suas mãos pingando a sangue, seus punhos roxos de tanto bater, ele finalmente para....{/cps}"
                            "{cps=40}E então, quando olha para o que restou de Subaru, onde era para ser seu rosto, apenas muitos hematomas, e um rosto irreconhecível...{/cps}"
                            "{cps=40}Kioku se levanta, com um grande suspiro, e um alivio junto ao um sentimento bom em seu peito...{/cps}"
                            "???" "{cps=40}{i}Isso Kioku, é isso que ele merece, alguem fraco como ele, não merece seu perdão, você mostrou a ele o {size=+10}SEU{/size} lugar{/i}{/cps}"
                            "{cps=40}Kioku respira fundo, ele então fecha os olhos por um momento e abre-os novamente processando tudo isso{/cps}"
                            $ unlock_achievement('killerpassager')
                            jump oquerealmenteaconteceu2
        "ignorar ele":
            $ subaruignorado = True
            k normal "{cps=40}\"Fala o que você quiser Subaru, eu tenho uma vida pela frente, não quero você atrapalhando ela.{/cps}\""
            hide Subaru irritado
            with dissolve
            "{cps=40}Kioku passa pelo Subaru que da um encontro de ombros nele de propósito, e então, começa a seguir em direção a sua sala.{/cps}"
            jump provafinal

label discussaoatraso:
    k triste "{cps=40}{i}Cheguei na faculdade atrasado... não tem ninguem no pátio, e pela janela parece que ninguém nos corredores, meu deus do céu eu tenho que correr.{/i}{/cps}"
    k normal "{cps=40}{i}Vou correr para a sala de aula o mais rápido possível, quem sabe eu consiga chegar a tempo.{/i}{/cps}{nw}"
    pause 0.5
    "???" "{cps=40}\"Aonde vai com tanta pressa Kioku? Perdeu o trem foi?{/cps}\""
    k bravo "{cps=40}{i}Merda... não é possivel que esse cara ainda ta aqui, porque caralhos ele não ta na aula dele?{/i}{/cps}"
    show Subaru sorisso
    with dissolve
    si sorisso "{cps=40}\"Ei, Kioku, espera, não precisa ter tanta pressa assim.\""
    k bravo "{cps=40}\"Não começa Subaru, por favor, eu to atrasado pra prova final, eu não tenho tempo pra perder contigo hoje, sai fora.{/cps}\""
    hide Subaru sorisso
    show Subaru bravo1
    si bravo1 "{cps=40}\"Ei Kioku, relaxa mano, é assim que se fala com o Prêsidente do Clube Estudantil?{/cps}\""
    k bravo "{cps=40}{i}Como caralhos esse cara conseguiu chegar a presidência? Meu deus.{/i}{/cps}"
    menu:
        "Confrontar Subaru":
            $ provaatraso = True
            $ subarusangue = True
            k irritado "{cps=40}\"Escuta aqui Subaru Ichida do caralho, eu tenho uma prova que é importante pra mim, eu to cagando se tu não quer nada com nada nessa vida, agora sai da minha frente.{/cps}\""
            hide Subaru bravo1
            show Subaru bravo2
            si bravo2 "{cps=40}\"Escuta aqui Kioku, você tem que me respeitar, eu sou o presidente do grêmio estudantil, e você apenas um aluno, posso facilmente acabar com sua vida na faculdade Kioku.{/cps}\""
            k irritado "{cps=40}\"Você acha que vou ter medo do filinho do Diretor? Eu só quero ir pra minha sala de aula, agora sai da minha frente antes que eu te arrebente.{/cps}\""
            hide Subaru bravo2
            show Subaru irritado
            si irritado "{cps=40}\"Você quer mesmo arriscar Kioku, o que sua mamãzinha falaria se fosse suspenso? Ou nem da sua mãe você se lembra?\""
            menu:
                "{b}{i}SoCaR A PoRrA dO SuBuRu{/i}{/b}":
                    stop music fadeout 1.0
                    play music "audio/Musicas/KiokuI.mp3" fadein 1.0
                    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                    scene narrador
                    with dissolve
                    "???" "{cps=40}{i}Kioku, você sabe o que fazer....{/i}{/cps}"
                    "???" "{cps=40}{i}Ele merece conhecer o verdadeiro Kioku Aida, mostre a ele quem você é.{/i}{/cps}"
                    "???" "{cps=40}{i}Ele merece a morte.... E você é ELA, mostre que não se deve mexer com a morte.{/i}{/cps}"
                    "{cps=40}Kioku cerra os punhos, encara Subaru nos fundos dos olhos, com aquele sorriso debochado, e então, Kioku pega Subaru pelo pescoço.{/cps}"
                    "{cps=40}Ele o ergue do chão, Subaru começa a se debater, tentando se soltar, mas Kioku o segura firme, como se fosse nada....{/cps}"
                    "{cps=40}E então, com sua mão, ele começa....{/cps}"
                    "1"
                    "2"
                    "3"
                    "4"
                    "5"
                    "6"
                    "{cps=40}Naquele momento Kioku perdeu as contas de quantos socos ele deu em Subaru, era como se tudo ao redor tivesse parado, a sua mente apenas pensava em sangue, e a única coisa que existia era ele e Subaru....{/cps}"
                    "{cps=40}Kioku não sentia dor, não sentia cansaço, tudo que ele sentia era uma raiva incontrolável, uma vontade de fazer Subaru pagar por tudo que ele fez....{/cps}"
                    "{cps=40}E assim, Kioku continua.{/cps}"
                    "{cps=40}Kioku finalmente para, ele não sabe por quanto tempo bateu no rosto de Subaru, ele só sabe que antes era uma pessoa que se debatia em seu braço....{/cps}"
                    "{cps=40}Agora era um corpo sendo segurado como se fosse carne, onde era para ser seu rosto, apenas um buraco afundado irreconhecível.{/cps}"
                    "{cps=40}Kioku larga o que um dia era o corpo de Subaru, seus punhos pingando sangue, suas falanges completamente enroxadas, ele olha para frente.{/cps}"
                    "{cps=40}E um grande sorisso toma conta de seu rosto, aquele sangue nas suas mãos, lhe fazia bem, {i}\"ele recebeu o que merecia\"{/i}.{/cps}"
                    "{cps=40}Por um segundo, então, Kioku fecha os olhos e respira fundo.{/cps}"
                    $ unlock_achievement('killerpassager')
                    jump oquerealmenteaconteceu
                "{b}{i}SoCaR SuBuRu{/i}{/b}":
                    stop music fadeout 1.0
                    play music "audio/Musicas/KiokuI.mp3" fadein 1.0
                    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                    scene narrador
                    with dissolve
                    "{cps=40}Kioku fecha seus punhos, é como se tudo ao redor ficasse lento, vendo Subaru Ichida na sua frente, rindo dele, e de sua situação....{/cps}"
                    "???" "{cps=40}{i}Ele ri de você Kioku, como se você fosse ninguém, ele ri da sua situação, você vai mesmo deixar ele te tratar dessa forma?{/i}{/cps}"
                    "???" "{cps=40}{i}Não..... você não vai deixar isso acontecer.... VOCÊ NÃO PODE DEIXAR ISSO ACONTECER.{/i}{/cps}"
                    "???" "{cps=40}{i}ELE RI DE VOCÊ.... ELE ZOA DA SUA SITUAÇÃO..... ELE RI DA SUA FAMILIA, AMIGOS E DE TODO MUNDO....{/i}{/cps}"
                    "???" "{cps=40}{i}{size=+10}ELE{/size} {size=+15}TEM{/size} {size=+20}QUE{/size} {size=+25}PAGAR....{/size}{/i}{/cps}"
                    "{cps=40}Tudo ficou escuro na visão de Kioku, unica coisa que ele conseguia ouvir era....{/cps}"
                    "{cps=40}De novo....{/cps}"
                    "{cps=40}De novo....{/cps}"
                    "{cps=40}De novo....{/cps}"
                    "{cps=40}E de novo...{/cps}"
                    "{cps=40}Até que.....{/cps}"
                    pause 1.0
                    "{cps=40}Kioku para de bater.... suas mãos encharcadas de sangue....{/cps}"
                    "???" "{cps=40}{i}É bom né Kioku, esse sentimento.... de prazer ao ver alguêm {size=+10}DESPREZIVEL{/sizel} como ele no chão...{/i}{/cps}"
                    "???" "{cps=40}{i}Olha para ele.... no chão..... seu rosto todo sangrento, ele não fica bem assim? Esse é o lugar que ele merece ficar....{/i}{/cps}"
                    "???" "{cps=40}{i}Agora pega a cabeça dele, mostra pra ele quem manda aqui Kioku, finaliza ele assim como você fez no passado.... Eu sei que você quer....{/i}{/cps}"
                    "???" "{cps=40}{i}Porque você ta parado Kioku? Vamos, eu sei que você queria ele bem pior do que ja está, e eu sei.... Que você consegue fazer ele ficar pior.{/i}{/cps}"
                    "???" "{cps=40}{i}{size=+25}VAMOS KIOKU, MOSTRE PARA ELE COM QUEM ELE TA MECHENDO, MOSTRA PRA ELE QUEM É KIOKU AIDA{/size}{/i}{/cps}"
                    menu:
                        "{b}{i}FiNaLiZaR O SuBuRu{/i}{/b}":
                            "{cps=40}Kioku pega Subaru pelo cabelo, como se não fosse nada, apenas uma carne que retirou do freezer....{/cps}"
                            "{cps=40}Olha para ele, ainda consciente, seus olhos marejados de dor, pedindo por qualquer perdão.....{/cps}"
                            "{cps=40}Mas Kioku não queria saber sobre perdoa-lo....{/cps}"
                            "{cps=40}Única coisa que passava pela cabeça de Kioku era que Subaru não sofreu o suficiente.{/cps}"
                            "{cps=40}Kioku então, joga Subaru no chão que grita de dor pelo impacto, o mesmo começa a gritar por socorro, com sua voz fraca por estar se engasgando com seu próprio sangue....{/cps}"
                            "{cps=40}Kioku olha para Subaru, seus olhos que agora eram olhos vazios, completamente pretos....{/cps}"
                            k morte "{cps=40}Odeio gente barulhenta...{/cps}"
                            play audio "audio/headbreak.mp3"
                            "{cps=40}Kioku esmaga a cabeça de Subaru contra o chão, o som da cabeça rompendo, seus ossos quebrando, aquele não era mais o Kioku....{/cps}"
                            $ unlock_achievement('killerpassager')
                            jump oquerealmenteaconteceu
                        "{b}{i}FiNaLiZaR SuBuRu{/i}{/b}":
                            "{cps=40}Kioku pega Subaru pelo cabelo, como se não fosse nada, apenas uma carne que retirou do freezer....{/cps}"
                            "{cps=40}Olha para ele, ainda consciente, seu rosto parecia distorcido, seus olhos marejados de dor, rindo e pedindo por mais.....{/cps}"
                            "{cps=40}Kioku sabia que aquele não era o Subaru, mas ele não reclamava, porque ele queria realmente fazer Subaru sofrer mais...{/cps}"
                            "{cps=40}Kioku olha nos fundos dos olhos de Subaru, o joga no chão com toda sua força, e se ajoelha por cima dele.{/cps}"
                            "{cps=40}Cerra seus punhos, prontos para mais um round.... e então, Kioku começa...{/cps}"
                            "1"
                            "2"
                            "3"
                            "4"
                            "5"
                            "6"
                            "7"
                            "{cps=40}....{/cps}"
                            "{cps=40}Kioku ja perdeu as contas, apenas continuava, até ele não poder mais....{/cps}"
                            "{cps=40}Então, ele continua, de novo...{/cps}"
                            "{cps=40}De novo....{/cps}"
                            "{cps=40}De novo....{/cps}"
                            "{cps=40}E de novo...{/cps}"
                            "{cps=40}Kioku da o seu último soco, com suas mãos pingando a sangue, seus punhos roxos de tanto bater, ele finalmente para....{/cps}"
                            "{cps=40}E então, quando olha para o que restou de Subaru, onde era para ser seu rosto, apenas muitos hematomas, e um rosto irreconhecível...{/cps}"
                            "{cps=40}Kioku se levanta, com um grande suspiro, e um alivio junto ao um sentimento bom em seu peito...{/cps}"
                            "???" "{cps=40}{i}Isso Kioku, é isso que ele merece, alguem fraco como ele, não merece seu perdão, você mostrou a ele o {size=+10}SEU{/size} lugar{/i}{/cps}"
                            "{cps=40}Kioku respira fundo, ele então fecha os olhos por um momento e abre-os novamente processando tudo isso{/cps}"
                            $ unlock_achievement('killerpassager')
                            jump oquerealmenteaconteceu
        "ignorar ele":
            $ provaatraso = False
            $ subaruignorado = True
            k normal "{cps=40}\"Fala o que você quiser Subaru, eu tenho uma vida pela frente, não quero você atrapalhando ela.{/cps}\""
            hide Subaru irritado
            with dissolve
            "{cps=40}Kioku passa pelo Subaru que da um encontro de ombros nele de propósito, e então, começa a seguir em direção a sua sala.{/cps}"
            jump provafinal

label oquerealmenteaconteceu:
    $ unlock_achievement('darkpassager')
    stop music fadeout 1.0
    play music "audio/Musicas/school.mp3" fadein 1.0
    $ renpy.music.set_volume(0.85, delay=1.0, channel='music')
    scene entradaescoladia
    with dissolve
    "{cps=40}Kioku abre os olhos, e se vê, ainda na entrada da Faculdade, ele, então, rapidamente olha para suas mãos{/cps}"
    "{cps=40}Elas estão limpas, sem nenhum arranhão, sem nenhum sinal de sangue{/cps}"
    "{cps=40}{i}\"Aquilo foi tudo uma imaginação?\"{/i} Kioku pensa, mas então, ele olha para frente, e ve Subaru com seu nariz sangrando{/cps}"
    show Subaru sangue
    with dissolve
    si sangue "{cps=40}\"I-isso n-não vai ficar assim Kioku....\"{/cps}"
    k normal "{cps=40}\"Não Subaru, o que vai acontecer é que você não vai mais mexer comigo..... Porque da próxima vez vai ser pior.\"{/cps}"
    call rolar_d20 (dc=10, atributo='labia', titulo="Teste de Intimidação: Subaru", reveal_result = True)
    $ resultado = _return
    if resultado:
        si sangue "{cps=40}\"....{/cps}\""
        si sangue "{cps=40}\"....{/cps}\""
        si sangue "{cps=40}\"Eu ainda irei resolver isso com você, g-guarde minhas palavras...\"{/cps}"
        hide Subaru sangue
        with dissolve
        k normal "{cps=40}{i}Finalmente, que merda cara, eu não queria ter feito isso, puta que pariu, bom, eu tenho que correr agora...{/i}{/cps}"
        k normal "{cps=40}{i}Espero que dê tempo ainda....{/i}{/cps}"
        jump provafinal
    else:
        si sangue "{cps=40}\"Não vou parar até a gente resolver isso, vai pra tua aul agora...\"{/cps}"
        hide Subaru sangue
        with dissolve
        k normal "{cps=40}{i}Agora eu preciso ir pra sala de aula, antes que eu me atrase mais ainda...{/i}{/cps}"
        jump provafinal 

label oquerealmenteaconteceu2:
    $ unlock_achievement('darkpassager')
    stop music fadeout 1.0
    play music "audio/Musicas/school.mp3" fadein 1.0
    $ renpy.music.set_volume(0.85, delay=1.0, channel='music')
    scene biblioteca2
    with dissolve
    "{cps=40}Kioku abre os olhos, e se vê, ainda na biblioteca, ele, então, rapidamente olha para suas mãos{/cps}"
    "{cps=40}Elas estão limpas, sem nenhum arranhão, sem nenhum sinal de sangue{/cps}"
    "{cps=40}{i}\"Aquilo foi tudo uma imaginação?\"{/i} Kioku pensa, mas então, ele olha para frente, e ve Subaru com seu nariz sangrando{/cps}"
    show Subaru sangue
    with dissolve
    si sangue "{cps=40}\"I-isso n-não vai ficar assim Kioku....\"{/cps}"
    k normal "{cps=40}\"Não Subaru, o que vai acontecer é que você não vai mais mexer comigo..... Porque da próxima vez vai ser pior.\"{/cps}"
    call rolar_d20 (dc=10, atributo='labia', titulo="Teste de Intimidação: Subaru", reveal_result = True)
    $ resultado = _return
    if resultado:
        si sangue "{cps=40}\"....{/cps}\""
        si sangue "{cps=40}\"....{/cps}\""
        si sangue "{cps=40}\"Eu ainda irei resolver isso com você, g-guarde minhas palavras...\"{/cps}"
        hide Subaru sangue
        with dissolve
        "{cps=40}Subaru começa a se afastar enquanto murmura algo para ele mesmo{/cps}"
        si sangue "{cps=40}Merda, agora tenho que me limpar, não posso me apresentar pra aluna nova assim{/cps}"
        k normal "{cps=40}{i}Finalmente, que merda cara, eu não queria ter feito isso, puta que pariu, bom, eu tenho que correr agora...{/i}{/cps}"
        k normal "{cps=40}{i}Espero que dê tempo ainda....{/i}{/cps}"
        jump provafinal
    else:
        si sangue "{cps=40}\"Não vou parar até a gente resolver isso\"{/cps}"
        hide Subaru sangue
        with dissolve
        "{cps=40}Subaru começa a se afastar enquanto murmura algo para ele mesmo{/cps}"
        si sangue "{cps=40}Merda, agora tenho que me limpar, não posso me apresentar pra aluna nova assim{/cps}"
        k normal "{cps=40}{i}Agora eu preciso ir pra sala de aula, antes que eu me atrase mais ainda...{/i}{/cps}"
        jump provafinal 



label provafinal:
    stop music fadeout 1.0
    play music "audio/Musicas/WAV_Everyday_Life.mp3" fadein 1.0
    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
    if provaatraso == True:
        scene corredordia
        with pixellate
        k normal "{cps=40}\"Tá, qual a sala mesmo? Hm....Ah, aquela ali.\"{/cps}"
        scene salaauladia
        with pixellate
        "{cps=40}Kioku entra na sala correndo, ele então para, o professor que estava cuidando de todos da turma olha para ele.{/cps}"
        show Yuki normal
        with dissolve
        y normal "{cps=40}\"Senhor Aida, está atrasado....De novo.... Você terá 1 período a menos que o restante da turma. Por favor, tome seu assento rapidamente para que você possa começar a prova final.{/cps}\""
        k normal "{cps=40}\"Desculpe professor Yuki, não vai mais acontecer.{/cps}\""
        hide Yuki normal
        show dissolve
        y normal "{cps=40}Sei....{/cps}"
        "{cps=40}Diz o Professor Yuki enquanto se afasta para cuidar dos outros alunos{/cps}"
        "{cps=40}Kioku então se senta numa das classes vazias, e começa a se concentrar na resolução da prova.{/cps}"
        scene narrador
        with dissolve
        "{cps=40}Algumas horas se passam, até que Kioku consegue terminar sua prova final, e faltando poucos minutos antes do término, ele a entrega para o professor Yuki.{/cps}"
        "{cps=40}Ele então se levanta da classe, e quando estava saindo da sala, ele ouve uma voz{/cps}"
        scene salaauladia
        with dissolve
        "???" "\"{cps=40}Psiiiiu, Kioku, aquiiii....\"{/cps}"
        "{cps=40}Kioku se vira na direção da voz, num dos cantos da sala.{/cps}"
        show JinseiFeliz3 at center
        with dissolve
        j Feliz3 "{cps=40}\"Aqui Kioku.{/cps}\""
        k feliz "{cps=40}{i}A Jinsei ja terminou a prova.{/i}{/cps}"
        "{cps=40}Kioku então, vai até a cadeira na frente de Jinsei, que animada começa a falar com ele.{/cps}"
        j Feliz3 "{cps=40}\"Eai como foi na prova?\"{/cps}"
        hide JinseiFeliz3
        show JinseiFeliz at center
        k normal "{cps=40}\"Foi bem, obrigado por perguntar...{/cps}\""
        hide JinseiFeliz 
        show JinseiTriste at center
        j Triste "{cps=40}\"Ta tudo bem Kioku? Aconteceu algo?{/cps}\""
        menu:
            "Contar sobre Subaru":
                $ amizade_add("jinsei", 3)
                if trematraso == True:
                    k normal "{cps=40}\"O Ichida quase me fez chegar atrasado da prova.\"{/cps}"
                    k normal "{cps=40}\"Ele parecia que não queria que eu fizesse a prova, porque tentou me segurar na biblioteca.\"{/cps}"
                else:
                    k normal "{cps=40}\"O Ichida quase me fez chegar atrasado da prova.\"{/cps}"
                    k normal "{cps=40}\"Ele parecia que não queria que eu fizesse a prova, porque tentou me segurar na entrada da Faculdade.\"{/cps}"
                hide JinseiTriste 
                show JinseiIrritada
                j Irritada "{cps=40}\"Esse Subaru, não para de te incomodar, depois eu converso com o diretor.\"{/cps}"
                k normal "{cps=40}\"Não se estressa com isso, eu só tento ignorar ele, e ta tudo bem.\"{/cps}"
                hide JinseIrritada 
                show JinseiTriste
                j Triste "{cps=40}\"Tem certeza? Ele é insistente...\"{/cps}"
                k normal "{cps=40}\"Tenho sim, ja resolvi a situação, ele não vai mais me incomodar\"{/cps}"
                hide JinseiTriste
                show JinseiSurpresa
                j Surpresa "{cps=40}\"Sério? O que você fez pra lidar com ele?\"{/cps}"
                menu:
                    "Contar a Verdade":
                        $ amizade_add("jinsei", 1)
                        k normal "{cps=40}\"Eu... dei um soco na cara dele, e o nariz dele sangrou, acho que quebrou ou deslocou, sei lá{/cps}"
                        hide JinseiSurpresa
                        show JinseiNormal
                        j Normal "{cps=40}\"Meu deus... E como foi?\"{/cps}"
                        "{cps=40}Jinsei responde com um tom de normalidade, como se não estivesse surpresa com o que o Kioku fez.{/cps}"
                        j Normal "{cps=40}\"Sentiu algo? Foi bom?\"{/cps}"
                        k normal "{cps=40}\"Não sei, eu não senti nada, mas ele sangrou bastante...\"{/cps}"
                        k divertindo "{cps=40}\"Mas acho que eu não acharia bom ou me sentir bem em bater em alguem hahaha\"{/cps}"
                        hide JinseiNormal
                        show JinseiFeliz4
                        j Feliz4 "{cps=40}\"Eu sei hahaha, mas vai que você é um serial killer né uuuuuuuuh.\"{/cps}"
                        "{cps=40}Jinsei fala isso com um tom de brincadeira, tentando falhamente imitar um fantasma.{/cps}"
                        k divertindo "{cps=40}\"hahaha, você nunca saberá.{/cps}\""
                        hide JinseiFeliz4
                        show JinseiFeliz2
                        j Feliz2 "{cps=40}\"hahaha...\"{/cps}"
                        hide JinseiFeliz2
                        show JinseiFeliz
                        j Feliz "{cps=40}\"Mas foi só isso? O soco? Ou algo a mais? \"{/cps}"
                        k normal "{i}{cps=40}Além das visões que eu tive de bater no Subaru até a morte.... Não sei se devo contar a Jinsei, e se ela achar que eu sou um louco?{/cps}{/i}"
                        menu:
                            "Contar o que realmente aconteceu":
                                $ amizade_add("jinsei", 2)
                                k normal "{cps=40}\"Na verdade... eu tive umas visões, de bater no Subaru, e de fazer ele sofrer, e de matar ele...\"{/cps}"
                                hide JinseiFeliz
                                show JinseiChocada
                                j Chocada "{cps=40}\"O-oi? O que? Você teve o que?\"{/cps}"
                                k normal "{cps=40}\"Eu sei que parece loucura, mas eu tive essas visões, e elas eram tão reais...\"{/cps}"
                                j Chocada "{cps=40}\"I-isso é muito estranho Kioku... V-você tem certeza que não s-se preciptou?\"{/cps}"
                                "{i}{cps=40}Pela primeira vez, Jinsei parece realmente assustada, impressionando até mesmo Kioku{/i}{/cps}"
                                k normal "{cps=40}\"Não sei... Eu só sei que eu tive essas visões, e elas eram tão reais...\"{/cps}"
                                j Chocada "{cps=40}\"B-bom... Se você tiver mais dessas visões, me conte tá? E se sentir algo estranho, me avisa também...\"{/cps}"
                                k normal "{cps=40}\"Pode deixar Jinsei... Obrigado por me ouvir...\"{/cps}"
                                hide JinseiChocada
                                show JinseiFeliz2
                                j Feliz2 "{cps=40}\"Claro, você pode contar comigo pra tudo.\"{/cps}"
                                $ show_consequence("Jinsei se lembrará disso", 3)
                                $ consequência_ativada["jinsei_visao_subaru"] = True
                                hide JinseiFeliz2
                                show JinseiFeliz
                                j Feliz "{cps=40}\"Mas bem, se você diz que está tudo bem e resolveu, por mim tá ótimo, espero que ele pare de incomodar você...\"{/cps}"
                            "Não contar o que realmente aconteceu":
                                    k normal "{cps=40}\"Ah, na verdade, não, eu só... dei um soco nele, e ele sangrou bastante...\"{/cps}"
                                    hide JinseiChocada
                                    show JinseiNormal
                                    j Normal "{cps=40}\"Ah, entendi... Mas se tiver mais alguma coisa, me conta tá?\"{/cps}"
                                    k normal "{cps=40}\"Pode deixar Jinsei... Obrigado por me ouvir...\"{/cps}"
                                    hide JinseiNormal
                                    show JinseiFeliz
                                    j Feliz "{cps=40}\"Mas bem, se você diz que está tudo bem e resolveu, por mim tá ótimo, espero que ele pare de incomodar você...\"{/cps}"
                    "Esconder a Verdade":
                        call rolar_d20 (dc=9, atributo='labia', titulo="Teste de Lábia: Esconder a Verdade", reveal_result = True)
                        $ resultado = _return
                        if resultado:
                            k normal "{cps=40}\"Nada de mais, eu apenas conversei com ele, e ele ficou meio irritado, e saiu da minha vista, graças a deus hahahaha\"{/cps}"
                            j Feliz "{cps=40}\"Bem, se você diz que está tudo bem e resolveu, por mim tá ótimo, espero que ele pare de incomodar você...\"{/cps}"
                        else:
                            $ amizade_add("jinsei", -1)
                            k normal "{cps=40}\"Ah, nada que você precisa se preocupar, de verdade, ta tudo tranquilo e resolvido...\"{/cps}"
                            hide JinseiSurpresa
                            show JinseiFeliz
                            j Feliz "{cps=40}\"Bem....\nSe você diz que está tudo bem e resolveu, por mim tá ótimo, espero que ele pare de incomodar você...\"{/cps}"
                stop music fadeout 1.0
                play music "audio/Musicas/kiokumente.mp3"
                "???" "{cps=40}{i}\"Ah sim... pode ter certeza que ele não vai mais incomodar nós dois...\"{i}{/cps}"
                "???" "{cps=40}{i}\"E se ele tentar enfrentar nós dois novamente, ele vai desejar nunca ter conheciodo a gente...\"{/i}{/cps}"
                k surpreso "{i}{cps=40}O que? Essa voz? Foi a mesma que conversou comigo nas visões com o Subaru?{/i}{/cps}"
                k surpreso "{i}{cps=40}Porque eu sinto que ela é tão real, até parece que ele está aqui na sala comigo ag{nw}"
                show JinseiFeliz at left_pos with move
                show KiokuM at right_pos with moveinright
                "???" "{cps=40}{i}\"Olá Kioku, é bom te ver de novo...\"{/i}{/cps}"
                k surpreso "{i}{cps=40}P-porque você é tão parecido comigo? O que caralhos é você?{/i}{/cps}"
                "???" "{cps=40}{i}\"Ora... ja esqueceu de mim? Bem, não posso culpar você, faz tanto tempo depois daquele dia...\"{/i}{/cps}"
                "???" "{cps=40}{i}\"Desde então, eu estava lá, adormecido na sua consiência, esperando o momento certo para aparecer de novo...\"{/i}{/cps}"
                k surpreso "{i}{cps=40}O que? Você estava adormecido na minha consciência?\nQuem é você?\nO que é você?\nO que você quer de mim?{/i}{/cps}"
                $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
                play sound "audio/SoundsEffect/sina2.mp3"
                pause 2.0
                stop sound fadeout 1.0
                $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                "???" "{cps=40}{i}\"Opa, acho que deu minha hora, então eu acho melhor a gente deixar isso para depois.\"{/i}{/cps}"
                "???" "{cps=40}{i}\"Nos veremos em breve Kioku....\"{/i}{/cps}"
                hide KiokuM with moveoutright
                show Yuki normal at right_pos with moveinright
                y normal "{cps=40}\"Senhor Ainda, você ouviu o que eu falei?\"{/cps}"
                k normal "{cps=40}\"Não senhor, eu acabei me distraindo nos meus pensamentos...\"{/cps}"
                "{cps=40}Yuki olha para Kioku, dando um suspiro profundo.{/cps}"
                y normal "{cps=40}\"Tome cuidado com os horários, senhor Aida, dessa vez eu permitirei porque é a última prova deste semestre.\"{/cps}"
                k normal "{cps=40}\"Obrigado professor Yuki...\"{/cps}"
                hide JinseiFeliz with moveoutleft
                hide Yuki normal with moveoutright
                "{cps=40}Kioku pega suas coisas, e começa a se retirar da sala, se despedindo de Jinsei no caminho\nEle, então, desce as escadas, até que houve uma voz.{/cps}"
                jump encontrostella
            "Não contar a verdade":
                call rolar_d20 (dc=9, atributo='labia', titulo="Teste de Lábia: Esconder a Verdade", reveal_result = True)
                $ resultado = _return
                if resultado:
                    k normal "{cps=40}\"Não foi nada, é que eu me atrasei um pouco hahaha, ai eu acabei perdendo um período, mas o que importa é que eu fiz a prova inteira.\"{/cps}"
                    hide JinseiTriste
                    show JinseiFeliz at center
                    j Feliz "{cps=40}\"Bem, se foi só isso hahaha, eu falei pra você não se atrasar idiota!\"{/cps}"
                    k feliz "{cps=40}\"Hahaha, eu sei, foi mal, mas não vai acontecer mais, fica tranquila\"{/cps}"
                else:
                    k normal "{cps=40}\"Nada, eu só to meio avoado, mas ta tudo certo\"{/cps}"
                    hide JinseiTriste
                    show JinseiFeli at center
                    j Feliz "{cps=40}\"Bom, se você diz, então eu fico tranquila\"{/cps}"
                "{cps=40}Kioku pega suas coisas, e começa a se retirar da sala, se despedindo de Jinsei no caminho\nEle, então, desce as escadas, até que houve uma voz.{/cps}"
                jump encontrostella
    else:
        if trematraso == True:
            scene escadaescoladia
            with pixellate
            k normal "{cps=40}\"Meu deus, faltam 2 minutos, ainda bem que eu ignorei o Subaru, se não eu taria ferrado.{/cps}\""
            scene corredordia
            with pixellate
            k normal "{cps=40}\"Qual a sala mesmo?...{/cps}\""
            k normal "{cps=40}\"Ah é essa.{/cps}\""
            scene salaauladia
            with pixellate
            "{cps=40}Kioku entra na sala, com poucas cadeiras livres, visto que ele chegou faltando 2 minutos para o começo da prova.{/cps}"
            "{cps=40}Ele então ouve algo.{/cps}"
            "???" "{cps=40}\"Psiiiiu, Kioku, aquiiii....\"{/cps}"
            "{cps=40}Kioku se vira na direção da voz, num dos cantos da sala.{/cps}"
            show JinseiFeliz3 at center
            with dissolve
            j Feliz3 "{cps=40}\"Aqui Kioku, tem essa cadeira livre{/cps}\""
            k feliz "{i}{cps=40}Jinsei ja tá ai, que bom que ela guardou um lugar pra mim{/i}{/cps}"
            "{cps=40}Kioku, então, vai em direção a Jinsei, e senta na classe a frente dela.{/cps}"
            hide JinseiFeliz3
            show JinseiFeliz2 at center
            j Feliz2 "{cps=40}\"Eai, como ta seus estudos? Estudou pra essa prova?\"{/cps}"
            k normal "{cps=40}\"Ah, dei uma revisada vindo pra sala, ta tranquilo.\"{/cps}"
            hide JinseiFeliz2
            show JinseiTriste at center
            j Triste "{cps=40}\"Ce ta bem? aconteceu algo?\"{/cps}"
            k normal "{cps=40}\"Ah ta tudo certo, o Subaru quase me atrasou pra prova, mas ignorei ele.\"{/cps}"
            hide JinseiTriste
            show JinseiFeliz2
            j Feliz2 "{cps=40}\"Bem, o bom é que você não se atrasou\"{/cps}"
            k normal "{cps=40}\"Exato, mas ea{nw}{/cps}"
            show JinseiFeliz at left_pos with move
            show Yuki normal at right_pos with moveinright
            y normal "{cps=40}\"Desculpa atrapalhar a conversa importantissima de vocês, mas tenho uma prova para aplicar, por favor, se ajeitem\"{/cps}"
            "{cps=40}Professor Yuki olha em direção ao Kioku surpreso{/cps}"
            y normal "{cps=40}\"Senhor Aida, você não chegou atrasado, que surpresa\"{/cps}"
            "{cps=40}{i}Por alguns segundos Kioku percebe um leve sorriso no Professor Yuki{/i}{/cps}"
            k feliz "{cps=40}\"Quando se trata das suas aulas senhor Yuki, é sempre pontual\"{/cps}"
            k feliz "{cps=40}\"O senhor sendo o melhor professor que ja tivemos, e que sempre{nw}"
            y normal "{cps=40}\"Não abuse da minha gratidão senhor Aida{/cps}"
            "{cps=40}O professor Yuki, então, caminha em direção a sua classe enquanto diz.{/cps}"
            y normal "{cps=40}\"Muito bem pessoal, chegamos a última prova deste semestre, esperam que tenham estudado, vocês sabem que a última sempre é a pior, com base nos antigos alunos.{/cps}"
            y normal "{cps=40}\"Mas não se preocupem, dessa vez está fácil, facilitei a prova para vocês, visto que são uma turma incrível\"{/cps}"
            "{cps=40}Quando Yuki, termina sua frase algumas conversas baixas podem ser ouvidas{/cps}"
            "Aluno A" "{cps=40}\"Sempre que ele fala isso, está pior que a última\""
            "Aluno B" "{cps=40}\"Não é pra tanto assim cara...\"{/cps}"
            "Aluno A" "{cps=40}\"É sério cara, os veteranos da Física falaram que quando ele diz isso quer dizer que mais da metade da turma vai reprovar, porque são perguntas IMPOSSÍVEIS.\"{/cps}"
            "{cps=40}Mais alguns murrmuros continuam na sala, até que Yuki termina de entregar a prova{/cps}"
            y normal "{cps=40}\"Okay senhoras e senhores.\nPodem Começar\""
            scene narrador
            with dissolve
            "{cps=40}E então, Kioku começa a fazer a prova, o foco dele é incrível, é como se o mundo ao redor tivesse sumido, e apenas a prova e ele estivessem naquele local\"{/cps}"
            "{cps=40}Se passa 1 hora, e Kioku está finalizando sua prova, Jinsei ja havia terminado e saido da sala, faltava apenas Kioku e alguns poucos alunos{/cps}"
            "{cps=40}Mais algums minutos, Kioku termina a prova, se leventa e entrega para Yuki, que recebe a prova e lhe deseja boa sorte.{/cps}"
            "{cps=40}Então, Kioku pega suas coisas, e começa a se retirar da sala\nEle, então, desce as escadas, até que houve uma voz.{/cps}"
            jump encontrostella
        else:        
            scene escadaescoladia
            with pixellate
            k normal "{cps=40}\"Graças a Deus, vou chegar a tempo o suficiente na prova.\"{/cps}"
            scene corredordia
            with pixellate
            k normal "{cps=40}\"Qual a sala mesmo?...{/cps}\""
            k normal "{cps=40}\"Ah é essa.{/cps}\""
            scene salaauladia
            with pixellate
            "{cps=40}Kioku entra na sala, com algumas cadeiras ainda livres, visto que ele chegou 5 minutos adiantado.{/cps}"
            "{cps=40}Ele então ouve algo.{/cps}"
            "???" "{cps=40}\"Psiiiiu, Kioku, aquiiii....\"{/cps}"
            "{cps=40}Kioku se vira na direção da voz, num dos cantos da sala.{/cps}"
            show JinseiFeliz3 at center
            with dissolve
            j Feliz3 "{cps=40}\"Aqui Kioku, tem essa cadeira livre{/cps}\""
            k feliz "{i}{cps=40}Jinsei ja tá ai, que bom que ela guardou um lugar pra mim{/i}{/cps}"
            "{cps=40}Kioku, então, vai em direção a Jinsei, e senta na classe a frente dela.{/cps}"
            hide JinseiFeliz3
            show JinseiFeliz2 at center
            j Feliz2 "{cps=40}\"Eai, como ta seus estudos? Estudou pra essa prova?\"{/cps}"
            k normal "{cps=40}\"Ah, dei uma revisada vindo pra sala, ta tranquilo.\"{/cps}"
            hide JinseiFeliz2
            show JinseiTriste at center
            j Triste "{cps=40}\"Ce ta bem? aconteceu algo?\"{/cps}"
            k normal "{cps=40}\"Ah ta tudo certo, o Subaru quase me atrasou pra prova, mas ignorei ele.\"{/cps}"
            hide JinseiTriste
            show JinseiFeliz2 at center
            j Feliz2 "{cps=40}\"Bem, o bom é que você não se atrasou\"{/cps}"
            k normal "{cps=40}\"Exato, mas eai, está pronta pra prova?\"{/cps}"
            j Feliz2 "{cps=40}\"Ah, mais ou menos, eu estudei, mas não tanto quanto eu queria...\"{/cps}"
            k surpreso "{cps=40}\"O que?\nA senhora perfeita Jinsei Boto não estudou o suficiente?\"{/cps}"
            hide JinseiFeliz2
            show JinseiFeliz4 at center
            j Feliz4 "{cps=40}\"Ah va a merda va hahahaha, eu estudei o suficiente pra mim poder passar\"{/cps}"
            k divertindo "{cps=40}\"Hahahaha, se você diz, quem sou eu pra acusar\"{/cps}"
            hide JinseiFeliz4 
            show JinseiBravanime at center
            j  bravanime "{cps=40}\"Cê vai ver, eu vou gabaritar essa prove e esfr{nw}{/cps}"
            hide JinseiFeliz
            show JinseiFeliz at left_pos with move
            show Yuki normal at right_pos with moveinright
            y normal "{cps=40}\"Desculpa atrapalhar a conversa importantissima de vocês, mas tenho uma prova para aplicar, por favor, se ajeitem.\"{/cps}"
            "{cps=40}Professor Yuki olha em direção ao Kioku surpreso{/cps}"
            y normal "{cps=40}\"Senhor Aida, você não chegou atrasado, que surpresa.\"{/cps}"
            "{cps=40}{i}Por alguns segundos Kioku percebe um leve sorriso no Professor Yuki{/i}{/cps}"
            k feliz "{cps=40}\"Quando se trata das suas aulas, senhor Yuki, sou sempre pontual.\"{/cps}"
            k feliz "{cps=40}\"O senhor sendo o melhor professor que ja tivemos, e que sempre{nw}"
            y normal "{cps=40}\"Não abuse da minha gratidão e bondade senhor Aida.{/cps}"
            "{cps=40}O professor Yuki, então, caminha em direção a sua classe enquanto diz.{/cps}"
            y normal "{cps=40}\"Muito bem pessoal, chegamos na última prova deste semestre, esperam que tenham estudado, vocês sabem que a última sempre é a pior, com base nos antigos alunos.{/cps}"
            y normal "{cps=40}\"Mas não se preocupem, dessa vez está fácil, facilitei a prova para vocês, visto que são uma turma incrível.\"{/cps}"
            "{cps=40}Quando Yuki, termina sua frase algumas conversas baixas podem ser ouvidas{/cps}"
            "Aluno A" "{cps=40}\"Sempre que ele fala isso, está pior que a última.\"{/cps}"
            "Aluno B" "{cps=40}\"Não é pra tanto assim cara...\"{/cps}"
            "Aluno A" "{cps=40}\"É sério cara, os veteranos da Física falaram que quando ele diz isso quer dizer que mais da metade da turma vai reprovar, porque são perguntas IMPOSSÍVEIS.\"{/cps}"
            "{cps=40}Mais alguns murrmuros continuam na sala, até que Yuki termina de entregar a prova{/cps}"
            y normal "{cps=40}\"Okay senhoras e senhores.\nPodem Começar!\"{/cps}"
            scene narrador
            with dissolve
            "{cps=40}E então, Kioku começa a fazer a prova, o foco dele é incrível, é como se o mundo ao redor tivesse sumido, e apenas a prova e ele estivessem naquele local.\"{/cps}"
            "{cps=40}Se passa 1 hora, e Kioku está finalizando sua prova, Jinsei ja havia terminado e saido da sala, faltava apenas Kioku e alguns poucos alunos.{/cps}"
            "{cps=40}Mais algums minutos, Kioku termina a prova, se leventa e entrega para Yuki, que recebe a prova e lhe deseja boa sorte.{/cps}"
            "{cps=40}Então, Kioku pega suas coisas, e começa a se retirar da sala\nEle, então, desce as escadas, até que houve uma voz.{/cps}"
            jump encontrostella

label encontrostella:
    stop music fadeout 1.0
    play music "audio/Musicas/voceEeu.mp3" fadein 1.0
    scene escadaescoladia
    with pixellate
    if StellaAmizade == True:
        "???" "{cps=40}\"Kioku.... É você?{/cps}\""
        "{cps=40}Kioku rapidamente se vira para ver quem estava falando com ele{/cps}"
        show Stella feliz
        with dissolve
        s feliz "{cps=40}\"Kioku, que conhecidência encontra você aqui...{/cps}\""
        k feliz "{cps=40}\"Oi Stella, que bom te ver.\"{/cps}"
        s feliz "{cps=40}\"Igualmente Kioku, eu estava passando por aqui e te vi, ai pensei em falar com você...\"{/cps}"
        k feliz "{cps=40}\"Ah, que legal, você também estuda aqui?\"{/cps}"
        hide Stella feliz
        show Stella happy1
        s happy1 "{cps=40}\"Sim, eu acabei de concluir minha transfêrencia pra cá, e me falaram que era para encontrar o Kioku que você iria me apresentar a Faculdade...\"{/cps}"
        k normal "{cps=40}\"Ah sim, claro, mas não seria o presidente do grêmio estudantil?\"{/cps}"
        hide Stella happy1
        show Stella envergonhada
        if subarusangue == True:
            s envergonhada "{cps=40}\"Ah, é, mas ele não estava disponível porque parece que ele machucou o nariz... Ai me falaram que era para me encontrar com você...\"{/cps}"
            k normal "{cps=40}\"Ah sim....\"{/cps}"
            k triste "{cps=40}{i}Merda ela não pode descobrir que fui eu que machuquei o Subaru, se não vai pensar que eu sou um bully...{/i}{/cps}"
        else:
            s envergonhada "{cps=40}\"Ah, é, mas ele não estava disponível porque parece que ele teve um imprevisto... Ai me falaram que era para me encontrar com você...\"{/cps}"
            k normal "{cps=40}\"Ah sim....\"{/cps}"
            k triste "{cps=40}{i}Subaru tendo imprevisto? Isso não é normal....{/i}{/cps}"
        hide Stela envergonhada
        show Stela triste
        s triste "{cps=40}\"O que aconteceu Kioku? Ta tudo bem?\"{/cps}"
        k normal "{cps=40}\"Ah.... oi?... Ah, sim, tudo bem, eu só.. me perdi nos pensamentos...\"{/cps}"
        k feliz "{cps=40}\"Eu lhe apresento a Faculdade sim.\"{/cps}"
        hide Stella triste
        show Stealla happy2
        s happy2 "{cps=40}\"Aeeee, obrigada Kioku, por onde começamos?\"{/cps}"
        hide Stella happy2
        scene narrador
        with dissolve
        "{cps=40}Kioku, então, começa a mostrar a Faculdade para Estella\nMostra corredores\nSalas de aulas\nCantina\nBanheiros...{/cps}"
        "{cps=40}Se passa uma hora, e então eles retornam para as escadas onde haviam se encontrado.{/cps}"
        scene escadaescoladia
        with dissolve
        show Stella feliz
        with dissolve
        s feliz "{cps=40}\"...Eai quando eu cheguei em casa, eu vejo ele embaixo da cama hahahahahaha...{/cps}\""
        hide Stella feliz 
        show Stella happy2
        s happy2 "{cps=40}\"Esse tempo todo, ele estava embaixo da minha cama, e eu dando voltas e voltas no meu bairro, hahahahah....{/cps}\""
        k divertindo "{cps=40}\"Hahahaha, você deve ter achado engraçado na hora né?\"{/cps}"
        s happy2 "{cps=40}\"Na hora eu briguei com ele porque ele não me respondia, nem quando eu chamava com a ração hahahaha.{/cps}\""
        s happy2 "{cps=40}\"Mas depois eu achei engraçado, porque ele estava lá, e eu nem tinha percebido...\"{/cps}"
        hide Stella happy2
        show Stella feliz
        s feliz "{cps=40}\"Aiai, nossa, nem vi o tempo passar, obrigada por me mostrar a Faculdade Kioku, eu adorei conhecer tudo isso...\"{/cps}"
        $ amizade_add("stella", 5)
        k feliz "{cps=40}\"Ah, que bom que você gostou Estella, eu também adorei te mostrar a Faculdade e conversar com você...\"{/cps}"
        hide Stella feliz
        show Stella envergonhada
        s envergonhada "{cps=40}\"...\"{/cps}"
        s envergonhada "{cps=40}\"Foi legal conversar com você também Kioku...\"{/cps}"
        hide Stella envergonhada
        show Stella feliz 
        s feliz "{cps=40}\"Bem, agora eu tenho que passar no mercado...\"{/cps}"
        if consequência_ativada["ajudar_estella_chave"] == True:
            s feliz "{cps=40}\"Depois quando voltar pra casa, eu te mando uma mensagem para você me ajudar a procurar a chave de hoje de manhã, se lembra?\"{/cps}"
            k feliz "{cps=40}\"Ah, claro, pode deixar, depois me avisa quando for procurar a chave...\"{/cps}"
            s feliz "{cps=40}\"Obrigada Kioku, bem, então, até mais tarde...\"{/cps}"
            k feliz "{cps=40}\"Até mais tarde Estella...\"{/cps}" 
            jump celularestella 
        else:
            s feliz "{cps=40}\"De qualquer forma, obrigada Kioku por me apresentar e pela conversa que tivemos, eu adorei.\"{/cps}"
            k feliz "{cps=40}\"Claro Estella, eu que agradeço por ter me deixado te mostrar a Faculdade, quando precisar de algo pode falar comigo.\"{/cps}"
            s feliz "{cps=40}\"Obrigada Kioku, pode deixar...\"{/cps}"            
            s feliz "{cps=40}\"Bem, então, até mais Kioku, nos vemos por aí...\"{/cps}"
            k feliz "{cps=40}\"Até mais Estella...\"{/cps}"
            jump celularestella  
    else: 
        "???" "{cps=40}\"Oi.... Com licença....{/cps}"
        "{cps=40}Kioku rapidamente se vira para ver quem estava falando com ele{/cps}"
        show Stella feliz
        with dissolve
        "???" "{cps=40}\"O-oi, desculpa te incomodar, mas me falaram que era você que iria me apresentar a Faculdade...{/cps}\""
        scene narrador
        with dissolve
        k normal "{cps=40}\"Ah, sim, claro.\"{/cps}"
        k normal "{cps=40}\"Mas bem, de qualquer forma, eu posso sim te apresentar a Faculdade, muito prazer, sou Kioku Aida, mas pode me chamar apenas de Kioku.\"{/cps}"
        $ desbloquear_Personagem("estella")
        s feliz "{cps=40}\"Muito prazer Kioku, eu sou Estella Nascimento, fui transferida para a Faculdade este ano.\"{/cps}"
        menu:
            "Perguntar sobre o nome":
                k normal "{cps=40}\"Estella... Que nome bonito, é diferente.\"{/cps}"
                hide Stella feliz 
                show Stella happy1
                s happy1 "{cps=40}\"Obrigada Kioku, é sim diferente, na verdade, não sou japonesa, eu sou brasileira.\"{/cps}"
                k surpreso "{cps=40}\"Nossa que legal, mas você nasceu no Japão?\"{/cps}"
                hide Stella happy1
                show Stella envergonhada
                s envergonhada "{cps=40}\"Sim, mas meus pais são brasileiros, eles vieram para cá quando eu ainda não tinha nascido haha...\"{/cps}"
                k normal "{cps=40}\"Ah, entendi... Que legal, deve ser uma experiência interessante crescer aqui com uma cultura tão diferente da dos seus pais...\"{/cps}"
                hide Stella envergonhada
                show Stella feliz
                s feliz "{cps=40}\"É, não conheço muito a cultura brasileira, mas eu gosto bastante, e meus pais sempre me contam sobre o Brasil, e me ensinam um pouco de português...\"{/cps}"
                menu:
                    "Perguntar sobre a transferência":
                        k feliz "{cps=40}\"Ah, que legal, mas ei... O que te fez se transferir para cá?\"{/cps}"
                        hide Stella feliz 
                        show Stella happy1
                        s happy1 "{cps=40}\"Ah, é uma longa história... Mas resumindo bastante, eu tive alguns problemas na minha antiga escola, e eu precisava de um recomeço, então meus pais decidiram me transferir pra cá...\"{/cps}"
                        k normal "{cps=40}\"Ah, entendi... Bom, espero que aqui seja um bom recomeço pra você então...\"{/cps}"
                        hide Stella happy1
                        show Stella feliz
                        s feliz "{cps=40}\"Obrigada Kioku, eu espero que sim também...\"{/cps}"
                        k feliz "{cps=40}\"Bem vamos iniciar o Tour da Faculdade então?\"{/cps}"
                        hide Stella feliz
                        show Stella happy1
                        s happy1 "{cps=40}\"Claro, vamo lá!\"{/cps}"
                    "Começar o tour da faculdade":
                        k feliz "{cps=40}\"Ah, que legal, mas acho que seria melhor eu te mostrar a Faculdade, o que acha?\"{/cps}"
                        hide Stella feliz 
                        show Stella happy1
                        s happy1 "{cps=40}\"Ah, sim, claro, eu adoraria conhecer a Faculdade...\"{/cps}"
                        hide Stella happy1
                        show Stella feliz
                        k feliz "{cps=40}\"Então vamos lá!\"{/cps}"
            "Perguntar sobre a transferência":
                k normal "{cps=40}\"O que te fez se transferir para cá?\"{/cps}"
                hide Stella feliz 
                show Stella happy1
                s happy1 "{cps=40}\"Ah, é uma longa história... Mas resumindo bastante, eu tive alguns problemas na minha antiga escola, e eu precisava de um recomeço, então meus pais decidiram me transferir pra cá...\"{/cps}"
                k normal "{cps=40}\"Ah, entendi... Bom, espero que aqui seja um bom recomeço pra você então...\"{/cps}"
                hide Stella happy1
                show Stella feliz
                s feliz "{cps=40}\"Obrigada Kioku, eu espero que sim também...\"{/cps}"
                menu:
                    "Perguntar sobre o nome":
                        k normal "{cps=40}\"Estella... Que nome bonito, é diferente.\"{/cps}"
                        hide Stella feliz 
                        show Stella happy1
                        s happy1 "{cps=40}\"Obrigada Kioku, é sim diferente, na verdade, não sou japonesa, eu sou brasileira!\"{/cps}"
                        k surpreso "{cps=40}\"Nossa que legal, mas você nasceu no Japão?\"{/cps}"
                        hide Stella happy1
                        show Stella envergonhada
                        s envergonhada "{cps=40}\"Sim, mas meus pais são brasileiros, eles vieram para cá quando eu ainda não tinha nascido haha...\"{/cps}"
                        k normal "{cps=40}\"Ah, entendi... Que legal, deve ser uma experiência interessante crescer aqui com uma cultura tão diferente da dos seus pais...\"{/cps}"
                        hide Stella envergonhada
                        show Stella feliz
                        s feliz "{cps=40}\"É, não conheço muito a cultura brasileira, mas eu gosto bastante, e meus pais sempre me contam sobre o Brasil, e me ensinam um pouco de português...\"{/cps}"
                    "Começar o tour da faculdade":
                        k feliz "{cps=40}\"Bom que tal eu começar o Tour pela Faculdade, o que acha?\"{/cps}"
                        hide Stella feliz 
                        show Stella happy1
                        s happy1 "{cps=40}\"Ah, sim, claro, eu adoraria conhecer a Faculdade...\"{/cps}"
                        hide Stella happy1
                        show Stella feliz
                        k feliz "{cps=40}\"Então vamos lá!\"{/cps}"
        scene narrador
        with dissolve
        "{cps=40}Kioku, então, começa a mostrar a Faculdade para Estella\nMostra corredores\nSalas de aulas\nCantina\nBanheiros...{/cps}"
        "{cps=40}Se passa uma hora, e então eles retornam para as escadas onde haviam se encontrado.{/cps}"
        scene escadaescoladia
        with dissolve
        show Stella feliz
        with dissolve
        s feliz "{cps=40}\"...Eai quando eu cheguei em casa, eu vejo ele embaixo da cama hahahahahaha...{/cps}\""
        hide Stella feliz 
        show Stella happy2
        s happy2 "{cps=40}\"Esse tempo todo, ele estava embaixo da minha cama, e eu dando voltas e voltas no meu bairro, hahahahah....{/cps}\""
        k divertindo "{cps=40}\"Hahahaha, você deve ter achado engraçado na hora né?\"{/cps}"
        s happy2 "{cps=40}\"Na hora eu briguei com ele porque ele não me respondia, nem quando eu chamava com a ração hahahaha.{/cps}\""
        s happy2 "{cps=40}\"Mas depois eu achei engraçado, porque ele estava lá, e eu nem tinha percebido...\"{/cps}"
        hide Stella happy2
        show Stella feliz
        s feliz "{cps=40}\"Aiai, nossa, nem vi o tempo passar, obrigada por me mostrar a Faculdade Kioku, eu adorei conhecer tudo isso...\"{/cps}"
        $ amizade_add("stella", 5)
        k feliz "{cps=40}\"Ah, que bom que você gostou Estella, eu também adorei te mostrar a Faculdade e conversar com você...\"{/cps}"
        hide Stella feliz
        show Stella envergonhada
        s envergonhada "{cps=40}\"...\"{/cps}"
        s envergonhada "{cps=40}\"Foi legal conversar com você também Kioku...\"{/cps}"
        hide Stella envergonhada
        show Stella feliz 
        s feliz "{cps=40}\"Bem, agora eu tenho que passar no mercado...\"{/cps}"
        s feliz "{cps=40}\"De qualquer forma, obrigada Kioku por me apresentar e pela conversa que tivemos, eu adorei.\"{/cps}"
        k feliz "{cps=40}\"Claro Estella, eu que agradeço por ter me deixado te mostrar a Faculdade, quando precisar de algo pode falar comigo.\"{/cps}"
        s feliz "{cps=40}\"Obrigada Kioku, pode deixar...\"{/cps}"            
        s feliz "{cps=40}\"Bem, então, até mais Kioku, nos vemos por aí...\"{/cps}"
        k feliz "{cps=40}\"Até mais Estella...\"{/cps}"
        jump celularestella  
                
                

label celularestella:
    if consequência_ativada["celular_estella"] == True:
        jump irembora
    else:
        s feliz "{cps=40}\"Ei Kioku, antes de você ir.\"{/cps}"
        s feliz "{cps=40}\"Você tem algum número de telefone pra me passar? Sabe, pra gente conversar melhor sobre a faculdade e tudo mais.\"{/cps}"
        k feliz "{cps=40}\"Ah, claro, eu te passo meu número...\"{/cps}"
        s feliz "{cps=40}\"Ah, obrigada Kioku.\"{/cps}"
        k feliz "{cps=40}\"Claro, meu número é 1724-1021, me manda uma mensagem mais tarde...\"{/cps}"
        s feliz "{cps=40}\"Pode deixar, eu te mando mensagem sim...\"{/cps}"
        hide Stella feliz
        show Stella feliz2
        s feliz2 "{cps=40}\"Muito obrigada de novo Kioku, até mais.\"{/cps}"
        k feliz "{cps=40}\"Até Estella.\"{/cps}"
    jump irembora
    
    





