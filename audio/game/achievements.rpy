# Achievements system: data, helper functions, and screens

default persistent.achievements = {}

# Runtime queue for pending achievement notifications (not persistent)
default achievement_notify_queue = []
init python:
    # Runtime list of achievement IDs that have been registered in code this session.
    registered_ach_ids = []
init python:
    # Persistent storage for achievements. Use `default persistent.achievements` above
    # so the linter and engine know this persistent exists.

    def add_achievement(aid, name, desc, icon=None, hide_desc=False, hide_name=False):
        """Register a new achievement.

        - aid: unique string id
        - name: display name
        - desc: description shown when unlocked
        - icon: optional path to an icon image
        """
        # Always record this achievement id as "registered" for this
        # session so purge_unregistered() knows to keep it. We do this
        # regardless of whether the achievement already exists in
        # persistent storage (prevents toggling on subsequent runs).
        try:
            if aid not in registered_ach_ids:
                registered_ach_ids.append(aid)
        except Exception:
            pass

        if aid in persistent.achievements:
            # If the achievement already exists, sync visibility flags so
            # changing the `add_achievement(...)` call updates presentation
            # without needing to call `update_achievement()` manually.
            try:
                ach = persistent.achievements[aid]
                changed = False
                if ach.get('hide_desc') != bool(hide_desc):
                    ach['hide_desc'] = bool(hide_desc)
                    changed = True
                if ach.get('hide_name') != bool(hide_name):
                    ach['hide_name'] = bool(hide_name)
                    changed = True
                if changed:
                    renpy.save_persistent()
                    renpy.log("Updated visibility flags for existing achievement: %s -> hide_desc=%r hide_name=%r" % (aid, bool(hide_desc), bool(hide_name)))
            except Exception:
                pass
            return False
        persistent.achievements[aid] = {
            'name': name,
            'desc': desc,
            'icon': icon,
            'hide_desc': bool(hide_desc),
            'hide_name': bool(hide_name),
            'unlocked': False,
            'discovered': False,
            'unlocked_time': None,
        }
        try:
            # Track registered IDs in this session for possible cleanup.
            registered_ach_ids.append(aid)
        except Exception:
            pass
        renpy.save_persistent()
        return True

    def unlock_achievement(aid, show_notify=True):
        """Unlock an achievement. Returns True if newly unlocked.

        If show_notify is True, shows a temporary notification in the
        bottom-right (like the consequence notify but for achievements).
        """
        ach = persistent.achievements.get(aid)
        if not ach:
            return False
        if ach.get('unlocked'):
            return False
        # Clear any hide flags when the player unlocks the achievement so
        # the player sees the real name and description after earning it.
        ach['unlocked'] = True
        ach['hide_desc'] = False
        ach['hide_name'] = False
        # Also mark as discovered and update unlocked_time.
        ach['discovered'] = True
        import time
        ach['unlocked_time'] = time.time()
        try:
            renpy.save_persistent()
            renpy.log("Unlocked achievement saved: %s -> %r" % (aid, {'unlocked': ach.get('unlocked'), 'hide_desc': ach.get('hide_desc'), 'hide_name': ach.get('hide_name'), 'discovered': ach.get('discovered')}))
        except Exception:
            renpy.log("Failed saving unlocked achievement: %s" % aid)
        # Force the UI to refresh so open screens reflect the new values.
        try:
            renpy.restart_interaction()
        except Exception:
            pass
        if show_notify:
            # Enqueue the notification; a watcher screen will display items when
            # possible. We avoid calling screens directly from other screens.
            try:
                achievement_notify_queue.append((ach['name'], ach['desc'], ach.get('icon'), 3))
            except Exception:
                # Fallback: try to call screen if queue unavailable
                try:
                    renpy.call_screen('achievement_notify', name=ach['name'], desc=ach['desc'], icon=ach.get('icon'))
                except Exception:
                    pass
        return True

    def is_unlocked(aid):
        ach = persistent.achievements.get(aid)
        return bool(ach and ach.get('unlocked'))

    def list_achievements():
        # Return a list of (id, data) tuples for iteration in screens.
        return list(persistent.achievements.items())

    # Debug helper: report which icon files are missing (writes to log).
    def debug_report_icons():
        missing = {}
        try:
            import os
            for aid, data in persistent.achievements.items():
                icon = data.get('icon')
                if icon:
                    ok = os.path.exists(icon)
                else:
                    ok = False
                if not ok:
                    missing[aid] = icon
                    renpy.log("Achievement icon missing: %s -> %s" % (aid, repr(icon)))
        except Exception as e:
            renpy.log("debug_report_icons error: %s" % e)
        return missing

    # Debug helper: unlock all achievements (for testing). Use in script as
    # $ debug_unlock_all()
    def debug_unlock_all(show_notify=False):
        for aid in list(persistent.achievements.keys()):
            try:
                unlock_achievement(aid, show_notify=show_notify)
            except Exception:
                renpy.log("Failed to unlock achievement: %s" % aid)

    def debug_lock_all():
        """Lock all achievements (for testing).

        Usage:
        - Console: `debug_lock_all()`
                - Script: use a line in `.rpy` like this without backticks:
                    $ debug_lock_all()
        """
        try:
            for aid, data in persistent.achievements.items():
                data['unlocked'] = False
                data['unlocked_time'] = None
            renpy.save_persistent()
            renpy.log("All achievements locked via debug_lock_all().")
            return True
        except Exception as e:
            renpy.log("debug_lock_all error: %s" % e)
            return False

    def update_achievement(aid, name=None, desc=None, icon=None, hide_desc=None, hide_name=None):
        """Update fields of an existing achievement. Returns True if updated.

        Use this to set an icon for achievements already registered in `persistent`.
        """
        ach = persistent.achievements.get(aid)
        if not ach:
            return False
        changed = False
        if name is not None and name != ach.get('name'):
            ach['name'] = name
            changed = True
        if desc is not None and desc != ach.get('desc'):
            ach['desc'] = desc
            changed = True
        if icon is not None and icon != ach.get('icon'):
            ach['icon'] = icon
            changed = True
        if hide_desc is not None and bool(hide_desc) != bool(ach.get('hide_desc')):
            ach['hide_desc'] = bool(hide_desc)
            changed = True
        if hide_name is not None and bool(hide_name) != bool(ach.get('hide_name')):
            ach['hide_name'] = bool(hide_name)
            changed = True
        if changed:
            renpy.save_persistent()
        return changed

    # Pop one notification from the queue (used by watcher screen)
    def pop_achievement_notify():
        try:
            if achievement_notify_queue:
                achievement_notify_queue.pop(0)
        except Exception:
            pass

    def debug_remove_achievement(aid):
        """Remove an achievement entry from persistent storage. Use in console:
        debug_remove_achievement('curioso')
        """
        try:
            if aid in persistent.achievements:
                del persistent.achievements[aid]
                renpy.save_persistent()
                renpy.log("Removed achievement from persistent: %s" % aid)
                return True
        except Exception as e:
            renpy.log("debug_remove_achievement error: %s" % e)
        return False

    def purge_unregistered():
        """Remove from `persistent.achievements` any entries whose id is not
        present in `registered_ach_ids` (useful after removing pre-registered
        achievements from code).
        """
        try:
            to_remove = [aid for aid in persistent.achievements.keys() if aid not in registered_ach_ids]
            for aid in to_remove:
                del persistent.achievements[aid]
                renpy.log("Purged unregistered achievement: %s" % aid)
            if to_remove:
                renpy.save_persistent()
            return to_remove
        except Exception as e:
            renpy.log("purge_unregistered error: %s" % e)
            return []
# Pre-register a couple example achievements (you can add more in future code)
init python:
    add_achievement('first_ach', "Não posso esquecer", "Eu preciso lembrar", "game/images/achievements/primeiraconquista.png", hide_desc=True, hide_name=False)
    add_achievement('estella', "Curioso", "Que barulho é esse?", "game/images/achievements/estella.png", hide_desc=False, hide_name=True)
    add_achievement('mingau', "Mingau", "Alimente o Mingau. É só isso mesmo...", "game/images/achievements/mingal.png", hide_desc=True, hide_name=False)
    add_achievement('trem_2', "Por um Tris", "Acho que você vai precisar de um pouco de descanso antes da prova...", "game/images/achievements/trem.png", hide_desc=False, hide_name=True)
    add_achievement('trem_3', "Pare esse trem", "Perder um trêm é sempre díficil, mas sempre tem um novo", "game/images/achievements/trem2.png", hide_desc=True, hide_name=False)
    add_achievement('trem', "Bem na hora", "Será que tem lugar vago?", "game/images/achievements/trem3.png", hide_desc=True, hide_name=False)
    add_achievement('darkpassager', "Passageiro Sombrio", "Esse sentimento é bom, não é Kioku?", "game/images/achievements/darkpassager.png", hide_desc=False, hide_name=True)
    add_achievement('killerpassager', "Passageiro Assassino", "Esse sentimento é ruim?.... Kioku", "game/images/achievements/killerpassager.png", hide_desc=False, hide_name=True)
    
    
    # Note: removed automatic purge of unregistered persistent achievements
    # to avoid accidentally deleting achievements the developer expects to keep.

# Auto-purge any persistent achievements that are not registered in this
# session. This removes leftover entries from old runs so the final game
# doesn't contain achievements you didn't add. If you want to keep this
# behavior off during development, either comment out this block or set
# `registered_ach_ids` appropriately before this runs.
init python:
    try:
        purged = purge_unregistered()
        if purged:
            renpy.log("Auto-purged unregistered achievements: %r" % (purged,))
    except Exception:
        renpy.log("Auto-purge of unregistered achievements failed.")

# Ensure persistent entries have visibility flags and sync defaults.
# This helps when editing `add_achievement(...)` during development.
init python:
    try:
        changed = False
        for aid, data in persistent.achievements.items():
            if 'hide_desc' not in data:
                data['hide_desc'] = False
                changed = True
            if 'hide_name' not in data:
                data['hide_name'] = False
                changed = True
        if changed:
            renpy.save_persistent()
            renpy.log("Synced missing visibility flags for achievements.")
    except Exception:
        renpy.log("Failed syncing achievement visibility flags.")
# Screen that lists all achievements
screen achievements():
    tag menu
    modal True
    zorder 500

    # When the player opens the achievements screen, mark locked achievements
    # as "discovered" so their description is shown (but the name remains hidden)
    python:
        try:
            changed = False
            for aid, data in persistent.achievements.items():
                if not data.get('unlocked') and not data.get('discovered'):
                    data['discovered'] = True
                    changed = True
            if changed:
                renpy.save_persistent()
        except Exception:
            pass

        # Ensure that any achievement already unlocked does not keep hide flags
        # set to True (this can happen if persistent was saved earlier). This
        # guarantees the UI shows name/description after unlocking.
        try:
            changed_unlocked = False
            for aid, data in persistent.achievements.items():
                if data.get('unlocked'):
                    if data.get('hide_desc') or data.get('hide_name'):
                        data['hide_desc'] = False
                        data['hide_name'] = False
                        changed_unlocked = True
            if changed_unlocked:
                renpy.save_persistent()
                renpy.log("Cleared hide flags for unlocked achievements on screen open.")
        except Exception:
            pass

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 14
        ypadding 14
        background Solid("#000c")
        vbox:
            spacing 12
            text _("Conquistas") size 46 color "#FFFFFF"
            text _("Feche com ESC ou clique fora.") size 18 color "#ddd"

            viewport id "ach_view" draggable True mousewheel True:
                vbox:
                    spacing 10
                    # iterate achievements
                    python:
                        ach_list = list_achievements()
                    for aid, data in ach_list:
                        python:
                            icon_path = data.get('icon')
                            try:
                                import os
                                icon_ok = bool(icon_path and os.path.exists(icon_path))
                            except Exception:
                                icon_ok = False

                        if data.get('unlocked'):
                            hbox:
                                spacing 12
                                if icon_ok:
                                    add data.get('icon') xysize (64,64)
                                else:
                                    frame background Solid("#2ecc71") xminimum 64 xmaximum 64 yminimum 64 ymaximum 64:
                                        null
                                vbox:
                                    # Unlocked always shows the real name. Descriptions
                                    # are shown unless explicitly hidden (and will be
                                    # cleared on unlock by `unlock_achievement`).
                                    text data.get('name') size 28 color "#fff"
                                    if not data.get('hide_desc'):
                                        text data.get('desc') size 18 color "#ddd"
                        elif data.get('discovered'):
                            # Discovered but not unlocked: reveal fields according
                            # to the per-achievement hide flags, substituting
                            # question marks where a field is hidden.
                            hbox:
                                spacing 12
                                frame background Solid("#555") xminimum 64 xmaximum 64 yminimum 64 ymaximum 64:
                                    text "🔒" xalign 0.5 yalign 0.5 size 34
                                vbox:
                                    if data.get('hide_name'):
                                        text "????????" size 28 color "#999"
                                    else:
                                        text data.get('name') size 28 color "#999"
                                    if data.get('hide_desc'):
                                        text "????????" size 18 color "#777"
                                    else:
                                        text data.get('desc') size 18 color "#ddd"
                        else:
                            # Not discovered: both name and description hidden
                            hbox:
                                spacing 12
                                frame background Solid("#555") xminimum 64 xmaximum 64 yminimum 64 ymaximum 64:
                                    text "🔒" xalign 0.5 yalign 0.5 size 34
                                vbox:
                                    text "????????" size 28 color "#999"
                                    text "????????????????????????" size 16 color "#777"

    # allow closing
    key "dismiss" action Return()

# Notification popup shown when an achievement is unlocked (bottom-right)
transform ach_slide_in:
    xalign 1.02
    yoffset 40
    linear 0.14 xalign 0.98 yoffset 0

transform ach_pulse:
    zoom 1.0
    linear 0.45 zoom 1.03
    linear 0.45 zoom 1.0
    repeat

transform desc_slide_in:
    xalign -0.02
    yoffset -40
    linear 0.14 xalign 0.02 yoffset 0

screen achievement_notify(name, desc, icon=None, duration=3):
    modal False
    zorder 450

    python:
        icon_ok = False
        try:
            import os
            icon_ok = bool(icon and os.path.exists(icon))
        except Exception:
            icon_ok = False

    frame:
        at ach_slide_in
        xalign 0.98
        yalign 0.98
        xpadding 12
        ypadding 10
        background Solid("#000c")
        vbox:
            spacing 6
            hbox:
                spacing 8
                if icon_ok:
                    add icon xysize (56,56)
                else:
                    frame background Solid("#f1c40f") xminimum 56 xmaximum 56 yminimum 56 ymaximum 56:
                        null
                vbox:
                    text name size 26 color "#fff" bold True at ach_pulse
                    text desc size 18 color "#ddd"

    timer duration action Return()


# Notification for appended character descriptions (top-left)
screen descricao_adicionada_notify(nome, duration=3):
    modal False
    zorder 460

    frame:
        at desc_slide_in
        xalign 0.02
        yalign 0.02
        xpadding 12
        ypadding 10
        background Solid("#000c")
        vbox:
            spacing 6
            text "Novas informações de %s foram adicionadas" % nome size 22 color "#fff" bold True

    timer duration action Return()


# Notification for diary updates/unlocks (top-left)
screen diario_notify(nome=None, duration=3):
    modal False
    zorder 461

    frame:
        at desc_slide_in
        xalign 0.02
        yalign 0.02
        xpadding 12
        ypadding 10
        background Solid("#000c")
        vbox:
            spacing 6
            if nome:
                text "Nota atualizada no Diário — %s" % nome size 22 color "#fff" bold True
            else:
                text "Nota atualizada no Diário" size 22 color "#fff" bold True

    timer duration action Return()


# Watcher screen: shows queued achievement notifications (bottom-right)
screen achievement_queue_watcher():
    modal False
    zorder 1200

    if achievement_notify_queue:
        # Peek first queued item
        $ name, desc, icon, duration = achievement_notify_queue[0]

        frame:
            at ach_slide_in
            xalign 0.98
            yalign 0.98
            xpadding 12
            ypadding 10
            background Solid("#000c")
            vbox:
                spacing 6
                hbox:
                    spacing 8
                    python:
                        icon_ok = False
                        try:
                            import os
                            icon_ok = bool(icon and os.path.exists(icon))
                        except Exception:
                            icon_ok = False

                    if icon_ok:
                        add icon xysize (56,56)
                    else:
                        frame background Solid("#f1c40f") xminimum 56 xmaximum 56 yminimum 56 ymaximum 56:
                            null
                    vbox:
                        text name size 26 color "#fff" bold True at ach_pulse
                        text desc size 18 color "#ddd"

        # Remove after duration
        timer duration action Function(pop_achievement_notify)

# Quick helper usage comment (how you should call it from story code):
# $ unlock_achievement('first_step')
# You can register new achievements from code using add_achievement(aid, name, desc, icon)
