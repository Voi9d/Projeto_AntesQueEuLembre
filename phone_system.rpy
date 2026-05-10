# =========================================
# PHONE SYSTEM - REN'PY
# Coloque em: game/phone_system.rpy
# =========================================

# -----------------------------------------
# IMAGENS
# -----------------------------------------

image phone_frame = "images/ui/phone_frame.png"

# Ícones
image app_whatsapp = "images/ui/whatsapp_icon.png"
image phone_icon_small = "images/ui/phone_small_icon.png"

# -----------------------------------------
# DADOS
# -----------------------------------------

default archived_unlocked = False

default archive_password = "1998"

default current_contacts = ["Jinsei", "Arquivado"]

default archived_contacts = [
    "Akemi",
    "Unknown",
    "Mãe"
]

# Conversas
default chats = {

    "Jinsei": [
        ("Jinsei", "Você chegou em casa?"),
        ("Player", "Sim."),
        ("Jinsei", "Tome cuidado hoje.")
    ],

    "Akemi": [
        ("Akemi", "Você prometeu esquecer isso."),
        ("Player", "Eu tentei.")
    ],

    "Unknown": [
        ("Unknown", "ELE ESTÁ OBSERVANDO."),
    ],

    "Mãe": [
        ("Mãe", "Me liga quando puder.")
    ]
}

# -----------------------------------------
# ANIMAÇÕES
# -----------------------------------------

transform phone_open:

    zoom 0.0
    alpha 0.0

    ease 0.25 zoom 1.0 alpha 1.0

transform app_hover:
    zoom 1.0

    on hover:
        ease 0.15 zoom 1.1

    on idle:
        ease 0.15 zoom 1.0

# -----------------------------------------
# ÍCONE SUPERIOR DIREITO
# -----------------------------------------

screen phone_hud():

    zorder 100

    imagebutton:

        idle "phone_small_icon.png"
        hover "phone_small_icon.png"

        xpos 1750
        ypos 30

        at app_hover

        action Show("phone_home")

# -----------------------------------------
# TELA INICIAL DO CELULAR
# -----------------------------------------

screen phone_home():

    modal True
    zorder 200

    add "phone_frame" at phone_open:
        xalign 0.5
        yalign 0.5

    fixed:

        xalign 0.5
        yalign 0.5

        xsize 600
        ysize 1100

        # Fundo da tela do celular
        frame:

            background "#101820"

            xsize 500
            ysize 950

            xpos 50
            ypos 70

        # Ícone do whatsapp
        imagebutton:

            idle "app_whatsapp"
            hover "app_whatsapp"

            xpos 100
            ypos 150

            at app_hover

            action Show("whatsapp_contacts")

        text "WhatsApp":
            color "#FFFFFF"
            size 25

            xpos 95
            ypos 260

    # Fechar celular clicando fora
    textbutton "X":

        xpos 1250
        ypos 120

        action Hide("phone_home")

# -----------------------------------------
# CONTATOS
# -----------------------------------------

screen whatsapp_contacts():

    modal True
    zorder 300

    add "phone_frame":

        xalign 0.5
        yalign 0.5

    frame:

        background "#0B141A"

        xalign 0.5
        yalign 0.5

        xsize 500
        ysize 950

        vbox:

            spacing 15
            xpos 20
            ypos 20

            text "Conversas":
                color "#FFFFFF"
                size 40

            # CONTATOS NORMAIS
            for contact in current_contacts:

                if contact != "Arquivado":

                    textbutton contact:

                        xsize 440
                        ysize 70

                        action Show("chat_screen", contato=contact)

                else:

                    textbutton "📁 Arquivado":

                        xsize 440
                        ysize 70

                        action Show("archive_password_screen")

    textbutton "←":

        xpos 730
        ypos 120

        action Hide("whatsapp_contacts")

# -----------------------------------------
# SENHA DOS ARQUIVADOS
# -----------------------------------------

screen archive_password_screen():

    modal True
    zorder 400

    default password_input = ""

    frame:

        background "#202C33"

        xalign 0.5
        yalign 0.5

        xsize 400
        ysize 300

        vbox:

            spacing 20

            xalign 0.5
            yalign 0.5

            text "Digite a senha":
                color "#FFFFFF"
                size 35

            input:

                default ""
                value ScreenVariableInputValue("password_input")

                length 20

            textbutton "Confirmar":

                action If(
                    password_input == archive_password,

                    [
                        SetVariable("archived_unlocked", True),
                        Hide("archive_password_screen"),
                        Show("archived_contacts_screen")
                    ],

                    Notify("Senha incorreta.")
                )

# -----------------------------------------
# CONTATOS ARQUIVADOS
# -----------------------------------------

screen archived_contacts_screen():

    modal True
    zorder 500

    add "phone_frame":

        xalign 0.5
        yalign 0.5

    frame:

        background "#111B21"

        xalign 0.5
        yalign 0.5

        xsize 500
        ysize 950

        vbox:

            spacing 15

            xpos 20
            ypos 20

            text "Arquivados":
                color "#FFFFFF"
                size 40

            for contact in archived_contacts:

                textbutton contact:

                    xsize 440
                    ysize 70

                    action Show("chat_screen", contato=contact)

    textbutton "←":

        xpos 730
        ypos 120

        action Hide("archived_contacts_screen")

# -----------------------------------------
# CHAT
# -----------------------------------------

screen chat_screen(contato):

    modal True
    zorder 600

    add "phone_frame":

        xalign 0.5
        yalign 0.5

    frame:

        background "#0B141A"

        xalign 0.5
        yalign 0.5

        xsize 500
        ysize 950

        vbox:

            spacing 10

            xpos 15
            ypos 15

            text "[contato]":
                color "#FFFFFF"
                size 35

            viewport:

                draggable True
                mousewheel True

                ysize 780

                vbox:

                    spacing 15

                    for sender, msg in chats[contato]:

                        if sender == "Player":

                            frame:

                                background "#005C4B"

                                xalign 1.0
                                xmaximum 350

                                padding (15,10)

                                text "[msg]":
                                    color "#FFFFFF"

                        else:

                            frame:

                                background "#202C33"

                                xalign 0.0
                                xmaximum 350

                                padding (15,10)

                                text "[msg]":
                                    color "#FFFFFF"

    textbutton "←":

        xpos 730
        ypos 120

        action Hide("chat_screen")

# -----------------------------------------
# INÍCIO
# -----------------------------------------

label start:

    show screen phone_hud

    scene black

    "O celular agora pode ser aberto pelo ícone superior direito."

    "Teste o WhatsApp."

    return