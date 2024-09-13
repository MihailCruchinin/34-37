from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text=' ', font_size='20sp', size_hint=(1, 0.2))
        self.layout.add_widget(self.label)

        def hex_to_rgba(hex_color):
            hex_color = hex_color.lstrip('#')
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            return (r, g, b, 1)  

        texts = [
            "#ff0000 Ц красный",
            "#ff8800 Ц оранжевый",
            "#ffff00 Ц желтый",
            "#00ff00 Ц зеленый",
            "00ffff Ц голубой",
            "#0000ff Ц синий",
            "#ff00ff Ц фиолетовый"
        ]

        hex_colors = [
            "#FF0000",  
            "#FF8800", 
            "#FFFF00",  
            "#00FF00",  
            "#00FFFF",  
            "#0000FF",  
            "#FF00FF"  
        ]

        # —оздание кнопок
        for text, hex_color in zip(texts, hex_colors):
            btn = Button(text=text, background_color=hex_to_rgba(hex_color), size_hint=(1, 0.1))
            btn.bind(on_press=self.change_text) 
            btn.text_value = text 
            self.layout.add_widget(btn)

        return self.layout

    def change_text(self, instance):
        self.label.text = instance.text_value 

if __name__ == '__main__':
    MyApp().run()