import PySimpleGUI as sg
import camera as cm
from pathlib import Path
from copy import deepcopy

def choose_color_size():
    color_layout = [
        [
            sg.Input(default_text=functions[3][1][2], key='-SIZE-')
        ],
        [
            sg.Button('Red', button_color='Red'),
            sg.Button('Blue', button_color='Blue'),
            sg.Button('Black', button_color='Black')
        ],
        [
            sg.Button('White', button_color='White'),
            sg.Button('Yellow', button_color='Yellow'),
            sg.Button('Green', button_color='Green')
        ],
    ]
    color_window = sg.Window('Editor', color_layout)
    while True:
        event, values = color_window.read()
        if event== sg.WIN_CLOSED:
            break
        else:
            if values['-SIZE-'].isnumeric():
                functions[3][1][2] = values['-SIZE-']
            functions[3][1][1]=event


            break
    color_window.close()


sg.theme('GrayGrayGray')

functions = [
    ['Draw ', ['Off DR']],
    ['Erase ', ['Off ER']],
    ['Place', ['Off PL']],
    ['Pen Color', ['Choose', 'Red', '5']],
    ['Screenshot', ['Take', 'Path']],
    ['Image replace', ['Change', 'Reset'] ]
]
cameras = cm.all_cameras()
cameras = cm
layout = [
    [sg.Menu(functions, key='-MENU-')],
    [sg.Input(key = '-INPUT-', expand_x=True), sg.Button('Open', key= '-OPEN-')],
    [sg.Button('Start', key= '-START-'), sg.Button('Stop', key= '-STOP-')],
    [sg.Checkbox('Use Image', key= '-IMUSAGE-'), sg.Checkbox('Double', key='-DOUBLE-')],
    [sg.Spin(cameras, key = '-CAMERAS-'), sp.Spin(resolutions, key = '-resolutions-')],
    []
    []
]

window = sg.Window('Editor', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    print(1)
    match event:
        case 'Take':
            print('screenshot')
            # here write place to locate screenshot
        case 'Path':
            print('choose path for screen shot')
        case 'On DR':
            functions[0][0] = 'Draw'
            functions[0][1][0] = 'Off DR'
            window['-MENU-'].update(functions)
        case 'Off DR':
            functions[0][0] = 'Draw *'
            functions[0][1][0] = 'On DR'
            window['-MENU-'].update(functions)
        case 'On ER':
            functions[1][0] = 'Erase'
            functions[1][1][0] = 'Off ER'
            window['-MENU-'].update(functions)
        case 'Off ER':
            functions[1][0] = 'Erase *'
            functions[1][1][0] = 'On ER'
            window['-MENU-'].update(functions)
        case 'On PL':
            functions[2][0] = 'Place'
            functions[2][1][0] = 'Off PL'
            window['-MENU-'].update(functions)
        case 'Off PL':
            functions[2][0] = 'Place *'

            functions[2][1][0] = 'On PL'
            window['-MENU-'].update(functions)
        case 'Choose':
            choose_color_size()
            window['-MENU-'].update(functions)
        case 'Change':
            'black screen'
        case 'Reset':
            print('black screen')
        case '-OPEN-':
            file_path = sg.popup_get_file('open', no_window=True)
            if file_path:
                window['-INPUT-'].update(file_path)
window.close()