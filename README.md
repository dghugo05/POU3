# POU3

##Description
POU3 is a program designed like a challenge to the user and a advanced use of python to learn to structure and managing terminals and hardware from python for new developers. ==This program should not be used with malicious intentions==.

##Structure Planning
I am presenting the main outline of the program, which has not yet been fully developed:

The program consists of 6 challenges with their punishments and 2 breaks:

Random Key: A random number between 1 and 30 is created, and the user needs to input the correct key.

Punishment: Every time the user fails, a random image or video from the ``Dependencias`` directory pops up on the screen.

Equation: For the second challenge the user needs to solve a random equation.

Punishment: When the user fails, the program will consume memory until the device ceases to function.

Break: There's no punishment in this round, just a little break of 24 hours.

Tic Tac Toe: In this challenge, the user needs to win a game against the program 3 times.

Punishment: If the user fails and the program wins 3 times, the program will disable the screen drivers.

Hangman: The user needs to guess a random word by inputting letters.

Punishment: ``Empty``

Break: Another break starts, and the program won't do anything for 72 hours.

File Search: A random file will be located in a random path on the device, and the user will need to find it.

Punishment: Every 5 minutes that pass on an internal timer, the program will consume 5% of the device's resources.

``Empty``

Punishment: If the user fails, the Bonzi Buddy malware will be installed on the device.

Extra Challenge:

If the user tries to delete the program, a copy located in another path will initiate a secret challenge.

A Minesweeper game the size of the whole screen will start running, and the user only has 1 move to point to where a mine is.

Punishment: Every time the user fails, a random number from 1 to 6 will be generated. If the number matches a specific condition, the program will delete the ``System32`` directory—effectively a Russian roulette for the device.

##Download
You can download the directory build for the ``.exe`` program or the remaining files to see, edit and run the code by terminal.

##Executable
When you download the directory build, you only need to enter the directories till you see the executable file, the dependencies are integrated in the lib directiory, there's all the modules needed for the correct work of the programm.

##``.py`` file and ``Dependecias`` directory
If you download the program by the ``.py`` file and the ``Dependencias`` directory you need to be aware about the next sections of the ``README`` to be able to run it.

  ###Dependencies
  Ensure you have the following Python libraries installed:

  opencv-python for handling images and videos.
  pygame for audio playback.
  moviepy for video file manipulation.
  threading for managing timers.



  You can install these libraries using pip in terminal:
  pip install opencv-python pygame moviepy
  
  
  ###File Structure
  The script relies on the following directory structure:
  
  /path_to_script
  │
  ├── Dependencias
  │   ├── importaciones.py   # File with necessary imports
  │   ├── multimedia          # Folder containing multimedia files
  │   ├── copy.ps1           # PowerShell script to be executed
  │   ├── Lista.txt          # Text file with a list of items
  │   └── Lista_negra.txt    # Text file with a blacklist of items
  

  ###Usage
  Download the CopiaPou3.py file and place it in a directory of your choice, ensuring that the above file structure is present.
  Open a terminal and navigate to the directory containing CopiaPou3.py.
  Run the script using the following command:
  
  python CopiaPou3.py
  
  The script will begin running, displaying images or playing random videos from the multimedia folder.
  You will be prompted to enter a numeric key between 1 and 30. The script allows a limited number of attempts to correctly guess a randomly generated number.
  
  
  ###Main Functions
  
  num_atleatorio(): Generates a random number between 1 and 30.
  temporizador(): Initiates a timer that calls the abrir function every 15 seconds.
  copiar(): Executes a PowerShell script.
  abrir(): Selects a random multimedia file and displays or plays it.
  resultado(): Manages the guessing logic for the access key.
  
  ###Additional Notes
  
  Ensure that the multimedia files in the multimedia folder are of the appropriate types (image formats: .jpg, .png, and video format: .mp4).
  Contributions
  If you would like to contribute or improve the script, please feel free to do so. Any enhancements are welcomed.

