from turtle import heading
from unicodedata import name
import PySimpleGUI as sg
import liminal_engine as lg
import base64

def execute_window():
    columns = ['time','Monday', 'Tuesday', 'Wednesday', 'Thurdsay', 'Friday']

    sg.theme('DarkPurple1')

    layout = [ [sg.Input(key='-ASSIG-'), sg.Button('Search')],


    [sg.OptionMenu(values=['Català', 'Castellà', 'English'], default_value='null', key='-LANG-'), # language selector
        sg.Radio('Matí', group_id='x'), sg.Radio('Tarda', group_id='x'), sg.Radio('null', group_id='x', default=True),
            sg.Text(key='-INFO-')],


    [sg.Table(values=[], headings=columns, col_widths=25, key='-SCHEDULE-')]
    ]

    window = sg.Window('LIMINAL SCHEDULE', layout, icon=base64.b64encode(open('assets/liminal_logo.png', 'rb').read()))


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Search':
            l = lg.filter_schedule(values['-LANG-'], values['-ASSIG-'], 'null', lg.get_schedule_list())
            window['-SCHEDULE-'].update(lg.schedule_to_matrix(l))

            window['-INFO-'].update(values['-ASSIG-'])
