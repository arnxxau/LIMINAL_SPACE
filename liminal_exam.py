from turtle import heading
from unicodedata import name
import PySimpleGUI as sg
import liminal_engine as lg
import base64

def execute_window():
    sg.theme('DarkPurple1')

    layout = [ [sg.Multiline(key='-ASSIGS-', enter_submits=True, size=(20, 10)), sg.Button('Load')], 
                [sg.Text(text='Loaded subjects: ', border_width=5), sg.Text(key='-OUTPUT-'), sg.Button('Confirm and search')]
    ]

    window = sg.Window('LIMINAL EXAMS', layout, icon=base64.b64encode(open('assets/liminal_logo.png', 'rb').read()))


    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break

        if event == 'Load':
            window['-OUTPUT-'].update(values['-ASSIGS-'].split('\n'))
            print(values['-ASSIGS-'].split('\n'))

        if event == 'Confirm and search':
            x = lg.get_exam(values['-ASSIGS-'].split('\n'))
            window['-ASSIGS-'].update(lg.fix_exams(x))
