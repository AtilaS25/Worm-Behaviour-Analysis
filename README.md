# Worm-Behaviour-Analysis

This code was made as a demonstartion to how a worm can infect a network.
This demo is to give an example of the transfer process and persistance that a worm might have.
For this to work a couple things must be done before hand in preperation.
I recommand having Wireshark open on one of the machines to better see how the machines interarct with eachother.


Preperations:
Paramiko library must be installed.
This code is made to infect Kali Linux Machines whose usernames & passwords are left at the default "Kali"
All machines must be in same network.
Tarket machines must have port 22 placed in listening mode.
Port 22 must be opened in listening mode on target machines prior to running script.
Python script should be placed inside of a folder named "RickyFiles" on desktop. (I picked a Desktop location so that the transfer of files is better visualized)
