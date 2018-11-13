import PySimpleGUI as sg
import time
from datetime import datetime

##=================================================== SET OPTIONS ===================================================##
sg.SetOptions(
    background_color = '#e2e2e2',
    text_element_background_color = '#e2e2e2'
    )

##================================================== SOME VARIABLES =================================================##
house_colours = {'Petronax':'#4286f4', 'Scholastica':'#f44141', 'Mauris':'#41f452', 'Hildegard':'#eef441'}
background_colour = '#e2e2e2'

##====================================================== FORMS ======================================================##
def FORMS(back_colour):
    #---------------------------------------------------- OPENING ----------------------------------------------------#
    global OPENING
    OPENING = [[sg.Text('Select House', size=(12, 1), font=('Courier New', 16))],
               [sg.InputOptionMenu(('Petronax', 'Mauris', 'Scholastica', 'Hildegard'), size=(17,1), key='House')],
               [sg.ReadFormButton('Select', size=(15, 1), font=('Courier New', 12))]]

    #----------------------------------------------------- START -----------------------------------------------------#
    global START
    START = [[sg.Text('Select Sport', size=(12, 1), font=('Courier New', 16), background_color=back_colour)],
             [sg.ReadFormButton('Running', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Swimming', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Weightlifting', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Shotput', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Discus', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Archery', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Records', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Close', size=(20, 1), font=('Courier New', 10))]]

    #---------------------------------------------------- RUNNING ----------------------------------------------------#
    global RUNNING
    RUNNING = [[sg.Text('Running', size=(12, 1), font=('Courier New', 16), background_color=back_colour)],
               [sg.ReadFormButton('Stopwatch', size=(20, 1), font=('Courier New', 10))],
               [sg.ReadFormButton('Speed Calculator', size=(20, 1), font=('Courier New', 10))],
               [sg.ReadFormButton('Back', size=(20, 1), font=('Courier New', 10))]]

    global START_BUTTON
    START_BUTTON = sg.ReadFormButton('Start', size=(32, 1), font=('Courier New', 10))
    global RESET_BUTTON
    RESET_BUTTON = sg.ReadFormButton('Reset', size=(32, 1), font=('Courier New', 10))
    global OVERALL_TIMER
    OVERALL_TIMER = sg.Text('0:00:00.000', size=(11, 1), font=('Courier New', 16), background_color=back_colour)
    global LAPPED_TIMER
    LAPPED_TIMER = sg.Text('0:00:00.000', size=(11, 1), font=('Courier New', 16), background_color=back_colour)
    global STOPWATCH
    STOPWATCH = [[sg.Text('Stopwatch', size=(12, 1), font=('Courier New', 16), background_color=back_colour)],
                 [sg.Text('Overall:', size=(8, 1), font=('Courier New', 16), background_color=back_colour),
                  OVERALL_TIMER],
                 [sg.Text('Lapped:', size=(8, 1), font=('Courier New', 16), background_color=back_colour),
                  LAPPED_TIMER],
                 [START_BUTTON],
                 [RESET_BUTTON],
                 [sg.ReadFormButton('Back', size=(32, 1), font=('Courier New', 10))]]

    global CALCULATOR_SPEED
    CALCULATOR_SPEED = sg.Text('0 km/h', size=(16, 1), font=('Courier New', 16), background_color=back_colour)
    global RUNNING_CALCULATOR
    RUNNING_CALCULATOR = [[sg.Text('Speed Calculator', size=(20, 1), font=('Courier New', 16), background_color=back_colour)],
                          [sg.Text('Distance:', size=(9, 1), font=('Courier New', 16), background_color=back_colour),
                           sg.InputText(size=(15, 1), key='Running Distance'),
                           sg.InputOptionMenu(('Kilometres', 'Metres'), size=(10, 1), key='Running Distance Unit')],
                          [sg.Text('Time:', size=(9, 1), font=('Courier New', 16), background_color=back_colour),
                           sg.InputText(size=(15, 1), key='Running Time'),
                           sg.InputOptionMenu(('Hours', 'Minutes', 'Seconds'), size=(10, 1), key='Running Time Unit')],
                          [sg.Text('Speed:', size=(9, 1), font=('Courier New', 16), background_color=back_colour),
                           CALCULATOR_SPEED],
                          [sg.ReadFormButton('Submit', size=(21, 1), font=('Courier New', 10)),
                           sg.ReadFormButton('Back', size=(21, 1), font=('Courier New', 10))]]

    #--------------------------------------------------- SWIMMING  ---------------------------------------------------#
    global SWIMMING
    SWIMMING = []

    #------------------------------------------------- WEIGHTLIFTING -------------------------------------------------#
    global WEIGHTLIFTING
    WEIGHTLIFTING = []

    #---------------------------------------------------- SHOTPUT ----------------------------------------------------#
    global SHOTPUT
    SHOTPUT = []

    #---------------------------------------------------- DISCUS  ----------------------------------------------------#
    global DISCUS
    DISCUS = []

    #---------------------------------------------------- ARCHERY ----------------------------------------------------#
    global ARCHERY
    ARCHERY = []

    #---------------------------------------------------- RECORDS ----------------------------------------------------#
    global RECORDS
    RECORDS = [[sg.Text('Records', size=(12, 1), font=('Courier New', 16), background_color=back_colour)],
             [sg.ReadFormButton('Running', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Swimming', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Weightlifting', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Shotput', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Discus', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Archery', size=(20, 1), font=('Courier New', 10))],
             [sg.ReadFormButton('Back', size=(20, 1), font=('Courier New', 10))]]
    
    global RECORDS_DATA
    RECORDS_DATA = {'Running':{'Speed':{}, 'Distance':{}, 'Time':{}},
                    'Swimming':{},
                    'Weightlifting':{},
                    'Shotput':{},
                    'Discus':{},
                    'Archery':{}}

    global RUNNING_RECORDS
    RUNNING_RECORDS = []
    
    global SWIMMING_RECORDS
    SWIMMING_RECORDS = []
    
    global WEIGHTLIFTING_RECORDS
    WEIGHTLIFTING_RECORDS = []
    
    global SHOTPUT_RECORDS
    SHOTPUT_RECORDS = []
    
    global DISCUS_RECORDS
    DISCUS_RECORDS = []
    
    global ARCHERY_RECORDS
    ARCHERY_RECORDS = []

##====================================================== CODE  ======================================================##
FORMS(background_colour)

window = sg.FlexForm('Track Compamion')
window.Layout(OPENING)

button, value = window.Read()
if button != None:
    house = value['House']
    background_colour = house_colours[house]
    window.CloseNonBlockingForm()
    sg.SetOptions(
        background_color = background_colour
        )
    FORMS(background_colour)
    while True:
        if button == None:
            break
        window = sg.FlexForm('Track Companion')
        window.Layout(START)
        button, value = window.Read()
        window.CloseNonBlockingForm()
        if button == 'Running':
            # Running
            while True:
                if button == None:
                    break
                window = sg.FlexForm('Track Companion')
                window.Layout(RUNNING)
                button, value = window.Read()
                window.CloseNonBlockingForm()
                if button == 'Stopwatch':
                    # Stopwatch
                    window = sg.FlexForm('Track Companion')
                    window.Layout(STOPWATCH)
                    RUN = False
                    RESET = True
                    LAP = True
                    while True:
                        button, value = window.ReadNonBlocking()
                        if button == 'Back':
                            START_BUTTON.Update(text='Start')
                            RESET_BUTTON.Update(text='Reset')
                            OVERALL_TIMER.Update('0:00:00.000')
                            LAPPED_TIMER.Update('0:00:00.000')
                            window.CloseNonBlockingForm()
                            break
                        elif not RUN:
                            if button == 'Start':
                                # Start
                                start = datetime.now()
                                start_LAP = start
                                START_BUTTON.Update(text='Stop')
                                RESET_BUTTON.Update(text='Lap')
                                RUN = True
                            elif button == 'Reset':
                                # Reset Time
                                RESET = True
                                OVERALL_TIMER.Update('0:00:00.000')
                                LAPPED_TIMER.Update('0:00:00.000')
                        else:
                            # Overall Timer
                            end = datetime.now()
                            overall = end - start
                            if not RESET:
                                overall += old_time
                            overall_S = str(overall)
                            overall_S = overall_S.replace('0', '0 ')
                            overall_S = overall_S.replace('1', '1 ')
                            overall_S = overall_S.replace('2', '2 ')
                            overall_S = overall_S.replace('3', '3 ')
                            overall_S = overall_S.replace('4', '4 ')
                            overall_S = overall_S.replace('5', '5 ')
                            overall_S = overall_S.replace('6', '6 ')
                            overall_S = overall_S.replace('7', '7 ')
                            overall_S = overall_S.replace('8', '8 ')
                            overall_S = overall_S.replace('9', '9 ')
                            overall_S = overall_S.replace(':', ': ')
                            overall_S = overall_S.replace('.', '. ')
                            overall_LIST = overall_S.split()
                            num = 0
                            overall_S = ''
                            for i in range(11):
                                try:
                                    overall_S += overall_LIST[num]
                                    num += 1
                                except IndexError:
                                    pass
                            # Lap Timer
                            lap = end - start_LAP
                            if not RESET and not LAP:
                                lap += old_time_LAP
                            lap_S = str(lap)
                            lap_S = lap_S.replace('0', '0 ')
                            lap_S = lap_S.replace('1', '1 ')
                            lap_S = lap_S.replace('2', '2 ')
                            lap_S = lap_S.replace('3', '3 ')
                            lap_S = lap_S.replace('4', '4 ')
                            lap_S = lap_S.replace('5', '5 ')
                            lap_S = lap_S.replace('6', '6 ')
                            lap_S = lap_S.replace('7', '7 ')
                            lap_S = lap_S.replace('8', '8 ')
                            lap_S = lap_S.replace('9', '9 ')
                            lap_S = lap_S.replace(':', ': ')
                            lap_S = lap_S.replace('.', '. ')
                            lap_LIST = lap_S.split()
                            num = 0
                            lap_S = ''
                            for i in range(11):
                                try:
                                    lap_S += lap_LIST[num]
                                    num += 1
                                except IndexError:
                                    pass
                            LAPPED_TIMER.Update(lap_S)
                            OVERALL_TIMER.Update(overall_S)
                            if button == 'Stop':
                                # Stop
                                START_BUTTON.Update(text='Start')
                                RESET_BUTTON.Update(text='Reset')
                                old_time = overall
                                old_time_LAP = lap
                                RUN = False
                                RESET = False
                                LAP = False
                            elif button == 'Lap':
                                # Lap
                                start_LAP = datetime.now()
                                LAPPED_TIMER.Update('0:00:00.000')
                                LAP = True
                elif button == 'Speed Calculator':
                    # Speed Calculator
                    window = sg.FlexForm('Track Companion')
                    window.Layout(RUNNING_CALCULATOR)
                    while True:
                        button, value = window.Read()
                        if button == 'Submit':
                            cont = True
                            if value['Running Distance Unit'] == 'Kilometres':
                                # Kilometres
                                try:
                                    dist =  float(value['Running Distance'])
                                except ValueError:
                                    print('Type a Number')
                                    cont = False
                            elif value['Running Distance Unit'] == 'Metres':
                                # Metres
                                try:
                                    dist = float(value['Running Distance'])
                                    if type(dist) == float:
                                        dist /= 1000
                                except ValueError:
                                    print('Type a Number')
                                    cont = False
                            if value['Running Time Unit'] == 'Hours':
                                # Hours
                                try:
                                    time = float(value['Running Time'])
                                except ValueError:
                                    print('Type a Number')
                                    cont = False
                            elif value['Running Time Unit'] == 'Minutes':
                                # Minutes
                                try:
                                    time = float(value['Running Time'])
                                    if type(time) == float:
                                        time /= 60
                                except ValueError:
                                    print('Type a Number')
                                    cont = False
                            elif value['Running Time Unit'] == 'Seconds':
                                # Seconds
                                try:
                                    time = float(value['Running Time'])
                                    if type(time) == float:
                                        time /= 3600
                                except ValueError:
                                    print('Type a Number')
                                    cont = False
                            if cont:
                                speed = dist / time
                                speed = round(speed, 4)
                                record_location = RECORDS_DATA['Running']['Speed']
                                if record_location == {}:
                                    record_location[speed] = dist, time
                                elif list(record_location)[0] < speed:
                                    del record_location[list(record_location)[0]]
                                    record_location[speed] = dist, time
                                CALCULATOR_SPEED.Update(str(str(speed) + ' km/h'))
                        elif button == 'Back':
                            window.CloseNonBlockingForm()
                            break
                        elif button == None:
                            break
                elif button == 'Back':
                    break
            if button == None:
                break
        elif button == 'Swimming':
            # Swimming
            window = sg.FlexForm('Track Companion')
            window.Layout(SWIMMING)
        elif button == 'Weightlifting':
            # Weightlifting
            window = sg.FlexForm('Track Companion')
            window.Layout(WEIGHTLIFTING)
        elif button == 'Shotput':
            # Shotput
            window = sg.FlexForm('Track Companion')
            window.Layout(SHOTPUT)
        elif button == 'Discus':
            # Discus
            window = sg.FlexForm('Track Companion')
            window.Layout(DISCUS)
        elif button == 'Archery':
            # Archery
            window = sg.FlexForm('Track Companion')
            window.Layout(ARCHERY)
        elif button == 'Records':
            # Records
            while True:
                if button == None:
                    break
                window = sg.FlexForm('Track Companion')
                window.Layout(RECORDS)
                button, value = window.Read()
                window.CloseNonBlockingForm()
                if button == 'Running':
                    # Running Records
                    window = sg.FlexForm('Track Companion')
                    window.Layout(RUNNING_RECORDS)
                elif button == 'Swimming':
                    # Swimming Records
                    window = sg.FlexForm('Track Companion')
                    window.Layout(SWIMMING_RECORDS)
                elif button == 'Weightlifting':
                    # Weightlifting Records
                    window = sg.FlexForm('Track Companion')
                    window.Layout(WEIGHTLIFTING_RECORDS)
                elif button == 'Shotput':
                    # Shotput Records
                    window = sg.FlexForm('Track Companion')
                    window.Layout(SHOTPUT_RECORDS)
                elif button == 'Discus':
                    # Discus Records
                    window = sg.FlexForm('Track Companion')
                    window.Layout(DISCUS_RECORDS)
                elif button == 'Archery':
                    # Archery Records
                    window = sg.FlexForm('Track Companion')
                    window.Layout(ARCHERY_RECORDS)
                elif button == 'Back':
                    break
        elif button == 'Close':
            break















