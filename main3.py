from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import subprocess
from kivy.uix.scrollview import ScrollView
import requests
from bs4 import BeautifulSoup


def scrap(TEXT):



    # Faire une requête HTTP GET à l'URL de recherche de Google
    url = "https://www.google.com/search"
    params = {
        "q": TEXT  # Terme de recherche
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers)

    # Créer un objet BeautifulSoup en utilisant le contenu de la réponse
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver tous les éléments de la page avec la classe CSS "g" (les résultats de recherche)
    results = soup.find_all("div", class_="g")
    A=[]
    # Parcourir chaque résultat de recherche et extraire le lien
    for result in results:
        # Extraire le lien de l'élément <a>
        link = result.find("a")["href"]

        # Afficher le lien
        A.append(link)
    return A


def scrap_bis():
	# Faire une requête HTTP GET à l'URL fictive
	url = "https://www.monoprix.tn"
	response = requests.get(url)

	# Créer un objet BeautifulSoup en utilisant le contenu de la réponse
	soup = BeautifulSoup(response.content, "html.parser")

	# Trouver la balise <p> avec la classe "titleproduct"
	title_element = soup.find("p", class_="titleproduct")

	# Extraire le texte de la balise
	title = title_element.text.strip()

	# Afficher le titre
	#print("Titre du produit :", title)
	return [title]




class CodeCompilerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Créer le bouton Compiler
        compile_button = Button(text='Compiler', size_hint=(1, 0.2))
        compile_button.bind(on_release=self.compile_code)
        layout.add_widget(compile_button)

        # Créer le champ de saisie de texte
        self.text_input = TextInput(multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.text_input)

        # Créer le widget de défilement
        scroll_view = ScrollView(size_hint=(1, 0.6))

        # Créer le layout pour afficher les mots
        self.words_layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 10, 10, 10))
        scroll_view.add_widget(self.words_layout)

        layout.add_widget(scroll_view)

        # Créer le bouton Fermer
        close_button = Button(text='Fermer', size_hint=(1, 0.1))
        close_button.bind(on_release=self.close_app)
        layout.add_widget(close_button)

        return layout

    def compile_code(self, instance):
        # Obtenir le mot saisi par l'utilisateur
        word = self.text_input.text

        # Appeler la fonction 'scrap' avec le mot
        #result = scrap(word)
	result = scrap2()

        # Effacer le contenu précédent
        self.words_layout.clear_widgets()

        # Afficher chaque mot dans une étiquette
        for word in result:
            label = Label(text=word, size_hint=(1, None), height='40dp')
            self.words_layout.add_widget(label)

    def close_app(self, instance):
        App.get_running_app().stop()


if __name__ == '__main__':
    CodeCompilerApp().run()