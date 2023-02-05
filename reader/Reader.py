from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
import time
from colorama import Fore

def process_pcap(file_name):
    print('Opening {}...'.format(file_name))

    count = 0
    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1

    print('{} contains {} packets'.format(file_name, count))

def filterTCP(file_name):
    print('Opening {}...'.format(file_name))

    count = 0
    interesting_packet_count = 0
    
    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        if("Firefox" in str(pkt_data)):
            print(pkt_data)
        count += 1
        
        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields:
            # LLC frames will have 'len' instead of 'type'.
            # We disregard those
            continue

        if ether_pkt.type != 0x0800:
            # disregard non-IPv4 packets
            continue

        ip_pkt = ether_pkt[IP]
        if ip_pkt.proto != 6:
            # Ignore non-TCP packet
            continue

        interesting_packet_count += 1

    print('{} contains {} packets ({} interesting)'.
          format(file_name, count, interesting_packet_count))

def filterData(filter, file_name):
        for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
            try:
                if(str(filter) in str(pkt_data)):
                    print(Fore.GREEN + "\n \tSTRING FOUND MATCHING " + Fore.BLUE + filter + Fore.RESET + "\n")
                    time.sleep(2)
                    print(pkt_data)
                # else:
                #     print(Fore.RED + "\n \tNO DATA FOUND FROM QUERY\n"+ Fore.RESET+ "\n")
                   
            except:
                print(Fore.RED + "\n \tNO DATA FOUND FROM QUERY\n"+ Fore.RESET+ "\n")
def init():
    print("\n\n" + Fore.RED + "\t\nSTARTING PCAP DEFENDER... \n\n "+ Fore.RED+ "\n")
# init()
# filterData("dummydqhiuqhd@", "NTLM-wenchao.pcap")


