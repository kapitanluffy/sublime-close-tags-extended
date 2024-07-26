import sublime
import sublime_plugin

class TagCloseCommand(sublime_plugin.TextCommand):
    def get_current_positions(self):
        selections = self.view.sel()
        regions = []
        for selection in selections:
            regions.append(sublime.Region(selection.a, selection.b))
        return regions

    def run(self, edit: sublime.Edit):
        self.view.run_command("insert", { "characters": ">" })
        regions = self.get_current_positions()
        self.view.run_command("close_tag")

        if len(regions) == 1:
            new_selections = self.view.sel()
            new_selections.clear()
            new_selections.add_all(regions)


