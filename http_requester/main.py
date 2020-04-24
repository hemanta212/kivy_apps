# -*- coding:utf-8 -*-

import requests
import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


class BaseWidget(Widget):
    def perform_http_request(self, method):
        url = self.input_url.text
        if url and not url.startswith("https://"):
            url = "https://" + url

        try:
            custom_request = requests.Request(method, url=url)
            response = requests.Session().send(custom_request.prepare())
            self.output_box.text = response.text
        except Exception as E:
            self.output_box.text = "ERROR:: \n" + str(E)

    def printer(self):
        print(self.input_url.text)
        print(self.output_box.text)


class TestApp(App):
    def build(self):
        win = BaseWidget()
        return win


if __name__ == '__main__':
    TestApp().run()
