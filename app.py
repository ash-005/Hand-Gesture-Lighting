import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
#from kivy.uix.camera import Camera


class mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(mygrid, self).__init__()
        self.add_widget(Label(text="UserName: "))
        
        self.s_name = TextInput(multiline=False)
        
        self.add_widget(self.s_name)
        
    # def build(self):
    #     return Label(text='Welcome to Lighting System')
class myapp(App):
    def build(self):
        return myapp()

if __name__ == "__main__":
    myapp().run()
