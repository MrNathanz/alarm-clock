import time
import webbrowser


def alarm():
    current_time = time.strftime("%H:%M")

    print("The current time is " + current_time + ".\n")
    print("At what time do you want to wake up?")
    print("Use the following form:\n Example: 07:30\n")

    wake_up_time = input("> ")

    while current_time != wake_up_time:
        current_time = time.strftime("%H:%M")

        print("It's " + current_time + ".")

        time.sleep(1)

    if current_time == wake_up_time:
        print("\nIt's time to wake up!")

        webbrowser.open_new("https://www.youtube.com/watch?v=GWXLPu8Ky9k")

        print("The alarm has gone off.\nPress any key to close the program...")

if __name__ == '__main__':
    alarm()
