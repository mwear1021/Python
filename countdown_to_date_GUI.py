import datetime
import PySimpleGUI as sg

def countdown_window(target_date):
    '''creates the countdown window'''

    layout = [
        [sg.Text('Countdown to target date: ', font=('Helvetica', 20), text_color='White', background_color="Black")],
        [sg.Text("", size=(20, 2), font=('Helvetica', 40), key="-TIME-", text_color="White", background_color="Black")],
        [sg.Button('Exit')]
    ]

    timer = sg.Window("Countdown", layout, background_color="Black")

    while True:
        event, _ = timer.read(timeout=1000)   #update every second

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        time_left = target_date - datetime.datetime.today()

        if time_left.total_seconds() <= 0:
            timer["-TIME-"].update("Time's Up!")
        else:
            timer["-TIME-"].update(str(time_left).split('.')[0])   # remove milliseconds

    timer.close()

def get_valid_date():
    while True:
        try:
            year = int(input("Enter target year: "))
            month = int(input("Enter target month: "))
            day = int(input("Enter target day: "))
            hour = int(input("Enter target hour: "))
            minute = int(input("Enter target minute: "))
            
            return datetime.datetime(year, month, day, hour, minute)
        except ValueError:
            print('Invalid input! Please enter valid numeric values for date/time.')
        except Exception as e:
            print("An unexpected error occurred:", str(e))

if __name__ == '__main__':
    target_date = get_valid_date()
    countdown_window(target_date)
