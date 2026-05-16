# =========================================
# PHONE SYSTEM COMPLETO - REN'PY
# =========================================



init python:
    
    import renpy.store as store

# =========================================
# IMAGENS
# =========================================

image sms_icon = "images/ui/sms.png"
image lock_icon = "images/ui/lock.png"

image phone_home_bg = "images/ui/celular.png"
image phone_contacts_bg = "images/ui/contatos.png"
image phone_chat_bg = "images/ui/celularsmsfundo.png"

image back_icon = "images/ui/back_button.png"
image info_icon = "images/ui/info_button.png"
image send_disabled = "images/ui/send_button_disabled.png"

image jinsei_avatar = "images/ui/fotos_contatos/jinsei_contato.png"

style phone_message is default:
    font "JMH Typewriter-Bold.ttf"

style phone_message_time is default:
    font "JMH Typewriter-Bold.ttf"

style phone_message_preview is default:
    font "JMH Typewriter-Bold.ttf"

style phone_header is default:
    font "JMH Typewriter-Bold.ttf"

# =========================================
# VARIÁVEIS
# =========================================

default editing_contact_name = False

default temp_contact_name = ""

default contact_display_names = {
    "Jinsei": "Jinsei",
}

default contact_avatars = {
    "Jinsei": "images/ui/fotos_contatos/jinsei_contato.png",
    "Estella": "images/ui/fotos_contatos/estella_contato.png"
}

default player_typing_active = False
default player_typing_contact = None
default player_typing_target = ""
default player_typing_shown = ""
default player_typing_label = None

default player_choice_text = ""
default player_choice_target_label = None
default player_choice_date = None
default player_choice_time = None

default typing_contact = None
default typing_active = False

default current_game_date = "2026-04-28"

default phone_open = False
default phone_screen = "home"

default archive_password = "0405"
default archive_input = ""
default archive_unlocked = False

default phone_notify_active = False
default phone_notify_sender = ""
default phone_notify_text = ""

default unlocked_contacts = ["Jinsei"]

default archived_contacts = ["Akemi", "Unknown", "Mãe"]

default current_chat = None

default phone_chat_scroll_bottom = False

default phone_choices = {
    "estella_novo_contato": [
        {
            "text": "Quem é?",
            "label": "reply_estella_novo1"
        },
        {
            "text": "Sim, é meu número.",
            "label": "reply_estella_novo2"
        },
    ],

    "jinsei_yuki_atraso": [
        {
            "text": "Relaxa, eu nunca me atraso ;)",
            "label": "reply_jinsei_atraso1",
            "time": "08:15"
        },
        {
            "text": "Pó dexa 👍",
            "label": "reply_jinsei_atraso2",
            "time": "08:15"
        }
    ]


}

default chats = {

    "Jinsei": [

        # =========================
        # PRIMEIRO CONTATO - 2023
        # =========================

        {"sender": "Jinsei", "text": "Oi... Kioku?", "date": "2023-04-11", "time": "08:42"},

        {"sender": "Player", "text": "Jinsei?", "date": "2023-04-11", "time": "08:44"},

        {"sender": "Jinsei", "text": "Quanto tempo...", "date": "2023-04-11", "time": "08:44"},

        {"sender": "Jinsei", "text": "Acho que somos colegas em Libras.", "date": "2023-04-11", "time": "08:45"},

        {"sender": "Player", "text": "Sério? Que coincidência.", "date": "2023-04-11", "time": "08:46"},

        {"sender": "Jinsei", "text": "Ou azar.", "date": "2023-04-11", "time": "08:46"},

        {"sender": "Player", "text": "Você continua estranha kk.", "date": "2023-04-11", "time": "08:47"},


        # =========================
        # REAPROXIMAÇÃO
        # =========================

        {"sender": "Jinsei", "text": "Você ainda toma café sem açúcar?", "date": "2023-05-02", "time": "16:11"},

        {"sender": "Player", "text": "Você lembra disso?", "date": "2023-05-02", "time": "16:12"},

        {"sender": "Jinsei", "text": "Eu lembro de muita coisa.", "date": "2023-05-02", "time": "16:13"},


        # =========================
        # PRIMEIRO MOMENTO ESTRANHO
        # =========================

        {"sender": "Player", "text": "Você vai no acampamento do pessoal Mês que vem?", "date": "2023-06-14", "time": "22:03"},

        {"sender": "Jinsei", "text": "Não gosto mais desse tipo de lugar.", "date": "2023-06-14", "time": "22:05"},

        {"sender": "Player", "text": "Desde quando?", "date": "2023-06-14", "time": "22:05"},

        {"sender": "Jinsei", "text": "...", "date": "2023-06-14", "time": "22:07"},

        {"sender": "Jinsei", "text": "Só não gosto.", "date": "2023-06-14", "time": "22:08"},


        # =========================
        # 2024
        # =========================

        {"sender": "Jinsei", "text": "Você dormiu na aula de novo.", "date": "2024-03-19", "time": "13:55"},

        {"sender": "Player", "text": "A culpa é do professor.", "date": "2024-03-19", "time": "13:56"},

        {"sender": "Jinsei", "text": "Você disse isso semestre passado também.", "date": "2024-03-19", "time": "13:57"},

        {"sender": "Player", "text": "Então... Ainda é culpa dos professores muito chato as aulas, ta loco.", "date": "2024-03-19", "time": "13:58"},

        {"sender": "Jinsei", "text": "Você tem que se esforçar mais.", "date": "2024-03-19", "time": "13:59"},

        {"sender": "Jinsei", "text": "Não pode ficar dormindo nas aulas", "date": "2024-03-19", "time": "14:00"},

        {"sender": "Player", "text": "To com nota de sobra nessa cadeira, to bem.", "date": "2024-03-19", "time": "14:05"},

        {"sender": "Player", "text": "Tá, tenho aula de Física II agora, até....", "date": "2024-03-19", "time": "14:05"},

        {"sender": "Jinsei", "text": "Não sei como você gosta de Exatas..", "date": "2024-03-19", "time": "14:07"},

        {"sender": "Player", "text": "Não entendo como você gosta de Artes Sênicas", "date": "2024-03-19", "time": "14:10"},


        # =========================
        # MENSAGENS MAIS PESSOAIS
        # =========================

        {"sender": "Jinsei", "text": "Você anda dormindo direito?", "date": "2024-09-02", "time": "01:14"},

        {"sender": "Player", "text": "Por que a pergunta?", "date": "2024-09-02", "time": "01:16"},

        {"sender": "Jinsei", "text": "Você parece cansado ultimamente.", "date": "2024-09-02", "time": "01:18"},

        {"sender": "Player", "text": "Talvez eu só esteja ficando velho.", "date": "2024-09-02", "time": "01:19"},

        {"sender": "Jinsei", "text": "Você fala como se fosse um senhor de 70 anos.", "date": "2024-09-02", "time": "01:20"},

        {"sender": "Player", "text": "E se eu for 😱😱😱😱", "date": "2024-09-02", "time": "01:25"},


        # =========================
        # 2025
        # =========================

        {"sender": "Player", "text": "Acha que pessoas podem esquecer algo importante?", "date": "2025-07-11", "time": "23:51"},

        {"sender": "Jinsei", "text": "Depende.", "date": "2025-07-11", "time": "23:53"},

        {"sender": "Player", "text": "Depende do quê?", "date": "2025-07-11", "time": "23:54"},

        {"sender": "Jinsei", "text": "Do quanto aquilo machucou ou traumatizou", "date": "2025-07-11", "time": "23:56"},

        {"sender": "Jinsei", "text": "Porquê?", "date": "2025-07-11", "time": "23:57"},

        {"sender": "Player", "text": "Nada, pra saber.", "date": "2025-07-11", "time": "23:58"},


        # =========================
        # ONTEM - 2026
        # =========================

        {"sender": "Jinsei", "text": "Você chegou em casa?", "date": "2026-04-27", "time": "17:30"},

        {"sender": "Player", "text": "Agora sim.", "date": "2026-04-27", "time": "18:00"},

        {"sender": "Jinsei", "text": "Você sumiu depois da aula.", "date": "2026-04-27", "time": "18:01"},

        {"sender": "Player", "text": "Tava cansado.", "date": "2026-04-27", "time": "18:02"},

        {"sender": "Jinsei", "text": "Você anda dizendo muito isso ultimamente.", "date": "2026-04-27", "time": "18:03"},

        {"sender": "Player", "text": "Talvez porque seja verdade.", "date": "2026-04-27", "time": "18:04"},

        {"sender": "Jinsei", "text": "Só tenta dormir cedo hoje.", "date": "2026-04-27", "time": "18:05"},
    ],

    "Akemi": [
        {"sender": "Akemi", "text": "Você prometeu esquecer isso."},
        {"sender": "Player", "text": "Eu tentei."}
    ],

    "Unknown": [
        {"sender": "Unknown", "text": "ELE ESTÁ OBSERVANDO."}
    ],

    "Mãe": [
        {"sender": "Mãe", "text": "Me liga quando puder."}
    ]
}

default pending_choices = {}

# =========================================
# TRANSFORMS
# =========================================

transform phone_home_transform:
    xalign 0.5
    yalign 0.5
    zoom 0.58
    xoffset 0
    yoffset 0

transform phone_contacts_transform:
    xalign 0.5
    yalign 0.5
    zoom 0.58
    xoffset 0
    yoffset 0

transform phone_chat_transform:
    xalign 0.5
    yalign 0.5
    zoom 0.58
    xoffset 0
    yoffset 0

transform phone_icon_idle:
    zoom 0.08
    xalign 0.98
    yalign 0.03

transform phone_center:
    xalign 0.5
    yalign 0.5
    zoom 0.58

transform phone_icon_shake:
    zoom 0.08
    xalign 0.98
    yalign 0.03
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset 0
    repeat

transform notif_slide:
    xalign 0.5
    yalign -0.2
    linear 0.35 yalign 0.05
    pause 2.5
    linear 0.35 yalign -0.2

transform dot_wave(delay=0.0):
    alpha 0.3
    yoffset 0
    pause delay
    block:
        linear 0.25 alpha 1.0 yoffset -8
        linear 0.25 alpha 0.3 yoffset 0
        pause 0.25
        repeat

# =========================================
# FUNÇÕES
# =========================================

init python:

    typing_key_list = [
        "K_a","K_b","K_c","K_d","K_e","K_f","K_g","K_h","K_i","K_j","K_k","K_l","K_m",
        "K_n","K_o","K_p","K_q","K_r","K_s","K_t","K_u","K_v","K_w","K_x","K_y","K_z",
        "K_0","K_1","K_2","K_3","K_4","K_5","K_6","K_7","K_8","K_9",
        "K_SPACE","K_RETURN","K_BACKSPACE"
    ]

    def begin_player_typing(contact, text, label_name=None):
        store.player_typing_active = True
        store.player_typing_contact = contact
        store.player_typing_target = text
        store.player_typing_shown = ""
        store.player_typing_label = label_name
        store.phone_chat_scroll_bottom = True
        renpy.restart_interaction()

    def player_type_next_char():
        if store.player_typing_active:
            current_len = len(store.player_typing_shown)
            target_len = len(store.player_typing_target)

            if current_len < target_len:
                store.player_typing_shown = store.player_typing_target[:current_len + 1]
            else:
                store.player_typing_active = False

        renpy.restart_interaction()

    def finish_player_typing():
        store.player_typing_active = False
        store.player_typing_contact = None
        store.player_typing_target = ""
        store.player_typing_shown = ""
        store.player_typing_label = None
        renpy.restart_interaction()

    def get_npc_typing_delay(text, base=0.8, per_char=0.05, minimum=0.8, maximum=6.0):
        if text is None:
            return minimum
        delay = base + len(text) * per_char
        return min(max(delay, minimum), maximum)

label player_choice_send:
    $ pending_choices.pop(current_chat, None)
    call send_player_message(current_chat, player_choice_text, player_choice_date, player_choice_time)
    $ next_label = player_choice_target_label
    $ player_choice_text = ""
    $ player_choice_target_label = None
    $ player_choice_date = None
    $ player_choice_time = None

    if next_label:
        jump expression next_label

    return

label send_player_message(contact, text, date=None, time=None):
    $ begin_player_typing(contact, text)

    while player_typing_active:
        pause 0.03

    $ add_message(contact, "Player", text, date, time)
    $ phone_chat_scroll_bottom = True
    $ finish_player_typing()

    return

label npc_type_and_send(contact, text, time=None):
    $ typing_contact = contact
    $ typing_active = True
    $ renpy.restart_interaction()

    pause get_npc_typing_delay(text)

    $ typing_active = False
    $ add_message(contact, contact, text, time=time)
    $ renpy.restart_interaction()

    return
init python:

    def unlock_contact(name):
        if name not in store.unlocked_contacts:
            store.unlocked_contacts.append(name)

    def add_message(contact, sender, text, date=None, time=None):
        if contact not in store.chats:
            store.chats[contact] = []
        if store.phone_screen == "chat" and store.current_chat == contact:
            store.phone_chat_scroll_bottom = True
        if date is None:
            date = store.current_game_date
        if time is None:
            time = ""
        store.chats[contact].append({
            "sender": sender,
            "text": text,
            "date": date,
            "time": time
        })

    import datetime

    def format_chat_date(date_text):
        months = {
            1: "janeiro",
            2: "fevereiro",
            3: "março",
            4: "abril",
            5: "maio",
            6: "junho",
            7: "julho",
            8: "agosto",
            9: "setembro",
            10: "outubro",
            11: "novembro",
            12: "dezembro"
        }

        msg_date = datetime.datetime.strptime(date_text, "%Y-%m-%d").date()
        today = datetime.datetime.strptime(store.current_game_date, "%Y-%m-%d").date()

        if msg_date == today:
            return "Hoje"

        if msg_date == today - datetime.timedelta(days=1):
            return "Ontem"

        if msg_date.year == today.year:
            return "%d de %s" % (msg_date.day, months[msg_date.month])

        return "%d de %s de %d" % (msg_date.day, months[msg_date.month], msg_date.year) 

    def get_chat_preview(text, max_chars=40):
        if text is None:
            return ""
        if len(text) <= max_chars:
            return text
        return text[:max_chars - 3].rstrip() + "..."

    def get_contact_name(contact):
        return store.contact_display_names.get(contact, contact)

    def get_contact_avatar(contact):
        return store.contact_avatars.get(contact, "images/ui/fotos_contatos/default.png")

    def register_contact(contact_id, display_name="???", avatar_file="default.png"):
        if contact_id not in store.unlocked_contacts:
            store.unlocked_contacts.append(contact_id)

        if contact_id not in store.chats:
            store.chats[contact_id] = []

        if contact_id not in store.contact_display_names:
            store.contact_display_names[contact_id] = display_name

        if contact_id not in store.contact_avatars:
            store.contact_avatars[contact_id] = "images/ui/fotos_contatos/" + avatar_file

    def receive_unknown_message(contact_id, text, avatar_file="default.png"):
        register_contact(contact_id, "???", avatar_file)

        add_message(contact_id, contact_id, text)

        store.phone_notify_active = True
        store.phone_notify_sender = "???"
        store.phone_notify_text = text

        renpy.restart_interaction()

    def receive_message(contact_id, text, time=None):
        register_contact(contact_id, get_contact_name(contact_id), "default.png")

        add_message(contact_id, contact_id, text, time=time)

        store.phone_notify_active = True
        store.phone_notify_sender = get_contact_name(contact_id)
        store.phone_notify_text = text

        renpy.restart_interaction()

    def clear_notification():
        store.phone_notify_active = False
        store.phone_notify_sender = ""
        store.phone_notify_text = ""
        renpy.restart_interaction()

    def set_pending_choice(contact, choice_id):
        store.pending_choices[contact] = choice_id

# =========================================
# ÍCONE GLOBAL DO CELULAR
# =========================================

screen phone_button():

    zorder 100

    if phone_notify_active:
        imagebutton:
            idle "images/ui/celular.png"
            hover "images/ui/celular.png"
            action [
                SetVariable("phone_open", True),
                SetVariable("phone_screen", "home"),
                Function(clear_notification)
            ]
            at phone_icon_shake
    else:
        imagebutton:
            idle "images/ui/celular.png"
            hover "images/ui/celular.png"
            action [
                SetVariable("phone_open", True),
                SetVariable("phone_screen", "home")
            ]
            at phone_icon_idle

# =========================================
# NOTIFICAÇÃO
# =========================================

screen phone_notification():

    zorder 101

    if phone_notify_active:

        frame:
            at notif_slide
            xsize 520
            ysize 95
            background "#111d"
            padding (20, 12)

            vbox:
                spacing 5

                text "[phone_notify_sender] enviou uma mensagem" size 24 color "#ffffff"
                text "[phone_notify_text]" size 18 color "#cccccc"

# =========================================
# CELULAR PRINCIPAL
# =========================================

screen phone_system():

    zorder 200

    if phone_open:

        modal True

        button:
            background "#0000"
            xfill True
            yfill True
            action NullAction()

        # TROCA AUTOMÁTICA DO FRAME
        if phone_screen == "chat":
            add "phone_chat_bg" at phone_chat_transform

        elif phone_screen == "sms" or phone_screen == "archive_list" or phone_screen == "archive_password":
            add "phone_contacts_bg" at phone_contacts_transform

        else:
            add "phone_home_bg" at phone_home_transform

        frame:
            background None
            xalign 0.5
            yalign 0.5
            xsize 390
            ysize 720

            if phone_screen == "home":
                use phone_home

            elif phone_screen == "sms":
                use phone_sms_main

            elif phone_screen == "chat":
                use phone_chat

            elif phone_screen == "archive_password":
                use phone_archive_password

            elif phone_screen == "archive_list":
                use phone_archive_list

# =========================================
# HOME DO CELULAR
# =========================================

screen phone_home():

    fixed:

        textbutton "X":
            xpos 300
            ypos 62
            text_size 28
            text_color "#ffffff"
            background None
            hover_background None
            action SetVariable("phone_open", False)

        vbox:
            xpos 62
            ypos 105
            spacing 4

            imagebutton:
                idle "sms_icon"
                hover "sms_icon"
                xysize (44, 44)
                action SetVariable("phone_screen", "sms")

            text "SMS" style "phone_header" size 18 color "#ffffff" xalign 0.5

        fixed:
            xpos 250
            ypos 105

            imagebutton:
                idle Transform("images/ui/lock.png", xysize=(52, 52))
                hover Transform("images/ui/lock.png", xysize=(52, 52))
                action SetVariable("phone_screen", "archive_password")
# =========================================
# TELA PRINCIPAL SMS
# =========================================

screen phone_sms_main():

    fixed:

        imagebutton:
            idle "back_icon"
            hover "back_icon"
            xpos 32
            ypos 38
            xysize (30, 30)
            action SetVariable("phone_screen", "home")

        text "CONTATOS":
            style "phone_header"
            xalign 0.5
            ypos 50
            size 20
            color "#d9d9d9"

        viewport:
            xpos 38
            ypos 115
            xsize 315
            ysize 470
            draggable True
            mousewheel True

            vbox:
                spacing 6

                for contact in unlocked_contacts:

                    button:
                        xsize 315
                        ysize 76
                        background "#00000000"
                        hover_background "#ffffff18"
                        action [
                            SetVariable("current_chat", contact),
                            SetVariable("phone_screen", "chat"),
                            SetVariable("phone_chat_scroll_bottom", True)
                        ]

                        hbox:
                            spacing 12
                            yalign 0.5

                            add get_contact_avatar(contact) xysize (54, 54)

                            vbox:
                                yalign 0.5
                                spacing 3

                                text get_contact_name(contact):
                                    style "phone_header"
                                    size 22
                                    color "#ffffff"

                                if len(chats.get(contact, [])) > 0:
                                    text get_chat_preview(chats[contact][-1]["text"], 40):
                                        style "phone_message_preview"
                                        size 14
                                        color "#aaaaaa"
                                        xmaximum 210
                                        text_align 0.0

# =========================================
# SENHA DOS ARQUIVADOS
# =========================================

screen phone_archive_password():

    fixed:

        imagebutton:
            idle "back_icon"
            hover "back_icon"
            xpos 32
            ypos 38
            xysize (30, 30)
            action SetVariable("phone_screen", "home")

        text "Digite sua senha:":
            style "phone_header"
            xalign 0.5
            ypos 100
            size 28
            color "#ffffff"

        text "[archive_input]":
            xalign 0.5
            ypos 142
            size 34
            color "#7BE0FF"

        grid 3 4:
            xpos 72
            ypos 220
            spacing 28

            for n in ["1","2","3","4","5","6","7","8","9","DEL","0","OK"]:

                textbutton n:
                    xsize 58
                    ysize 58
                    background None
                    text_size 28
                    text_color "#ffffff"
                    text_hover_color "#7BE0FF"

                    if n == "DEL":
                        action SetVariable("archive_input", archive_input[:-1])

                    elif n == "OK":
                        if archive_input == archive_password:
                            action [
                                SetVariable("archive_unlocked", True),
                                SetVariable("archive_input", ""),
                                SetVariable("phone_screen", "archive_list")
                            ]
                        else:
                            action SetVariable("archive_input", "")

                    else:
                        if len(archive_input) < 4:
                            action SetVariable("archive_input", archive_input + n)
                        else:
                            action NullAction()
# =========================================
# LISTA DE ARQUIVADOS
# =========================================

screen phone_archive_list():

    fixed:

        imagebutton:
            idle "back_icon"
            hover "back_icon"
            xpos 32
            ypos 38
            xysize (30, 30)
            action SetVariable("phone_screen", "home")

        viewport:
            xpos 38
            ypos 115
            xsize 315
            ysize 470
            draggable True
            mousewheel True

            vbox:
                spacing 6

                for contact in archived_contacts:

                    button:
                        xsize 315
                        ysize 76
                        background "#00000000"
                        hover_background "#ffffff18"
                        action [
                            SetVariable("current_chat", contact),
                            SetVariable("phone_screen", "chat"),
                            SetVariable("phone_chat_scroll_bottom", True)
                        ]

                        hbox:
                            spacing 12
                            yalign 0.5

                            add "lock_icon" xysize (48, 48)

                            vbox:
                                yalign 0.5
                                spacing 3

                                text get_contact_name(contact):
                                    style "phone_header"
                                    size 22
                                    color "#ffffff"

                                if len(chats.get(contact, [])) > 0:
                                    text get_chat_preview(chats[contact][-1]["text"], 40) size 14 color "#aaaaaa" xmaximum 220 text_align 0.0

# =========================================
# TELA DE CONVERSA
# =========================================

screen phone_chat():

    fixed:

        imagebutton:
            idle "back_icon"
            hover "back_icon"
            xpos 32
            ypos 38
            xysize (30, 30)

            if current_chat in archived_contacts:
                action SetVariable("phone_screen", "archive_list")
            else:
                action SetVariable("phone_screen", "sms")

        imagebutton:
            idle "info_icon"
            hover "info_icon"
            xpos 295
            ypos 35
            xysize (28, 28)
            action [
                SetVariable("editing_contact_name", True),
                SetVariable("temp_contact_name", get_contact_name(current_chat))
            ]

        text "[get_contact_name(current_chat)]":
            style "phone_header"
            xalign 0.5
            ypos 48
            size 26
            color "#ffffff"

        $ yinitial_scroll = 1.0 if phone_chat_scroll_bottom else 0.0

        viewport:
            id "phone_chat_viewport"
            xpos 35
            ypos 115
            xsize 320
            ysize 455
            draggable True
            mousewheel True
            yinitial yinitial_scroll

            vbox:
                spacing 8

                $ last_date = None

                for msg in chats.get(current_chat, []):

                    if msg.get("date", current_game_date) != last_date:

                        $ last_date = msg.get("date", current_game_date)

                        frame:
                            xalign 0.5
                            background "#000000aa"
                            padding (10, 4)

                            text format_chat_date(last_date) size 12 color "#ffffff"

                    if msg["sender"] == "Player":

                        hbox:
                            xsize 320

                            frame:
                                xalign 1.0
                                xoffset -8
                                xmaximum 270
                                xminimum 110
                                yminimum 44
                                padding (16, 12, 16, 12)
                                background Solid("#2E88FF")

                                vbox:
                                    spacing 4
                                    xmaximum 248

                                    text msg["text"]:
                                        style "phone_message"
                                        xmaximum 248
                                        text_align 0.0
                                        size 13
                                        color "#ffffff"

                                    if msg.get("time", "") != "":
                                        text msg["time"]:
                                            style "phone_message_time"
                                            xalign 1.0
                                            size 8
                                            color "#dceeff"

                    else:

                        hbox:
                            xsize 320

                            frame:
                                xmaximum 280
                                xminimum 110
                                yminimum 44
                                padding (16, 12, 16, 12)
                                background Solid("#ffffff")

                                vbox:
                                    spacing 4
                                    xmaximum 248

                                    text msg["text"]:
                                        style "phone_message"
                                        xmaximum 248
                                        text_align 0.0
                                        size 13
                                        color "#111111"

                                    if msg.get("time", "") != "":
                                        text msg["time"]:
                                            style "phone_message_time"
                                            xalign 1.0
                                            size 8
                                            color "#666666"

                            null:
                                xfill True

                if player_typing_active and player_typing_contact == current_chat:

                    timer 0.04 repeat True action Function(player_type_next_char)

                    hbox:
                        xsize 320
                        yalign 0.0

                        frame:
                            xalign 1.0
                            xoffset -8
                            xmaximum 270
                            xminimum 110
                            yminimum 44
                            padding (16, 12, 16, 12)
                            background Solid("#2E88FF")

                            vbox:
                                spacing 4
                                xmaximum 248

                                text player_typing_shown:
                                    style "phone_message"
                                    xmaximum 248
                                    text_align 0.0
                                    size 13
                                    color "#ffffff"

                if typing_active and typing_contact == current_chat:

                    fixed:
                        xsize 320
                        ysize 62

                        add Frame(Solid("#ffffff"), 12, 12):
                            xpos 0
                            ypos 0
                            xysize (250, 60)

                        hbox:
                            xpos 42
                            ypos 21
                            spacing 7

                            text "●" size 14 color "#111111" at dot_wave(0.0)
                            text "●" size 14 color "#111111" at dot_wave(0.15)
                            text "●" size 14 color "#111111" at dot_wave(0.30)

        if phone_chat_scroll_bottom:
            timer 0.01 action [Scroll("phone_chat_viewport", "vertical increase", 9999, delay=0.0), SetVariable("phone_chat_scroll_bottom", False)]

        add "send_disabled":
            xpos 288
            ypos 615
            xysize (50, 50)

        if current_chat in pending_choices:

                    vbox:
                        xpos 52
                        ypos 585
                        spacing 8

                        $ choice_id = pending_choices[current_chat]

                        if choice_id in phone_choices:

                            for option in phone_choices[choice_id]:

                                textbutton option["text"]:
                                    xmaximum 285
                                    xfill True
                                    text_align 0.0
                                    text_size 16
                                    padding (10, 10)
                                    background Solid("#ffffff22")
                                    hover_background Solid("#ffffff44")
                                    action [
                                        SetVariable("player_choice_text", option["text"]),
                                        SetVariable("player_choice_target_label", option["label"]),
                                        SetVariable("player_choice_date", option.get("date", None)),
                                        SetVariable("player_choice_time", option.get("time", None)),
                                        Call("player_choice_send")
                                    ]

        if editing_contact_name:

            frame:
                xpos 58
                ypos 170
                xsize 240
                ysize 170

                background "#111111ee"
                padding (18, 18)

                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5

                    if current_chat == "jinsei":
                        add "jinsei_avatar":
                            xalign 0.5
                            xysize (70, 70)

                    text "Alterar nome":
                        xalign 0.5
                        size 20
                        color "#ffffff"

                    input:
                        value VariableInputValue("temp_contact_name")
                        length 18
                        color "#ffffff"
                        size 20
                        xalign 0.5
                        xmaximum 180

                    textbutton "Confirmar":
                        xalign 0.5
                        action [
                            SetDict(contact_display_names, current_chat, temp_contact_name),
                            SetVariable("editing_contact_name", False),
                            SetVariable("temp_contact_name", "")
                        ]

# =========================================
# LABELS DE RESPOSTA
# =========================================

label reply_jinsei_atraso1:
    call npc_type_and_send("Jinsei", "Hmmm... Sei.... quero ver então 😠", time="08:15")

    call jinsei_yuki_final
    
    return

label jinsei_yuki_final:

    call send_player_message("Jinsei", "O Professor Yuki me adora, não tem porque dele brigar comigo pô", time="08:16")

    call npc_type_and_send("Jinsei", "Adora tanto, que você dorme em TODAS as aulas deles", time="08:16")

    call send_player_message("Jinsei", "Não, mas você tem que entender que eu estudo por fora, sabe como é né!", time="08:16")
    call send_player_message("Jinsei", "Sou um gênio imcompreendido", time="08:16")

    call npc_type_and_send("Jinsei", "Incompreendido*", time="08:17")

    call send_player_message("Jinsei", "Ta, ta... Vou indo nessa tchau", time="08:17")

    call npc_type_and_send("Jinsei", "Tchau, até daqui a pouco 😊", time="08:17")

    return

label reply_jinsei_atraso2:
    call npc_type_and_send("Jinsei", "Esse emoji de joinha é de tiozão hahahaha 🤣", time="08:15")

    call jinsei_yuki_final

    return






label reply_estella_novo1:
    call npc_type_and_send("Estella", "Ai que bom! Achei que você tinha passado o número errado hahaha")

    call estella_primeiraconversa

    return

label reply_estella_novo2:
    call npc_type_and_send("Estella", "Ah que bom! Sou eu a Estella, você me passou seu número se lembra?")

    call estella_primeiraconversa

    return

label estella_primeiraconversa:
    call npc_type_and_send("Estella", "Você tinha me pedido para te mandar mensagem quando chegasse em casa.")

    if consequência_ativada["ajudar_stella_chave"] == True:
        $ renpy.restart_interaction()

        pause 0.5

        call npc_type_and_send("Estella", "Eu acabei de chegar em casa, e queria saber se você consegue me ajudar a procura-la agora?")
        $ set_pending_choice("Estella", "estella_escolha_02")
        $ renpy.restart_interaction()

        return




# =========================================
# EXEMPLOS DE USO DURANTE O JOGO
# =========================================