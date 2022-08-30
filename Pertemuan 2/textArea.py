import PySimpleGUI as sg

def main():
    layout = [  [sg.Text('Enter the command you wish to run')],
                [sg.Input(key='_IN_')],
                [sg.Output(size=(60,15))],
                [sg.Button('Run'), sg.Button('Exit')] ]

    window = sg.Window('Realtime Shell Command Output', layout)

    
    window.Close() 