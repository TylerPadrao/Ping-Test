#! /usr/bin/python3
# Script 1
# Tyler Padrao
# September 17th, 2021

# Imports
import sys
import netifaces
import os
import subprocess
import time
import socket

# Function for testing connectivity to your gateway
def gateway_connect() :
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Print statement to inform user
	print("Testing connectivity to your gateway...\n")
	# Get the IP from the system
	ip_addr = netifaces.gateways()['default'][netifaces.AF_INET][0]
	# Ping the gateway IP to test for connectivity
	response = subprocess.Popen(["ping", ip_addr, "-c", "4"], stdout=subprocess.DEVNULL)
	response.wait()
	# Check if response is equal to zero (if it is, its a successful ping)
	if response.poll() == 0:
		# Print statement to inform user
		print("Please inform your system administrator that the test was SUCCESSFUL!")
	else:
		# Print statement to inform user
		print("Please inform your system administrator that the test has FAILED!")
	# Wait 3.5 seconds before going back to menu
	time.sleep(3.5)
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')

# Function for testing remote connectivity
def remote_connect() :
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Ip address for tetsing remote connectivity
	ip_addr = '129.21.3.17'
	# Print statement to inform user
	print("Testing for remote connectivity... trying ip address " + ip_addr + ".\n")
	# Ping the remote IP (RIT's DNS) to test for connectivity
	response = subprocess.Popen(["ping", ip_addr, "-c", "4"], stdout=subprocess.DEVNULL)
	response.wait()
	# Check if response is equal to zero (if it is, its a successful ping)
	if response.poll() == 0:
		# Print statement to inform user
		print("Please inform your system administrator that the test was SUCCESSFUL!")
	else:
		# Print statement to inform user
		print("Please inform your system administrator that the test has FAILED!")
	# Wait 3.5 seconds before going back to menu
	time.sleep(3.5)
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')

# Function for testing DNS resolution
def dns_resolution() :
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Google URL
	url = 'www.google.com'
	# Print statement to inform user
	print("Resolving DNS: trying URL... " + url + ".\n")
	# Ping google's URL to test for DNS resolution
	response = subprocess.Popen(["ping", url, "-c", "4"], stdout=subprocess.DEVNULL)
	response.wait()
	# Check if response is equal to zero (if it is, its a successful ping)
	if response.poll() == 0:
		# Print statement to inform user
		print("Please inform your system administrator that the test was SUCCESSFUL!")
	else:
		# Print statement to inform user
		print("Please inform your system administrator that the test has FAILED!")
	# Wait 3.5 seconds before going back to menu
	time.sleep(3.5)
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')

# Function for displaying the gateway IP address
def gateway_ip() :
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Grab gateway IP from the system
	#gatewayIP = subprocess.check_output("ip route | grep default | awk '{print $3}'", shell=True)
	# Obtain gateway IP from system
	gatewayIP = netifaces.gateways()['default'][netifaces.AF_INET][0]
	# Print statement to inform user
	print("Your gateway IP address is " + gatewayIP + ".")
	# Wait 3.5 seconds before going back to menu
	time.sleep(3.5)
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')

# Set flag to true for loop
flag = True

# While True
while flag == True:
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# User interface for program
	print("\nPing Test Troubleshooter\n")
	print("Enter Selection:\n")
	print("\t1 - Test connectivity to your gateway.")
	print("\t2 - Test for remote connectivity.")
	print("\t3 - Test for DNS resolution.")
	print("\t4 - Display gateway IP Address.\n")
	# Grab user's input
	choice = input("Please enter a number (1-4) or 'Q/q' to quit the program: ")
	# If choice is 1, test gateway connectivity
	if choice == "1":
		gateway_connect()
		flag = True
	# If choice is 2, test remote connectivity
	elif choice == "2":
		remote_connect()
		flag = True
	# If choice is 3, test DNS resolution
	elif choice == "3":
		dns_resolution()
		flag = True
	# If choice is 4, display gateway IP
	elif choice == "4":
		gateway_ip()
		flag = True
	# If choice is Q or q, quit program
	elif choice == "Q" or choice == "q":
		# Clear window
		os.system('cls' if os.name == 'nt' else 'clear')
		# Inform user
		print("Quitting program: returning to shell.\n\nHave a wonderful day!")
		# Wait 3.5 seconds before going back to menu
		time.sleep(3.5)
		# Clear window
		os.system('cls' if os.name == 'nt' else 'clear')
		# Exit script
		sys.exit()
	# If user did not select one of the valid options, they have to reselect
	else:
		# Inform user
		print("\nYou entered an invalid option!\n\nPlease enter a number between 1 through 4")
		# Wait 3.5 seconds before going back to menu
		time.sleep(3.5)
		# Clear window
		os.system('cls' if os.name == 'nt' else 'clear')
		


	

