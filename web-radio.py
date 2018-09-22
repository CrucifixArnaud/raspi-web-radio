from gpiozero import Button, LED
from subprocess import check_call
from signal import pause

# Button Play
button_play = Button(3)

# Led 
led_power = LED(18)

# Rotary Switch Button State
button_radio_1 = Button(21)
button_radio_2 = Button(20)
button_radio_3 = Button(26)
button_radio_4 = Button(16)
button_radio_5 = Button(19)
button_radio_6 = Button(13)
button_radio_7 = Button(12)
button_radio_8 = Button(6)
button_radio_9 = Button(5)
button_radio_10 = Button(25)
button_radio_11 = Button(24)
button_radio_12 = Button(23)

# Variables
radio = 1
started = False

# Methods
def init():
    load_last_radio()

def start_radio():
    global started   
    
    print("started radio")
    
    led_power.on()
    
    started = True
    play_radio()

def load_last_radio():
    global radio
    
    last_radio_file  = open("last-radio", "r")
    last_radio = last_radio_file.read(2)
    
    if last_radio:
        print("Last opened radio:", last_radio)
        radio = int(last_radio)

def save_current_radio():
    global radio
    
    last_radio_file = open("last-radio", "w")
    last_radio_file.write(str(radio))
    print("Save current radio", radio)
    
    last_radio_file.close()

def play_radio():
    print("Launch radio")
    check_call(['mpc', 'play', str(radio)])
    
def stop_radio():
    led_power.off()
    
    print("Stop radio")
    check_call(['mpc', 'stop'])

def select_radio(val):
    global radio
    
    print("Select radio",val)
    
    radio = val
    
    save_current_radio()
    
    print("Started", started)
    
    if started == True:
        #stop_radio()
        play_radio()

def select_radio1():
    select_radio(1)

def select_radio2():
    select_radio(2)

def select_radio3():
    select_radio(3)

def select_radio4():
    select_radio(4)

def select_radio5():
    select_radio(5)
    
def select_radio6():
    select_radio(6)
    
def select_radio7():
    select_radio(7)
    
def select_radio8():
    select_radio(8)
    
def select_radio9():
    select_radio(9)

def select_radio10():
    select_radio(10)

def select_radio11():
    select_radio(11)

def select_radio12():
    select_radio(12)

# On Opening
init()

# Bind method for play button
button_play.when_held = start_radio
button_play.when_released = stop_radio

# Bind method to rotary switch
button_radio_1.when_held = select_radio1
button_radio_2.when_held = select_radio2
button_radio_3.when_held = select_radio3
button_radio_4.when_held = select_radio4
button_radio_5.when_held = select_radio5
button_radio_6.when_held = select_radio6
button_radio_7.when_held = select_radio7
button_radio_8.when_held = select_radio8
button_radio_9.when_held = select_radio9
button_radio_10.when_held = select_radio10
button_radio_11.when_held = select_radio11
button_radio_12.when_held = select_radio12

pause()
