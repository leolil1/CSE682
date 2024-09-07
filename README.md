# CSE682

## CSE682 Software Engineering Course Project
Weather information plays a major role in our daily decision-making and event planning. Knowing the weather information, we can better prepare for our daily activities and ensure safety as well. To address these needs, we are developing a Python program that aims to provide users with real-time weather conditions and forecasts. The program will have an easy-to-use interface and clear data display that provides quick weather information updates to the user. 

The weather information our program will provide includes weather conditions, temperature, and supports up to 7-day forecasts with daily high and low temperatures. It’ll also provide users with the ability to search for weather information for locations nationwide. This document will outline the user and system requirements detailing all the features mentioned above of the program.


## Dev Environment Setup:
1) Create a Python virtual environment<br />
_$python -m venv GiveItAName_

2) Clone git repo

3) Activate the Python virtual environment<br />
_$cd GiveItAName/Scripts_<br />
_$activate_

4) Install libraries/dependencies via requirements.txt<br />
_(GiveItAName) $cd CSE682_<br />
_(GiveItAName) $pip -r install requirements.txt_ 



## Run The Python Program:
(Make sure you are executing the main.py from the project root directory. Meaning, run the program from CSE682/. This will prevent many of the local file access errors. This will not be an issue anymore once we move away from text file for data keeping to an actual database or to the cloud.)

_$python main.py_



## Run The Python Unit Test:
(Under development...)

_(GiveItAName)$pytest whatever_test.py_
