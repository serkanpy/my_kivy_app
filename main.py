from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class UDFViewer(BoxLayout):
    def __init__(self, **kwargs):
        super(UDFViewer, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.filechooser = FileChooserIconView()
        self.filechooser.bind(on_selection=self.load_file)
        
        self.label = Label(text="Seçilen dosya içeriği burada gösterilecek.", size_hint_y=None)
        self.label.bind(texture_size=self.label.setter('size'))
        
        self.scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height/2))
        self.scrollview.add_widget(self.label)
        
        self.add_widget(self.filechooser)
        self.add_widget(self.scrollview)
    
    def load_file(self, filechooser, selection):
        if selection:
            with open(selection[0], 'r', encoding='utf-8') as file:
                self.label.text = file.read()

class UDFViewerApp(App):
    def build(self):
        return UDFViewer()

if __name__ == '__main__':
    UDFViewerApp().run()