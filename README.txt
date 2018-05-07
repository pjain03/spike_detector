This is a utility to raise an alert if a particular process's CPU usage is
too high. Built with cryptojacking in mind, given an argument specifying which
browser you're using, this utility raises an alarm if it uses up more than
a specified amount of your CPUs power at which you may verify the state of 
your computer. 

To avoid cryptojacking please look into the following tools:-
1. NoCoin: a simplistic extension that verifies your web browsing against a 
           blacklist.
2. MinerBlock: a more sophisticated tool that blocks any proxy chains/inlined
           JS being used to cryptojack via browser.

This utility is the final line of defense after which you need to confirm the
status of your computer yourself. Cryptojackers are forever changing their
tactics but the one thing that can stop them is if you're aware of how your
computer is being used - this utility helps you in that goal!

Software used: 
Python 2.7.13
pip 10.0.1

Some useful commands:
pip install -r requirements.txt
python app.py -h