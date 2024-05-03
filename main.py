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
orangeLaps = 0
purpleLaps = 0

def onevent_bumper_a_released_0():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, orangeLaps, purpleLaps, vexcode_brain_precision, vexcode_console_precision
    optical_11.set_light_power(0, PERCENT)
    # Laps are set to 0
    redLaps = 0
    blueLaps = 0
    greenLaps = 0
    yellowLaps = 0
    PLACE = 1
    while True:
        if optical_11.color() == Color.GREEN:
            greenLaps = greenLaps + 1
        if optical_11.color() == Color.BLUE:
            blueLaps = blueLaps + 1
        if optical_11.color() == Color.RED:
            redLaps = redLaps + 1
        # Ranking System, Changes who is displayed by color
        if greenLaps == 4:
            brain.screen.set_cursor(3 + PLACE, 1)
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("GREEN")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(" Seconds")
            brain.screen.next_row()
            brain.screen.set_cursor(3, 1)
            PLACE = PLACE + 1
        if blueLaps == 4:
            brain.screen.set_cursor(3 + PLACE, 1)
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("BLUE")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(" Seconds")
            brain.screen.next_row()
            brain.screen.set_cursor(3, 1)
            PLACE = PLACE + 1
        if redLaps == 4:
            brain.screen.set_cursor(3 + PLACE, 1)
            brain.screen.print(PLACE, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(")")
            brain.screen.print("RED")
            brain.screen.print("    TIME: ")
            brain.screen.print(brain.timer.time(SECONDS), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.print(" Seconds")
            brain.screen.next_row()
            brain.screen.set_cursor(3, 1)
            PLACE = PLACE + 1
        wait(5, MSEC)

def onevent_bumper_a_released_1():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, orangeLaps, purpleLaps, vexcode_brain_precision, vexcode_console_precision
    # When Bumper Switch is Released, the Race Starts and the Timer starts
    brain.screen.print("GO!!")
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
        wait(5, MSEC)

def when_started1():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, orangeLaps, purpleLaps, vexcode_brain_precision, vexcode_console_precision
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(0, 0, 1000, 1000)
    brain.screen.set_font(FontType.MONO30)
    brain.screen.print("    {WELCOME TO THE OLYMPICS}")
    brain.screen.set_cursor(5, 1)
    brain.screen.set_font(FontType.MONO20)
    brain.screen.print("    (Press and Hold The Button to Start!) ")
    brain.screen.next_row()
    brain.screen.print("    (Release When You Are Ready!)")
    # Bumper Switch needs to Be Pressed to Start the Race
    while not bumper_a.pressing():
        wait(5, MSEC)

def onevent_bumper_a_pressed_0():
    global message1, RunnersStepUp, myVariable, fastest, purpleColor, redColor, orangeColor, redLaps, blueLaps, greenLaps, yellowLaps, PLACE, orangeLaps, purpleLaps, vexcode_brain_precision, vexcode_console_precision
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.draw_rectangle(0, 0, 10000, 1000)
    # Runners line up before it is released
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Runners Step Up To The Line")
    brain.screen.next_row()

# system event handlers
bumper_a.released(onevent_bumper_a_released_0)
bumper_a.released(onevent_bumper_a_released_1)
bumper_a.pressed(onevent_bumper_a_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
