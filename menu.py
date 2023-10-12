import PySimpleGUI as sg

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
