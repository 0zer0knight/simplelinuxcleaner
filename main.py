#this is for daily cleaner system
import os
from datetime import datetime

def main():
    waktu = datetime.now()
    user = os.getlogin()
    os.system("sudo apt-get remove ; sudo apt-get clean ; sudo apt-get purge ; sudo journalctl --vacuum-time=2weeks ; sudo find /tmp -type f -atime +10 -delete ; rm -rf ~/.cache/* ; sudo apt-get makecache ;")

    with open("datalog.txt", "a") as file:
        file.write(f"user : {user} telah melakukan pembersihan pada waktu = {waktu} \n")


if __name__ == "__main__":
       main()
