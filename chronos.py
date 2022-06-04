#!/usr/bin/env python3
import os
import time
from os.path import expanduser

default_user = 'tihonasiy'
default_time = '7200'
current_date_f = expanduser('~') + '/chronos/current_date.txt'
remaining_time_f = expanduser('~') + '/chronos/remaining_time.txt'

with open(current_date_f, encoding='utf-8') as f: # read last date from file
                                                      # to compare it with current one                                               
    last_date =  f.readline()
    last_date = last_date.strip()
    last_date  = last_date.split(' ')
    last_date = [int(elem) for elem in last_date] # create list of year, mounth and day elements as integers



current_date = time.struct_time(time.localtime(time.time())) # get current date 



if last_date[0] == current_date[0] and last_date[1] == current_date[1] and last_date[2] == current_date[2]:   #check if last saved date is todays date
    

    with open(remaining_time_f, encoding='utf-8') as f: # read remaining time from file
                                                            # to count it down
        remaining_time = int(f.readline())

        
    while (remaining_time) > 0:   # run time counter and write its values into file on each iteration

        with open(remaining_time_f, mode='w',  encoding='utf-8') as f:   
        
            remaining_time -= 1
            
            f.write(str(remaining_time))

            f.flush()

            time.sleep(1)
    
    os.system('pkill -KILL -u {0}'.format(default_user))

else:

    with open(current_date_f, mode='w', encoding='utf-8') as f:  # update current date in current_date.txt

        for i in range(0, 3, 1):

            f.write(str(current_date[i]) + ' ')

    with open(remaining_time_f, mode='w',  encoding='utf-8') as f:  # update play time for new day 
        
        f.write(str(default_time))

    with open(remaining_time_f, encoding='utf-8') as f: # read remaining time from file
                                                            # to count it down
        remaining_time = int(f.readline())    
    
    while (remaining_time) > 0:   # run time counter and write its values into file on each iteration

        with open(remaining_time_f, mode='w',  encoding='utf-8') as f:   
        
            remaining_time -= 1
            
            f.write(str(remaining_time))

            f.flush()

            time.sleep(1)

    os.system('pkill -KILL -u {0}'.format(default_user))
