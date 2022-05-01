import PySimpleGUI as sg
import liminal_prof
import liminal_exam
import liminal_schedule
import base64

sg.theme('DarkPurple1')


layout = [ 
            [sg.Text('Welcome to LIMINAL LAYOUT, what do you want to check?')],
            [sg.Button('Professor e-mail'), sg.Button('Exams'), sg.Button('Schedule')],
            [sg.Button('Exit')],
            [sg.Image(source='assets/liminal_background.png', size=(500, 500))]
         ]


window = sg.Window('LIMINAL HOMEPAGE', layout, icon=base64.b64encode(open('assets/liminal_logo.png', 'rb').read()))


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    elif event == 'Professor e-mail':
        liminal_prof.execute_window()
        print('You pressed professor e-mail button')
    elif event == 'Exams':
        liminal_exam.execute_window()
        print('You pressed exams button')  
    elif event == 'Schedule':
        liminal_schedule.execute_window()
        print('You pressed schedule button')
window.close()
