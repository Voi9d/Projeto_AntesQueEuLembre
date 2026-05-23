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
image typing_dot = "images/ui/typing_dot.png"

image jinsei_avatar = "images/ui/fotos_contatos/jinsei_contato.png"

style phone_message is default:
    font "Aquifer.ttf"

style phone_message_time is default:
    font "Aquifer.ttf"

style phone_message_preview is default:
    font "Aquifer.ttf"

style phone_header is default:
    font "Aquifer.ttf"

# =========================================
# VARIÁVEIS
# =========================================

default editing_contact_name = False

default temp_contact_name = ""

default contact_display_names = {
    "Jinsei": "Jinsei",
    "star_contact": "\u661f",
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

default archived_contacts = ["Akemi", "Unknown", "Mãe", "star_contact"]

default current_chat = None

default phone_chat_scroll_bottom = False
default phone_chat_scroll_positions = {}
default phone_chat_opened = {}
default phone_chat_force_bottom = {}

init python:

    def phone_blocks_game():
        return store.phone_open

    def phone_allows_dialogue_dismiss():
        return not phone_blocks_game()

    def run_phone_choice(text, label_name, date=None, time=None):
        store.player_choice_text = text
        store.player_choice_target_label = label_name
        store.player_choice_date = date
        store.player_choice_time = time
        renpy.call_in_new_context("phone_choice_send_context")

    config.say_allow_dismiss = phone_allows_dialogue_dismiss

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

    "Mãe": [
        {"sender": "Mãe", "text": "Me liga quando puder."},
    ],

    "star_contact": [
        {"sender": "???", "text": "Você vai faltar amanhã?", "date": "2014-09-12", "time": "20:14"},

        {"sender": "Player", "text": "Talvez.", "date": "2014-09-12", "time": "20:15"},

        {"sender": "???", "text": "Kioku.", "date": "2014-09-12", "time": "20:15"},

        {"sender": "Player", "text": "Que foi.", "date": "2014-09-12", "time": "20:16"},

        {"sender": "???", "text": "Você disse isso ontem também.", "date": "2014-09-12", "time": "20:16"},

        {"sender": "Player", "text": "Preguiça.", "date": "2014-09-12", "time": "20:17"},

        {"sender": "???", "text": "Mentira.", "date": "2014-09-12", "time": "20:17"},

        {"sender": "Player", "text": "Como você sabe?", "date": "2014-09-12", "time": "20:18"},

        {"sender": "???", "text": "Porque eu te conheço.", "date": "2014-09-12", "time": "20:18"},


        # =========================
        # ROTINA DOS DOIS
        # =========================

        {"sender": "???", "text": "Minha mãe perguntou de você hoje.", "date": "2014-10-03", "time": "18:44"},

        {"sender": "Player", "text": "Ela gosta mais de mim do que de você.", "date": "2014-10-03", "time": "18:45"},

        {"sender": "???", "text": "Isso porque você é falso.", "date": "2014-10-03", "time": "18:45"},

        {"sender": "Player", "text": "Sua mãe literalmente me chamou pra jantar amanhã.", "date": "2014-10-03", "time": "18:46"},

        {"sender": "???", "text": "Minha mãe já te adotou emocionalmente.", "date": "2014-10-03", "time": "18:46"},

        {"sender": "Player", "text": "A sua também me trata melhor que a minha.", "date": "2014-10-03", "time": "18:47"},

        {"sender": "???", "text": "MENTIROSO.", "date": "2014-10-03", "time": "18:47"},


        # =========================
        # SHOPPING
        # =========================

        {"sender": "???", "text": "Você demorou MUITO pra escolher uma camisa.", "date": "2014-11-08", "time": "21:03"},

        {"sender": "Player", "text": "Você me fez experimentar 12.", "date": "2014-11-08", "time": "21:04"},

        {"sender": "???", "text": "Porque você fica bonito de preto.", "date": "2014-11-08", "time": "21:04"},

        {"sender": "Player", "text": "...", "date": "2014-11-08", "time": "21:05"},

        # =========================
        # PRIMEIROS SINAIS
        # =========================

        {"sender": "???", "text": "Minha mãe perguntou se a gente tava namorando.", "date": "2015-01-12", "time": "22:11"},

        {"sender": "Player", "text": "E o que você respondeu?", "date": "2015-01-12", "time": "22:12"},

        {"sender": "???", "text": "Que infelizmente não.", "date": "2015-01-12", "time": "22:12"},

        {"sender": "Player", "text": "Cruel.", "date": "2015-01-12", "time": "22:13"},

        {"sender": "???", "text": "Você ficou vermelho hoje quando a atendente achou que eu era sua namorada.", "date": "2015-01-12", "time": "22:14"},

        {"sender": "Player", "text": "Porque você começou a rir.", "date": "2015-01-12", "time": "22:14"},

        # =========================
        # APROXIMAÇÃO
        # =========================

        {"sender": "???", "text": "Você vai comigo no festival sábado?", "date": "2015-02-06", "time": "19:22"},

        {"sender": "Player", "text": "Só nós dois?", "date": "2015-02-06", "time": "19:23"},

        {"sender": "???", "text": "Você quer chamar mais alguém?", "date": "2015-02-06", "time": "19:23"},

        {"sender": "Player", "text": "Não.", "date": "2015-02-06", "time": "19:24"},

        {"sender": "???", "text": "Então pronto.", "date": "2015-02-06", "time": "19:24"},

        {"sender": "Player", "text": "Isso é um encontro?", "date": "2015-02-06", "time": "19:25"},

        {"sender": "???", "text": "Talvez.", "date": "2015-02-06", "time": "19:25"},

        {"sender": "Player", "text": "Talvez?", "date": "2015-02-06", "time": "19:26"},

        {"sender": "???", "text": "Depende se você vai ser legal comigo.", "date": "2015-02-06", "time": "19:26"},


        # =========================
        # DEPOIS DO FESTIVAL
        # =========================

        {"sender": "???", "text": "Chegou em casa?", "date": "2015-02-07", "time": "22:48"},

        {"sender": "Player", "text": "Cheguei.", "date": "2015-02-07", "time": "22:49"},

        {"sender": "???", "text": "Hoje foi legal.", "date": "2015-02-07", "time": "22:49"},

        {"sender": "Player", "text": "Foi.", "date": "2015-02-07", "time": "22:50"},

        {"sender": "???", "text": "Só isso?", "date": "2015-02-07", "time": "22:50"},

        {"sender": "Player", "text": "Foi muito legal.", "date": "2015-02-07", "time": "22:51"},

        {"sender": "???", "text": "Melhorou.", "date": "2015-02-07", "time": "22:51"},

        {"sender": "Player", "text": "Você ficou bonita de yukata.", "date": "2015-02-07", "time": "22:52"},

        {"sender": "???", "text": "...", "date": "2015-02-07", "time": "22:52"},

        {"sender": "Player", "text": "O que foi?", "date": "2015-02-07", "time": "22:53"},

        {"sender": "???", "text": "Nada. Só gostei de ler isso.", "date": "2015-02-07", "time": "22:53"},

        {"sender": "Player", "text": "kkkk Idiota.", "date": "2015-02-07", "time": "22:54"},

        {"sender": "???", "text": "Chato! kkkk.", "date": "2015-02-07", "time": "22:56"},


        # =========================
        # DEPOIS DA DECLARAÇÃO
        # =========================

        {"sender": "???", "text": "Você ainda tá acordado?", "date": "2015-03-18", "time": "23:48"},

        {"sender": "Player", "text": "Sim.", "date": "2015-03-18", "time": "23:49"},

        {"sender": "???", "text": "Eu ainda não acredito que falei aquilo.", "date": "2015-03-18", "time": "23:49"},

        {"sender": "Player", "text": "Você tava vermelha.", "date": "2015-03-18", "time": "23:50"},

        {"sender": "???", "text": "Você também tava.", "date": "2015-03-18", "time": "23:50"},

        {"sender": "Player", "text": "Porque você me pegou desprevenido?!", "date": "2015-03-18", "time": "23:51"},

        {"sender": "???", "text": "Mentira.", "date": "2015-03-18", "time": "23:51"},

        {"sender": "Player", "text": "Como mentira?", "date": "2015-03-18", "time": "23:52"},

        {"sender": "???", "text": "Você já sabia.", "date": "2015-03-18", "time": "23:52"},

        {"sender": "Player", "text": "Talvez...", "date": "2015-03-18", "time": "23:53"},

        {"sender": "???", "text": "Kioku...", "date": "2015-03-18", "time": "23:53"},

        {"sender": "Player", "text": "Tá, eu sabia um pouco.", "date": "2015-03-18", "time": "23:54"},

        {"sender": "???", "text": "IDIOTA.", "date": "2015-03-18", "time": "23:54"},

        {"sender": "Player", "text": "Mas eu achei que você nunca ia falar.", "date": "2015-03-18", "time": "23:55"},

        {"sender": "???", "text": "Eu quase não falei.", "date": "2015-03-18", "time": "23:55"},

        {"sender": "Player", "text": "Você começou a chorar no meio da frase.", "date": "2015-03-18", "time": "23:56"},

        {"sender": "???", "text": "PARA.", "date": "2015-03-18", "time": "23:56"},

        {"sender": "Player", "text": "Foi fofo.", "date": "2015-03-18", "time": "23:57"},

        {"sender": "???", "text": "Você também ficou nervoso.", "date": "2015-03-18", "time": "23:57"},

        {"sender": "Player", "text": "Porque eu gosto de você faz tempo...", "date": "2015-03-18", "time": "23:58"},

        {"sender": "???", "text": "...", "date": "2015-03-18", "time": "23:58"},

        {"sender": "???", "text": "Você não pode simplesmente mandar isso...", "date": "2015-03-18", "time": "23:59"},

        {"sender": "Player", "text": "Mas é verdade.", "date": "2015-03-19", "time": "00:00"},

        {"sender": "???", "text": "Minha barriga tá formigando.", "date": "2015-03-19", "time": "00:01"},

        {"sender": "Player", "text": "Isso foi estranhamente específico.", "date": "2015-03-19", "time": "00:01"},

        {"sender": "???", "text": "É culpa sua .", "date": "2015-03-19", "time": "00:02"},

        {"sender": "Player", "text": "Então oficialmente você é minha namorada agora?", "date": "2015-03-19", "time": "00:03"},

        {"sender": "???", "text": "Você quer mesmo perguntar isso por mensagem depois de tudo?", "date": "2015-03-19", "time": "00:03"},

        {"sender": "Player", "text": "Sim.", "date": "2015-03-19", "time": "00:04"},

        {"sender": "???", "text": "Então sim.", "date": "2015-03-19", "time": "00:04"},

        {"sender": "Player", "text": "Legal.", "date": "2015-03-19", "time": "00:05"},

        {"sender": "???", "text": "Você é MUITO ruim em reagir emocionalmente.", "date": "2015-03-19", "time": "00:05"},

        {"sender": "Player", "text": "Eu tô feliz.", "date": "2015-03-19", "time": "00:06"},

        {"sender": "???", "text": "Eu também.", "date": "2015-03-19", "time": "00:06"},


        # =========================
        # AS MÃES DESCOBREM
        # =========================

        {"sender": "???", "text": "Minha mãe descobriu!!!!", "date": "2015-03-20", "time": "18:42"},

        {"sender": "Player", "text": "Achei que ela só suspeitava.", "date": "2015-03-20", "time": "18:43"},

        {"sender": "???", "text": "Não, ela literalmente entrou no meu quarto sorrindo.", "date": "2015-03-20", "time": "18:43"},

        {"sender": "Player", "text": "Isso parece assustador.", "date": "2015-03-20", "time": "18:44"},

        {"sender": "???", "text": "PIOROU.", "date": "2015-03-20", "time": "18:44"},

        {"sender": "???", "text": "Ela perguntou se podia finalmente te chamar de genro.", "date": "2015-03-20", "time": "18:45"},

        {"sender": "Player", "text": "...", "date": "2015-03-20", "time": "18:45"},

        {"sender": "???", "text": "Ela também perguntou se eu queria que ela comprasse um bolo.", "date": "2015-03-20", "time": "18:46"},

        {"sender": "Player", "text": "UM BOLO? Porque um bolo?", "date": "2015-03-20", "time": "18:46"},

        {"sender": "???", "text": "Eu também não sei kkkkkk.", "date": "2015-03-20", "time": "18:47"},

        # =========================
        # MÃE DO KIOKU DESCOBRE
        # =========================

        {"sender": "Player", "text": "Minha mãe acabou de me olhar estranho.", "date": "2015-03-20", "time": "20:02"},

        {"sender": "???", "text": "Por quê?", "date": "2015-03-20", "time": "20:02"},

        {"sender": "Player", "text": "Porque sua mãe ligou pra ela.", "date": "2015-03-20", "time": "20:03"},

        {"sender": "???", "text": "ELA FEZ O QUÊ?", "date": "2015-03-20", "time": "20:03"},

        {"sender": "Player", "text": "Minha mãe tá sorrindo desde então.", "date": "2015-03-20", "time": "20:04"},

        {"sender": "???", "text": "Minha mãe é uma TRAIDORA.", "date": "2015-03-20", "time": "20:04"},

        {"sender": "Player", "text": "A minha perguntou se você vai jantar aqui algum dia.", "date": "2015-03-20", "time": "20:15"},

        {"sender": "???", "text": "Minha mãe perguntou a mesma coisa sobre você.", "date": "2015-03-20", "time": "20:15"},

        {"sender": "Player", "text": "Acho que perdemos o controle da situação.", "date": "2015-03-20", "time": "20:16"},

        {"sender": "???", "text": "Nossas mães estão vivendo um dorama.", "date": "2015-03-20", "time": "20:16"},

        # =========================
        # CONVITE PARA JANTAR
        # =========================

        {"sender": "???", "text": "Minha mãe convidou você e sua mãe pra jantar sábado.", "date": "2015-03-22", "time": "16:11"},

        {"sender": "Player", "text": "Por que eu tô nervoso?", "date": "2015-03-22", "time": "16:12"},

        {"sender": "???", "text": "Porque meu pai vai estar lá.", "date": "2015-03-22", "time": "16:12"},

        {"sender": "Player", "text": "...", "date": "2015-03-22", "time": "16:13"},

        {"sender": "???", "text": "HAHAHAHA.", "date": "2015-03-22", "time": "16:13"},

        {"sender": "Player", "text": "Seu pai me assusta.", "date": "2015-03-22", "time": "16:14"},

        {"sender": "???", "text": "Ele gosta de você.", "date": "2015-03-22", "time": "16:14"},

        {"sender": "Player", "text": "Esse é o problema.", "date": "2015-03-22", "time": "16:15"},


        # =========================
        # AFTER DO JANTAR
        # =========================

        {"sender": "???", "text": "Você tá vivo?", "date": "2015-03-28", "time": "22:48"},

        {"sender": "Player", "text": "Fisicamente.", "date": "2015-03-28", "time": "22:49"},

        {"sender": "???", "text": "Você tava MUITO nervoso.", "date": "2015-03-28", "time": "22:49"},

        {"sender": "Player", "text": "Seu pai ficou me encarando por 20 minutos.", "date": "2015-03-28", "time": "22:50"},

        {"sender": "???", "text": "Ele faz isso com todo mundo.", "date": "2015-03-28", "time": "22:50"},

        {"sender": "Player", "text": "Ele apertou minha mão forte demais.", "date": "2015-03-28", "time": "22:51"},

        {"sender": "???", "text": "Ele tava tentando parecer intimidador.", "date": "2015-03-28", "time": "22:51"},

        {"sender": "Player", "text": "Funcionou... pra karalho", "date": "2015-03-28", "time": "22:52"},

        {"sender": "???", "text": "Minha mãe ficou MUITO feliz vendo você lá.", "date": "2015-03-28", "time": "22:53"},

        {"sender": "Player", "text": "Ela me chamou de \"namorado oficial\" na frente de todo mundo.", "date": "2015-03-28", "time": "22:54"},

        {"sender": "???", "text": "Você ficou vermelho.", "date": "2015-03-28", "time": "22:54"},

        {"sender": "Player", "text": "Sua mãe tava claramente se divertindo.", "date": "2015-03-28", "time": "22:55"},

        {"sender": "???", "text": "A sua também.", "date": "2015-03-28", "time": "22:55"},

        {"sender": "Player", "text": "Minha mãe nunca sorriu tanto.", "date": "2015-03-28", "time": "22:56"},


        # =========================
        # PRIMEIROS MESES
        # =========================

        {"sender": "???", "text": "A gente praticamente passa todo dia junto agora.", "date": "2015-04-11", "time": "21:04"},

        {"sender": "Player", "text": "Você reclama?", "date": "2015-04-11", "time": "21:05"},

        {"sender": "???", "text": "Não.", "date": "2015-04-11", "time": "21:05"},

        {"sender": "???", "text": "Só acho estranho como isso virou normal rápido.", "date": "2015-04-11", "time": "21:06"},

        {"sender": "Player", "text": "Acho que porque já parecia normal antes.", "date": "2015-04-11", "time": "21:06"},

        {"sender": "???", "text": "...", "date": "2015-04-11", "time": "21:07"},

        {"sender": "Player", "text": "O quê?", "date": "2015-04-11", "time": "21:07"},

        {"sender": "???", "text": "Nada... Só gostei disso.", "date": "2015-04-11", "time": "21:08"},


        # =========================
        # AMADURECIMENTO
        # =========================

        {"sender": "Player", "text": "Obrigado por ficar comigo hoje.", "date": "2015-05-03", "time": "00:48"},

        {"sender": "???", "text": "Você não precisa agradecer.", "date": "2015-05-03", "time": "00:49"},

        {"sender": "Player", "text": "Mesmo assim.", "date": "2015-05-03", "time": "00:49"},

        {"sender": "???", "text": "Kioku...", "date": "2015-05-03", "time": "00:50"},

        {"sender": "???", "text": "Você não precisa passar pelas coisas sozinho só porque acha que deve.", "date": "2015-05-03", "time": "00:51"},

        {"sender": "Player", "text": "Eu sei.", "date": "2015-05-03", "time": "00:52"},

        {"sender": "???", "text": "Então deixa eu ficar do seu lado.", "date": "2015-05-03", "time": "00:52"},

        {"sender": "Player", "text": "Tá bom.", "date": "2015-05-03", "time": "00:53"},

        # =========================
        # RELAÇÃO MAIS MADURA
        # =========================

        {"sender": "???", "text": "Você percebeu que a gente quase não briga?", "date": "2015-08-14", "time": "22:18"},

        {"sender": "Player", "text": "Isso é ruim?", "date": "2015-08-14", "time": "22:19"},

        {"sender": "???", "text": "Não.", "date": "2015-08-14", "time": "22:19"},

        {"sender": "???", "text": "Só achei que namoro fosse mais complicado.", "date": "2015-08-14", "time": "22:20"},

        {"sender": "Player", "text": "Talvez porque a gente já agia como casal antes.", "date": "2015-08-14", "time": "22:21"},

        {"sender": "???", "text": "Minha mãe disse exatamente isso ontem.", "date": "2015-08-14", "time": "22:21"},

        # =========================
        # ANTES DO ANIVERSÁRIO DA ESTELLA
        # =========================

        {"sender": "???", "text": "Não compra nada caro pra mim.", "date": "2015-09-03", "time": "19:42"},

        {"sender": "Player", "text": "Você acha que eu tenho dinheiro?", "date": "2015-09-03", "time": "19:43"},

        {"sender": "???", "text": "Você gastaria tudo mesmo assim!", "date": "2015-09-03", "time": "19:43"},

        {"sender": "Player", "text": "Talvez...", "date": "2015-09-03", "time": "19:44"},

        {"sender": "???", "text": "Kioku...", "date": "2015-09-03", "time": "19:44"},

        {"sender": "Player", "text": "O quê?", "date": "2015-09-03", "time": "19:45"},

        {"sender": "???", "text": "Só aparece sábado. Isso já é suficiente.", "date": "2015-09-03", "time": "19:45"},


        # =========================
        # PÓS ANIVERSÁRIO DA ESTELLA
        # =========================

        {"sender": "Player", "text": "Você chorou por causa de uma carta!?", "date": "2015-09-05", "time": "23:08"},

        {"sender": "???", "text": "Porque você escreveu coisa lindas.", "date": "2015-09-05", "time": "23:09"},

        {"sender": "Player", "text": "Você literalmente tava tremendo.", "date": "2015-09-05", "time": "23:09"},

        {"sender": "???", "text": "E você tava vermelho quando minha mãe começou a tirar foto.", "date": "2015-09-05", "time": "23:10"},

        {"sender": "Player", "text": "Ela tirou 37 fotos.", "date": "2015-09-05", "time": "23:10"},

        {"sender": "???", "text": "Ela te ama mais do que me ama...", "date": "2015-09-05", "time": "23:11"},

        {"sender": "Player", "text": "Seu pai ainda me assusta.", "date": "2015-09-05", "time": "23:11"},

        {"sender": "???", "text": "Mas ele gostou do presente que você me deu.", "date": "2015-09-05", "time": "23:12"},

        {"sender": "Player", "text": "Como você sabe?", "date": "2015-09-05", "time": "23:12"},

        {"sender": "???", "text": "Porque ele falou \"pelo menos o garoto presta atenção em você\".", "date": "2015-09-05", "time": "23:13"},

        {"sender": "Player", "text": "... isso foi quase fofo da parte do seu pai.", "date": "2015-09-05", "time": "23:13"},


        # =========================
        # ANTES DO ANIVERSÁRIO DO KIOKU
        # =========================

        {"sender": "???", "text": "Sua mãe me mandou mensagem escondida.", "date": "2015-11-18", "time": "18:02"},

        {"sender": "Player", "text": "Isso nunca é bom.", "date": "2015-11-18", "time": "18:03"},

        {"sender": "???", "text": "Ela perguntou qual bolo você gosta.", "date": "2015-11-18", "time": "18:03"},

        {"sender": "Player", "text": "Minha mãe tá organizando coisa demais de novo?", "date": "2015-11-18", "time": "18:04"},

        {"sender": "???", "text": "As nossas mães estão organizando juntas.", "date": "2015-11-18", "time": "18:04"},

        {"sender": "Player", "text": "... estamos ferrados.", "date": "2015-11-18", "time": "18:05"},


        # =========================
        # PÓS ANIVERSÁRIO DO KIOKU
        # =========================

        {"sender": "???", "text": "Sua mãe chorou vendo você apagar as velas...", "date": "2015-11-21", "time": "22:28"},

        {"sender": "Player", "text": "Eu percebi.", "date": "2015-11-21", "time": "22:29"},

        {"sender": "???", "text": "Ela ficou olhando pra você o jantar inteiro.", "date": "2015-11-21", "time": "22:29"},

        {"sender": "Player", "text": "Acho que ela tava feliz.", "date": "2015-11-21", "time": "22:30"},

        {"sender": "???", "text": "Ela parecia orgulhosa.", "date": "2015-11-21", "time": "22:31"},

        {"sender": "Player", "text": "...", "date": "2015-11-21", "time": "22:31"},

        {"sender": "???", "text": "O que foi?", "date": "2015-11-21", "time": "22:32"},

        {"sender": "Player", "text": "Só fiquei feliz ouvindo isso.", "date": "2015-11-21", "time": "22:33"},


        # =========================
        # 1 ANO DE NAMORO
        # =========================

        {"sender": "???", "text": "Você percebeu que daqui a pouco vai fazer 1 ano?", "date": "2016-02-26", "time": "20:14"},

        {"sender": "Player", "text": "Não parece tudo isso...", "date": "2016-02-26", "time": "20:15"},

        {"sender": "???", "text": "Porque a gente se conhece desde sempre.", "date": "2016-02-26", "time": "20:15"},

        {"sender": "Player", "text": "É verdade.", "date": "2016-02-26", "time": "20:16"},

        {"sender": "???", "text": "O que você quer fazer no nosso aniversário?", "date": "2016-02-26", "time": "20:17"},

        {"sender": "Player", "text": "Você falando isso faz a gente parecer velhos casados.", "date": "2016-02-26", "time": "20:18"},

        {"sender": "???", "text": "Responde!!", "date": "2016-02-26", "time": "20:18"},

        {"sender": "Player", "text": "Quero passar o dia contigo, isso ja é o suficiente.", "date": "2016-02-26", "time": "20:19"},

        {"sender": "???", "text": "...", "date": "2016-02-26", "time": "20:19"},

        {"sender": "Player", "text": "O que foi?", "date": "2016-02-26", "time": "20:20"},

        {"sender": "???", "text": "Você fica fofo sem perceber.", "date": "2016-02-26", "time": "20:20"},

        {"sender": "Player", "text": "Idiota...", "date": "2016-02-26", "time": "20:21"},

        {"sender": "???", "text": "kkkkkkk ❤️.", "date": "2016-02-26", "time": "20:21"},

        # =========================
        # AS MÃES PLANEJANDO DEMAIS
        # =========================

        {"sender": "???", "text": "Nossas mães estão planejando coisas escondidas.", "date": "2016-03-02", "time": "18:41"},

        {"sender": "Player", "text": "Minha mãe literalmente perguntou qual foto nossa eu gostava mais.", "date": "2016-03-02", "time": "18:42"},

        {"sender": "???", "text": "MINHA MÃE MANDOU IMPRIMIR UMA.", "date": "2016-03-02", "time": "18:42"},

        {"sender": "Player", "text": "Elas estão vivendo nosso namoro mais que a gente.", "date": "2016-03-02", "time": "18:43"},

        {"sender": "???", "text": "Minha mãe falou \"vocês cresceram juntos\".", "date": "2016-03-02", "time": "18:43"},

        {"sender": "Player", "text": "Ela falou isso olhando pra mim também.", "date": "2016-03-02", "time": "18:44"},

        {"sender": "???", "text": "Às vezes eu acho que elas planejaram isso desde crianças.", "date": "2016-03-02", "time": "18:45"},

        {"sender": "Player", "text": "Provavelmente planejaram mesmo 😱.", "date": "2016-03-02", "time": "18:45"},

        # =========================
        # PÓS 1 ANO DE NAMORO
        # =========================

        {"sender": "???", "text": "Você ainda tá vivo depois de hoje?", "date": "2016-03-18", "time": "23:42"},

        {"sender": "Player", "text": "Mentalmente não...", "date": "2016-03-18", "time": "23:43"},

        {"sender": "???", "text": "Minha mãe chorou TRÊS vezes...", "date": "2016-03-18", "time": "23:43"},

        {"sender": "Player", "text": "A sua e a minha!", "date": "2016-03-18", "time": "23:44"},

        {"sender": "???", "text": "As duas ficam insuportáveis juntas.", "date": "2016-03-18", "time": "23:44"},

        {"sender": "Player", "text": "Elas literalmente fizeram um álbum nosso.", "date": "2016-03-18", "time": "23:45"},

        {"sender": "???", "text": "TINHA FOTO NOSSA DE CRIANÇA.", "date": "2016-03-18", "time": "23:45"},

        {"sender": "Player", "text": "Sua mãe mostrou aquela foto que você caiu no parque.", "date": "2016-03-18", "time": "23:46"},

        {"sender": "???", "text": "EU TINHA 8 ANOS.", "date": "2016-03-18", "time": "23:46"},

        {"sender": "Player", "text": "Você continua dramática igual.", "date": "2016-03-18", "time": "23:47"},

        {"sender": "???", "text": "Kioku...", "date": "2016-03-18", "time": "23:47"},

        {"sender": "Player", "text": "O quê?", "date": "2016-03-18", "time": "23:48"},

        {"sender": "???", "text": "... você falou \"eu te amo\".", "date": "2016-03-18", "time": "23:48"},

        {"sender": "Player", "text": "...", "date": "2016-03-18", "time": "23:49"},

        {"sender": "???", "text": "Na frente dos nossos pais...", "date": "2016-03-18", "time": "23:49"},

        {"sender": "Player", "text": "Foi sem pensar...", "date": "2016-03-18", "time": "23:50"},

        {"sender": "???", "text": "Você nunca tinha falado antes...", "date": "2016-03-18", "time": "23:50"},

        {"sender": "Player", "text": "Eu sei...", "date": "2016-03-18", "time": "23:51"},

        {"sender": "???", "text": "Minha cabeça travou na hora", "date": "2016-03-18", "time": "23:51"},

        {"sender": "Player", "text": "Você ficou olhando pra mim sem reação.", "date": "2016-03-18", "time": "23:52"},

        {"sender": "???", "text": "Porque meu coração tava quase saindo pela boca...", "date": "2016-03-18", "time": "23:52"},

        {"sender": "Player", "text": "Seu pai quase me matou com o olhar.", "date": "2016-03-18", "time": "23:53"},

        {"sender": "???", "text": "EU VI kkkkkkk", "date": "2016-03-18", "time": "23:53"},

        {"sender": "Player", "text": "Eu achei que ele ia levantar da mesa e seila me trucidar ali mesmo.", "date": "2016-03-18", "time": "23:54"},

        {"sender": "???", "text": "kkkkkkkk, mas depois ele sorriu, olha pelo lado bom", "date": "2016-03-18", "time": "23:54"},

        {"sender": "Player", "text": "Isso foi mais assustador!!!", "date": "2016-03-18", "time": "23:55"},

        {"sender": "???", "text": "Idiota.", "date": "2016-03-18", "time": "23:55"},

        {"sender": "???", "text": "Depois que vocês foram embora ele veio falar comigo.", "date": "2016-03-18", "time": "23:57"},

        {"sender": "Player", "text": "... e?", "date": "2016-03-18", "time": "23:57"},

        {"sender": "???", "text": "Ele perguntou se você me fazia feliz.", "date": "2016-03-18", "time": "23:58"},

        {"sender": "Player", "text": "...", "date": "2016-03-18", "time": "23:58"},

        {"sender": "???", "text": "E eu disse que sim.", "date": "2016-03-18", "time": "23:59"},

        {"sender": "???", "text": "Aí ele ficou quieto um tempo.", "date": "2016-03-19", "time": "00:00"},

        {"sender": "Player", "text": "Isso parece uma ameaça...😨😨😨", "date": "2016-03-19", "time": "00:00"},

        {"sender": "???", "text": "Não!", "date": "2016-03-19", "time": "00:01"},

        {"sender": "???", "text": "Ele falou que você olha pra mim do mesmo jeito que ele olha pra minha mãe.", "date": "2016-03-19", "time": "00:02"},

        {"sender": "Player", "text": "...", "date": "2016-03-19", "time": "00:02"},

        {"sender": "???", "text": "E depois disse pra eu cuidar bem de você também.", "date": "2016-03-19", "time": "00:03"},

        {"sender": "Player", "text": "Seu pai falou isso mesmo?", "date": "2016-03-19", "time": "00:04"},

        {"sender": "???", "text": "Sim.", "date": "2016-03-19", "time": "00:04"},

        {"sender": "Player", "text": "Duvido!", "date": "2016-03-19", "time": "00:05"},

        {"sender": "???", "text": "Para quieto idiota kkkkkk.", "date": "2016-03-19", "time": "00:05"},

        {"sender": "Player", "text": "Aliás.", "date": "2016-03-19", "time": "00:06"},

        {"sender": "???", "text": "Hm?", "date": "2016-03-19", "time": "00:06"},

        {"sender": "Player", "text": "Eu realmente te amo.", "date": "2016-03-19", "time": "00:07"},

        {"sender": "???", "text": "... para.", "date": "2016-03-19", "time": "00:07"},

        {"sender": "Player", "text": "Nunca.", "date": "2016-03-19", "time": "00:08"},

        {"sender": "???", "text": "Minha barriga tá formigando de novo.", "date": "2016-03-19", "time": "00:08"},

        # =========================
        # ÚLTIMOS MESES JUNTOS
        # =========================

        {"sender": "???", "text": "Você percebeu que a gente praticamente mora na casa um do outro agora?", "date": "2016-01-08", "time": "21:42"},

        {"sender": "Player", "text": "Claro... Sua mãe me alimenta e me da moradia kkkkk", "date": "2016-01-08", "time": "21:43"},

        {"sender": "???", "text": "Ai para idiota kkkkkk, ela faz isso porquê ama você", "date": "2016-01-08", "time": "21:43"},

        {"sender": "Player", "text": "A minha ama você também.", "date": "2016-01-08", "time": "21:44"},

        {"sender": "???", "text": "Ela ficou muito feliz hoje.", "date": "2016-01-08", "time": "21:44"},

        {"sender": "Player", "text": "Por quê?", "date": "2016-01-08", "time": "21:45"},

        {"sender": "???", "text": "Porque você tava sorrindo mais.", "date": "2016-01-08", "time": "21:45"},

        # =========================
        # MOMENTOS MAIS ÍNTIMOS
        # =========================

        {"sender": "Player", "text": "Obrigado por ficar comigo ontem.", "date": "2016-02-02", "time": "00:13"},

        {"sender": "???", "text": "Você não precisa agradecer por isso.", "date": "2016-02-02", "time": "00:14"},

        {"sender": "Player", "text": "Mesmo assim.", "date": "2016-02-02", "time": "00:14"},

        {"sender": "???", "text": "Kioku...", "date": "2016-02-02", "time": "00:15"},

        {"sender": "???", "text": "Eu vou continuar do seu lado mesmo nos dias ruins, tá?", "date": "2016-02-02", "time": "00:16"},

        {"sender": "Player", "text": "Tá bom.", "date": "2016-02-02", "time": "00:16"},

        # =========================
        # MORTE DA MÃE DO KIOKU
        # =========================

        {"sender": "Estella", "text": "Kioku?", "date": "2016-04-18", "time": "02:11"},

        {"sender": "Estella", "text": "A mãe me ligou antes...", "date": "2016-04-18", "time": "02:12"},

        {"sender": "Estella", "text": "O que aconteceu?", "date": "2016-04-18", "time": "02:12"},

        {"sender": "Player", "text": "...", "date": "2016-04-18", "time": "02:16"},

        {"sender": "Player", "text": "Minha mãe morreu.", "date": "2016-04-18", "time": "02:17"},

        {"sender": "Estella", "text": "...", "date": "2016-04-18", "time": "02:17"},

        {"sender": "Estella", "text": "Eu tô indo pra aí.", "date": "2016-04-18", "time": "02:18"},

        {"sender": "Player", "text": "Não precisa.", "date": "2016-04-18", "time": "02:18"},

        {"sender": "Estella", "text": "Precisa sim.", "date": "2016-04-18", "time": "02:19"},

        {"sender": "Estella", "text": "Eu quero ficar com você, e não existe não como resposta, to saindo, 15 minutos eu chego ai!!!", "date": "2016-04-18", "time": "02:19"},

        # =========================
        # PRIMEIROS DIAS
        # =========================

        {"sender": "Estella", "text": "Você comeu alguma coisa hoje?", "date": "2016-04-21", "time": "13:04"},

        {"sender": "Player", "text": "Não tô com fome...", "date": "2016-04-21", "time": "13:05"},

        {"sender": "Estella", "text": "Kioku...", "date": "2016-04-21", "time": "13:05"},

        {"sender": "Player", "text": "Desculpa.", "date": "2016-04-21", "time": "13:06"},

        {"sender": "Estella", "text": "Você não precisa pedir desculpa por estar mal.", "date": "2016-04-21", "time": "13:06"},

        {"sender": "Estella", "text": "Eu vou dormir aí hoje também.", "date": "2016-04-21", "time": "21:44"},

        {"sender": "Player", "text": "Você tá dormindo aqui faz 3 dias...", "date": "2016-04-21", "time": "21:45"},

        {"sender": "Estella", "text": "E vou continuar.", "date": "2016-04-21", "time": "21:45"},

        {"sender": "Player", "text": "Sua mãe não liga?", "date": "2016-04-21", "time": "21:46"},

        {"sender": "Estella", "text": "Ela que tá mandando eu ficar e mesmo se não mandasse eu ainda iria ai!", "date": "2016-04-21", "time": "21:46"},

        # =========================
        # COLAPSO EMOCIONAL
        # =========================

        {"sender": "Player", "text": "Eu continuo esperando ouvir ela pela casa....", "date": "2016-04-22", "time": "01:13"},

        {"sender": "Estella", "text": "...", "date": "2016-04-22", "time": "01:14"},

        {"sender": "Player", "text": "Toda vez que a porta faz barulho eu acho que ela voltou.", "date": "2016-04-22", "time": "01:15"},

        {"sender": "Player", "text": "Mas aí eu lembro.", "date": "2016-04-22", "time": "01:15"},

        {"sender": "Estella", "text": "Kioku...", "date": "2016-04-22", "time": "01:16"},

        {"sender": "Estella", "text": "Me escuta.", "date": "2016-04-22", "time": "01:17"},

        {"sender": "Estella", "text": "Você não tá sozinho.", "date": "2016-04-22", "time": "01:17"},

        {"sender": "Player", "text": "Eu tô tentando continuar normal.", "date": "2016-04-22", "time": "01:20"},

        {"sender": "Player", "text": "Mas parece que tem alguma coisa quebrada dentro de mim agora.", "date": "2016-04-22", "time": "01:21"},

        {"sender": "Estella", "text": "Então eu vou ficar ai até você conseguir respirar sem sentir isso.", "date": "2016-04-22", "time": "01:22"},

        # =========================
        # NOITE MAIS ÍNTIMA
        # =========================

        {"sender": "Estella", "text": "Cheguei em casa.", "date": "2016-04-26", "time": "02:14"},

        {"sender": "Player", "text": "Sua mãe brigou?", "date": "2016-04-26", "time": "02:15"},

        {"sender": "Estella", "text": "Ela perguntou se eu tava bem.", "date": "2016-04-26", "time": "02:15"},

        {"sender": "Player", "text": "E você?", "date": "2016-04-26", "time": "02:16"},

        {"sender": "Estella", "text": "...", "date": "2016-04-26", "time": "02:17"},

        {"sender": "Estella", "text": "Eu acho que nunca me senti tão próxima de alguém antes.", "date": "2016-04-26", "time": "02:18"},

        {"sender": "Player", "text": "Desculpa se eu tava estranho.", "date": "2016-04-26", "time": "02:20"},

        {"sender": "Estella", "text": "Kioku.", "date": "2016-04-26", "time": "02:20"},

        {"sender": "Estella", "text": "Você não precisa pedir desculpa por nada hoje.", "date": "2016-04-26", "time": "02:21"},

        {"sender": "Player", "text": "Eu só...", "date": "2016-04-26", "time": "02:23"},

        {"sender": "Player", "text": "Eu tava com medo de quebrar de vez.", "date": "2016-04-26", "time": "02:24"},

        {"sender": "Estella", "text": "Então deixa eu continuar segurando os pedaços com você.", "date": "2016-04-26", "time": "02:25"},

        {"sender": "Player", "text": "...", "date": "2016-04-26", "time": "02:26"},

        {"sender": "Estella", "text": "Eu te amo.", "date": "2016-04-26", "time": "02:27"},

        {"sender": "Player", "text": "...", "date": "2016-04-26", "time": "02:28"},

        {"sender": "Player", "text": "Você nunca falou isso primeiro antes.", "date": "2016-04-26", "time": "02:28"},

        {"sender": "Estella", "text": "Não importa, é verdade.", "date": "2016-04-26", "time": "02:29"},

        {"sender": "Estella", "text": "Minha barriga tá formigando de novo.", "date": "2016-04-26", "time": "02:29"},

        {"sender": "Player", "text": "Isso definitivamente não parece saudável.", "date": "2016-04-26", "time": "02:30"},

        {"sender": "Estella", "text": "Cala a boca idiota kkkk.", "date": "2016-04-26", "time": "02:30"},

        {"sender": "Player", "text": "Eu também te amo, Estella.", "date": "2016-04-26", "time": "02:31"},


        # =========================
        # DIA SEGUINTE
        # =========================

        {"sender": "Player", "text": "Você tá acordada?", "date": "2016-04-26", "time": "10:14"},

        {"sender": "Estella", "text": "Agora tô.", "date": "2016-04-26", "time": "10:15"},

        {"sender": "Player", "text": "Eu tava pensando...", "date": "2016-04-26", "time": "10:16"},

        {"sender": "Estella", "text": "Hm?", "date": "2016-04-26", "time": "10:16"},

        {"sender": "Player", "text": "Ontem foi a primeira vez em dias que eu não senti vontade de desaparecer.", "date": "2016-04-26", "time": "10:17"},

        {"sender": "Estella", "text": "...", "date": "2016-04-26", "time": "10:18"},

        {"sender": "Estella", "text": "Então continua aqui comigo.", "date": "2016-04-26", "time": "10:18"},

        {"sender": "Player", "text": "Eu amo você.", "date": "2016-04-26", "time": "10:19"},

        {"sender": "Estella", "text": "Eu também amo você, Kioku.", "date": "2016-04-26", "time": "10:20"},


        # =========================
        # REVELAÇÃO DO NOME
        # =========================

        {"sender": "Estella", "text": "Minha tia do Brasil perguntou de você de novo.", "date": "2016-04-27", "time": "18:02"},

        {"sender": "Player", "text": "Ela ainda lembra de mim?", "date": "2016-04-27", "time": "18:03"},

        {"sender": "Estella", "text": "Kioku, você ficou duas horas tentando aprender português só pra conversar com ela.", "date": "2016-04-27", "time": "18:03"},
        
        {"sender": "Player", "text": "Eu lembro de 'obrigado'.", "date": "2016-04-27", "time": "18:04"},

        {"sender": "Estella", "text": "Seu sotaque era horrível.", "date": "2016-04-27", "time": "18:04"},

        {"sender": "Player", "text": "Você riu de mim por dias.", "date": "2016-04-27", "time": "18:05"},
        
        {"sender": "Estella", "text": "Porque foi fofo.", "date": "2016-04-27", "time": "18:05"},

        # =========================
        # VIAGEM PRO BRASIL
        # =========================

        {"sender": "Estella", "text": "Meu voo é semana que vem...", "date": "2016-04-29", "time": "22:14"},

        {"sender": "Player", "text": "Ainda acho injusto você fugir pro Brasil sem mim.", "date": "2016-04-29", "time": "22:15"},

        {"sender": "Estella", "text": "Você ia reclamar do calor em menos de 10 minutos.", "date": "2016-04-29", "time": "22:15"},

        {"sender": "Player", "text": "Mentira!!!!!", "date": "2016-04-29", "time": "22:16"},

        {"sender": "Estella", "text": "Você literalmente reclama do calor no inverno...", "date": "2016-04-29", "time": "22:16"},

        {"sender": "Player", "text": "Isso...... tá, é verdade tem razão.", "date": "2016-04-29", "time": "22:17"},


        # =========================
        # ANTES DO ACAMPAMENTO
        # =========================

        {"sender": "Player", "text": "Oiiii, amanhã vou ir num acampamento com o grupo aqui pra aproveitar as férias.", "date": "2016-05-03", "time": "21:07"},

        {"sender": "Player", "text": "Mas eu volto antes de você voltar pra casa.", "date": "2016-05-03", "time": "21:08"},

        {"sender": "Player", "text": "Tô com saudades já.", "date": "2016-05-03", "time": "21:08"},

        {"sender": "Estella", "text": "Você literalmente vai ficar 4 dias longe de mim dramático.", "date": "2016-05-03", "time": "21:09"},

        {"sender": "Player", "text": "É muito tempo.", "date": "2016-05-03", "time": "21:10"},

        {"sender": "Estella", "text": "Então volta vivo do acampamento.", "date": "2016-05-03", "time": "21:10"},

        {"sender": "Player", "text": "Vou voltar só pra te irritar de novo.", "date": "2016-05-03", "time": "21:11"},

        {"sender": "Estella", "text": "Promete?", "date": "2016-05-03", "time": "21:11"},

        {"sender": "Player", "text": "Prometo.", "date": "2016-05-03", "time": "21:12"},


        # =========================
        # APÓS O ACIDENTE
        # =========================

        {"sender": "Estella", "text": "Oi?", "date": "2016-05-08", "time": "18:42"},

        {"sender": "Estella", "text": "Você sumiu de repente.", "date": "2016-05-08", "time": "18:44"},

        {"sender": "Estella", "text": "Jinsei me contou que aconteceu alguma coisa...", "date": "2016-05-08", "time": "18:45"},

        {"sender": "Estella", "text": "Você tá bem?", "date": "2016-05-08", "time": "18:46"},

        {"sender": "Estella", "text": "Kioku?", "date": "2016-05-09", "time": "22:03"},

        {"sender": "Estella", "text": "Talvez você só precise de um tempo...", "date": "2016-05-11", "time": "00:14"},

        {"sender": "Estella", "text": "Eu voltei do Brasil hoje.", "date": "2016-05-14", "time": "16:22"},

        {"sender": "Estella", "text": "A Jinsei disse que você perdeu algumas memórias.", "date": "2016-05-14", "time": "16:24"},

        {"sender": "Estella", "text": "Você realmente não lembra de nada?", "date": "2016-05-14", "time": "16:25"},

        {"sender": "Estella", "text": "Tudo bem...", "date": "2016-05-14", "time": "16:31"},

        {"sender": "Estella", "text": "Eu só queria ouvir você falando comigo normalmente de novo.", "date": "2016-05-14", "time": "16:32"},

        {"sender": "Estella", "text": "Vou esperar você melhorar.", "date": "2016-05-14", "time": "16:34"},

        # =========================
        # ÚLTIMA MENSAGEM
        # =========================

        {"sender": "Estella", "text": "Boa noite, Kioku.", "date": "2016-05-21", "time": "23:58"}

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

label phone_choice_send_context:
    show screen phone_button
    show screen phone_notification
    show screen phone_system

    call player_choice_send

    return

label send_player_message(contact, text, date=None, time=None, typing_delay=1.0):
    if typing_delay > 0:
        pause typing_delay

    $ begin_player_typing(contact, text)

    while player_typing_active:
        pause 0.04
        $ player_type_next_char()

    $ add_message(contact, "Player", text, date, time)
    $ phone_chat_scroll_bottom = True
    $ finish_player_typing()

    return

label npc_type_and_send(contact, text, time=None):
    $ typing_contact = contact
    $ typing_active = True
    $ phone_chat_scroll_bottom = True
    $ renpy.restart_interaction()

    pause get_npc_typing_delay(text)

    $ typing_active = False
    $ add_message(contact, contact, text, time=time)
    $ phone_chat_scroll_bottom = True
    $ renpy.restart_interaction()

    return
init python:

    def unlock_contact(name):
        if name not in store.unlocked_contacts:
            store.unlocked_contacts.append(name)

    def first_chat_starts_at_top(contact):
        return normalize_contact_id(contact) in ("star_contact", "Estella")

    def get_chat_scroll_initial(contact):
        contact = normalize_contact_id(contact)
        if store.phone_chat_scroll_bottom or store.phone_chat_force_bottom.get(contact, False):
            return 1.0
        if contact in store.phone_chat_scroll_positions:
            return store.phone_chat_scroll_positions[contact]
        if first_chat_starts_at_top(contact):
            return 0.0
        return 1.0

    def save_current_chat_scroll():
        contact = normalize_contact_id(store.current_chat)
        if contact is None:
            return

        try:
            viewport = renpy.get_widget("phone_chat", "phone_chat_viewport")
            adjustment = viewport.yadjustment
            scroll_range = max(float(adjustment.range), 1.0)
            position = max(0.0, min(float(adjustment.value) / scroll_range, 1.0))
            store.phone_chat_scroll_positions[contact] = position
        except Exception:
            pass

    def mark_current_chat_at_bottom():
        contact = normalize_contact_id(store.current_chat)
        if contact is None:
            return
        store.phone_chat_scroll_positions[contact] = 1.0
        store.phone_chat_force_bottom[contact] = False
        store.phone_chat_opened[contact] = True

    def open_phone_chat(contact):
        save_current_chat_scroll()
        contact = normalize_contact_id(contact)
        store.current_chat = contact
        store.phone_screen = "chat"

        if not store.phone_chat_opened.get(contact, False):
            store.phone_chat_scroll_bottom = not first_chat_starts_at_top(contact)
            if first_chat_starts_at_top(contact):
                store.phone_chat_scroll_positions[contact] = 0.0
                store.phone_chat_force_bottom[contact] = False
        elif store.phone_chat_force_bottom.get(contact, False):
            store.phone_chat_scroll_bottom = True
        else:
            store.phone_chat_scroll_bottom = False

        store.phone_chat_opened[contact] = True
        renpy.restart_interaction()

    def add_message(contact, sender, text, date=None, time=None):
        contact = normalize_contact_id(contact)
        if contact not in store.chats:
            store.chats[contact] = []
        store.phone_chat_force_bottom[contact] = True
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

    def normalize_contact_id(contact):
        if contact in ("star_contact", "\u661f", "\u2b50"):
            return "star_contact"
        return contact

    def repair_phone_contacts():
        old_star_ids = ["\u661f", "\u2b50"]

        for old_id in old_star_ids:
            if old_id in store.chats:
                if "star_contact" not in store.chats:
                    store.chats["star_contact"] = store.chats[old_id]
                else:
                    store.chats["star_contact"].extend(store.chats[old_id])
                del store.chats[old_id]

        store.archived_contacts = [
            normalize_contact_id(contact) for contact in store.archived_contacts
        ]
        store.archived_contacts = list(dict.fromkeys(store.archived_contacts))

        for state_dict in (
            store.phone_chat_scroll_positions,
            store.phone_chat_opened,
            store.phone_chat_force_bottom,
        ):
            for old_id in old_star_ids:
                if old_id in state_dict:
                    state_dict["star_contact"] = state_dict[old_id]
                    del state_dict[old_id]

        if "star_contact" not in store.archived_contacts:
            store.archived_contacts.append("star_contact")

        store.contact_display_names["star_contact"] = "\u661f"

        if store.current_chat in old_star_ids:
            store.current_chat = "star_contact"

    def get_contact_name(contact):
        contact = normalize_contact_id(contact)
        return store.contact_display_names.get(contact, contact)

    def get_contact_font(contact):
        if normalize_contact_id(contact) == "star_contact":
            return "SourceHanSansLite.ttf"
        return "Coolvetica Rg It.otf"

    def confirm_contact_name(contact):
        contact = normalize_contact_id(contact)
        new_name = store.temp_contact_name.strip()

        if contact == "star_contact" and new_name in ("", "\u2b50", "\ufffd", "\u25a1", "\u25af"):
            new_name = "\u661f"

        store.contact_display_names[contact] = new_name
        store.current_chat = contact
        store.editing_contact_name = False
        store.temp_contact_name = ""
        renpy.restart_interaction()

    def get_contact_avatar(contact):
        return store.contact_avatars.get(contact, "images/ui/fotos_contatos/default.png")

    def register_contact(contact_id, display_name="???", avatar_file="default.png"):
        contact_id = normalize_contact_id(contact_id)
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

    on "show" action Function(repair_phone_contacts)

    if phone_open:

        modal True

        key "K_ESCAPE" action NullAction()

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
            action [Function(save_current_chat_scroll), SetVariable("phone_open", False)]

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
                        action Function(open_phone_chat, contact)

                        hbox:
                            spacing 12
                            yalign 0.5

                            add get_contact_avatar(contact) xysize (54, 54)

                            vbox:
                                yalign 0.5
                                spacing 3

                                text get_contact_name(contact):
                                    style "phone_header"
                                    font get_contact_font(contact)
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
                        action Function(open_phone_chat, contact)

                        hbox:
                            spacing 12
                            yalign 0.5

                            add "lock_icon" xysize (48, 48)

                            vbox:
                                yalign 0.5
                                spacing 3

                                text get_contact_name(contact):
                                    style "phone_header"
                                    font get_contact_font(contact)
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
                action [Function(save_current_chat_scroll), SetVariable("phone_screen", "archive_list")]
            else:
                action [Function(save_current_chat_scroll), SetVariable("phone_screen", "sms")]

        imagebutton:
            idle "info_icon"
            hover "info_icon"
            xpos 295
            ypos 35
            xysize (28, 28)
            action [
                Function(repair_phone_contacts),
                SetVariable("editing_contact_name", True),
                SetVariable("temp_contact_name", get_contact_name(current_chat))
            ]

        text "[get_contact_name(current_chat)]":
            style "phone_header"
            font get_contact_font(current_chat)
            xalign 0.5
            ypos 48
            size 26
            color "#ffffff"

        $ yinitial_scroll = get_chat_scroll_initial(current_chat)

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
                                            size 11
                                            color "#ffffff"
                                            outlines [(1, "#1b5fbd", 0, 0)]

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
                                            size 11
                                            color "#333333"

                            null:
                                xfill True

                if player_typing_active and player_typing_contact == current_chat:

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

                            add "typing_dot":
                                xysize (10, 10)
                                at dot_wave(0.0)

                            add "typing_dot":
                                xysize (10, 10)
                                at dot_wave(0.15)

                            add "typing_dot":
                                xysize (10, 10)
                                at dot_wave(0.30)

        if phone_chat_scroll_bottom:
            timer 0.01 action [Scroll("phone_chat_viewport", "vertical increase", 9999, delay=0.0), Function(mark_current_chat_at_bottom), SetVariable("phone_chat_scroll_bottom", False)]

        timer 0.5 repeat True action Function(save_current_chat_scroll)

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
                                    action Function(run_phone_choice, option["text"], option["label"], option.get("date", None), option.get("time", None))

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
                        font get_contact_font(current_chat)
                        color "#ffffff"
                        size 20
                        xalign 0.5
                        xmaximum 180

                    textbutton "Confirmar":
                        xalign 0.5
                        action Function(confirm_contact_name, current_chat)

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
