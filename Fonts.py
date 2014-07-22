import sublime
import sublime_plugin
import Cocoa
# import platform, sys

# ON_WINDOWS = platform.system() is 'Windows'
# ST2 = sys.version_info < (3, 0)

# if not ON_WINDOWS:
    # not implemented yet...

class Fonts(sublime_plugin.TextCommand):
    def run(self):
    	manager = Cocoa.NSFontManager.sharedFontManager()
        self.show_panel(list(manager.availableFontFamilies())

