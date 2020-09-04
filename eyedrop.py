#!/usr/bin/python

import os
import time

iterations = 6
duration = 10 * 60

counter = 1
while counter <= iterations:
    command = 'notify-send "{0} {1}" && paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'.format("It's time for drop", str(counter))
    os.system(command)

    counter += 1
    time.sleep(duration)
