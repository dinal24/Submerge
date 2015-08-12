import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):

	print("In the Class")
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")
		print("In the method")
		braces = False
		sels = self.view.sel()
		r = sublime.Region(1, 4)
		print(r)
		self.view.add_regions('text', [r], 'keyword', 'dot', sublime.DRAW_SQUIGGLY_UNDERLINE |sublime.DRAW_NO_OUTLINE | sublime.DRAW_NO_FILL)
        #view.add_regions('highlighted_lines', [0,5], 'keyword', 'dot', sublime.DRAW_OUTLINED)
		#sublime.Window.show_quick_panel(sublime.active_window(), 4, None,None, sublime.MONOSPACE_FONT)
		messages = "line1"
		window = sublime.active_window()
		window.show_quick_panel(messages, None, sublime.MONOSPACE_FONT)
		for sel in sels:
		    if self.view.substr(sel).find('{') != -1:
		        braces = True
		        #self.view.insert(edit, 0, "Hello, World!")
		        #console.log ("Hello Console")
		        print("Hello!")
