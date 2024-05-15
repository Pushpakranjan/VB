
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image,  AsyncImage
from kivy.uix.widget import Canvas
from kivy.lang import Builder




class MainBoxLayout(BoxLayout):
    def button_pressed(self):


        if self.ids.my_text.text == "4096":
            self.ids.my_image.source = "Image/4096.PNG"
        elif self.ids.my_text.text == "4097":
            self.ids.my_image.source = "Image/4097.PNG"
        elif self.ids.my_text.text == "4099":
            self.ids.my_image.source = "Image/4099.PNG"
        else:
            self.ids.my_image.source = "Image/error.PNG"



        pass

    def button_reset(self):
        self.ids.my_image.source= "Image/bg.PNG"
        self.ids.my_text.text=""



class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

class MainButton(Button):

    pass
class MainTextInput(TextInput):
    pass
class MainLabel(Label):

    pass
class MainImage(Image):

    pass
class MianAsyncImage(AsyncImage):
    pass
class MainCanvas(Canvas):
    pass




class VBTroubleshootingApp(App):


    def build(self):
        kv = Builder.load_file("vbtroubleshooting.kv")
        return kv
        #Window.clearcolor = (1, 0, .5, 1)

VBTroubleshootingApp().run()