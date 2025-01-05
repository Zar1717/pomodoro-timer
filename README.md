# Pomodoro Timer

## Description
This is a Python implementation of the Pomodoro Timer, a productivity tool based on the Pomodoro Technique. It helps users stay focused by alternating between work sessions and short or long breaks.

## Features
- Work and break intervals:
  - Default work session: 25 minutes.
  - Short break: 5 minutes.
  - Long break: 15 minutes.
- Countdown timer with a visual tomato graphic.
- Automatically switches between work and break sessions.
- Displays checkmarks to track completed work intervals.
- Reset functionality to restart the timer at any time.

## How to Use
1. Run the `main.py` file in your terminal or Python IDE.
2. Press the **Start** button to begin a work session.
3. The timer will alternate between work and break sessions automatically.
4. Use the **Reset** button to restart the timer at any point.

## Requirements
- Python 3.7 or higher
- Required Libraries:
  - tkinter
  - math
- Ensure the `tomato.png` image is in the same directory as the `main.py` file.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Zar1717/pomodoro-timer.git
2. Navigate to the project folder:
   ```bash
   cd pomodoro-timer
3. Run the program:
   ```bash
   python main.py



Notes:

- The default time intervals can be modified in the main.py file by changing the values of WORK_MIN, SHORT_BREAK_MIN, and LONG_BREAK_MIN.
- Ensure the tomato.png file is in the same folder for the visual element to display properly.

Future Improvements:

- Add a settings menu to customize session durations without editing the code.
- Include audio notifications for session transitions.
- Create a graphical progress tracker for completed Pomodoro cycles.


