#!/usr/bin/env python3


import PySimpleGUI as sg
import colour
from colour.utilities.verbose import message_box

sg.theme('dark grey 9')

def nits_to_PQ(input_nits):
    PQ_OETF = round(colour.models.eotf_inverse_ST2084(input_nits), 4)
    return PQ_OETF

# Define the window's contents
layout = [[sg.Text("Enter a value in Nits"), sg.Input(key='-INPUT-')],
          [sg.Text("Resulting value in PQ", size=(20,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('PQ_colorConvert_gui', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # run the nits_to_PQ function
    input_nits = values['-INPUT-']
    # nits_to_PQ(input_nits)
    PQ_OETF = nits_to_PQ(input_nits)
    bit8 = round(PQ_OETF * (2**8-1))
    bit10 = round(PQ_OETF * (2**10-1))
    bit12 = round(PQ_OETF * (2**12-1))
    bit16 = round(PQ_OETF * (2**16-1))
    print('float PQ OETF is {} ---- 10 bit {} ---- 12 bit {}'.format(PQ_OETF, bit10, bit12))

    # Output a message to the window
    window.Element('-OUTPUT-').Update('', bit10) # need to update this to window.write_event_value()
    #window.write_event_value['-OUTPUT-'].Update('Nits = ', bit10out[1])
    #window['-OUTPUT-'].update('Nits =' + input_nits['input_nits'] + "gives you " + bit10out['bit10out'])

# Finish up by removing from the screen
window.close()

'''
message_box('With an input of {0} Nits,\n'
            'colour.models.eotf_inverse_ST2084:{1}\n'
            '8 bit code value:                 {2}\n'
            '10 bit code value:                {3}\n'
            '12 bit code value:                {4}\n'
            '16 bit code value:                {5}'
            .format(input_nits,
            f'{PQ_OETF:>30}',
            f'{bit8:>30}',
            f'{bit10:>30}',
            f'{bit12:>30}',
            f'{bit16:>30}'))


input_bit10 = int(input("Enter a 10 bit value (0-1023): "))

input_float = input_bit10/1023
PQ_EOTF = round(colour.models.eotf_ST2084(input_float), 4)
bit10 = round(input_bit10)
bit8 = round(bit10/(2**10-1) * (2**8-1))
bit12 = round(bit10/(2**10-1) * (2**12-1))
bit16 = round(bit10/(2**10-1) * (2**16-1))

message_box('With an input of {0} 10-bit code value,\n'
            'colour.models.eotf_ST2084:        {1}\n'
            '8 bit code value:                 {2}\n'
            '10 bit code value:                {3}\n'
            '12 bit code value:                {4}\n'
            '16 bit code value:                {5}'
            .format(input_bit10,
            f'{PQ_EOTF:>30}',
            f'{bit8:>30}',
            f'{bit10:>30}',
            f'{bit12:>30}',
            f'{bit16:>30}'))

#print('\n''With an input of {} Nits, one can derive the following:\n'.format(input_nits))
#print('using colour.models.eotf_inverse_ST2084:\t{}\n'.format(PQ_OETF))
#print('with a 10 bit code value of:\t{}\n'.format(int(colour.models.eotf_inverse_ST2084(input_nits)*1023)))
#print('using colour.models.eotf_ST2084:\t{}\n'.format(colour.models.eotf_ST2084(input_nits)))

'''