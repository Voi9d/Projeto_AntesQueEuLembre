init python:

    def setup_chapters():
        if not hasattr(persistent, "unlocked_chapters") or persistent.unlocked_chapters is None:
            persistent.unlocked_chapters = [1]
            renpy.save_persistent()

    def unlock_chapter(chapter_number):
        setup_chapters()

        if chapter_number not in persistent.unlocked_chapters:
            persistent.unlocked_chapters.append(chapter_number)
            renpy.save_persistent()

    def chapter_is_unlocked(chapter_number):
        setup_chapters()
        return chapter_number in persistent.unlocked_chapters


init 1 python:
    setup_chapters()

label chapter_1_start:
    jump start

label chapter_2_start:
    jump Capítulo_2

label chapter_3_start:
    jump Capítulo_3

screen chapter_select():

    tag menu

    add menu_background_image("main")

    frame:
        background "#000000cc"
        xfill True
        yfill True

    text "Seletor de Capítulos":
        xalign 0.5
        ypos 50
        size 48
        color "#ffffff"

    grid 2 3:
        xalign 0.5
        yalign 0.56
        spacing 35

        use chapter_button(1, "Capítulo 1", "images/chapters/cap1.png", "chapter_1_start")
        use chapter_button(2, "Capítulo 2", "images/chapters/cap2.png", "chapter_2_start")
        use chapter_button(3, "Capítulo 3", "images/chapters/cap3.png", "chapter_3_start")
        use chapter_button(4, "Capítulo 4", "images/chapters/cap4.png", "chapter_4_start")
        use chapter_button(5, "Capítulo 5", "images/chapters/cap5.png", "chapter_5_start")
        use chapter_button(6, "Capítulo 6", "images/chapters/cap6.png", "chapter_6_start")

    textbutton "Voltar":
        xpos 60
        ypos 60
        action Return()


screen chapter_button(number, title, image_path, label_name):

    $ card_w = 420
    $ card_h = 236

    if chapter_is_unlocked(number):

        button:
            style "chapter_card_button"
            xsize card_w
            ysize card_h

            action ShowMenu(
                "confirm",
                message="Ir para este capítulo fará você perder o progresso não salvo. Continuar?",
                yes_action=[
                    Hide("confirm"),
                    Start(label_name)
                ],
                no_action=Hide("confirm")
            )

            fixed:
                xsize card_w
                ysize card_h

                add Solid("#000000")

                add Transform(
                    image_path,
                    zoom=0.22,
                    xalign=0.5,
                    yalign=0.42
                )

    else:

        frame:
            xsize card_w
            ysize card_h
            background "#050505"

            fixed:

                text "🔒":
                    xalign 0.5
                    yalign 0.42
                    size 58
                    color "#ffffff"

                text title:
                    xalign 0.5
                    yalign 0.75
                    size 24
                    color "#777777"

style chapter_card_button is button:
    background None
    hover_background None
    selected_background None
    selected_hover_background None
    insensitive_background None
    xpadding 0
    ypadding 0

