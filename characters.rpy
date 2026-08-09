# personagens_codex.rpy

define CODEX_TITULO = "Personagens"

default codex_personagem_selecionado = None
default codex_desbloqueados = []
default codex_relacoes_custom = {}

# Persistent stores for amizade/romance
default persistent.codex_amizade = {}
default persistent.codex_romance = {}
default persistent.codex_amizade_seed_version = 0
default persistent.codex_descricoes = {}
default persistent.codex_desbloqueados = []
default persistent.atributos = {}
default persistent.atributos_confirmed = False

# Runtime visibility flags/stores exposed to Ren'Py's store so screens
# and other script code can reference them safely.
default runtime_codex_amizade = {}
default runtime_codex_descricoes = {}
default codex_unsaved_changes = False
default codex_prechange_amizade_snapshot = {}
default codex_prechange_descricoes_snapshot = {}

init -2 python:
    # -- Sistema de Amizade (configurável) ----------------------------------
    # Níveis de amizade: lista de dicionários com level, min, max e nome.
    # Edite esses valores para ajustar thresholds e nomes.
    AMIZADE_LEVELS = [
        { 'level': -1, 'min': -10000000, 'max': -10, 'name': 'Desconhecidos' },
        { 'level': 0,  'min': 0,    'max': 9,  'name': 'Distantes' },
        { 'level': 1,  'min': -9,    'max': -1,  'name': 'Inimigos' },
        { 'level': 2,  'min': 10,   'max': 39, 'name': 'Amigos' },
        { 'level': 3,  'min': 40,   'max': 59, 'name': 'Bons Amigos' },
        { 'level': 4,  'min': 60,   'max': 100, 'name': 'Melhores Amigos' },
        { 'level': 5,  'min': 101,  'max': 99999, 'name': 'Romance' },
    ]

    # Nível a partir do qual a barra de Romance é desbloqueada. Edite conforme
    # desejar (pode ser um número de nível da lista acima, por exemplo 5).
    ROMANCE_UNLOCK_LEVEL = 5

    # Valores iniciais padrão por personagem (não sobrescreve saved progress).
    # Adicione aqui os pids com os pontos iniciais desejados.
    DEFAULT_AMIZADE_STARTS = {
        ## "KiokuAida": 50,
        "jinsei": 50,  
        "subaru": -9, 
    }

    # Seed version: bump this to force re-seeding defaults on next run.
    DEFAULT_AMIZADE_SEED_VERSION = 3

    # Persistência dos pontos de amizade por personagem: garantir dict
    try:
        if not hasattr(persistent, 'codex_amizade'):
            persistent.codex_amizade = {}
    except Exception:
        persistent.codex_amizade = {}

    try:
        if not hasattr(persistent, 'codex_desbloqueados') or persistent.codex_desbloqueados is None:
            persistent.codex_desbloqueados = []
    except Exception:
        persistent.codex_desbloqueados = []

    # Runtime (non-persistent) store for amizade during a session. Changes here
    # are not written to disk until `amizade_commit()` is called.
    runtime_codex_amizade = {}
    # Runtime (non-persistent) store for appended descriptions during a session.
    # These are lost when the player quits or resets without saving.
    runtime_codex_descricoes = {}

    # Track unsaved session changes so they can be reverted if desired.
    codex_unsaved_changes = False
    # Snapshots of persistent values prior to any session changes.
    codex_prechange_amizade_snapshot = {}
    codex_prechange_descricoes_snapshot = {}

    def codex_mark_unsaved_change(pid):
        """Record the pre-change persistent values for `pid` the first time
        the session mutates data. This allows `revert_unsaved_codex_changes()`
        to restore the previous saved state.
        """
        global codex_unsaved_changes, codex_prechange_amizade_snapshot, codex_prechange_descricoes_snapshot
        try:
            if not codex_unsaved_changes:
                codex_unsaved_changes = True
        except Exception:
            pass
        try:
            if pid not in codex_prechange_amizade_snapshot:
                # Capture the persistent value (not runtime) as the baseline.
                codex_prechange_amizade_snapshot[pid] = int(persistent.codex_amizade.get(pid, relacao_base(pid, 'amizade')))
        except Exception:
            pass
        try:
            if pid not in codex_prechange_descricoes_snapshot:
                codex_prechange_descricoes_snapshot[pid] = list(persistent.codex_descricoes.get(pid, []))
        except Exception:
            pass

    def revert_unsaved_codex_changes():
        """Restore in-memory runtime changes and clear unsaved snapshots.
        This does NOT display any warnings; it simply discards unsaved
        runtime changes so the game will continue using the last persisted
        values.
        Returns True if any changes were reverted.
        """
        global codex_unsaved_changes, codex_prechange_amizade_snapshot, codex_prechange_descricoes_snapshot
        renpy.log("revert_unsaved_codex_changes: called")
        reverted = False
        try:
            # If we have explicit pre-change snapshots, remove those runtime
            # overrides. Otherwise, clear all runtime stores to be safe.
            if codex_prechange_amizade_snapshot:
                for pid in list(codex_prechange_amizade_snapshot.keys()):
                    if pid in runtime_codex_amizade:
                        del runtime_codex_amizade[pid]
                        reverted = True
            else:
                if runtime_codex_amizade:
                    runtime_codex_amizade.clear()
                    reverted = True

            if codex_prechange_descricoes_snapshot:
                for pid in list(codex_prechange_descricoes_snapshot.keys()):
                    if pid in runtime_codex_descricoes:
                        del runtime_codex_descricoes[pid]
                        reverted = True
            else:
                if runtime_codex_descricoes:
                    runtime_codex_descricoes.clear()
                    reverted = True
        except Exception:
            pass

        # Reset tracking regardless.
        try:
            codex_prechange_amizade_snapshot.clear()
            codex_prechange_descricoes_snapshot.clear()
            codex_unsaved_changes = False
        except Exception:
            pass

        return bool(reverted)

    # Banco de dados dos personagens e ordem de registro
    personagens_db = {}
    personagens_ordem = []

    def amizade_get_points(pid):
        """Retorna os pontos atuais de amizade (persistentes)."""
        # Prefer runtime (unsaved) value if present
        try:
            if pid in runtime_codex_amizade:
                return int(runtime_codex_amizade.get(pid, 0))
        except Exception:
            pass
        try:
            pts = persistent.codex_amizade.get(pid)
            if pts is not None:
                return int(pts)
        except Exception:
            pass
        # fallback: use relacao_base if disponível
        try:
            return int(relacao_base(pid, 'amizade'))
        except Exception:
            return 0

    def amizade_set_points(pid, pts):
        """Define pontos e checa unlocks (salva persistent)."""
        # Mark unsaved change and update runtime store only. Persist when player explicitly saves.
        try:
            codex_mark_unsaved_change(pid)
        except Exception:
            pass
        runtime_codex_amizade[pid] = int(pts)
        # checar romance
        try:
            lvl = amizade_get_level(pid)
            if lvl >= ROMANCE_UNLOCK_LEVEL:
                personagens_db.setdefault(pid, {})['romance_unlocked'] = True
        except Exception:
            pass

    def amizade_commit():
        """Persist current runtime amizade values to disk.
        Call this when the player saves the game to persist progress.
        """
        global codex_unsaved_changes, codex_prechange_amizade_snapshot, codex_prechange_descricoes_snapshot
        try:
            # Persist runtime values to persistent store.
            for k, v in list(runtime_codex_amizade.items()):
                persistent.codex_amizade[k] = int(v)
            renpy.save_persistent()
            # After saving, clear runtime overrides so subsequent screens
            # read the persisted values, and reset the unsaved-change tracking.
            try:
                for k in list(runtime_codex_amizade.keys()):
                    # remove runtime override to force reading from persistent
                    del runtime_codex_amizade[k]
            except Exception:
                runtime_codex_amizade.clear()
            try:
                codex_prechange_amizade_snapshot.clear()
                codex_prechange_descricoes_snapshot.clear()
                codex_unsaved_changes = False
            except Exception:
                pass
        except Exception:
            pass

    def amizade_add(pid, delta):
        """Adiciona (positivo/negativo) pontos de amizade e retorna novo valor."""
        pts = amizade_get_points(pid) + int(delta)
        amizade_set_points(pid, pts)
        return pts

    def amizade_get_level(pid):
        """Calcula nível atual baseado nos thresholds definidos em AMIZADE_LEVELS."""
        pts = amizade_get_points(pid)
        for lvl in AMIZADE_LEVELS:
            if pts >= lvl['min'] and pts <= lvl['max']:
                return lvl['level']
        # fallback: highest level if beyond ranges
        return AMIZADE_LEVELS[-1]['level']

    def amizade_level_info(level):
        for lvl in AMIZADE_LEVELS:
            if lvl['level'] == level:
                return lvl
        return AMIZADE_LEVELS[0]

    def amizade_set_romance_enabled(pid, enabled=True):
        personagens_db.setdefault(pid, {})['romance_unlocked'] = bool(enabled)

    # --- Descrições dinâmicas: permitir anexar notas à descrição padrão ---
    def adicionar_descricao(pid, texto):
        """Anexa `texto` à ficha do personagem `pid` e mostra notificação.
        Exemplo de uso em script: adicionar_descricao("jinsei", "Nova informação sobre ele.")
        """
        try:
            codex_mark_unsaved_change(pid)
        except Exception:
            pass
        try:
            lst = runtime_codex_descricoes.setdefault(pid, [])
            lst.append(str(texto))
        except Exception:
            pass
        try:
            nome = personagens_db.get(pid, {}).get('nome', pid)
            renpy.call_screen('diario_notify', nome=game_tr(nome))
        except Exception:
            pass

    # Alias curto
    adicionar_desc = adicionar_descricao

    def descricao_commit():
        """Persist runtime appended descriptions into `persistent.codex_descricoes`.
        Call this when the player saves to make session notes permanent.
        """
        global codex_unsaved_changes, codex_prechange_descricoes_snapshot
        try:
            for k, v in list(runtime_codex_descricoes.items()):
                persistent.codex_descricoes.setdefault(k, []).extend(list(v))
            renpy.save_persistent()
            # clear runtime appended descriptions after commit so menus
            # reflect the persisted values immediately
            try:
                for k in list(runtime_codex_descricoes.keys()):
                    del runtime_codex_descricoes[k]
            except Exception:
                runtime_codex_descricoes.clear()
            try:
                codex_prechange_descricoes_snapshot.clear()
                codex_unsaved_changes = False
            except Exception:
                pass
        except Exception:
            pass

    def reset_codex_amizade_for(pid):
        """Developer helper: reset a single personagem's persistent amizade
        value to the DEFAULT_AMIZADE_STARTS or the character's relacao_base.
        Usage (in script or console):
            $ reset_codex_amizade_for("jinsei")
        Returns True on success.
        """
        try:
            if 'DEFAULT_AMIZADE_STARTS' in globals() and pid in DEFAULT_AMIZADE_STARTS:
                base = int(DEFAULT_AMIZADE_STARTS[pid])
            else:
                base = int(relacao_base(pid, 'amizade'))
        except Exception:
            base = 0
        try:

            persistent.codex_amizade[pid] = int(base)
            renpy.save_persistent()
            renpy.log("reset_codex_amizade_for: %s -> %s" % (pid, base))
            return True
        except Exception:
            return False

    def _reset_persistent_save_folder(path):
        import os
        import shutil

        if not path:
            return

        try:
            if os.path.isdir(path):
                for fname in os.listdir(path):
                    fp = os.path.join(path, fname)
                    try:
                        if os.path.isdir(fp):
                            shutil.rmtree(fp)
                        else:
                            os.unlink(fp)
                    except Exception:
                        pass
        except Exception:
            pass

    def reset_game_progress():
        """Reset persistent codex progress and delete all save files."""
        global codex_unsaved_changes, codex_personagem_selecionado
        import os

        try:
            persistent.codex_amizade = {}
            persistent.codex_descricoes = {}
            persistent.codex_desbloqueados = []
            persistent.codex_romance = {}
            persistent.achievements = {}
            persistent.atributos = {}
            persistent.atributos_confirmed = False
            persistent.d20_last_final = None
            persistent.d20_natural_20_count = 0
            persistent.d20_natural_1_count = 0
            persistent.codex_amizade_seed_version = 0
            persistent._codex_one_time_jinsei_reset_done = False
            runtime_codex_amizade.clear()
            runtime_codex_descricoes.clear()
            codex_prechange_amizade_snapshot.clear()
            codex_prechange_descricoes_snapshot.clear()
            codex_relacoes_custom.clear()
            achievement_notify_queue.clear()
            codex_unsaved_changes = False
            codex_personagem_selecionado = None
        except Exception:
            pass

        try:
            for pid in list(personagens_ordem):
                desbloqueado_inicial = bool(personagens_db.get(pid, {}).get('desbloqueado_inicial', False))
                personagens_db.setdefault(pid, {})["desbloqueado"] = desbloqueado_inicial
                if desbloqueado_inicial and pid not in persistent.codex_desbloqueados:
                    persistent.codex_desbloqueados.append(pid)

                if pid in persistent.codex_amizade:
                    continue

                if 'DEFAULT_AMIZADE_STARTS' in globals() and pid in DEFAULT_AMIZADE_STARTS:
                    base = int(DEFAULT_AMIZADE_STARTS[pid])
                else:
                    base = 0
                    for rel in personagens_db.get(pid, {}).get('relacoes', []):
                        if rel.get('chave') == 'amizade':
                            base = int(rel.get('base', 0))
                            break
                persistent.codex_amizade[pid] = int(base)

            persistent.codex_amizade_seed_version = DEFAULT_AMIZADE_SEED_VERSION
            if getattr(renpy.config, 'savedir', None):
                os.makedirs(renpy.config.savedir, exist_ok=True)
                os.makedirs(os.path.join(renpy.config.savedir, "sync"), exist_ok=True)
            renpy.save_persistent()
        except Exception:
            pass

        try:
            save_dirs = []
            if getattr(renpy.config, 'savedir', None):
                save_dirs.append(renpy.config.savedir)
            if getattr(renpy.config, 'gamedir', None):
                save_dirs.append(os.path.join(renpy.config.gamedir, 'saves'))

            for path in save_dirs:
                _reset_persistent_save_folder(path)
                os.makedirs(os.path.join(path, "sync"), exist_ok=True)
        except Exception:
            pass

    def confirm_new_game():
        reset_game_progress()
        return Start()

    def player_has_saved_game():
        """Return True if there is at least one normal save file for this game."""
        import os

        try:
            save_dirs = []
            if getattr(renpy.config, 'savedir', None):
                save_dirs.append(renpy.config.savedir)
            if getattr(renpy.config, 'gamedir', None):
                save_dirs.append(os.path.join(renpy.config.gamedir, 'saves'))

            for directory in save_dirs:
                if not os.path.isdir(directory):
                    continue
                for fname in os.listdir(directory):
                    if not isinstance(fname, str):
                        continue
                    if fname.lower().endswith('.save'):
                        return True
            return False
        except Exception:
            return False

init python:
    def cadastrar_personagem(
        pid,
        nome,
        idade,
        imagem,
        descricao,
        descricao_bloqueado="",
        relacoes=None,
        desbloqueado=False
    ):
        """
        pid: ID interno do personagem, ex: "fulano"
        nome: nome exibido
        idade: idade exibida quando desbloqueado
        imagem: caminho da imagem desbloqueada
        descricao: texto em estilo diário quando desbloqueado
        descricao_bloqueado: texto opcional quando bloqueado
        relacoes: lista de fichas, ex:
            [
                {"chave": "amizade", "nome": "Amizade", "base": 5, "maximo": 10, "cor": "#4ec9b0"},
                {"chave": "confianca", "nome": "Confiança", "base": 8, "maximo": 10, "cor": "#9cdcfe"},
            ]
        """
        if relacoes is None:
            relacoes = []

        try:
            if not hasattr(persistent, 'codex_desbloqueados') or persistent.codex_desbloqueados is None:
                persistent.codex_desbloqueados = []
            if desbloqueado and pid not in persistent.codex_desbloqueados:
                persistent.codex_desbloqueados.append(pid)
                renpy.save_persistent()
            desbloqueado_atual = bool(desbloqueado or pid in persistent.codex_desbloqueados)
        except Exception:
            desbloqueado_atual = bool(desbloqueado)

        personagens_db[pid] = {
            "id": pid,
            "nome": nome,
            "idade": idade,
            "imagem": imagem,
            "descricao": descricao,
            "descricao_bloqueado": descricao_bloqueado,
            "relacoes": relacoes,
            "desbloqueado_inicial": bool(desbloqueado),
            "desbloqueado": desbloqueado_atual,
}

        if pid not in personagens_ordem:
            personagens_ordem.append(pid)
        # Initialize amizade persistent points from relacoes base if not set.
        try:
            if pid not in persistent.codex_amizade:
                # priority: DEFAULT_AMIZADE_STARTS -> relacoes base -> 0
                if 'DEFAULT_AMIZADE_STARTS' in globals() and pid in DEFAULT_AMIZADE_STARTS:
                    base = int(DEFAULT_AMIZADE_STARTS[pid])
                else:
                    base = 0
                    for r in relacoes:
                        if r.get('chave') == 'amizade':
                            base = int(r.get('base', 0))
                            break
                persistent.codex_amizade[pid] = int(base)
                renpy.save_persistent()
        except Exception:
            pass
        # Ensure romance flag exists — set based on current amizade level (persistent)
        try:
            lvl_now = amizade_get_level(pid)
            personagens_db[pid]['romance_unlocked'] = (lvl_now >= ROMANCE_UNLOCK_LEVEL)
        except Exception:
            personagens_db[pid].setdefault('romance_unlocked', False)


    def personagem_desbloqueado(pid):
        try:
            if pid in getattr(persistent, 'codex_desbloqueados', []):
                return True
        except Exception:
            pass
        return personagens_db[pid]["desbloqueado"]


    def desbloquear_Personagem(pid):
        if pid in personagens_db:
            ja_desbloqueado = personagem_desbloqueado(pid)
            personagens_db[pid]["desbloqueado"] = True
            try:
                if not hasattr(persistent, 'codex_desbloqueados') or persistent.codex_desbloqueados is None:
                    persistent.codex_desbloqueados = []
                if pid not in persistent.codex_desbloqueados:
                    persistent.codex_desbloqueados.append(pid)
                    renpy.save_persistent()
            except Exception:
                pass
            try:
                if not ja_desbloqueado:
                    nome = personagens_db.get(pid, {}).get('nome', pid)
                    renpy.call_screen('diario_notify', nome=game_tr(nome))
            except Exception:
                pass

    def bloquear_Personagem(pid):
        if pid in personagens_db:
            personagens_db[pid]["desbloqueado"] = False
            try:
                if pid in persistent.codex_desbloqueados:
                    persistent.codex_desbloqueados.remove(pid)
                    renpy.save_persistent()
            except Exception:
                pass


    def nome_personagem(pid):
        p = personagens_db[pid]
        return game_tr(p["nome"]) if personagem_desbloqueado(pid) else "?????"


    def idade_personagem(pid):
        p = personagens_db[pid]
        return str(p["idade"]) if personagem_desbloqueado(pid) else "????"


    def descricao_personagem(pid):
        p = personagens_db[pid]
        if personagem_desbloqueado(pid):
            base = game_tr(p.get("descricao", "") or "")
            try:
                extras = [game_tr(x) for x in list(runtime_codex_descricoes.get(pid, []))]
                if not extras:
                    extras = [game_tr(x) for x in list(persistent.codex_descricoes.get(pid, []))]
            except Exception:
                extras = []
            if extras:
                base_strip = base.rstrip()
                if base_strip and base_strip[-1] in '.!?':
                    sep = ' '
                else:
                    sep = '. '
                return base_strip + sep + ' '.join(extras)
            return base
        return game_tr(p["descricao_bloqueado"]) or "???"

    def relacao_base(pid, chave):
        p = personagens_db[pid]
        for rel in p["relacoes"]:
            if rel["chave"] == chave:
                return int(rel.get("base", 0))
        return 0

    def relacao_maximo(pid, chave):
        p = personagens_db[pid]
        for rel in p["relacoes"]:
            if rel["chave"] == chave:
                return int(rel.get("maximo", 10))
        return 10

    def relacao_cor(pid, chave):
        p = personagens_db[pid]
        for rel in p["relacoes"]:
            if rel["chave"] == chave:
                return rel.get("cor", "#4ec9b0")
        return "#4ec9b0"

    def relacao_atual(pid, chave):
        # Se existir valor customizado, usa ele.
        if (pid, chave) in codex_relacoes_custom:
            return int(codex_relacoes_custom[(pid, chave)])

        # Senão, usa o valor base definido no personagem.
        return relacao_base(pid, chave)

    def definir_relacao(pid, chave, valor):
        maximo = relacao_maximo(pid, chave)
        valor = int(valor)

        if valor < 0:
            valor = 0
        if valor > maximo:
            valor = maximo

        codex_relacoes_custom[(pid, chave)] = valor

    def ajustar_relacao(pid, chave, delta):
        definir_relacao(pid, chave, relacao_atual(pid, chave) + int(delta))


# Exemplos de personagens.
# Copie e edite quantos quiser.
init python:
    cadastrar_personagem(
        "KiokuAida",
        nome="Kioku Aida",
        idade= 19,
        imagem="images/personagens/Kioku Aida/KiokuCNormal.png",
        descricao="Kioku Aida... esse sou eu. Ou pelo menos acho que sou. Às vezes sinto que esqueço coisas simples, outras vezes tenho a impressão estranha de que existe algo faltando em mim. Talvez seja apenas cansaço. Ou talvez eu pense demais.",
        desbloqueado=True,
    )

    cadastrar_personagem(
        "jinsei",
        nome="Jinsei Boto",
        idade=18,
        imagem="images/Personagens/Jinsei Boto/Jinsei Boto Tela Escola/JinseiNormal.png",
        descricao="Jinsei Boto. Somos amigos há tempo suficiente pra ela me irritar sem pedir permissão. Ela gosta de agir como se tivesse resposta pra tudo... e, honestamente, às vezes isso é irritantemente útil.",
        descricao_bloqueado="Um rosto difícil de esquecer, mesmo antes de entender quem é.",
        desbloqueado=False,
    )
    cadastrar_personagem(
        "estella",
        nome="Estella Nascimento",
        idade=19,
        imagem="images/Personagens/Estella Nascimento/StellaNascimento.png",
        descricao="Estella Nascimento... Ela é uma garota de cabelos prateados e olhos azuis. Ela tem um jeito misterioso e reservado, mas também parece ser gentil e atenciosa. Ainda não tive muitas oportunidades de conversar com ela, mas sinto que há algo especial nela que me intriga... Como se eu já conhecesse ela?",
        descricao_bloqueado="Uma pessoa misteriosa. Não sei nada sobre ela ainda.",
        desbloqueado=False,
    )
    cadastrar_personagem(
        "subaru",
        nome="Subaru Ichida",
        idade=20,
        imagem="images/Personagens/Subaru Ichida/SubaruIchidanormal.png",
        descricao="Subaru Ichida. Presidente do clube estudantil e, aparentemente, alguém que não foi muito com a minha cara. Tem esse jeito irritante de agir como se soubesse exatamente como me tirar do sério.",
        descricao_bloqueado="Uma pessoa enigmática. Não sei nada sobre ele ainda.",
        desbloqueado=False,
    )
    cadastrar_personagem(
        "yuki",
        nome="Yuki Tatsuo",
        idade=38,
        imagem="images/Personagens/Yuki Tatsuo/YukiTatsuo.png",
        descricao="Professor Yuki Tatsuo. Sério, organizado e provavelmente mais paciente do que demonstra. Tenho a impressão de que ele percebe mais coisas do que costuma comentar.",
        desbloqueado=False,
    )


init 2 python:
    # One-time reseed: if seed version differs, initialize missing persistent
    # values only. Do NOT overwrite any existing saved amizade values.
    try:
        current = getattr(persistent, 'codex_amizade_seed_version', None)
        if current != DEFAULT_AMIZADE_SEED_VERSION:
            for _pid in list(personagens_ordem):
                if _pid in DEFAULT_AMIZADE_STARTS:
                    persistent.codex_amizade[_pid] = int(DEFAULT_AMIZADE_STARTS[_pid])
                elif _pid not in persistent.codex_amizade:
                    try:
                        base = relacao_base(_pid, 'amizade')
                    except Exception:
                        base = 0
                    persistent.codex_amizade[_pid] = int(base)
            persistent.codex_amizade_seed_version = DEFAULT_AMIZADE_SEED_VERSION
            renpy.save_persistent()
    except Exception:
        pass

init 3 python:
    # One-time targeted reset for Jinsei if the user reported an incorrect level.
    # Runs after character registration and the reseed step so it can update
    # the persistent store safely. Sets a flag so it only runs once.
    try:
        if not getattr(persistent, '_codex_one_time_jinsei_reset_done', False):
            try:
                if 'jinsei' in personagens_db:
                    reset_codex_amizade_for('jinsei')
            except Exception:
                pass
            persistent._codex_one_time_jinsei_reset_done = True
            renpy.save_persistent()
    except Exception:
        pass


init 4 python:
    # Ensure Jinsei's persistent amizade is initialized only if missing.
    try:
        desired = DEFAULT_AMIZADE_STARTS.get('jinsei') if 'DEFAULT_AMIZADE_STARTS' in globals() else None
        if desired is not None:
            cur = persistent.codex_amizade.get('jinsei')
            if cur is None:
                persistent.codex_amizade['jinsei'] = int(desired)
                renpy.save_persistent()
                renpy.log("One-time apply DEFAULT_AMIZADE_STARTS for jinsei: %s" % (desired,))
    except Exception:
        pass



screen personagens_codex():
    tag menu

    use game_menu(CODEX_TITULO, scroll="viewport"):

        if codex_personagem_selecionado is None and len(personagens_ordem) > 0:
            # Prefer the first unlocked character so the detail and relation
            # bars are visible when opening the codex. Fall back to the
            # first registered character if none are unlocked.
            python:
                _sel = None
                for _pid in personagens_ordem:
                    if personagens_db.get(_pid, {}).get("desbloqueado"):
                        _sel = _pid
                        break
                if _sel is None:
                    _sel = personagens_ordem[0]
                codex_personagem_selecionado = _sel

        hbox:
            spacing 24
            xfill True
            yfill True

            # COLUNA ESQUERDA: LISTA DE პერს

            frame:
                xsize 360
                yfill True
                padding (18, 18)

                vbox:
                    spacing 12
                    text _("Lista") size 30

                    viewport:
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        xfill True
                        yfill True

                        vbox:
                            spacing 10

                            for cid in personagens_ordem:
                                $ p = personagens_db.get(cid, {})
                                $ relacoes_lista = list(p.get("relacoes", []))

                                button:
                                    xfill True
                                    action SetScreenVariable("codex_personagem_selecionado", cid)


                                    hbox:
                                        spacing 12
                                        xfill True

                                        fixed:
                                            xsize 78
                                            ysize 78

                                            if personagem_desbloqueado(cid):
                                                add Transform(p["imagem"], xysize=(78, 78))
                                            else:
                                                add Solid("#000")
                                                text "?" size 42 xalign 0.5 yalign 0.5

                                        vbox:
                                            spacing 2
                                            text nome_personagem(cid) size 22
                                            text (_("Desbloqueado") if personagem_desbloqueado(cid) else _("Bloqueado")) size 16

            # COLUNA DIREITA: FICHA DO PERSONAGEM
            frame:
                xfill True
                padding (22, 22)

                if codex_personagem_selecionado is not None:
                    $ pid = codex_personagem_selecionado
                    $ p = personagens_db.get(pid, {})
                    $ relacoes_lista = list(p.get("relacoes", []))
                    $ desbloqueado = personagem_desbloqueado(pid)
                    $ imagem_codex_w = 340 if pid == "jinsei" else 280
                    $ imagem_codex_h = 380

                    vbox:
                        spacing 18
                        xfill True
                        yfill True

                        hbox:
                            spacing 22
                            xfill True

                            fixed:
                                xsize imagem_codex_w
                                ysize imagem_codex_h

                                if desbloqueado:
                                    add Transform(p["imagem"], xysize=(imagem_codex_w, imagem_codex_h))
                                else:
                                    add Solid("#000")
                                    text "?" size 140 xalign 0.5 yalign 0.5

                            vbox:
                                spacing 10
                                xfill True

                                text (game_tr(p["nome"]) if desbloqueado else "???") size 40 
                                text _("Idade: [idade_personagem(pid)]") size 24

                                null height 10

                                text _("Diário") size 22
                                text descricao_personagem(pid) size 20 xmaximum 520

                                if pid == "KiokuAida" and persistent.atributos_confirmed:
                                    frame:
                                        xfill True
                                        padding (16, 16)
                                        background Solid("#111")

                                        vbox:
                                            spacing 10
                                            text _("Atributos") size 24
                                            hbox:
                                                spacing 10
                                                xfill True
                                                for attr, name in ATRIBUTOS_DEF:
                                                    frame:
                                                        background Solid("#222")
                                                        xminimum 100
                                                        xmaximum 140
                                                        yminimum 110
                                                        ymaximum 120
                                                        vbox:
                                                            spacing 6
                                                            xalign 0.5
                                                            yalign 0.5
                                                            text atributo_display_name(attr)[:3].upper() size 18 
                                                            hbox:
                                                                spacing 6
                                                                xalign 0.5
                                                                text _("[persistent.atributos.get(attr, 10)]") size 32 
                                                                text _("([atributo_modifier_value(attr):+d])") size 22

                                # Colocar as fichas/bares logo abaixo da descrição
                                # Estella is a special NPC and does not use relationship bars.
                                if pid not in ("KiokuAida", "estella", "yuki"):
                                    frame:
                                        xfill True
                                        padding (16, 16)

                                        vbox:
                                            spacing 10

                                            # DEBUG: log and show a safe summary (names/count) so
                                            # we don't accidentally render raw dicts as text tags.
                                            python:
                                                try:
                                                    renpy.log("[codex] relacoes_lista for %s: %r" % (pid, relacoes_lista))
                                                except Exception:
                                                    pass
                                            python:
                                                try:
                                                    _rel_names = ', '.join([str(r.get('nome', '?')) for r in relacoes_lista])
                                                except Exception:
                                                    _rel_names = '%d entries' % len(relacoes_lista)
                                            # text "Debug relations: [_rel_names]" size 14 color "#f88"

                                            if desbloqueado:
                                                text _("Relacionamentos") size 24
                                                # Sistema unificado: apenas a barra de Amizade
                                                python:
                                                    pts = amizade_get_points(pid)
                                                    lvl = amizade_get_level(pid)
                                                    info = amizade_level_info(lvl)
                                                    try:
                                                        rng = max(1, info['max'] - info['min'])
                                                        pct = float(pts - info['min']) / float(rng)
                                                    except Exception:
                                                        pct = 0.0
                                                    pct = max(0.0, min(1.0, pct))
                                                    filled = int(520 * pct)
                                                vbox:
                                                    spacing 6
                                                    text game_tr_format("Relacionamento - {nome}", nome=game_tr(info['name'])) size 18
                                                    # Render the bar as a single stacked area: dark background
                                                    # with the filled color overlaid to the left.
                                                    fixed:
                                                        xsize 520
                                                        ysize 22
                                                        add Solid("#222") xysize (520, 22)
                                                        if filled > 0:
                                                            add Solid("#4ec9b0") xysize (filled, 22)

                                                # Barra de Romance (aparece apenas se desbloqueada)
                                                python:
                                                    romance_ok = bool(personagens_db.get(pid, {}).get('romance_unlocked'))
                                                    romance_pts = int(persistent.codex_romance.get(pid, 0))
                                                    romance_max = 100
                                                    romance_filled = int(520 * (float(romance_pts) / float(max(1, romance_max)))) if romance_ok else 0
                                                if romance_ok:
                                                    text _("Romance") size 18
                                                    frame background Solid("#222") xmaximum 520 xminimum 520 ymaximum 16 yminimum 16:
                                                        null
                                                    frame background Solid("#ff77aa") xmaximum romance_filled xminimum 0 ymaximum 16 yminimum 16:
                                                        null
                                            else:
                                                text _("As fichas de relacionamento só aparecem quando o personagem é desbloqueado.") size 18

                else:
                    text _("Nenhum personagem selecionado.") size 22
