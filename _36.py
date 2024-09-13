from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.title = 'Калькулятор'
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.result_label = Label(text='0', font_size='40sp', size_hint=(1, 0.2))
        self.layout.add_widget(self.result_label)

        button_layout = BoxLayout(orientation='vertical', spacing=10)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '^2', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, size_hint=(1, None), height=70)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            button_layout.add_widget(h_layout)
        
        self.layout.add_widget(button_layout)
        return self.layout

    def on_button_press(self, instance):
        current_text = self.result_label.text
        
        if instance.text == '=':
            try:
                result = eval(current_text)
                self.result_label.text = str(result)
            except Exception:
                self.result_label.text = 'Error'
        elif instance.text == '^2':
                result = float(current_text)**2
                self.result_label.text = str(result)
        else:
            if current_text == '0':
                self.result_label.text = instance.text
            else:
                self.result_label.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()
