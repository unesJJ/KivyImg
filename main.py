from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image

Window.clearcolor = (0/255,0/255,0/255)
Window.size = (400, 600)

class MyTest(App):
    def build(self):
        self.title = "Image Test"
        img = Image(
            source = "JJ.jpg"
        )
        return img

if __name__ == "__main__":
    MyTest().run()