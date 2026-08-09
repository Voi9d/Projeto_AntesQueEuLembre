init -20 python:
    def game_tr(text):
        if text is None:
            return ""
        try:
            if isinstance(text, str):
                return renpy.translate_string(text)
        except Exception:
            pass
        return text

    def game_tr_format(text, *args, **kwargs):
        try:
            return game_tr(text).format(*args, **kwargs)
        except Exception:
            return text
