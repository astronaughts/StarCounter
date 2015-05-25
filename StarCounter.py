import sublime, sublime_plugin

class StarCounterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()
        view = window.active_view()
        for num, region in enumerate(view.find_all('★')):
            view.replace(edit, region, str(num + 1))
