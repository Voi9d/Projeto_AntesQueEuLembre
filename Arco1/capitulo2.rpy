label dia2:
    call save_point
    play music "audio/Musicas/lembrancas.mp3" fadein 1.0
    scene Cap2
    with dissolve
    pause 1.0
    $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
    play sound "audio/SoundsEffects/alarme.mp3" fadein 0.5
    pause 0.25
    scene Quarto1
    with pixellate
    pause 1.0

    stop sound fadeout 0.25
    
    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')

    k normal "{i}{cps=40}O que caralhos aconteceu....{/i}{/cps}"
    k normal "{i}{cps=40}Q-que sonho foi esse?{/i}{/cps}"
    k normal "{i}{cps=40}Que horas são?{i}{/cps}"
    k normal "{i}{cps=40}São 9:00 horas da manhã, deixa eu lavar o rosto{/i}{/cps}"
    scene banheiroap
    with pixellate
    pause 0.5
    $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
    play sound "audio/SoundsEffects/torneira.mp3" fadein 0.5
    pause 4.0
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
    k normal "{i}{cps=40}Esse sonho....{/i}{/cps}"
    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    scene casakiokuentrada
    with flash
    
    pause 0.5

    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    scene casakiokucorredor
    with flash

    pause 0.5

    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    scene chegoutardekioku
    with flash

    pause 0.5

    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    scene banheiroap
    with flash
    k triste "{i}{cps=40}A-aquele era eu?{/i}{/cps}"
    k triste "{i}{cps=40}E-ela... era....a minh{w=0.5}{nw}{/i}{/cps}"
    $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
    play sound "audio/SoundsEffects/batendonaporta.mp3" fadein 0.5
    pause 3.0
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
    k normal "{i}{cps=40}Quem será essa hora?{/i}{/cps}"
    menu:
        "Ir até a porta":
            scene cozinhaap
            with pixellate
            k normal "{cps=40}{i}09:03 da manhã, eu não encomendei nada, não estou esperando por visita... Quem seria?{/i}{cps=40}"
            menu:
                "Olhar pelo olho mágico":
                    scene narrador
                    with pixellate
                    "{cps=40}Kioku, então, utilizaa seu olho mágico, com um sentimento pequeno de tensão, visto que não esperava por ninguém{/cps}"
                    pause 0.5
                    scene apartamentoexterno
                    with pixellate
                    show Stella envergonhada2
                    with dissolve
                    s envergonhada2 "{cps=40}...{/cps}"
                    scene cozinhaap
                    with pixellate
                    hide Stella envergonhada2
                    k surpreso "{cps=40}{i}Estella? O que ela ta fazendo aqui?{/cps}{/i}"
                    k feliz "{cps=40}{i}Porquê eu estou feliz e nervoso ao mesmo tempo quando eu vi ela?{/cps}{/i}"
                    k triste "{cps=40}{i}Será que escovei o dente? Será que eu to fedendo?{/cps}{/i}"
                    $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
                    play sound "audio/SoundsEffects/batendonaporta.mp3" fadein 0.5
                    pause 3.0
                    stop sound fadeout 1.0
                    $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                    if consequência_ativada["conheceu_estella_apartamento"] == True:
                        if consequência_ativada["ajudar_estella_chave"] == True:
                            "Estella Nascimento" "{cps=40}\"Só queria ver com você se ainda ta de pé aquela ajuda que você me falou ontem de manhã?\"{/cps}"
                            "Estella Nascimento" "{cps=40}\"Se não der agora, tudo bem, eu vou tentar achar dai\"{/cps}"
                            menu:
                                "Eu te ajudo":
                                    k normal "{cps=40}\"Oi, eu to aqui, eu tava lavando o rosto, eu te ajudo sim, não esqueci, me da só uns 5 minutos\"{/cps}"
                                    "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui\"{/cps}"
                                    k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                                    call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                                    $ resultado = _return
                                    if resultado:
                                        scene narrador
                                        with pixellate
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                    else:
                                        scene narrador
                                        with pixellate
                                        "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                "Ja vou":
                                    k normal "{cps=40}\"Oi, eu ja to indo, só preciso comer algo\"{/cps}"
                                    "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui\"{/cps}"
                                    k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                                    call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                                    $ resultado = _return
                                    if resultado:
                                        scene narrador
                                        with pixellate
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                    else:
                                        scene narrador
                                        with pixellate
                                        "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                        else:
                            "Estella Nascimento" "{cps=40}\"Então, eu queria pedir uma ajuda, a procurar a minha chave da lavanderia.\"{/cps}"
                            k normal "{cps=40}\"Mas essa chave todos ganham quando chegam? Você perdeu ela aonde?\"{/cps}"
                            "Estella Nascimento" "{cps=40}\"Ta no meu apartamento, ai eu vi pedir uma ajudinha pra ti\"{/cps}"
                            menu:
                                "Eu te ajudo":
                                    k normal "{cps=40}\"Okay, eu te ajudo, só me da só uns 5 minutos\"{/cps}"
                                    "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui\"{/cps}"
                                    k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                                    call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                                    $ resultado = _return
                                    if resultado:
                                        scene narrador
                                        with pixellate
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                    else:
                                        scene narrador
                                        with pixellate
                                        "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                "Ja vou":
                                    k normal "{cps=40}\"Okay, eu ja vou, só deixa eu escovar os dentes.\"{/cps}"
                                    "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui.\"{/cps}"
                                    k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                                    call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                                    $ resultado = _return
                                    if resultado:
                                        scene narrador
                                        with pixellate
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                    else:
                                        scene narrador
                                        with pixellate
                                        "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                        if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            $ consequência_ativada["pasta_nova"] == True
                                            "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                            call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                            $ resultado = _return
                                            if resultado:
                                                "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                                "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                                            else:
                                                "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                                "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                                "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                                "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                                jump chavedaestella
                    else:
                        "Estella Nascimento" "{cps=40}\"Oi, é a Estella, da faculdade, eu queria te pedir um favor\"{/cps}"
                        "Estella Nascimento" "{cps=40}\"Eu queria pedir ajuda a procurar a minha chave da lavanderia.\"{/cps}"
                        k normal "{cps=40}\"Mas essa chave todos ganham quando chegam? Você perdeu ela aonde?\"{/cps}"
                        "Estella Nascimento" "{cps=40}\"Eu procurei pelos corredores, mas acabei não encontrando, ai sobrou meu apartamento, dai eu pensei em vir pedir uma ajudinha pra ti!\"{/cps}"
                        menu:
                            "Eu te ajudo":
                                k normal "{cps=40}\"Okay, eu te ajudo, só me da só uns 5 minutos.\"{/cps}"
                                "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui\"{/cps}"
                                k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                                call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                                $ resultado = _return
                                if resultado:
                                    scene narrador
                                    with pixellate
                                    if consequência_ativada["pasta_nova"] == True:
                                        "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        $ consequência_ativada["pasta_nova"] == True
                                        "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                        call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                        $ resultado = _return
                                        if resultado:
                                            "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                            "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                            "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                else:
                                    scene narrador
                                    with pixellate
                                    "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                    if consequência_ativada["pasta_nova"] == True:
                                        "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        $ consequência_ativada["pasta_nova"] == True
                                        "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                        call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                        $ resultado = _return
                                        if resultado:
                                            "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                            "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                            "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                            "Ja vou":
                                k normal "{cps=40}\"Okay, eu ja vou, só deixa eu escovar os dentes.\"{/cps}"
                                "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui.\"{/cps}"
                                k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                                call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                                $ resultado = _return
                                if resultado:
                                    scene narrador
                                    with pixellate
                                    if consequência_ativada["pasta_nova"] == True:
                                        "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        $ consequência_ativada["pasta_nova"] == True
                                        "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                        call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                        $ resultado = _return
                                        if resultado:
                                            "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                            "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                            "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                else:
                                    scene narrador
                                    with pixellate
                                    "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                    if consequência_ativada["pasta_nova"] == True:
                                        "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        $ consequência_ativada["pasta_nova"] == True
                                        "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                        call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                        $ resultado = _return
                                        if resultado:
                                            "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                            "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                        else:
                                            "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                            "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                "Abrir a porta":
                    scene narrador
                    with pixellate
                    play sound "audio/SoundsEffects/abrindoporta.mp3" fadein 1.0
                    pause 1.25
                    scene apartamentoexterno
                    with pixellate
                    show Stella envergonhada2
                    with dissolve
                    "{cps=40}Quando Kioku abre a porta, ele a vê, Estella, parecia um pouco vermelha olhando pra baixo esperando uma resposta, até que quando ela ouve a porta se abrir ela olha para frente{/cps}"
                    hide Stella envergonhada2
                    show Stella felizz
                    s felizz "\"{cps=40}K-kioku, o-oi, tudo bem?\"{/cps}"
                    k feliz "{cps=40}\"Tudo sim Estella, e com você?\"{/cps}"
                    s felizz "{cps=40}\"Tô bem sim, obrigada por perguntar...{/cps}\""
                    if consequência_ativada["ajudar_estella_chave"] == True:
                        hide Stella felizz
                        show Stella felizz2
                        s felizz2 "{cps=40}\"Se lembra que ontem combinamos de encontrar minha chave?{/cps}"
                        k feliz "{cps=40}\"Ah sim, lembro sim\"{/cps}"
                        hide Stella felizz2
                        show Stella felizz
                        s felizz "{cps=40}\"Se você puder agora, como estou livre, podemos procura-la.{/cps}\""
                        k feliz "{cps=40}\"Claro, porquê não?\"{/cps}"
                        hide Stella felizz
                        show Stella felizz3
                        s felizz3 "{cps=40}\"Okay então, vem comigo, provavelmente tá no meu apartamento, em algum buraco ou sei lá hahaha\"{/cps}"
                        jump apartamentodaestella
                    else:
                        if consequência_ativada["conheceu_estella_apartamento"] == True:
                            s felizz "{cps=40}\"Bem, como nós somos praticamente vizinhos, eu vim aqui te pedir uma ajuda.\"{/cps}"
                            k feliz "{cps=40}\"Claro, o que você precisaria?\"{/cps}"
                            hide Stella felizz
                            show Stella envergonhadaa
                            s envergonhadaa "{cps=40}\"Sabe a chave da lavandaria? Então haha, eu meio que perdi....{/cps}"
                            k divertindo "{cps=40}\"O que? hahaha, como você conseguiu?\"{/cps}"
                            s envergonhadaa "{cps=40}\"Também não sei, mas ó, pelo lado bom, provavelmente tá no meu AP.\"{/cps}"
                            k feliz "{cps=40}\" \"Provavelmente\", tipo quanto? 100%%?\"{/cps}"
                            s envergonhadaa "{cps=40}\"Ah... acho que uns.... 99,99%%\"{/cps}"
                            hide Stella envergonhadaa
                            show Stella felizz
                            s feliz "{cps=40}\"Mas vai dar tudo certo.\"{/cps}"
                            k feliz "{cps=40}\"Olha... ainda tem 00,01%% de chance de não dar cer-{w=0.5}{nw}{/cps}"
                            hide Stella felizz
                            show Stella smugg
                            s smug "{cps=40}\"Eiii... não fica agourando não.\"{/cps}"
                            k divertindo "{cps=40}\"Okay, okay, parei, vou confiar em você.\"{/cps}"
                            hide Stella smugg
                            show Stella felizz
                            s felizz "{cps=40}\"Beleza, então vamo nessa.\"{/cps}"
                            jump apartamentodaestella
                        else:
                            s felizz "{cps=40}\"Eu sei que você deve ta se perguntando como eu sei que você morra aqui.\"{/cps}"
                            hide Stella felizz
                            show Stella envergonhadaa
                            s envergonhadaa "{cps=40}\"E bom, eu tenho uma explicação até que fácil, eu moro também no prédio, eu meio que te vi ontem de noite chegando, mas parecia tão cansado, que dai nem falei com você.\"{/cps}"
                            s envergonhadaa "{cps=40}\"Desculpa se foi ou é meio estranho.\"{/cps}"
                            k divertindo "{cps=40}\"Olha, se eu não te conhecesse eu teria chamado a polícia ein hahahaha.\"{/cps}"
                            s envergonhadaa "{cps=40}\"Hehe, é eu mereceria.\"{/cps}"
                            hide Stella envergonhadaa
                            show Stella felizz
                            s felizz "{cps=40}\"Sem querer ficar enrolando...\"{/cps}"
                            s felizz "{cps=40}\"Bem, eu vim aqui te pedir uma ajuda.\"{/cps}"
                            k feliz "{cps=40}\"O que você precisaria?\"{/cps}"
                            hide Stella felizz
                            show Stella envergonhadaa
                            s envergonhadaa "{cps=40}\"Sabe a chave da lavandaria?{/cps}"
                            k feliz "{cps=40}\"Sei, todo mundo ganha uma cópia pra poder acessar mais fácil... Porquê?\"{/cps}"
                            s envergonhadaa "{cps=40}\"Então, meio que eu perdi ela haha..... MAAAAAAAS.\"{/cps}"
                            s envergonhadaa "{cps=40}\"Provavelmente tá no meu AP.\"{/cps}"
                            k feliz "{cps=40}\" \"Provavelmente\", tipo quanto? 100%%?\"{/cps}"
                            s envergonhadaa "{cps=40}\"Ah... acho que uns.... 99,99%%\"{/cps}"
                            hide Stella envergonhadaa
                            show Stella felizz
                            s felizz "{cps=40}\"Mas vai dar tudo certo.\"{/cps}"
                            k feliz "{cps=40}\"Olha... ainda tem 00,01%% de chance de não dar certo{/cps}"
                            hide Stella felizz
                            show Stella smugg
                            s smugg "{cps=40}\"Eiii... não fica agourando não.\"{/cps}"
                            k divertindo "{cps=40}\"Okay, okay, parei, vou confiar em você.\"{/cps}"
                            hide Stella smugg
                            show Stella felizz
                            s felizz "{cps=40}\"Isso é um sim?\"{/cps}"
                            k feliz "{cps=40}\"Sim, eu te ajudo Estella\"{/cps}"
                            hide Stella felizz
                            show Stella felizz2
                            s felizz2 "{cps=40}\"Obrigada, vamo lá, eu te levo.\"{/cps}"
                            jump apartamentodaestella
        "Perguntar quem é":
                k normal "{cps=40}{size=+15}\"QUEM É?\"{/size}{/cps}"
                if consequência_ativada["conheceu_estella_apartamento"] == True:
                    "Estella Nascimento" "{cps=40}{size=-10}\"É a Estella, a gente conversou ontem na lavanderia e na faculdade, se lembra?\"{/cps}{/size}"
                else:
                    "Estella Nascimento" "{cps=40}{size=-10}\"É a Estella, a gente conversou na faculdade ontem, se lembra?\"{/cps}{/size}"
                k normal "{cps=40}{size=+15}\"Ah sim, pera um pouquinho!{/cps}{/size}\""
                scene cozinhaap
                with pixellate
                "{cps=40}Kioku, então, se aproxima da prota de entrada e utiliza o olho mágico, mesmo sabendo quem era, ele ainda sente um calafrio{/cps}"
                pause 0.5
                scene apartamentoexterno
                with pixellate
                show Stella envergonhada2
                with dissolve
                s envergonhada2 "{cps=40}...{/cps}"
                scene cozinhaap
                with pixellate
                hide Stella envergonhada2
                k surpreso "{cps=40}{i}Mas porquê a Estella ta aqui?{/cps}{/i}"
                k feliz "{cps=40}{i}Porquê eu estou feliz e nervoso ao mesmo tempo quando eu vi e ouvi ela?{/cps}{/i}"
                k triste "{cps=40}{i}Será que escovei o dente? Será que eu to fedendo?{/cps}{/i}"
                $ renpy.music.set_volume(0.3, delay=0.5, channel='music')
                play sound "audio/SoundsEffects/batendonaporta.mp3" fadein 0.5
                pause 3.0
                stop sound fadeout 1.0
                $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
                "Estella Nascimento" "{cps=40}\"Kioku? Você ta ai ainda?\"{/cps}"        
                if consequência_ativada["ajudar_estella_chave"] == True:
                    "Estella Nascimento" "{cps=40}\"Só queria ver com você se ainda ta de pé aquela ajuda que você me falou ontem de manhã?\"{/cps}"
                    "Estella Nascimento" "{cps=40}\"Se não der agora, tudo bem, eu vou tentar achar dai.\"{/cps}"
                    menu:
                        "Eu te ajudo":
                            k normal "{cps=40}\"Oi, eu to aqui, eu tava lavando o rosto, eu te ajudo sim, não esqueci, me da só uns 5 minutos!\"{/cps}"
                            "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui\"{/cps}"
                            k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                            call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                            $ resultado = _return
                            if resultado:
                                scene narrador
                                with pixellate
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                            else:
                                scene narrador
                                with pixellate
                                "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                        "Ja vou":
                            k normal "{cps=40}\"Oi, eu ja to indo, só preciso comer algo.\"{/cps}"
                            "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui.\"{/cps}"
                            k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                            call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                            $ resultado = _return
                            if resultado:
                                scene narrador
                                with pixellate
                                if consequência_ativada["pasta_nova"] == True:
                                            "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                            "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                            "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                            jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                            else:
                                scene narrador
                                with pixellate
                                "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                else:
                    "Estella Nascimento" "{cps=40}\"Então, eu queria pedir uma ajuda, a procurar a minha chave da lavanderia.\"{/cps}"
                    k normal "{cps=40}\"Mas essa chave todos ganham quando chegam? Você perdeu ela aonde?\"{/cps}"
                    "Estella Nascimento" "{cps=40}\"Eu procurei pelos corredores, mas acabei não encontrando, ai sobrou meu apartamento, dai eu pensei em vir pedir uma ajudinha pra ti!\"{/cps}"
                    menu:
                        "Eu te ajudo":
                            k normal "{cps=40}\"Okay, eu te ajudo, só me da só uns 5 minutos.\"{/cps}"
                            "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui\"{/cps}"
                            k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                            call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                            $ resultado = _return
                            if resultado:
                                scene narrador
                                with pixellate
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                            else:
                                scene narrador
                                with pixellate
                                "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                        "Ja vou":
                            k normal "{cps=40}\"Okay, eu ja vou, só deixa eu escovar os dentes.\"{/cps}"
                            "Estella Nascimento" "{cps=40}\"O-okay então, eu te espero aqui.\"{/cps}"
                            k normal "{cps=40}{i}Ta, agora eu só preciso escovar os dentes, tomar banho e me arrumar, tudo em menos de 5 minutos.... Vamos lá né....{/i}{/cps}"
                            call rolar_d20_base(dc=15, atributo='agilidade', titulo="Corra: Tente fazer tudo em 5 minutos")
                            $ resultado = _return
                            if resultado:
                                scene narrador
                                with pixellate
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, corre pelo apartamento, consegue pegar uma roupa enquanto liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                            else:
                                scene narrador
                                with pixellate
                                "{cps=40}Kioku começa a correr para dentro, pega suas roupas, deixa-as cair durante o caminho, enquanto ele pega seu desodorante, tudo ao mesmo tempo enquanto corre pro banheiro.{/cps}"
                                if consequência_ativada["pasta_nova"] == True:
                                    "{cps=40}Kioku, então, liga o chuveiro, pega o que restou da pasta, mesmo sendo quase nada...{/cps}"
                                    "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                    "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                    jump chavedaestella
                                else:
                                    $ consequência_ativada["pasta_nova"] == True
                                    "{cps=40}Kioku, então, liga o chuveiro, pega a sua pasta, e tenta utilizar toda a força que possui para retirar o resto da bisnaga.{/cps}"
                                    call rolar_d20_base(dc=5, atributo='forca', titulo="Força: Utilize toda sua força para retirar o resto da pasta.")
                                    $ resultado = _return
                                    if resultado:
                                        "{cps=40}Kioku, enquanto toma banho, consegue finalmente tirar o restante da sua pasta que tinha.{/cps}"
                                        "{cps=40}Ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
                                    else:
                                        "{cps=40}Kioku, tenta utilizar toda sua força para retirar o resto da pasta, mas como estava com pressa ele joga ela na lixeira e entra no banho{/cps}"
                                        "{cps=40}Por sorte(ou por pura conhêcidência do roteiro) kioku encontra um enxaguante bocal, então, decide usa-lo, pelo menos por enquanto{/cps}"
                                        "{cps=40}Enquanto toma banho, ele começa a escovar os dentes, a pasta e o sabão começam a se misturar, pela primeira vez kioku por algum motivo queria ficar cheiroso.{/cps}"
                                        "{cps=40}Se passa alguns minutos, até que finalmente kioku, toma o banho mais rápido da sua vida, e se prepara para sair do apartamento.{/cps}"
                                        jump chavedaestella
label chavedaestella:
    scene narrador
    with pixellate
    play sound "audio/SoundsEffects/abrindoporta.mp3" fadein 1.0
    pause 1.25
    stop music fadeout 1.0
    play music "audio/Musicas/Fique_comigo.mp3" fadein 1.0
    scene apartamentoexterno
    with pixellate
    show Stella envergonhada2
    with dissolve
    "{cps=40}Quando Kioku abre a porta, ele a vê, Estella, parecia um pouco vermelha olhando pra baixo esperando por ele, até que quando ela ouve a porta se abrir ela olha para frente...{/cps}"
    hide Stella envergonhada2
    show Stella felizz
    s felizz "\"{cps=40}K-kioku, o-oi, tudo bem?\"{/cps}"
    k feliz "{cps=40}\"Tudo sim Estella, e com você?\"{/cps}"
    s felizz "{cps=40}\"Tô bem sim, obrigada por perguntar...{/cps}\""
    if consequência_ativada["conheceu_estella_apartamento"] == False:
        s felizz "{cps=40}\"Eu sei que você deve ta se perguntando como eu sei que você morra aqui.\"{/cps}"
        hide Stella felizz
        show Stella envergonhadaa
        s envergonhadaa "{cps=40}\"E bom, eu tenho uma explicação até que fácil, eu moro também no prédio, eu meio que te vi ontem de noite chegando, mas parecia tão cansado, que dai nem falei com você.\"{/cps}"
        s envergonhadaa "{cps=40}\"Desculpa se foi ou é meio estranho.\"{/cps}"
        k divertindo "{cps=40}\"Olha, se eu não te conhecesse eu teria chamado a polícia ein hahahaha.\"{/cps}"
        s envergonhadaa "{cps=40}\"Hehe, é eu mereceria.\"{/cps}"
        hide Stella envergonhadaa
        show Stella felizz
    k feliz "{cps=40}\"Você falou que ta no seu Apartamento né?\"{/cps}"
    s felizz "{cps=40}\"Isso, ele provavelmente tá lá.\"{/cps}"
    k feliz "{cps=40}\" \"Provavelmente\", tipo quanto? 100%%?\"{/cps}"
    hide Stella felizz
    show Stella envergonhadaa
    s envergonhadaa "{cps=40}\"Ah... acho que uns.... 99,99%%\"{/cps}"
    hide Stella envergonhada
    show Stella felizz
    s felizz "{cps=40}\"Mas vai dar tudo certo!\"{/cps}"
    k feliz "{cps=40}\"Olha... ainda tem 00,01%% de chance de não dar certo.{/cps}"
    hide Stella felizz
    show Stella smugg
    s smugg "{cps=40}\"Eiii... não fica agourando não!!\"{/cps}"
    k divertindo "{cps=40}\"Okay, okay, parei, vou confiar em você.\"{/cps}"
    hide Stella smugg
    show Stella felizz2
    s felizz2 "{cps=40}\"Beleza, então vamo nessa.\"{/cps}"
    jump apartamentodaestella

label apartamentodaestella:
    hide Stella felizz2
    with dissolve
    scene narrador
    with pixellate
    pause 0.5
    play sound "audio/SoundsEffects/abrindoporta.mp3"
    pause 1.0
    play sound "audio/SoundsEffects/fechandoporta.mp3"
    scene cozinhaestelladia
    with dissolve
    show Stella felizz
    with dissolve
    s felizz "{cps=40}\"Chegamos!!\"{/cps}"
    s felizz "{cps=40}\"Pode entrar viu Kioku, e fica a vontade\nMi Casa, Su Casa...{/cps}\""
    hide Stella felizz
    with dissolve
    s felizz "{cps=40}\"Mãeeeee\nPaaaai\nChegamos\"{/cps}"
    menu:
        "Seguir Estella":
            jump conhecendoPais

label conhecendoPais:
    scene salaestelladia
    with dissolve
    show PaisEstella felizes:
        xalign 1.0
        yalign 1.5
    with dissolve
    show Stella felizz:
        zoom 0.7
        yalign 1.0
        xalign 0.25
    with dissolve
    s felizz "{cps=40}\"Mãe, Pai, esse é o Kioku Aida, meu vizinho e colega de faculdade\"{/cps}"
    mel feliz "{cps=40}\"Olá Kioku, prazer em conhecer você\"{/cps}"
    ali feliz "{cps=40}\"Olá Ki{/cps}{w=1.5}{nw}"
    hide PaisEstella felizes
    show PaisEstella primeiroencontro:
        xalign 1.0
        yalign 1.5
    ali bravo "{cps=20}\"Kioku Aida....{/cps}\""
    ali bravo "{cps=20}\"Você.....{/cps}\""
    "{cps=40}Antes que Kioku pudesse reagir, ele sente algo pegando sua mão. Estella, o pega pelo braço e começa a levar em direção ao seu quarto.{/cps}"
    hide PaisEstella primeiroencontro
    with dissolve
    hide Stella felizz
    with dissolve
    scene Quarto1
    with pixellate
    show Stella Triste2
    with dissolve
    s Triste2 "{cps=40}\".....{/cps}\""
    s Triste2 "{cps=40}\"...{/cps}\""
    "{cps=40}O silêncio tomava conta no quarto, Estella encolhida no meio do quarto olhando para baixo completamente envergonhada.{/cps}"
    "{cps=40}Até que finalmente Estella olha em direção ao Kioku.{/cps}"
    hide Stella Triste2
    show Stella Triste1
    s Triste1 "{cps=40}\"Desculpa.... por você ter visto o que viu, não sei o que deu com meu pai, eu... vou pegar uma coisa e ja volto, ai a gente procura minha chave ta bom?\"{/cps}"
    k triste "{cps=40}\"Ta tudo bem Estella, fica tranquila, vou esperar você{/cps}\""
    hide Stella Triste1
    with dissolve
    play sound "audio/SoundsEffects/abrindoporta.mp3"
    pause 1.0
    play sound "audio/SoundsEffects/fechandoporta.mp3"
    "{cps=40}Estella sai do quarto, fechando ele nas costas, e Kioku fica parado ainda perdido em seus pensamentos{/cps}"
    k normal "{cps=40}{i}O que acabou de acontecer? Meu deus...{/cps}{/i}"
    k normal "{cps=40}{i}Ele reagiu de uma forma como...{/cps}{/i}"
    scene salaestelladia
    with flash
    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    show PaisEstella primeiroencontro:
        xalign 1.0
        yalign 1.5
    ali bravo "{cps=20}\"Kioku Aida....{/cps}\""
    ali bravo "{cps=20}\"Você.....{/cps}\""
    scene Quarto1
    with flash
    play sound "audio/SoundsEffects/Flash.mp3" fadein 0.1
    k normal "{cps=40}{i}Acho que é só coisa da minha cabeça, vai que ele só não foi com minha cara{/cps}{/i}"
    "{cps=40}Enquanto Kioku esperava pelo retorno de Estella, ele começa a ouvir alguns cochichos vindo em direção a cozinha{/cps}"
    menu:
        "Espiar a Conversa":
            $ consequência_ativada["conversa_intima_pai_e_filha_estella"] = True
            k normal "{cps=40}{i}Ja dizia minha vó, a curiosidade matou o gato, mas mesmo assim, e se tiverem falando de mim?{/cps}{/i}"
            scene narrador
            with dissolve
            play sound "audio/SoundsEffects/abrindoporta.mp3"
            pause 1.0
            play sound "audio/SoundsEffects/fechandoporta.mp3"
            scene salaestelladia
            with dissolve
            show Alisson Bravo:
                xalign 1.0
                yalign 1.5
            with dissolve
            show Stella Brava:
                zoom 0.7
                yalign 1.0
                xalign 0.25
            with dissolve
            ali Bravo "{cps=40}\"...Não é isso que eu quero dizer, o que eu quero dizer é que{w=0.5}{nw}{/cps}"
            hide Stella Brava
            show Stella Brava2:
                zoom 0.7
                yalign 1.0
                xalign 0.25
            s Brava2 "{cps=40}\"EU CAGUEI PAI para o que você quer dizer, ele é uma pessoa importante pra mim e você não vai estragar tudo\"{/cps}"
            hide Alisson Bravo
            show Alisson Triste:
                xalign 1.0
                yalign 1.5
            ali Triste "{cps=40}\"Eu....\"{/cps}"
            hide Alisson Triste
            show Alisson Envergonhado:
                xalign 1.0
                yalign 1.5
            ali Envergonhado "{cps=40}\"*Suspira* Eu... Só não quero que você se machuque de novo...{/cps}\""
            hide Stella Brava2
            show Stella Triste:
                zoom 0.7
                yalign 1.0
                xalign 0.25
            s Triste "{cps=40}\"Eu sei pai.... É só que....\"{/cps}"
            s Triste "{cps=40}\"Só.... tenta dar uma chance a ele\"{/cps}"
            ali Envergonhado "{cps=40}\"...Ta bem filha.... eu... vou tentar *suspira*...{/cps}\""
            "{cps=40}Os dois então se abraçam por um tempo, Kioku olha toda aquela cena paralisado e com olhar firme.{/cps}"
            "{cps=40}Kioku volta a tona, e rapidamente volta ao quarto{/cps}"
            scene narrador
            with dissolve
            play sound "audio/SoundsEffects/abrindoporta.mp3"
            pause 1.0
            play sound "audio/SoundsEffects/fechandoporta.mp3"
            scene Quarto1
            with dissolve
            "{cps=40}Se passam alguns segundos, até que o som de passos se aproximando são ouvidos.{/cps}"
        "Esperar pela Estella":
            k normal "{cps=40}{i}Ja dizia minha vó, a curiosidade matou o gato, é melhor eu não ir, não é da minha conta.{/cps}{/i}"
            "{cps=40}Se passam alguns minutos, os cochichos finalmente param, até que o som de passos se aproximando são ouvidos.{/cps}"
    play sound "audio/SoundsEffects/abrindoporta.mp3"
    pause 1.0
    play sound "audio/SoundsEffects/fechandoporta.mp3"
    show Stella envergonhada2
    with dissolve
    "{cps=40}Estella aparece, com ainda um olhar para baixo{/cps}"
    s envergonhada2 "{cps=40}\"Foi mal pela demora, eu parei pra conversar com o meu pai na cozinha{/cps}"
    if consequência_ativada["conversa_intima_pai_e_filha_estella"] == True:
        k normal "{cps=40}{i}Eu ouvi a conversa que ela teve com o pai dela, quem sabe eu posso tentar anima-la, ou fazer ela contar comigo ja que ela se importa comigo.{/cps}{/i}"
        menu:
            "Perguntar o que aconteceu":
                k normal "{cps=40}\"Estella, o que aconteceu? Você parece um pouco triste.\"{/cps}"
                s envergonhada2 "{cps=40}\"Ah... é que eu tava conversando com meu pai, e ele... parece que não quer me ver perto de você?\"{/cps}"
                k surpreso "{cps=40}\"Mas foi algo que eu fiz?\"{/cps}"
                s envergonhada2 "{cps=40}\"N-não, imagina, é que....\"{/cps}"
                s envergonhada2 "{cps=40}\"*suspira* eu tinha um amigo no passado, e tipo, ele era muito próximo de mim, e eu gostava dele, mas ai aconteceu que ele acabou mudando de cidade derrepente, e ele não respondia mais minhas mensagens.\"{/cps}"
                s envergonhda2 "{cps=40}\"Foi ai que meu pai percebeu o quão mal aquela situação me fez, e ai que ele começou a cuidar dessa forma comigo, mais protetor sabe?{/cps}"
                k normal "{cps=40}\"Hmmm... entendi, bem, quero que você saiba que eu não sou nenhum perigo e não irei te deixar triste.{/cps}\""
                hide Stella envergonhada2
                show Stella feliz
                s feliz "{cps=40}\"Obrigada Kioku, eu confio em você... Enfim, vamos procurar essa maldita chave então?{/cps}"
            "Deixar pra lá":
                k normal "{cps=40}\"Ta tranquilo, não demorou não, vamos procurar a chave então?\"{/cps}"
                hide Stella envergonhada2
                show Stella feliz
                s feliz "{cps=40}\"Vamos!{/cps}\""
    else:
        k normal "{cps=40}\"Ta tranquilo, não demorou não, vamos procurar a chave então?\"{/cps}"
        hide Stella envergonhada2
        show Stella feliz
        s feliz "{cps=40}\"Vamos!{/cps}\""
    hide Stella feliz
    with dissolve
    jump quem_e_você


label quem_e_você:
    scene narrador
    with pixellate
    "{cps=40}Alguns bons minutos se passam, Estella e Kioku começam a revirar todo o quarto dela, bagunçam a cama, tiram as gavetas do lugar, abre todas as portas dos armários, até que finalmente...{/cps}"
    scene Quarto1
    with dissolve
    s feliz2 "{cps=40}\"Achei!!\"{/cps}"
    show Stella felizchave
    with dissolve
    s felizchave "{cps=40}\"Achei a chave da lavanderia!!\"{/cps}"
    s felizchave "{cps=40}\"Tava atrás do grande armário, acho que deixei cair em algum momento quando tava trazendo os móveis pro quarto, sei lá hahaha{/cps}\""
    k feliz "{cps=40}\"Aeee, que bom que conseguimos encontrar!!!{/cps}"
    s felizchave "{cps=40}\"Sim!!! Muito Obrigada Kioku, de verdade.\"{/cps}"
    "{cps=40}Estella olha para o relógio do celular e se espanta.{/cps}"
    hide Stella felizchave
    show Stella feliz2
    s feliz2 "{cps=40}\"Meu deus, ja é 11:15, nossa eu ocupei muito do seu tempo Kioku, me desculpa{/cps}"
    k feliz "{cps=40}\"Ei ta tudo bem, eu gostei de te ajudar, principalmente porque você é nova no prédio e muito legal.{/cps}"
    hide Stella feliz2
    show Stella envergonhadaa
    s envergonhadaa "{cps=40}\"O-obrigada Kioku, você também é muito legal, adorei passar esse tempo com você{/cps}\""
    k feliz "{cps=40}\"Mas bem, eu acho que vou indo pra casa, tenho que fazer almoço ainda, muito obrigado por essa aventura hahaha{/cps}\""
    hide Stella envergonhadaa
    show Stella Feliz2
    s feliz2 "{cps=40}\"Hahaha, verdade, tem razão, bem quando quiser pode me mandar mensagem, você tem meu número agora né.{/cps}"
    k feliz "{cps=40}\"Claro, tenho sim, pode deixar que eu vou fazer isso, enfim, um bom resto de manhã Estella.{/cps}"
    s feliz2 "{cps=40}\"Brigada, pra ti também{/cps}\""
    scene narrador
    with pixellate
    "{cps=40}Kioku se despede de Estella, e vai embora de seu apartamento, indo direto de volta ao seu{/cps}"
    play sound "audio/SoundsEffects/abrindoporta.mp3"
    pause 1.0
    scene cozinhaap
    with dissolve
    stop music fadeout 1.0
    play music "audio/Musicas/NoitedeVerão.mp3" fadein 1.0
    play sound "audio/SoundsEffects/fechandoporta.mp3"
    k normal "{cps=40}{i}Ai, que manhãzinha ein, nossa, minha internet ta desativada, será que eu recebi alguma mensagem?{/cps}"
    show screen phone_button
    show screen phone_notification
    show screen phone_system
    if consequência_ativada["respondeu_jinseipreocupada"] == True:
        $ receive_message("Jinsei", "Oiii, acabei dormindo, ai que bom, achei que você seila, tinha morrido...", time="10:07")
        pause 1.0
        $ receive_message("Jinsei", "Chegou bem? Dormiu bem?", time="10:07")
        $ set_pending_choice("Jinsei", "jinsei_mensagemManhã_dia2")
    else:
        $ receive_message("Jinsei", "Oiiiiiiiiiiii??????", time="10:07")
        pause 1.0
        $ receive_message("Jinsei", "Pelu Amor de Deus Kioku, você ta vivo????", time="10:07")
        pause 1.0
        $ receive_message("Jinsei", "Você recebeu as mensagens de hoje, porque deu dois certinhos, mas seila me manda qualquer coisa, to preocupada.", time="10:08")
        $ set_pending_choice("Jinsei", "jinsei_mensagemManhã_dia2_responder")
    k normal "{cps=40}{i}Bom, além da Jinsei falando comigo, não teve mais nenhuma mensagem...{/cps}{/i}"
    $ receive_unknown_message("Akira", "Oi.", time="10:08")
    pause 1.0
    $ receive_unknown_message("Akira", "Você não me conhece", time="10:08")
    pause 1.0
    $ receive_unknown_message("Akira", "Como consegui seu número? Isso não importa", time="10:08")
    pause 1.0
    $ receive_unknown_message("Akira", "A real pergunta que você deve se fazer é....", time="10:08")
    pause 1.0
    $ receive_unknown_message("Akira", "Você está bem?", time="10:09")
    $ set_pending_choice("Akira", "akira_resposta_")
    $ unlock_achievement("bocasanta")
    k normal "."





    
    
    




