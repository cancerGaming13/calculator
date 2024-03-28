import math

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Calc_layout(BoxLayout):
    display = StringProperty("0")
    user_input = StringProperty("0")
    num1 = 0
    num2 = 0
    operation = None

    def on_click_square(self):
        try:
            sqr = float(self.display) ** 2
            self.user_input = self.display + " squared =" + str(sqr)
            if sqr.is_integer():
                self.display = str(int(sqr))
            else:
                self.display = str(sqr)
        except ValueError:
            self.display = "Invalid Input"
            Clock.schedule_once(self.on_click_clear, 0.5)

    def on_click_sqrt(self):
        try:
            sqrt = math.sqrt(float(self.display))
            self.user_input = "square root of (" + self.display + ")"
            if sqrt.is_integer():
                self.display = str(int(sqrt))
            else:
                self.display = str(sqrt)
        except ValueError:
            self.display = "Invalid Input"
            Clock.schedule_once(self.on_click_clear, 0.5)

    def on_click(self, widget):
        if (self.display == "0"):
            if (widget.text == "."):
                self.display = self.display + widget.text
                self.user_input = self.user_input + widget.text
            else:
                self.display = ""
                self.display = self.display + widget.text
                self.user_input = ""
                self.user_input = self.user_input + widget.text

        else:
            self.display = self.display + widget.text
            self.user_input = self.user_input + widget.text

    def on_click_del(self):
        lst_display = list(self.display)
        user_display = list(self.user_input)
        if not lst_display or len(lst_display) == 1:
            self.display = "0"
            self.user_input = "0"
        else:
            lst_display.pop(-1)
            user_display.pop(-1)
            self.display = ''.join(lst_display)
            self.user_input = ''.join(user_display)

    def on_click_clear(self, dt):
        self.display = "0"
        self.num1 = 0
        self.num2 = 0
        self.operation = None
        self.user_input = "0"

    def on_click_operation(self, widget):
        self.num1 = float(self.display)
        self.operation = widget.text
        self.display = ""
        self.user_input = self.user_input + widget.text

    def on_click_equal(self, widget):
        res = None
        try:
            self.num2 = float(self.display)
            if (self.operation == "+"):
                res = self.num1 + self.num2
            elif (self.operation == "-"):
                res = self.num1 - self.num2
            elif (self.operation == "x"):
                res = self.num1 * self.num2
            elif (self.operation == "/"):
                if self.num2 != 0:
                    res = self.num1 / self.num2

            if res == None:
                self.display = "Invalid Operation"
                Clock.schedule_once(self.on_click_clear, 0.5)
            elif res.is_integer():
                self.display = str(int(res))
                self.user_input = self.user_input + widget.text + str(int(res))
            else:
                self.display = str(res)
                self.user_input = self.user_input + widget.text + str(res)
            self.operation = None
        except ValueError:
            self.display = "Invalid Operation"


class Calculator(App):
    def build(self):
        self.root = Calc_layout()
        return self.root

    def on_start(self):
        for child in self.root.children:
            if isinstance(child, GridLayout):
                for btn in child.children:
                    if isinstance(btn, Button):
                        btn.font_size = 15


if __name__ == "__main__":
    Calculator().run()
