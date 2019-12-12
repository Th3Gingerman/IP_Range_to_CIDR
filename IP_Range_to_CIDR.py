#!/Program Files/Python38/python3
# 2019 Zachary Gorby - v1.2 #

import ipaddress 
import csv 

IP_File = open('IP_Ranges.txt') #Input filename, CSV of firstip,lastip
IP_FileReader = csv.reader(IP_File) 
IP_Data = list(IP_FileReader) 
output_filename = 'Output_CIDRs.txt' 
output_file = open(output_filename,'w')

print(IP_Data) #Here for checks and troubleshooting

for row in IP_Data:
    Start_IP = row[0]
    End_IP = row[1]
    Start_IP = ipaddress.ip_address(Start_IP) 
    End_IP = ipaddress.ip_address(End_IP)
    CIDR = list(ipaddress.summarize_address_range(Start_IP, End_IP))
    CIDR = str(CIDR) 
    CIDR_Only = CIDR.split('\'')[1].strip() 
	#You can use either or both of the following output methods
    print(CIDR_Only) 
    print ((CIDR_Only), file=output_file)
	
