#  ---------=========|  Credits: Miles Bierie   |   Developed: Tuesday, 12 December - ???   |=========---------  #

import winsound
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal, Vertical, Container
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Static, Label
from tkinter import filedialog as fd
import cv2

    
class Sidebar(Static):
    def compose(self) -> ComposeResult:
        with Horizontal():
            self.container = Container()
            with self.container:
                with Vertical(classes='center'):
                    yield Button(label=' Video to Sequence ', id='vts', classes='defButton')
                    yield Button(label=' Sequence to Video ', id='stv', classes='defButton')
                    yield Button(label='File to Image Strip', id='ftis', classes='defButton')
            yield self.container

            with Vertical(id='sidebarB'):
                yield Button(label='<\n\n<\n\n<', id='labelButton')
        
    def on_mount(self):
        self.container.styles.animate("opacity", value=1.0, duration=2)

class VideoToSequence(Screen):
    BINDINGS = [
        ('ctrl+q', 'quit', 'Quit'),
        ('ctrl+d', 'toggle_dark_mode', 'Toggle Dark Mode'),
    ]
    
    CSS_PATH = "sequencer.tcss"
    
    def compose(self):
        yield Label('Video to Sequence', id='header', expand=True)
        yield Sidebar(classes='-hidden')
        
        with Horizontal():
            with Vertical(id='sidebarB'):
                yield Button(label='>\n\n>\n\n>', id='labelButton')
                
            with Grid(id='vts_grid',):
                yield Button('Test')
                yield Button('Test')
                yield Button('Test')
                yield Button('Test')
        yield Footer()
        
    @on(Button.Pressed, "#labelButton, defButtons")
    def press(self):
        self.query_one(Sidebar).toggle_class('-hidden')
    
class SequenceToVideo(Screen):
    BINDINGS = [
        ('ctrl+q', 'quit', 'Quit'),
        ('ctrl+d', 'toggle_dark_mode', 'Toggle Dark Mode'),
    ]
    
    CSS_PATH = "sequencer.tcss"
    
    def compose(self):
        yield Label('Sequence to Video', id='header', expand=True)
        yield Sidebar(classes='-hidden')
        
        with Horizontal():
            with Vertical(id='sidebarB'):
                yield Button(label='>\n\n>\n\n>', id='labelButton')
                
        yield Footer()
        
    @on(Button.Pressed, "#labelButton, #sb1, #sb2, sb3")
    def press(self):
        self.query_one(Sidebar).toggle_class('-hidden')
        
class FileToImageStrip(Screen):
    BINDINGS = [
        ('ctrl+q', 'quit', 'Quit'),
        ('ctrl+d', 'toggle_dark_mode', 'Toggle Dark Mode'),
    ]
    
    CSS_PATH = "sequencer.tcss"
    
    def compose(self):
        yield Label('File to Image Strip', id='header', expand=True)
        yield Sidebar(classes='-hidden')
        
        with Horizontal():
            with Vertical(id='sidebarB'):
                yield Button(label='>\n\n>\n\n>', id='labelButton')
                
        yield Footer()
        
    @on(Button.Pressed, "#labelButton")
    def press(self):
        self.query_one(Sidebar).toggle_class('-hidden')

class Default(App):
    BINDINGS = [
        ('ctrl+q', 'quit', 'Quit'),
        ('ctrl+d', 'toggle_dark_mode', 'Toggle Dark Mode'),
    ]
    
    SCREENS = {
        'video': VideoToSequence,
        'sequence': SequenceToVideo,
        'file': FileToImageStrip
    }
    
    CSS_PATH = "sequencer.tcss"
    
    def compose(self):
        yield Label('Sequencer', id='header', expand=True)

        with Container(classes='center'):
            with Horizontal(id='mainScreen', classes='border'):
                yield Button(label='Video to Sequence', id='vts', classes='defButton')
                yield Button(label='Sequence to Video', id='stv', classes='defButton')
                yield Button(label='File to Image Strip', id='ftis', classes='defButton')

        yield Footer()
            
    @on(Button.Pressed, '#vts, #stv, #ftis')
    def show_screen(self, event):
        try:
            self.query_one(Sidebar).toggle_class('-hidden')
        except:
            pass
        
        if event.button.id == 'vts':
            self.push_screen('video')
        elif event.button.id == 'stv':
            self.push_screen('sequence')
        elif event.button.id == 'ftis':
            self.push_screen('file')
        
    def action_toggle_dark_mode(self):
        self.dark = not self.dark
        
    def action_quit(self):
        self.exit()


if __name__ == '__main__':
    app = Default(watch_css=True)
    app.run()
