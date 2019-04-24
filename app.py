#!/usr/bin/python

# Goal: to raise an alarm if a specified process is utilizing too much of your
#       resources.

import time
import psutil
import argparse


# setting up arguments for the tool
parser = argparse.ArgumentParser(description='Tool to help you detect spikes \
  in CPU usage')
parser.add_argument('-n', dest='NAME', help='Specifies the name of the type \
  of process to be watched eg. Google Chrome, Safari etc.', 
  default='Google Chrome')
parser.add_argument('-l', dest='LIMIT', help='Specifies the CPU percentage \
  you want to limit this process to', default=200)
args = parser.parse_args()

DONE, INTERVAL, PREV = False, 1.25, 0
args.NAME = str(args.NAME)
args.LIMIT = int(args.LIMIT)

print("Starting up Spike Detector...")
while not DONE:
  # locate and check all processes linked with current process
  ps = [proc.cpu_percent() < args.LIMIT for proc in psutil.process_iter() 
          if args.NAME in proc.name()]
  if ps:
    # all should be within limit within 100 * INTERVAL, otherwise fresh vector is detected
    if not all(ps) and PREV < 100 * INTERVAL: 
      PREV = 100 * INTERVAL
      print('ALERT! %(N)s is going over %(L)d percent CPU usage!' % {"N": args.NAME, "L": args.LIMIT})
    else: 
      PREV = 0 if PREV <= 0 else PREV - 1
      time.sleep(INTERVAL)
  else:
    DONE = True
print("Thank you for using Spike Detector!")