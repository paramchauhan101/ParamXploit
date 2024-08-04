#!/usr/bin/env python3
#
# Copyright (c) 2024 ParamXploit (Param)
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import subprocess
import sys
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def matrix_effect():
    for _ in range(10):
        line = ''.join(random.choice('01') for _ in range(80))
        print(Fore.GREEN + line)
        time.sleep(0.1)
    print(Fore.RED + "\nParamXploit\n" + Style.RESET_ALL)

def nmap_scan(target):
    print(Fore.GREEN + f"[*] Starting basic Nmap scan on {target}")
    try:
        result = subprocess.run(["nmap", "-T4", "-F", target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred during Nmap scan: {e}")

def nikto_scan(target):
    print(Fore.GREEN + f"[*] Starting Nikto scan on {target}")
    try:
        process = subprocess.Popen(["nikto", "-h", target, "-ask", "no"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                print(Fore.RED + output.strip())
        process.wait()
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred during Nikto scan: {e}")

def secheader_scan(target):
    print(Fore.GREEN + f"[*] Starting security header scan on {target}")
    try:
        result = subprocess.run(["python3", "secheader.py", target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred during security header scan: {e}")

def main():
    matrix_effect()
    while True:
        print(Fore.RED + "===================================================================")
        print(Fore.GREEN + "ParamXploit")
        print(Fore.RED + "===================================================================")
        print(Fore.GREEN + "\n1. Basic Nmap Scan")
        print(Fore.GREEN + "2. Nikto Scan")
        print(Fore.GREEN + "3. Security Header Scan")
        print(Fore.GREEN + "E. Exit\n")
        print(Fore.RED + "===================================================================")

        ans = input(Fore.GREEN + "\nWhat would you like to do? Enter your selection: ").upper()

        if ans == "1":
            target = input(Fore.GREEN + "Enter the target IP or hostname: ")
            nmap_scan(target)
        elif ans == "2":
            target = input(Fore.GREEN + "Enter the target IP or hostname: ")
            nikto_scan(target)
        elif ans == "3":
            target = input(Fore.GREEN + "Enter the target IP or hostname: ")
            secheader_scan(target)
        elif ans == "E":
            sys.exit()
        else:
            print(Fore.RED + "Invalid selection. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n Keyboard Interrupt. ")
        sys.exit()
