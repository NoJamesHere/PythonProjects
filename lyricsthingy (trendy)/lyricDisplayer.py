import time
import sys

ORANGE = "\033[38;2;255;165;0m"  # RGB for orange
YELLOW = "\033[93m"
RESET = "\033[0m"

lyricswithtimes_rockthatbody = [
    ["I wanna da-", 0.5, YELLOW],
    ["I wanna dance in the lights", 1.5, YELLOW],
    ["I wanna rock-", 0.3, YELLOW],
    ["I wanna rock your body", 1.5, YELLOW],
    ["I wanna go,", 0.4, YELLOW],
    ["I wanna go for a ride", 1.5, YELLOW],
    ["Hop in the music", 0.3, YELLOW],
    ["and rock your body right", 1.0, YELLOW],
    ["Rock that body,", 0.5, YELLOW],
    ["Come on, come on", 0.3, YELLOW],
    ["Rock that body", 0.3, YELLOW],
    ["(rock your body)", 0.2, ORANGE],
     ["Rock that body,", 0.5, YELLOW],
    ["Come on, come on", 0.1, YELLOW],
    ["Rock that body", 0.8, YELLOW],
    ["Rock that body,", 0.5, YELLOW],
    ["Come on, come on", 0.3, YELLOW],
    ["Rock that body", 0.3, YELLOW],
    ["(rock your body)", 0.2, ORANGE],]

lyricswithtimes_iloveyou = [
    ["Hmm~, Hmm~", 0.5, YELLOW],
    ["Maybe won't you take it back?", 0.6, YELLOW],
    ["Say you were tryna make me laugh", 0.8, YELLOW],
    ["And nothing has to change today", 0.4, YELLOW],
    ["You didn't mean to say 'I love you'", 6.5, ORANGE],
    ["I love you..", 4.8, ORANGE],
    ["and I don't want to", 6.0, ORANGE],
    ["Ooooh~", 8.0, YELLOW]
    ]

inputted = input("Press Enter the following to start the lyrics animation... (iloveyou, rockthatbody): ").lower()
currentlyrics = []
if(inputted == "iloveyou"):
    currentlyrics = lyricswithtimes_iloveyou
    print("Timestamp: 2:54")
    speed = 0.09
elif(inputted == "rockthatbody"):
    currentlyrics = lyricswithtimes_rockthatbody
    speed = 0.05

for lyric, delay, color, in currentlyrics:
    for char in lyric:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        
        time.sleep(speed)
    print()
    time.sleep(delay)