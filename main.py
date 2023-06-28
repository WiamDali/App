from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class GameApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')

        # Créer le bouton bleu
        blue_button = Button(background_color=(0, 0, 1, 1))
        blue_button.bind(on_release=self.play_blue_sound)
        layout.add_widget(blue_button)

        # Créer le bouton rouge
        red_button = Button(background_color=(1, 0, 0, 1))
        red_button.bind(on_release=self.play_red_sound)
        layout.add_widget(red_button)

        return layout

    def play_blue_sound(self, instance):
        sound = SoundLoader.load('Sons/blue_sound.wav')
        if sound:
            sound.play()

    def play_red_sound(self, instance):
        sound = SoundLoader.load('Sons/red_sound.wav')
        if sound:
            sound.play()


if __name__ == '__main__':
    GameApp().run()