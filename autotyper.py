import pyautogui
import time

def type_text(text, initial_delay=10, cpm=900, period_pause=60):
    characters = len(text.replace(" ", ""))  # Count the number of characters
    delay = 60 / cpm  # Calculate the delay between each character based on CPM

    print(f"Starting in {initial_delay} seconds...")
    time.sleep(initial_delay)
    print("Typing...")

    period_count = 0  # Counter for the number of periods typed

    for char in text:
        if char == ".":
            period_count += 1
            pyautogui.typewrite(char, interval=delay)  # Delay between each character

            if period_count == 2:
                print(f"Pausing for {period_pause} seconds after two periods...")
                progress_bar(period_pause)  # Use the progress_bar function
                period_count = 0  # Reset the period count after pausing
        elif char == "\n":
            pyautogui.hotkey("shift", "enter")  # Simulate a new line
        else:
            pyautogui.typewrite(char, interval=delay)  # No pause for non-period characters

    print("Text typing complete.")

def progress_bar(duration):
    for i in range(duration):
        progress = "=" * i + "-" * (duration - i)
        print(f"\r[{progress}] {i+1}/{duration} seconds", end="")
        time.sleep(1)
    print("\n")

def main():
    print("Text Typer Program")
    print()

    user_input = input("Enter the text you want to type: ")
    initial_delay_input = input("Enter the initial delay in seconds (default is 10): ")
    cpm_input = input("Enter the desired typing speed in CPM (default is 900): ")

    try:
        initial_delay = int(initial_delay_input)
    except ValueError:
        print("Invalid initial delay value. Using the default delay of 10 seconds.")
        initial_delay = 10

    try:
        cpm = int(cpm_input)
    except ValueError:
        print("Invalid CPM value. Using the default speed of 900 CPM.")
        cpm = 900

    type_text(user_input, initial_delay, cpm)

if __name__ == "__main__":
    main()
