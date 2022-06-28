import PySimpleGUI as sg

global finalCode

sg.theme('Dark')

layout = [

    [sg.Text('Enter Multiple Lines', font='Helvetica 15', justification='center', background_color='#0d1b2a'),
     sg.Button('compress', font='Helvetica 15', key='-minify-',
               border_width=0, button_color='#07a54b', mouseover_colors='#079a46')],
    [sg.Multiline('', size=(56, 7), enter_submits=False, autoscroll=True, do_not_clear=True, pad=(6, 6),
                  font='Helvetica 15',
                  key="multi-line", background_color='#22466d', border_width=0, sbar_background_color='#0d1b2a',
                  sbar_arrow_color='#e0e1dd', sbar_frame_color='#0d1b2a', sbar_width=0, sbar_trough_color='#0d1b2a')],
    [sg.Text('Output:', font='Helvetica 15', background_color='#0d1b2a'),
     sg.InputText('Output here', font='Helvetica 15', key="-output-",
                  background_color='#22466d', border_width=0),
     sg.Button('Copy', font='Helvetica 15', key='-copy-',
               border_width=0, button_color='#07a54b', mouseover_colors='#079a46', use_ttk_buttons=True)],
    [sg.Button('Close', font='Helvetica 15', key='-close-',
               border_width=0, button_color='#07a54b', mouseover_colors='#079a46')]
]

window = sg.Window('minify code', layout, background_color='#0d1b2a')
text = sg.Text(background_color="#0d1b2a")


def minify(inputCode):
    global finalCode
    finalCode = inputCode.replace("\n", "\\n")
    finalCode = finalCode.replace("\"", "\\\"")

    window['-output-'].update(finalCode)


while True:
    event, values = window.read()
    if event == '-copy-':
        sg.clipboard_set(finalCode)

    if event == '-minify-':
        minify(values['multi-line'])
    if event == '-close-':
        break
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()
