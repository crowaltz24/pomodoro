# Pomodoro Timer

Small pomodoro timer project for my dad.
Flashes the screen red and plays a little melody when a phase ends.

### Prerequisites
[Python](https://www.python.org/downloads/) installed on system.

### How to use
- Download all the files, and place them in a folder together.
- Run `pomodoro.bat` to start the timer!
- Edit the `config.json` file (in notepad) to change durations/order of the phases, or to enable/disable screen flash and sound. Restart after editing.

### Notes
If you want the script to run on startup:
- Press Win + R, type shell:startup, and press Enter. This opens the Startup folder.
- Right click on `pomodoro.bat` and create a shortcut.
- Move the shortcut to the Startup folder.
- Verify by restarting the system! Any changes made to `config.json` will take effect on next startup.

If you don't want the console window with the countdown to remain open:
- Right click `pomodoro.bat` and open in Notepad.
- Remove `pause` command from the last line.
