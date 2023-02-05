# PcapDefender
### User preview release
```
                                _       __               _              
                               | |     / _|             | |             
    _ __   ___ __ _ _ __     __| | ___| |_ ___ _ __   __| | ___ _ __    
   | '_ \ / __/ _` | '_ \   / _` |/ _ |  _/ _ | '_ \ / _` |/ _ | '__|   
  _| |_) | (_| (_| | |_) | | (_| |  __| ||  __| | | | (_| |  __| |      
 (_| .__/ \___\__,_| .__/   \__,_|\___|_| \___|_| |_|\__,_|\___|_|      
  _| |             | |                 _                                
 | |_|             |_|                | |                               
 | |__  _   _   _ __ ___   __ _  ___  | | __ ___      _____  ___  _ __  
 | '_ \| | | | | '_ ` _ \ / _` |/ __| | |/ _` \ \ /\ / / __|/ _ \| '_ \ 
 | |_) | |_| | | | | | | | (_| | (__  | | (_| |\ V  V /\__ | (_) | | | |
 |_.__/ \__, | |_| |_| |_|\__,_|\___| |_|\__,_| \_/\_/ |___/\___/|_| |_|
         __/ |                                                          
        |___/  

```

## About
PcapDefender is a python tool for searching .pcap files for strings. 

## Install
Clone the repo:
```
git clone https://github.com/mac-lawson/PcapDefender.git
```

Install deps:
```
python3 -m pip install colorama
python3 -m pip install scapy
```

## Usage
Example usage using the demo.pcap file and searching for the string 'Windows NT':
```
python3 pcapdef.py -s "Windows NT" -f demo.pcap 
``` 


## Release notes
- 