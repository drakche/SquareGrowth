from kivy.app import App
from kivy.uix.button import Button


class TutorialApp(App):
    def build(self):
        return Button(
            text='Hello!',
            backgraound_color=(0, 0, 1, 1),
            font_size=15
            )

if __name__ == "__main__":
    TutorialApp().run()


