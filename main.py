import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget

class BaseWidget(Widget):
    pass


class TestApp(App):
    def build(self):
        return BaseWidget()


if __name__ == '__main__':
    TestApp().run()
