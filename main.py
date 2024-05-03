#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
optical_11 = Optical(Ports.PORT11)
bumper_a = Bumper(brain.three_wire_port.a)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration



vexcode_brain_precision = 0
vexcode_console_precision = 0
message1 = Event()
RunnersStepUp = Event()
myVariable = 0
fastest = 0
purpleColor = 0
redColor = 0
orangeColor = 0
redLaps = 0
blueLaps = 0
greenLaps = 0
yellowLaps = 0
PLACE = 0

def when_started1():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, vexcode_brain_precision, vexcode_console_precision
#The Race isn't ready to start until the switch is pressed as a means of control
    while not bumper_a.pressing():
        wait(5, MSEC)
        brain.screen.set_font(FontType.MONO40)
        brain.screen.print("    {WELCOME TO THE OLYMPICS}")
        brain.screen.set_font(FontType.MONO20)
        brain.screen.print("    [press the bumper switch to START]")







def onevent_bumper_a_pressed_0():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, vexcode_brain_precision, vexcode_console_precision
#The switch being pressed triggers the message of having runners step up to the line
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Runners Step Up To The Line")
    brain.screen.next_row()

def onevent_bumper_a_released_0():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, vexcode_brain_precision, vexcode_console_precision
#When the Bumper Switch is released, the race starts, and the time begins
    brain.screen.print("GO!!")
    brain.screen.next_row()
    brain.timer.clear()
    brain.screen.set_cursor(3, 1)
    brain.screen.clear_row(3)
    brain.screen.set_cursor(brain.screen.row(), 1)
    while True:
        brain.screen.clear_row(3)
        brain.screen.set_cursor(brain.screen.row(), 1)
        brain.screen.print("Time: ")
        brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.print(" Seconds")
        brain.screen.next_row()
        wait(5, MSEC)

def onevent_bumper_a_released_1():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, vexcode_brain_precision, vexcode_console_precision
#When the Bumper Switch is released, the race has started, and it will keep going until all colors have finished
    redLaps = 0
    blueLaps = 0
    greenLaps = 0
    yellowLaps = 0
    while True:
    # Uses the optical sensor to detect the color of the runner.
        while not optical_11.is_near_object():
            wait(5, MSEC)
        if optical_11.color() == Color.RED:
            redLaps = redLaps + 1
        if optical_11.color() == Color.GREEN:
            greenLaps = greenLaps + 1
        if optical_11.color() == Color.BLUE:
            blueLaps = blueLaps + 1
        if optical_11.color() == Color.YELLOW:
            yellowLaps = yellowLaps + 1
        if greenLaps == 4:
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("GREEN")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.next_row()
            PLACE = PLACE + 1
        if redColor == 4:
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("RED")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.next_row()
            PLACE = PLACE + 1
        if blueLaps == 4:
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("BLUE")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.next_row()
            PLACE = PLACE + 1
        if yellowLaps == 4:
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("RED")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.next_row()
            PLACE = PLACE + 1
        wait(5, MSEC)

# system event handlers
bumper_a.pressed(onevent_bumper_a_pressed_0)
bumper_a.released(onevent_bumper_a_released_0)
bumper_a.released(onevent_bumper_a_released_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
