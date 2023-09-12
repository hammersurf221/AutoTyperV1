import pyautogui
import time

def type_text(text, initial_delay=15, cpm=540, period_pause=5):
    characters = len(text.replace(" ", ""))  # Count the number of characters
    delay = 60 / cpm  # Calculate the delay between each character based on CPM

    print(f"Starting in {initial_delay} seconds...")
    time.sleep(initial_delay)
    print("Typing...")

    for char in text:
        if char == ".":
            pyautogui.typewrite(char, interval=period_pause)  # Pause after typing a period
        else:
            pyautogui.typewrite(char, interval=delay)  # Delay between each character

    print("Text typing complete.")

def main():
    print("Text Typer Program")
    print("------------------")
    print("This program types the text you provide using keypresses.")
    print("Make sure to switch to the desired input field or application.")
    print()

    user_input = input("Enter the text you want to type: ")
    initial_delay_input = input("Enter the initial delay in seconds (default is 15): ")
    cpm_input = input("Enter the desired typing speed in CPM (default is 540): ")
    period_pause_input = input("Enter the pause in seconds after a period (default is 5): ")

    try:
        initial_delay = int(initial_delay_input)
    except ValueError:
        print("Invalid initial delay value. Using the default delay of 15 seconds.")
        initial_delay = 15

    try:
        cpm = int(cpm_input)
    except ValueError:
        print("Invalid CPM value. Using the default speed of 540 CPM.")
        cpm = 540

    try:
        period_pause = int(period_pause_input)
    except ValueError:
        print("Invalid period pause value. Using the default pause of 5 seconds.")
        period_pause = 5

    type_text(user_input, initial_delay, cpm, period_pause)

if __name__ == "__main__":
    main()
