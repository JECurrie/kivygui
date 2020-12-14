import kivy
from kivy.app import App
from kivy.uix.label import Label
"""
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
"""
"""
class MyGridLayout(GridLayout):
	# Initialize infinite keyout
	def __init__(self, **kwargs):
		# Call grid layout constructor
		super(MyGridLayout, self).__init__(**kwarg)

		# Set columns
		self.cols = 2

		# Add widgets
		self.add_widget(Label(text="Name "))
		# Add Input Box
		self.name = TextInput(multi=False)
		self.add_widget(self.name)

		# Add widgets
		self.add_widget(Label(text="Favorite Pizza: "))
		# Add Input Box
		self.pizza = TextInput(multi=False)
		self.add_widget(self.pizza)

		# Add widgets
		self.add_widget(Label(text="Favorite Color: "))
		# Add Input Box
		self.color = TextInput(multi=False)
		self.add_widget(self.color)
"""

class MyApp(App):
	def build(self):
		return Label(text="Hi", font_size=72)


if __name__ == '__main__':
	MyApp().run()