from turtle import heading
from unicodedata import name
import PySimpleGUI as sg
import base64
import liminal_engine as lg

def execute_window():
    sg.theme('DarkPurple1')

    layout = [ [sg.Text('Nom'), sg.Input(key='-NAME-', size=(10, 10)), sg.Text('Cognoms'),sg.Input(key='-SURNAME-', size=(15, 10)), sg.Button('Search')], 
            [sg.Frame(title='Mail output', size=(200, 100), layout=[[sg.Output(key='-MAIL-', expand_y=True)]])]]

    window = sg.Window('LIMINAL PROFESSOR', layout, icon=base64.b64encode(open('assets/liminal_logo.png', 'rb').read()))


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
           break
        if event == 'Search':
            window['-MAIL-'].update(lg.get_professor(values['-NAME-'], values['-SURNAME-']))
