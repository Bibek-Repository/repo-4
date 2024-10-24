from datetime import datetime
from playsound import playsound


# Taking the alarm time and extracting the time from the input data

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]   # extracting hour by using string slicing
alarm_minute = alarm_time[3:5] # extracting minute by using string slicing
alarm_seconds = alarm_time[6:8]   # extracting second by using string slicing
alarm_period = alarm_time[9:11].upper()   # extracting period by using string slicing. upper() converts it to uppercase
print("Setting up alarm..")

# Matching the time with current time

while True:   # Infinite loop: It will continuously check the current time using a while loop
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound(r'C:\Users\Bibekster\pythonproject\alarmclockproject\dark-engine-logo-141942.mp3')
                    break