from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from requests import delete

Window.size = (500, 700)
Window.clearcolor = (1, 1, 1, 0.1)

Builder.load_file('Calculator.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if prior == "0" or prior == "Error type":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            self.ids.calc_input.text = f'{prior}.'
        elif '.' in prior:
            pass
        else:
            self.ids.calc_input.text = f'{prior}.'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = f'{answer:.3f}'  # str(answer)
        except:
            self.ids.calc_input.text = "Error type"

    def delete(self):
        prior = self.ids.calc_input.text
        if len(prior) == 1:
            self.ids.calc_input.text = "0"
        else:
            self.ids.calc_input.text = prior[0:-1]

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = prior[1:]
        else:
            self.ids.calc_input.text = f'-{prior}'


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
