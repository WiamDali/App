from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class GameApp(App):
    def build(self):
        layout = FloatLayout()

        # Créer le bouton bleu
        blue_button = Button(background_color=(49/255, 140/255, 231/255, 1), size_hint=(0.5, 0.5), pos_hint={'center_x': 0.25, 'center_y': 0.5})
        blue_button.bind(on_release=self.play_blue_sound)
        layout.add_widget(blue_button)

        # Créer le bouton rouge
        red_button = Button(background_color=(207/255, 10/255, 29/255, 1), size_hint=(0.5, 0.5), pos_hint={'center_x': 0.75, 'center_y': 0.5})
        red_button.bind(on_release=self.play_red_sound)
        layout.add_widget(red_button)

        # Créer le bouton d'arrêt
        stop_button = Button(text="Arrêter", size_hint=(0.1, 0.1), pos_hint={'center_x': 0.2, 'center_y': 0.9})
        stop_button.bind(on_release=self.stop_app)
        layout.add_widget(stop_button)

        return layout

    def play_blue_sound(self, instance):
        sound = SoundLoader.load('Sons/blue_sound.wav')
        if sound:
            sound.play()

    def play_red_sound(self, instance):
        sound = SoundLoader.load('Sons/red_sound.wav')
        if sound:
            sound.play()

    def stop_app(self, instance):
        App.get_running_app().stop()


if __name__ == '__main__':
    GameApp().run()