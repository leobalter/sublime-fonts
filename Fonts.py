import sublime
import sublime_plugin
import Cocoa


class Fonts(sublime_plugin.TextCommand):

    def run(self, *args, **kwargs):
    	manager = NSFontManager.sharedFontManager()
		font_families = manager.availableFontFamilies()
		sublime.message_dialog("%s" % font_families)
