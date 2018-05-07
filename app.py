#!/usr/bin/python

# Goal: to raise an alarm if a specified process is utilizing too much of your
#       resources.

import psutil
import argparse


# setting up arguments for the tool
parser = argparse.ArgumentParser('Tool to help you detect spikes in CPU usage')
parser.add_argument('-n', dest='NAME', help='Specifies the name of the type \
  of process to be watched eg. Google Chrome, Safari etc.', default='Google \
  Chrome')
parser.add_argument('-l', dest='LIMIT', help='Specifies the CPU% you want\
   to limit this process to', default=50)
args = parser.parse_args()

DONE = False

try:
  while not DONE:
    # locate and check all processes linked with current process
    ps = [proc.cpu_percent() < args.LIMIT for proc in psutil.process_iter() 
            if args.NAME in proc.name()]
    if ps:
      if not all(ps): # all should be within limit
        print "ALERT! {} is going over {}% CPU usage!".format(args.NAME, 
                                                              args.LIMIT) 
    else:
      DONE = True
except:
  print "Error occured while parsing your arguments - are you sure the target \
    process is running?"