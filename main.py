import os
from termcolor import colored


def check_if_attacking():

    my_defaultGeteway = os.popen('netstat -nr | grep default | grep en0').read().split()
    mac_adrres_of_network = str(os.popen(f"arp -a | grep {my_defaultGeteway[1]}").read()).split(" ")[3]
    arp_table = str(os.popen('arp -a').read())
    count = 0
    a_data = arp_table.split(" ")

    for i in a_data:
        if mac_adrres_of_network in i:
            count += 1
            if count == 2:
                print(colored("-----------------  YOUR NETWORK UNDER ATTACK  -M-I-T-M---------","red"))
                attacker_mac = i
                attacker_data = os.popen(f"arp -a | grep {i}").read().split("]")

                for j in attacker_data[0:1]:
                    if f"{my_defaultGeteway[1]}" not in j:
                        attacker_ip = list(j.split(" "))[1].replace("(","").replace(")","")
                        print(colored(f"{arp_table}","green"))
                        print(colored(f"Attacker ip is: {attacker_ip}  MAC Addres is: {attacker_mac}","red"))
                        break
                        return False

    print(colored("----------YOUR NETWORK IS OK----------","green"))
    return True

while(check_if_attacking()==True):
    check_if_attacking()

