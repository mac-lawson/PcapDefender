from reader import Reader
from output import Output
import sys
from colorama import Fore, Back


logo = ''' 

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
 '''
def handel():
        # try:
            if(len(sys.argv) > 1):
                if((sys.argv[1] == "-s" and sys.argv[3] == "-f")):

                    Reader.filterData((sys.argv[2]), (sys.argv[4]))


        # except:
        #     Output.error("No parameters were provided. If they were, they were not correct. Refer to the 'Usage' guide.")

print(logo)
Output.usage()
handel()

