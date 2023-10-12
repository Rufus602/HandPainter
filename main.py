import PySimpleGUI as sg
import cv2
import camera as cm
import painter as pr
import menu
import threading
from pathlib import Path
from copy import deepcopy



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
if cameras != 0 :
    layout = [
        [sg.Menu(functions, key='-MENU-')],
        [sg.Text('Background image')],
        [sg.Input(key = '-INPUT-', expand_x=True), sg.Button('Open', key= '-OPEN-')],
        [sg.Checkbox('Do not use Image', key='-IMUSAGE-'), sg.Checkbox('Do not Double', key='-DOUBLE-')],
        [sg.Text('Camera: '), sg.Spin(cameras, initial_value=cameras[0], key='-CAMERAS-'),
         sg.Button('Change camera', key='-CAMERA-')],
        [sg.Button('Start', key= '-START-'), sg.Button('Stop', key= '-STOP-')],


        [sg.Text(text= "These parameters can be changed dynamically, changes in head menu must be applied too")],
        [sg.Text('Which hand will be used: '),sg.Radio('Both','hands', key='-BOTH-', default=True, enable_events=True ), sg.Radio('Left', 'hands', key='-LEFT-', enable_events=True), sg.Radio('Right', 'hands', key='-RIGHT-', enable_events=True)],
        [sg.Text('FPS regulation (less value will load cpu), use natural numbers'), sg.Input(default_text=1, key='-WAIT-')],
        [sg.Volume],
        [sg.Button('Apply', key='-APPLY-')]


    ]
else:
    layout = [
        [sg.Text(text='Connect camera, and reopen program')]
    ]

window = sg.Window('Editor', layout)
cameraNo = 0
cap = cv2.VideoCapture(0)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
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
            menu.choose_color_size()
            window['-MENU-'].update(functions)
        case 'Change':
            'black screen'
        case 'Reset':
            print('black screen')
        case '-OPEN-':
            file_path = sg.popup_get_file('open', no_window=True)
            if file_path:
                window['-INPUT-'].update(file_path)
        case '-START-':
            cap = cv2.VideoCapture(values['-CAMERAS-'])
            pr.Paint()
window.close()