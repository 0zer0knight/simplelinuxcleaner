import os
import schedule
from datetime import datetime
import time

def cleaner():
        ctime = datetime.now()
        gettime = ctime.strftime("%H:%M:%S")

        os.system('sudo dnf clean all ; sudo dnf autoremove ; sudo dnf remove $(dnf repoquery --installonly --latest-limit=-2 -q) ; sudo journalctl --vacuum-time=2weeks ; sudo find /tmp -type f -atime +10 -delete ; rm -rf ~/.cache/* ; sudo dnf makecache ; ')

        with open('log.txt', 'a') as file:
            file.write(f"pembersihan dilakukan pada pukul {gettime}\n")


def main():
        userask = int(input("pembersihan mau diulang berapa jam = "))
        try:
            print(f'program cleaner akan diulang {userask} jam sekali')

            cleaner()
            schedule.every(userask).hours.do(cleaner)

            while True:
                 schedule.run_pending()
                 time.sleep(1)
                
        except ValueError as e:
            print("bukan input yang valid")

        
if __name__ == "__main__":
    main()