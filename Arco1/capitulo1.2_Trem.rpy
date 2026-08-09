label tremestacao:
    scene narrador
    with pixellate
    
    "{cps=40}Kioku segue em direção a estação de trem, tentando não se atrasar e perder o mesmo.{/cps}"
    "{cps=40}Ele sabe que se perder este trem, ele perde um dos períodos da prova final, e isso pode prejudicar sua nota na matéria.{/cps}"
    call save_point
    if trematraso == True:
        stop music fadeout 1.0
        play music "audio/Musicas/PEGAOTREMKIOKU.mp3" fadein 1.0
        call rolar_d20_base(dc=17, atributo='agilidade', titulo="Correr para pegar o trem", reveal_result = True)
        $ resultado = _return
        if resultado:
            $ trematraso = False
            $ unlock_achievement('trem')
            "{cps=40}Kioku começa a correr, e utilizar toda sua energia que tinha no corpo, ele sabia que se perdesse o trem, sua nota na prova final poderia ser prejudicada.{/cps}"
            "{cps=40}Kioku, então, pula a catraca, deixando alguns trocados para retribuir a passagem, começa a descer as escadas como um jato...{/cps}"
            scene estacaodetrem
            with pixellate
            "{cps=40}Ele, então, chega na plataforma, olha para os lados e.....{/cps}"
            "{cps=20}...{/cps}"
            "{cps=20}...{/cps}"
            "Maquinista" "{cps=40}\"Última chamada para o trem com destino a Universidade de Tokyo, embarque imediatamente.\"{/cps}"
            stop music fadeout 1.0
            play music "audio/Musicas/frozen_winter.mp3" fadein 1.0
            scene trem
            with pixellate
            k normal "{cps=40}\"Puta merda, consegui chegar a tempo, meu deus do céu... Deus é muito bom e o diabo não presta nem um pouco nossa.\"{/cps}"
            call rolar_d20_base(dc=10, atributo='sorte', titulo="Tente a Sorte: Tem um lugar vago?")
            $ resultado = _return
            if resultado:
                "{cps=40}Kioku começa a vasculhar cada assento possível no vagão que estava e, por sorte, ele encontra um assento em um dos cantos do vagão (que sorte ein Kioku).\"{/cps}"
                k normal "{cps=40}\"Ai, ainda bem que achei um assento, nossa senhora, to exausto... Tenho que me exercitar mais, meu deus.\"{/cps}"
                k normal "{cps=40}{i}Vou tentar descansar um pouco aqui, antes da prova...{/i}{/cps}"
                jump escola
            else:
                "{cps=40}Kioku começa a vasculhar cada assento possível no vagão que estava, mas infelizmente não havia mais nenhum para ele poder sentar.{/cps}"
                k bravo "{cps=40}\"Puta merda cara, vou tem que ficar 30 minutos de pé agora... se eu tivesse chegado um pouco mais cedo...\"{/cps}"
                k normal "{cps=40}{i}Vou tentar descansar um pouco aqui em pé, antes da prova, espero que não freie bruscamente e eu caia no chão...{/cps}"
                "{cps=40}Não se preocupem, isso não vai acontecer{/cps}{cps=10}..................{/cps}"
                jump escola
        else:
            "{cps=40}Kioku começa a correr, utiliza toda a sua adrenalina, suas pernas começam a formigar, esse garoto nunca correu tanto na sua vida pra pegar um trem.{/cps}"
            "{cps=40}Ele salta a catraca da estação, deixando algumas moedas para trás como pagamento, começa a descer as escadas como um foguete...{/cps}"
            scene estacaodetrem
            with pixellate
            "{cps=40}Ele chega na plataforma, olha para os lados e.....{/cps}"
            "{cps=20}...{/cps}"
            "{cps=20}...{/cps}"
            "{cps=40}Kioku olha ao redor e vê que o seu trem começa a fechar as portas, Kioku sente que pode arriscar tudo e tentar de alguma forma adentrar na porta antes que ela feche.{/cps}"
            menu:
                "Tentar entrar no trem":
                    call rolar_d20_base(dc=20, atributo='agilidade', titulo="Seja Ágil: Passar pelas frestas da porta antes que ela feche.")
                    $ resultado = _return
                    if resultado:
                        $ tremporta = True
                        $ unlock_achievement('trem_2')
                        $ trematraso = False
                        "{cps=40}Kioku corre em direção ao trem, e com um salto impressionante, ele consegue entrar no trem antes que as portas se fechassem completamente.{/cps}"
                        stop music fadeout 1.0
                        play music "audio/Musicas/frozen_winter.mp3" fadein 1.0
                        scene trem
                        with pixellate
                        "{cps=40}Você é muito sortudo ein, nossa, o Kioku ta nas mãos certas mesmo.{/cps}"
                        k normal "{cps=40}\"Ufa... consegui entrar no trem... nossa senhora, senti minha vida passando pelos meus olhos.... 1 erro ali e era morte na certa.\"{/cps}"
                        k normal "{cps=40}{i}Não tem nenhum assento livre, que merda, bom, vou tentar descansar de pé aqui, e me escorrar nessa parede, espero que não freie bruscamente e eu caia no chão.\"{/i}{/cps}"
                        "{cps=40}Não se preocupem, isso não vai acontecer..................{/cps}"
                        jump escola
                    else:
                        $ provaatraso = True
                        "{cps=40}Kioku corre em direção a porta do trem, tenta saltar antes dela fechar, mas ele bate de cara na porta, e o trem começa a sair.{/cps}"
                        "{cps=40}Kioku fica ali parado, vendo o trem se afastar, ele sente uma mistura de raiva e frustração, ele sabia que tinha que chegar a tempo, mas não conseguiu.{/cps}"
                        stop music fadeout 1.0
                        play music "audio/Musicas/frozen_winter.mp3" fadein 1.0
                        k bravo "{cps=40}\"Merda... eu perdi o trem... que porra de dia é esse meu deus... agora vou me fuder na prova final... nossa senhora.\"{/cps}"
                        k bravo "{cps=40}{i}Foda-se... vou ter que esperar o próximo trem... que merda...{/i}{/cps}"
                        "{cps=40}Kioku então se afasta da plataforma, indo para a sala de espera, e se senta, esperando o próximo trem chegar.{/cps}"
                        "{cps=40}Depois de 30 minutos, o próximo trem chega, Kioku entra no vagão, e procura um assento vago para se sentar, e facilmente ele o encontra.{/cps}"
                        scene trem
                        with pixellate
                        k bravo "{cps=40}{i}Finalmente consegui entrar no trem... eu espero que não me atrase muito na prova final... nossa senhora...{/i}{/cps}"
                        k normal "{cps=40}{i}Vou tentar descansar um pouco aqui, antes da prova...{/i}{/cps}"
                        $ unlock_achievement('trem_3')
                        jump escola 
                "Desistir e esperar o próximo trem":
                    $ provaatraso = True
                    stop music fadeout 1.0
                    play music "audio/Musicas/frozen_winter.mp3" fadein 1.0
                    "{cps=40}Kioku vê que o trem está prestes a fechar as portas, e decide não arriscar sua vida tentando entrar na porta, ele se afasta da plataforma, indo para a sala de espera, e se senta, esperando o próximo trem chegar.{/cps}"
                    "{cps=40}Depois de 30 minutos, o próximo trem chega, Kioku entra no vagão, e procura um assento vago para se sentar, e facilmente ele o acha.{/cps}"
                    scene trem
                    with pixellate
                    k bravo "{cps=40}{i}Porra do caralho, vou me atrasar pra prova, que merda de dia é esse ein...{/i}{/cps}"
                    k normal "{cps=40}{i}Vou tentar descansar um pouco aqui, antes da prova...{/i}{/cps}"
                    $ unlock_achievement('trem_3')
                    jump escola
    else:
        $ unlock_achievement('trem')
        "{cps=40}Kioku chega na estação de trem com tempo de sobra, ele entra no vagão, e procura um assento vago para se sentar, e rapidamente o encontra.{/cps}"
        scene trem
        with pixellate
        k normal "{cps=40}\"Ufa... consegui chegar a tempo, meu deus do céu... Deus é muito bom e o diabo não presta mesmo.\"{/cps}"
        k normal "{cps=40}{i}Vou tentar descansar um pouco aqui, antes da prova...{/i}{/cps}"
        jump escola
