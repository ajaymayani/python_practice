from pygame import mixer
from time import time
from datetime import datetime

def alarm(file,str):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        userInput = input()

        if userInput==str:
            mixer.music.stop()
            break

def log(msg):
    with open("activitylogs.txt","a") as f:
        f.write(f"{msg} at {datetime.now()}\n")

def getTime():
    return datetime.datetime.now();


if __name__ == '__main__':
    init_water = time()
    init_exercise = time()
    init_eyes = time()

    water_time = 30 * 60
    exercise_time = 45 * 60
    eye_time = 35 * 60

    while True:
        if time() - init_water > water_time:
            print("Water drinking time. Enter drank to stop the alarm")
            alarm("water.mp3","drank")
            log("Drank water at ")
            ini_water = time()

        if time() - init_exercise > exercise_time:
            print("Physical activity time. Enter done to stop the alarm")
            alarm("exercise.mp3","done")
            log("Physical Activity done at ")
            ini_exercise = time()

        if time() - init_eyes > eye_time:
            print("Eye exercise time. Enter done to stop the alarm")
            alarm("eye.mp3","done")
            log("Eye exercise done at ")
            ini_eyes = time()
