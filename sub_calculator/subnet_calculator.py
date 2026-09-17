"""THIS IS MY SECOND PROJECT, A SUBNET CALCULATOR"""
"""It Takes an IP address and subnet mask as input, and print the network address,
broadcast address, and usable host range."""
## This block of code requests an IP and a Mask address from the user.
ip = input("Enter an IP address: ")
subnet_mask = input("Enter a subnet mask: ")

### This block breaks the IP into 4 parts
ip_parts = ip.split(".")
if len(ip_parts) != 4:
    print("Error: ip address must have exactly 4 parts separated by dots.")
    exit()
for ip_part in ip_parts:
    if not ip_part.isdigit():
        print("Error: ip address must contain only numbers.")
        exit()  
## This block converts each part of ip from text to number
ip_1 = int(ip_parts[0])
ip_2 = int(ip_parts[1])
ip_3 = int(ip_parts[2])
ip_4 = int(ip_parts[3])

## This block breaks the subnet_mask into 4 parts
mask_parts = subnet_mask.split(".")
if len(mask_parts) != 4:
    print("Error: subnet mask must have exactly 4 parts separated by dots.")
    exit()
for mask_part in mask_parts:
    if not mask_part.isdigit():
        print("Error: subnet mask must contain only numbers.")
        exit()  
## This block converts each part of subnet_mask from a text to number 
mask_1 = int(mask_parts[0])
mask_2 = int(mask_parts[1])
mask_3 = int(mask_parts[2])
mask_4 = int(mask_parts[3]) 

## The following blocks of code calculates the network address
## Network address = ip AND mask
network_1 = ip_1 & mask_1 
network_2 = ip_2 & mask_2
network_3 = ip_3 & mask_3
network_4 = ip_4 & mask_4

## The following blocks of code calculates the broadcast address
## Broadacast address = Network address OR (NOT Mask) 
## (NOT mask) flips every bit of the mask, so we use the wildcard trick
wildcard_1 = 255 - mask_1
wildcard_2 = 255 - mask_2
wildcard_3 = 255 - mask_3
wildcard_4 = 255 - mask_4

broadcast_1 = network_1 | wildcard_1
broadcast_2 = network_2 | wildcard_2
broadcast_3 = network_3 | wildcard_3
broadcast_4 = network_4 | wildcard_4

## This block calculates the first and last usable host
## First usable host = network address +1 (in the last octet)
## Last usable host = network address -1 (in the last octet)
first_host4 = network_4 + 1
last_host4 = broadcast_4 - 1

## This blocks of code puts the numbers back to text by joining all networks together
## and join the broadcasts together too.
network_address = f"{network_1}.{network_2}.{network_3}.{network_4}"
broadcast_address = f"{broadcast_1}.{broadcast_2}.{broadcast_3}.{broadcast_4}"
first_usable_host = f"{network_1}.{network_2}.{network_3}.{first_host4}"
last_usable_host = f"{network_1}.{network_2}.{network_3}.{last_host4}"

### The final result is displayed here.
print("Network Address: " + network_address)
print("Broadcast Address: " + broadcast_address)
print("First Usable Host: " + first_usable_host)
print("Last Usable Host: " + last_usable_host) 
