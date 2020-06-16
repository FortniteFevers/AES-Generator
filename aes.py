import requests
import tweepy
import time
from colorama import *
init()
print(Fore.GREEN+"Fortnite AES key Generator")
print(Fore.GREEN+"Made by FortniteFevers")
print(Fore.GREEN+"Starting the program now.")
response = requests.get('https://benbotfn.tk/api/v1/aes')
aes = response.json()['mainKey']
response = requests.get('https://benbotfn.tk/api/v1/status')
version = response.json()['currentFortniteVersionNumber']
print("AES key has been succesfully retrived!")
time.sleep(1)
print("Current AES key:")
print(Fore.BLUE+aes)
time.sleep(1)
print(Fore.CYAN+"Now tweeting...")

auth = tweepy.OAuthHandler('API', 'API-SECRET')
auth.set_access_token('ACESS', 'ACESS-SECRET')
api = tweepy.API(auth)
api.update_status('AES Key for version v'+str(version)+':\n\n'+str(aes))
print("The AES key has been succesfully tweeted!")
time.sleep(1)
print(Fore.RED+"Cloasing program in 5 seconds....")
time.sleep(5)
