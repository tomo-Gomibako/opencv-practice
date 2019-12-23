from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class Window(App):
  title = "OpenCV practice"

  def __init__(self, image, **kwargs):
    super().__init__(**kwargs)
    if image is None:
      raise "image is None"
    self.image = image
    
  def build(self):
    img = self.image
    widget = Widget()

    texture = Texture.create(
      size=(img.shape[1], img.shape[0]),
      colorfmt="bgr",
      bufferfmt="ubyte")
    texture.blit_buffer(
      img.tostring(),
      colorfmt="bgr",
      bufferfmt="ubyte")
    texture.flip_vertical()
    
    with widget.canvas:
      Rectangle(
        texture=texture,
        pos=(0, 0),
        size=(img.shape[1], img.shape[0]))

    return widget

if __name__ == "__main__":
    Window().run()
