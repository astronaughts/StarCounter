import sublime, sublime_plugin

class StarCounterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for num, region in enumerate(self.view.find_all('★')):
            self.view.replace(edit, region, str(num + 1))
