# The script of the game goes in this file.

init -100 python:
    # Register a noop `{ale}` tag as early as possible so lines that
    # contain {ale} won't raise "Unknown text tag" while the full
    # animated handler is set up later.
    try:
        renpy.register_text_tag("ale", lambda tag, argument, contents: contents)
    except Exception:
        pass


# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Amizade Verdadeira = 80+
# Amizade Normal = 50 - 79
# Amizade Ruim = 20 - 49
# Amizade Distante = 1 - 19
# Estranhos = 0
# Inimigos = -1 ou menos

# Configuração da música do menu principal
default persistent.atributos = {}
default persistent.atributos_confirmed = False
init python:
    # Música que toca no menu principal
    import os

    nome_pc = (
        os.environ.get("USERNAME") or
        os.environ.get("USER") or
        "Jogador"
    )
    del os
    
    config.main_menu_music = "audio/hope.mp3"
    #jinseiamizade = 40
    #stellaamizade = 0
    #subaruamizade = 0
    augustinaignora = False
    subarusangue = False
    subaruignorado = False
    modohistoria = False
    modoimersivo = False
    

    import math

    # Atributos do sistema de D20: Sorte, Agilidade, Lábia e Força.
    if not hasattr(persistent, 'atributos'):
        persistent.atributos = {}
    if not hasattr(persistent, 'atributos_confirmed'):
        persistent.atributos_confirmed = False

    ATRIBUTOS_DEF = [
        ('sorte', 'Sorte'),
        ('agilidade', 'Agilidade'),
        ('labia', 'Lábia'),
        ('forca', 'Força'),
    ]

    def atributo_display_name(attr):
        for aid, name in ATRIBUTOS_DEF:
            if aid == attr:
                return name
        return str(attr)

    def atributo_default_value(attr):
        return 10

    def atributo_value(attr):
        try:
            return int(persistent.atributos.get(attr, 10))
        except Exception:
            return 10

    def atributo_modifier_value(attr):
        try:
            value = int(atributo_value(attr))
            return int(math.floor((value - 10) / 2.0))
        except Exception:
            return 0

    def atributo_modifier_edit_value(attr):
        try:
            value = int(atributos_edit.get(attr, 10))
            return int(math.floor((value - 10) / 2.0))
        except Exception:
            return 0

    def init_atributos():
        try:
            if not hasattr(persistent, 'atributos'):
                persistent.atributos = {}
            for attr, _name in ATRIBUTOS_DEF:
                if attr not in persistent.atributos:
                    persistent.atributos[attr] = 10
            if not hasattr(persistent, 'atributos_confirmed'):
                persistent.atributos_confirmed = False
        except Exception:
            pass

    def atributos_edit_reset():
        global atributos_edit
        atributos_edit = {attr: int(atributo_value(attr)) for attr, _ in ATRIBUTOS_DEF}

    def atributos_points_used():
        return sum(max(0, atributos_edit.get(attr, 10) - 10) for attr, _ in ATRIBUTOS_DEF)

    def atributos_points_extra():
        return sum(max(0, 10 - atributos_edit.get(attr, 10)) for attr, _ in ATRIBUTOS_DEF)

    def atributos_available_max():
        return 6 + atributos_points_extra()

    def atributos_points_remaining():
        return atributos_available_max() - atributos_points_used()

    def atributos_adjust(attr, delta):
        try:
            if attr not in atributos_edit:
                return False
            current = int(atributos_edit[attr])
            candidate = current + int(delta)
            if candidate < 6 or candidate > 20:
                return False
            current_used = max(0, current - 10)
            candidate_used = max(0, candidate - 10)
            new_used = atributos_points_used() - current_used + candidate_used
            if candidate > current and new_used > atributos_available_max():
                return False
            atributos_edit[attr] = candidate
            return True
        except Exception:
            return False

    def atributos_adjust_action(attr, delta):
        atributos_adjust(attr, delta)
        return None

    def confirm_atributos_values():
        try:
            for attr, _name in ATRIBUTOS_DEF:
                persistent.atributos[attr] = int(atributos_edit.get(attr, 10))
            persistent.atributos_confirmed = True
            renpy.save_persistent()
            return True
        except Exception:
            return False

    def atributo_modifier(attr):
        return atributo_modifier_value(attr)
    
    


    # Define valor padrão para variável persistente usada no D20
    if not hasattr(persistent, 'd20_last_final'):
        setattr(persistent, 'd20_last_final', None)

    # Função auxiliar para finalizar a rolagem do D20 com segurança
    def d20_finish_roll(modifier, dc):
        # Garante que cada nova rolagem resulte em um número diferente da última
        last = getattr(persistent, 'd20_last_final', None)
        roll = renpy.random.randint(1, 20)
        if last is not None:
            # Evita repetir o último número; tenta algumas vezes e, se necessário, força um diferente
            for _ in range(10):
                if roll != last:
                    break
                roll = renpy.random.randint(1, 20)
            if roll == last:
                roll = (last % 20) + 1

        setattr(persistent, 'd20_last_final', roll)

        store.d20_final = roll
        store.d20_total = roll + modifier
        store.d20_success = (store.d20_total >= dc)
        store.d20_rolling = False
        store.d20_time_left = 0.0


default consequência_ativada = {
    "jinsei_mentira_sonho": False,
    "esqueceu_pao": False,
    "pasta_nova": False,
    "jinsei_verdade_sonho": False,
    "jinsei_visao_subaru": False,
    "ajuda_jinsei_subaru": False,
    "naoajuda_jinsei_subaru": False,
    "ajudar_estella_chave": False,
}

transform left_pos:
    zoom 0.7
    xalign 0.25
    yalign 1.0

transform right_pos:
    zoom 0.7
    xalign 0.75
    yalign 1.0

# Label para permitir salvar o jogo em pontos específicos
label save_point:
    menu:
        "Deseja salvar o jogo?"
        "Sim, salvar agora":
            $ amizade_commit()
            $ descricao_commit()
            $ renpy.take_screenshot()
            call screen save
            "Jogo salvo com sucesso!"
        "Não, continuar sem salvar":
            pass
    return

define k = Character("Kioku Aida", color="#4A90E2", image = "Kioku")
define j = Character("Jinsei Boto", color="#10d6d6", image = "Jinsei")
define s = Character("Estella Nascimento", color="#9B59B6", image = "Estella")
define si = Character("Subaru Ichida", color="#F5A623", image = "Subaru")
define ag = Character("Augustina Floriere", color="#27AE60", image = "Augustina")
define y = Character("Yuki Tatsuo", color="#2C3E50", image = "Yuki")
define yn = Character("Yoshida Namikaze", color="#E67E22", image = "Yoshida")

define dentesprimeiro = False
define banhoprimeiro = False
define mingaualimentadoprimeiro = False
define tomarcafeprimeiro = False

define dentesegundo = False
define banhosegundo = False
define mingaualimentadosegundo = False
define tomarcafesegundo = False

define trematraso = False
define provaatraso = False





# Variável para progresso do minigame (cliques)
default pasta_clicks = 0
default pasta_time_left = 5
default teste_pao_sucesso = False
default teste_pao_falha = False

# Variáveis do minigame de D20
default d20_rolling = False
default d20_current = 1
default d20_final = None
default d20_total = 0
default d20_success = False
default d20_time_left = 0.0
default atributos_edit = {}
default atributos_confirmed = False
default atributos_confirm_dialog = False

default persistent.atributos = {}
default persistent.atributos_confirmed = False

# Tela do minigame: clicar 20 vezes em 5 segundos
screen minigame_pasta():
    modal True
    zorder 300
    # Evita que ESC abra Preferências durante o minigame
    key "game_menu" action NullAction()

    # Contagem regressiva visual (5, 4, 3, 2, 1)
    timer 1.0 repeat True action [
        SetVariable('pasta_time_left', max(pasta_time_left - 1, 0)),
        If(pasta_time_left <= 1, Return(False))
    ]

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            label _("Tente tirar a pasta de dente!")
            text _("Clique 20 vezes em 5 segundos.")
            text _("Tempo: [pasta_time_left]")
            text _("Progresso: [pasta_clicks]/20")

            textbutton _("Clique aqui para tentar tirar a pasta de dente") action [
                SetVariable('pasta_clicks', pasta_clicks + 1),
                If(pasta_clicks + 1 >= 20, Return(True))
            ]

    # Fallback: se algo falhar, encerra após 6s
    timer 6.0 action If(pasta_time_left > 0, Return(False))

screen button:
    textbutton "Clique "

# Animações para o dado
transform d20_spin:
    rotate 0
    linear 0.12 rotate 20
    linear 0.12 rotate -15
    linear 0.12 rotate 10
    linear 0.12 rotate -5
    repeat

transform d20_shake:
    xoffset 0 yoffset 0
    linear 0.06 xoffset 8
    linear 0.06 xoffset -8
    repeat

screen minigame_d20(dc=10, modifier=0, title="Teste de D20", reveal_result=True, atributo=None):
    modal True
    zorder 300
    key "game_menu" action NullAction()

    # Atualiza número mostrado enquanto o dado está rolando
    timer 0.08 repeat True action If(d20_rolling, [
        SetVariable('d20_current', renpy.random.randint(1, 20)),
        SetVariable('d20_time_left', max(d20_time_left - 0.08, 0.0)),
        If(d20_time_left <= 0.08, Function(d20_finish_roll, modifier, dc))
    ])

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

            label _(title)
            if atributo is not None:
                text _("Atributo: [atributo_display_name(atributo)]    Dificuldade (DC): [dc]    Modificador: [modifier]")
            else:
                text _("Dificuldade (DC): [dc]    Modificador: [modifier]")

            if d20_final is None:
                if d20_rolling:
                    # Dado rolando: animações de spin e shake
                    frame at d20_shake:
                        xalign 0.5
                        yalign 0.5
                        xminimum 180
                        yminimum 180
                        xpadding 10
                        ypadding 10
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 6
                            text _("D20") size 24 at d20_spin
                            text _("[d20_current]") size 64 at d20_spin
                else:
                    # Dado parado, pronto pra clique
                    button:
                        xalign 0.5
                        yalign 0.5
                        xminimum 180
                        yminimum 180
                        background Solid("#333")
                        hover_background Solid("#444")
                        action [
                            SetVariable('d20_final', None),
                            SetVariable('d20_total', 0),
                            SetVariable('d20_success', False),
                            SetVariable('d20_rolling', True),
                            SetVariable('d20_time_left', 2.0)
                        ]
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 6
                            text _("Clique para rolar") xalign 0.5 size 25
                            # text _("[d20_current]") size 64
            else:
                # Resultado final
                if reveal_result:
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 12
                        text _("Resultado: [d20_final] + [modifier] = [d20_total]") size 42
                        if d20_success:
                            text _("Sucesso!") color "#00c853" size 44
                        else:
                            text _("Falha...") color "#d50000" size 44

                textbutton _("Continuar") action Return({
                    'success': d20_success,
                    'roll': d20_final,
                    'total': d20_total,
                    'dc': dc,
                    'modifier': modifier
                }) xalign 0.5

screen atributos_distribution():
    modal True
    zorder 350
    key "game_menu" action NullAction()

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            label _("Distribuir Atributos")
            text _("Você tem [atributos_points_remaining()] pontos restantes para gastar.")
            text _("Mínimo: 6, máximo: 20 para cada atributo.")
            text _("Lembre-se de clicar em Confirmar quando terminar a distribuição.")

            for attr, name in ATRIBUTOS_DEF:
                hbox:
                    spacing 16
                    text _("[name]") xminimum 140
                    text _("[atributos_edit.get(attr, 10)] (mod: [atributo_modifier_edit_value(attr):+d])")
                    textbutton _("-") action Function(atributos_adjust_action, attr, -1)
                    textbutton _("+") action Function(atributos_adjust_action, attr, 1)

            if atributos_points_remaining() < 0:
                text _("Erro: pontos negativos. Ajuste seus atributos.") color "#ff5555"

            hbox:
                spacing 14
                textbutton _("Redefinir") action Function(atributos_edit_reset)
                textbutton _("Confirmar") action SetVariable("atributos_confirm_dialog", True)

            if atributos_confirm_dialog:
                frame:
                    background Solid("#000c")
                    xfill True
                    yfill True
                    xalign 0.5
                    yalign 0.5
                    padding (20, 20)
                    vbox:
                        spacing 14
                        text _("Confirmação") size 26 bold True
                        text _("Você tem certeza que distribuiu da forma que queria? Os pontos só poderão ser distribuidos novamente após cada final de ato.") size 20
                        hbox:
                            spacing 14
                            textbutton _("Sim") action [Function(confirm_atributos_values), SetVariable("atributos_confirm_dialog", False), Return(True)]
                            textbutton _("Não") action SetVariable("atributos_confirm_dialog", False)

# Label utilitário para reaproveitar o minigame em diferentes cenas
# Use: "call rolar_d20 (dc=12, modifier=2, sucesso_label=\"minha_label_sucesso\", falha_label=\"minha_label_falha\", titulo=\"Teste de Força\")"
label rolar_d20(dc=10, modifier=0, atributo=None, sucesso_label=None, falha_label=None, titulo="Teste de D20", reveal_result=True):
    # Reset do estado do D20 para evitar reutilizar resultado anterior
    $ d20_final = None
    $ d20_total = 0
    $ d20_success = False
    $ d20_rolling = False
    $ d20_time_left = 0.0
    $ d20_current = renpy.random.randint(1, 20)

    if atributo is not None:
        $ modifier = modifier + atributo_modifier(atributo)
        if titulo == "Teste de D20":
            $ titulo = "Teste de D20: %s" % atributo_display_name(atributo)

    $ resultado = renpy.call_screen("minigame_d20", dc=dc, modifier=modifier, title=titulo, reveal_result=reveal_result, atributo=atributo)
    if resultado['success']:
        if sucesso_label is not None:
            jump expression sucesso_label
        return True
    else:
        if falha_label is not None:
            jump expression falha_label
        return False

# Notificações de consequência: animação e destaque visual
transform notify_slide_in:
    yoffset -48
    linear 0.14 yoffset 0

transform notify_pulse:
    zoom 1.0
    linear 0.45 zoom 1.06
    linear 0.45 zoom 1.0
    repeat

# Tela de notificação para escolhas com consequências (canto superior esquerdo).
# Aparece somente se `modohistoria` for True. Chame-a via `show_consequence(message, duration)`.
screen consequence_notify(message, duration=3):
    if modohistoria:
        modal False
        zorder 400
        frame:
            at notify_slide_in
            xalign 0.01
            yalign 0.02
            xpadding 14
            ypadding 10
            background Solid("#000c")
            text message color "#FFFFFF" size 34 bold True at notify_pulse

        timer duration action Return()

init python:
    # Helper para chamar a tela de notificação a partir do script.
    # Uso: $ show_consequence("Fulano se lembrará disso", 3)
    def show_consequence(message, duration=3):
        try:
            if not modohistoria:
                return
        except Exception:
            # Se a variável não existir por algum motivo, não tenta mostrar
            return

        renpy.call_screen("consequence_notify", message=message, duration=duration)


image side Kioku normal = im.Scale("images/Personagens/Kioku Aida/KiokuCNormal.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku feliz = im.Scale("images/Personagens/Kioku Aida/KiokuCFeliz1.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku superfeliz = im.Scale("images/Personagens/Kioku Aida/KiokuCFeliz2.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku hiperfeliz = im.Scale("images/Personagens/Kioku Aida/KiokuCFeliz3.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku bravo = im.Scale("images/Personagens/Kioku Aida/KiokuCIrritado1.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku irritado = im.Scale("images/Personagens/Kioku Aida/KiokuCIrritado2.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku achando = im.Scale("images/Personagens/Kioku Aida/KiokuCMal.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku divertindo = im.Scale("images/Personagens/Kioku Aida/KiokuCRir.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku surpreso = im.Scale("images/Personagens/Kioku Aida/KiokuCSurpreso.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku triste = im.Scale("images/Personagens/Kioku Aida/KiokuCTriste.png", 470, 570, xoffset=0, yoffset=100)
image side Kioku morte = im.Scale("images/Personagens/Kioku Aida/KiokuM.png", 470, 570, xoffset=0, yoffset=100)

image KiokuM:
    "Personagens/Kioku Aida/KiokuM.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image side Jinsei sorisso = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCFeliz.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei encantadaf = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCeencantada.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei brava = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCbrava.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei choro = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCChoro.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei encantada = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCEncantada.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei furiosa = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCGrito.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei bravanime = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCirritada.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei normal = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCNormal.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei achando = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCSmug.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei sorissof = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCSorriso.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei seachando = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCssmuga.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei surpresa = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCSurpresa.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei triste = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Pijama/JinseiCTriste.png", 570, 570, xoffset=-30, yoffset=100)

image JinseiCbravanime:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCirritada.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCsorisso:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCSorriso.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCbrava:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCbrava.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCchoro:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCChoro.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCEEncantada:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCeencantada.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCencantada:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCEncantada.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCfeliz:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCFeliz.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCgrito:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCGrito.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCnormal:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCNormal.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCsmug:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCSmug.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCsmuga:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCsmuga.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCsurpresa:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCSurpresa.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiCtriste:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Pijama/JinseiCTriste.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5


image side Jinsei Brava = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCBrava.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Bravanime = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCBravanime.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Choro = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCChoro.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Dormindo = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCDormindo.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Feliz = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCFeliz.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Feliz2 = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCFeliz2.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Feliz3 = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCFeliz3.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Feliz4 = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCFeliz4.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Irritada = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCIrritada.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei NNormal = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCNormal.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Sono = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCSono.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Surpresa = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCSurpresa.png", 570, 570, xoffset=-30, yoffset=100)
image side Jinsei Triste = im.Scale("images/Personagens/Jinsei Boto/Jinsei Boto Fala Escola/JinseiCTriste.png", 570, 570, xoffset=-30, yoffset=100)

image Jinseibravanime:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiBravanime.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiFeliz2:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiFeliz2.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Jinseibrava:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiBrava.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiChoro:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiChoro.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiDormindo:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiDormindo.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiFeliz3:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiFeliz3.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiFeliz:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiFeliz.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiFeliz4:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiFeliz4.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiNormal:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiNormal.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiIrritada:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiIrritada.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiSono:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiSono.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiSurpresa:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiSurpresa.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image JinseiTriste:
    "Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiTriste.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5



image side Subaru normal = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidanormal.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru sorisso = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidasorisso.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru bravo1 = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidabravo.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru bravo2 = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidabravo2.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru irritado = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidairritado.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru assustado = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidaassustado.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru triste = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidatriste.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru triste2 = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidatriste2.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru fond = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidafond.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru fond2 = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidafond2.png", 470, 570, xoffset=0, yoffset=100)
image side Subaru sangue = im.Scale("images/Personagens/Subaru Ichida/SubaruIchidaSangue.png", 470, 570, xoffset=0, yoffset=100)

image Subaru sorisso:
    "images/Personagens/Subaru Ichida/SubaruIchidasorisso.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Subaru assustado:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidaassustado.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru bravo2:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidabravo2.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru bravo1:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidabravo.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru fond:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidafond.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru fond2:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidafond2.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru irritado:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidairritado.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru normal:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidanormal.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru triste:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidatriste.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru triste2:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidatriste2.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Subaru sangue:
    "images/Personagens/Subaru Ichida/Subaru Ichida Tela/SubaruIchidaSangue.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Yuki normal:
    "images/Personagens/Yuki Tatsuo/Yuki Tela/YukiTatsuo.png"
    zoom 0.7
    xalign 0.5
    yalign 1.5

image Augustina feliz:
    "images/Personagens/Augustina Floriere/Augustinafeliz.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0
 
image Augustina normal:
    "images/Personagens/Augustina Floriere/Augustinanormal.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0

image side Yoshida normal = im.Scale("images/Personagens/Yoshida Namikaze/YoshidaNamikaze.png", 370, 470, xoffset=25, yoffset=50)

image Yoshida normal:
    "images/Personagens/Yoshida Namikaze/YoshidaNamikaze.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0


image side Estella normal = im.Scale("images/Personagens/Estella Nascimento/StellaNascimento.png", 470, 570, xoffset=0, yoffset=100)
image side Estella envergonhada = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoEnvergonhada.png", 470, 570, xoffset=0, yoffset=100)
image side Estella feliz = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoFeliz.png", 470, 570, xoffset=0, yoffset=100)
image side Estella feliz2 = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoFeliz2.png", 470, 570, xoffset=0, yoffset=100)
image side Estella feliz3 = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoFeliz3.png", 470, 570, xoffset=0, yoffset=100)
image side Estella happy1 = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoHappy1.png", 470, 570, xoffset=0, yoffset=100)
image side Estella happy2 = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoHappy2.png", 470, 570, xoffset=0, yoffset=100)
image side Estella triste = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoSad.png", 470, 570, xoffset=0, yoffset=100)
image side Estella smug = im.Scale("images/Personagens/Estella Nascimento/StellaNascimentoSmug.png", 470, 570, xoffset=0, yoffset=100)

image Stella normal:
    "images/Personagens/Estella Nascimento/StellaNascimento.png"
    zoom 0.5
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella envergonhada:
    "images/Personagens/Estella Nascimento/StellaNascimentoEnvergonhada.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella feliz:
    "images/Personagens/Estella Nascimento/StellaNascimentoFeliz.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella feliz2:
    "images/Personagens/Estella Nascimento/StellaNascimentoFeliz2.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella feliz3:
    "images/Personagens/Estella Nascimento/StellaNascimentoFeliz3.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella happy1:
    "images/Personagens/Estella Nascimento/StellaNascimentoHappy1.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella happy2:
    "images/Personagens/Estella Nascimento/StellaNascimentoHappy2.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella triste:
    "images/Personagens/Estella Nascimento/StellaNascimentoSad.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image Stella smug:
    "images/Personagens/Estella Nascimento/StellaNascimentoSmug.png"
    zoom 0.7
    xalign 0.5
    yalign 1.0 # Ou 1.0 se quiser que ela fique "em pé" no chão da tela

image side Yuki normal = im.Scale("images/Personagens/Yuki Tatsuo/YukiTatsuo.png", 470, 570, xoffset=0, yoffset=100)

image side Augustina feliz = im.Scale("images/Personagens/Augustina Floriere/Augustinafeliz.png", 244.5, 554, xoffset=100, yoffset=100)
image side Augustina normal = im.Scale("images/Persoangens/Augustina Floriere/Augustinanormal.png", 244.5, 554, xoffset=100, yoffset=100)




image Ato1 = "Atos/Ato I/AtoI.png"
image Cap1 = "Atos/Ato I/Capítulo_1.png"
image Quarto1 = "Predio/QuartoManha.png"
image narrador = "blackbackground.png"
image sonhokioku = "SonhoKioku.png"
image kiokujovem = "KiokuJovem.png"
image kiokujovemf = "KiokuJovemF.png"
image banheiroap = "Predio/Bathroom.png"
image banheiroapbanho = "Predio/Bathroom_Foggy.png"
image apartamentoexterno = "Predio/Apartment_Exterior.png"
image apartamentoexternonoite = "Predio/Apartment_Exterior_Night.png"
image armariodetoalhas = "Predio/Futon_Room.png"
image cozinhaap = "Predio/Small_Apartment_Kitchen.png"
image cozinhaapnoite = "Predio/Small_Apartment_Kitchen_Night.png"
image trem = "Train_Day.png"
image sala = "Predio/Sitting_Room.png"
image salaanoite = "Predio/Sitting_Room_Dark.png"
image escadalavanderia = "Predio/Outdoor_Stairs.png"
image estacaodetrem = "EstacaoTrem.png"
image entradaescoladia = "Escola/Entrada Dia.png"
image hallescoladia = "Escola/Hall de Entrada Dia.png"
image escadaescoladia = "Escola/Escadas Dia.png"
image corredordia = "Escola/Corredor Dia.png"
image salaauladia = "Escola/Sala de Aula Dia.png"
image saladiretordia = "Escola/Sala do Diretor Dia.png"
image salaprofessordia = "Escola/Sala dos Professores Dia.png"
image vestiarioescoladia = "Escola/Vestiário Dia.png"
image refeitorioescoladia = "Escola/Refeitório Dia.png"
image patioescoladia = "Escola/Pátio1 Dia.png"
image patioescoladia2 = "Escola/Pátio2 Dia.png"
image banheiroescoladia = "Escola/Banheiro Dia.png"
image biblioteca1 = "Escola/Biblioteca/Biblioteca_1.png"
image biblioteca2 = "Escola/Biblioteca/Biblioteca_2.png"
image biblioteca3 = "Escola/Biblioteca/Biblioteca_3.png"


image mingaudormindo = "fuff_zzz.png"
image minguaufeliz = "fuff_smug.png"

# The game starts here.

label start:


    show screen phone_button
    show screen phone_notification
    show screen phone_system
    # Ensure the attribute system is initialized for a new game.
    $ init_atributos()
    if not persistent.atributos_confirmed:
        $ atributos_edit_reset()
        $ renpy.call_screen("atributos_distribution")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show narrador
    with pixellate
    show screen achievement_queue_watcher


label escolhamodo:
    $ receive_unknown_message("Estella", "Oi... esse é seu número?", "estella_contato.png")
    "{cps=40}Antes de começarmos, por favor escolha o modo de jogo:{/cps}"

    jump modojogo

label modojogo:
    
    menu:
        "Modo História":
            "{cps=40}{i}Neste modo, você poderá aproveitar a história completamente, porém terão informações a mais.{/i}{/cps}"
            "{cps=40}{i}Como exemplo, você saberá quando uma escolha terá consequências, escolhas que personagens poderão lembra-las mais tarde, entre outras coisas...{/i}{/cps}"
            "{cps=40}{i}Dito isso, você tem certeza que deseja escolher esta opção?"
            menu:
                "Sim":
                    $ modohistoria = True
                    "{cps=40}{i}Você escolheu o Modo História.{/i}{/cps}"
                    jump jogo
                "Não, voltar":
                    jump modojogo
        "Modo Imersivo":
            "{cps=40}{i}Diferente do Modo História, aqui você terá uma experiência mais imersiva.{/i}{/cps}"
            "{cps=40}{i}Você não saberá quando uma escolha terá consequências, escolhas que personagens poderão lembra-las mais tarde, caberá a você decidir se aquela escolha foi a certa.{/i}{/cps}"
            "{cps=40}{i}Esteja ciente que algumas escolhas poderão te levar a finais \"ruin\".{/i}{/cps}"
            "{cps=40}{i}Este modo é o recomendado pelo desenvolvedor, para que você se sinta na pela de Kioku, e sinta que realmente suas escolhas podem afetar o futuro, mesmo não sabendo na hora.{/i}{/cps}"
            "{cps=40}{i}Dito isso, você tem certeza que deseja escolher esta opção?"
            menu:
                "Sim":
                    $ modoimersivo = True
                    "{cps=40}{i}Você escolheu o Modo Imersivo.{/i}{/cps}"
                    jump jogo
                "Não, voltar":
                    jump modojogo

label jogo:
    pause 1.5
    "{cps=30}{i}Olá, você pode não me conhecer, mas eu conheço você muito bem [nome_pc]...{/i}{/cps}"
    "{cps=30}{i}Você está prestes a adentrar na vida de Kioku Aida, um jovem comum que vive em uma cidade comum...{/i}{/cps}"
    "{cps=30}{i}Mas como você verá, nem tudo é tão comum assim...{/i}{/cps}"
    "{cps=30}{i}Durante esta jornada, você poderá descobrir segredos, mentiras e até mesmo verdades ocultas...{/i}{/cps}"
    "{cps=30}{i}E cabe a VOCÊ [nome_pc] decidir o destino de Kioku...{/i}{/cps}"
    "{cps=30}{i}Apenas você pode escolher o caminho que ele seguirá...{/i}{/cps}"
    "{cps=30}{i}Ele pode ter um ponto final dessa história\nUma reviravolta que não o fara bem para a cabeça\nOu até mesmo ele nunca sequer saber de nada...{/i}{/cps}"
    "{cps=30}{i}O poder da dúvida e da certeza está nas suas mãos, cada escolha, cada memória, cada lembrança, cada amizade, cabe a você decidir se vale ou não a pena tê-las...{/i}{/cps}"
    "{cps=30}{i}Mas lembre-se, cada ação tem uma consequência...{/i}{/cps}"
    "{cps=30}{i}Então escolha sabiamente, e boa sorte...{/i}{/cps}"
    "{cps=30}{i}Eu estarei observando, nos vemos..... em breve [nome_pc]....{/i}{/cps}"
    jump Capítulo_1