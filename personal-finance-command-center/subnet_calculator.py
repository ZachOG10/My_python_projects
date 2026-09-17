"""THIS IS MY SECOND PROJECT, A SUBNET CALCULATOR"""
## This block of code requests an IP and a Mask address from the user.

ip = input("Enter an IP address: ")
subnet_mask = input("Enter a subnet mask: ")

### This block breaks the IP into 4 parts
ip_parts = ip.split(".")
## This block converts each part of ip from text to number
ip_1 = int(ip_parts[0])
ip_2 = int(ip_parts[1])
ip_3 = int(ip_parts[2])
ip_4 = int(ip_parts[3])

## This block breaks the subnet_mask into 4 parts
mask_parts = subnet_mask.split(".")
## This block converts each part of subnet_mask from a text to number 
mask_1 = int(subnet_parts[0])
mask_2 = int(subnet_parts[1])
mask_3 = int(subnet_parts[2])
mask_4 = int(subnet_parts[3])

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
broadcast_address = f"{broadcast_1}.{broadcast_2}.{broadcast_3}.{broadcast_4}" 

