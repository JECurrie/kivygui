import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
	# Initialize infinite keyout
	def __init__(self, **kwargs):
		# Call grid layout constructor
		super(MyGridLayout, self).__init__(**kwargs)

		# Set columns
		self.cols = 1

		# Create a second gridlayout
		self.top_grid = GridLayout()
		self.top_grid.cols = 2




		# Add widgets
		self.top_grid.add_widget(Label(text="Name: "))
		# Add Input Box
		self.name = TextInput(multiline=False)
		self.top_grid.add_widget(self.name)

		self.top_grid.add_widget(Label(text="Address: "))
		# Add Input Box
		self.address = TextInput(multiline=False)
		self.top_grid.add_widget(self.address)

		self.top_grid.add_widget(Label(text="City: "))
		# Add Input Box
		self.city = TextInput(multiline=False)
		self.top_grid.add_widget(self.city)

		# Add the new top_rid to our app
		self.add_widget(self.top_grid)



		# Create a Submit Button
		self.submit = Button(text="Submit", font_size=32)
		# Bind the button
		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)

	def press(self, instance):	
		name = self.name.text
		address = self.address.text
		city = self.city.text

		#print(f'Hello {name}.  You like {pizza} and your favorite color is {color}.')
		# Print it to the screen
		self.add_widget(Label(text=f'Hello {name}.  Your address is {address} and your city is {city}.'))

		# Clear the input boxes
		self.name.text = ""
		self.address.text = ""
		self.city.text = ""		

class MyApp(App):
	def build(self):
		return MyGridLayout()


if __name__ == '__main__':
	MyApp().run()