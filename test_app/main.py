from kivy.app import App
from kivy.uix.button import Button


class testApp(App):
    def build(self):
        return Button(text="Hellow world")
        
        
testApp().run()