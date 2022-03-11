from urllib.request import urlopen
import json
import colorama
from colorama import Fore
colorama.init(autoreset=True)
dom = f"""
{Fore.CYAN}                            _____ _  ____     ___               _____      __ ___  
{Fore.CYAN}                          / ____| |/ /\ \   / / |        /\   |  __ \    / // _ \ 
{Fore.CYAN}                         | (___ | ' /  \ \_/ /| |       /  \  | |__) |  / /| (_) |
{Fore.CYAN}                          \___ \|  <    \   / | |      / /\ \ |  _  /  | '_ \__, |
{Fore.CYAN}                          ____) | . \    | |  | |____ / ____ \| | \ \  | (_) |/ / 
{Fore.CYAN}                         |_____/|_|\_\   |_|  |______/_/    \_\_|  \_\  \___//_/  
"""
print(dom)

def balance():
    print("CHECK ANY ONE BTC BALANCE WITH THEIR ADDRESS")
    address = input("Enter BTC Wallet Address:\n")
    htmlfile = urlopen(f"https://blockchain.info/rawaddr/{address}/?format=json")
    htmltext = htmlfile.read().decode('utf-8')
    load = json.loads(htmltext)
    tnx = load["n_tx"]
    final = [load["address"], load["n_tx"], load["total_received"], load["total_sent"], load["final_balance"],
             load["txs"]]
    print(
        f"BTC ADDRESS : {final[0]} \n TOTAL TRANSCTIONS : {final[1]} \n TOTAL RECIVED : {final[2] / 100000000} \n TOTAL SENT : {final[3] / 100000000} \n FINAL BALANCE : {final[4] / 100000000}")

balance()