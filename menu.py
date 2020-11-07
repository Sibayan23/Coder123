import pyttsx3 as py
import os
import subprocess

py.speak("Hello!! welcome to my menu driven program")
print()
print('                                                           ----   ------   -------                                           ')
print('                                                         | MENU | DRIVEN | PROGRAM |                                         ')
print('                                                           -----  ------  --------                                           ')
print()
x=1

py.speak("This is my tool. It have some features like it will launch or open")
py.speak("paint, calculator, notepad editor, sublime text editor, chrome default browser, windows media player, VLC media player, internet explore,") 
py.speak("notepad++, command prompt, microsoft edge, VMware workstation. And it will show you the date and current time in pc.")
py.speak("So here we go!! you give any requirement as your wish")

while True:
	if x==1:
		py.speak("Write  your requirement")
		print('Write  your requirement: ', end='')
		x=x+1
	else:
		py.speak("Write your next requirement")
		print('Write your next requirement: ', end='')

	p=input()
	#print(p)
	# os.system(p)
	p.lower()

	if ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and ("edge" in p)):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! microsoft edge for you!!")
			os.system("msedge")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and (("notepad" in p) or ("editor" in p))):
		#if (("dont" in p) or ("don't" in p) or ("not" in p)):
			#py.speak("okay!! it will not open for you.")
		#else:
			py.speak("opening!! notepad editor for you!!")
			os.system("notepad")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and (("player" in p) and ("vlc" not in p))):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! windows media player for you!!")
			os.system("wmplayer")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and (("chrome" in p) or ("browser" in p))):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! chrome browser for you!!")		
			os.system("chrome google.com")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and (("vlc" in p) and ("player" in p))):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! VLC media player for you!!")
			os.system("vlc")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and ("vmware" in p)):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! VMware workstation for you!!")
			os.system("vmware")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and ("explore" in p)):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! internet explore for you!!")		
			os.system("iexplore")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and ("notepad++" in p)):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! notepad++ editor for you!!")		
			os.system("notepad++")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and ("sublime" in p)):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! sublime text editor for you!!")		
			os.system("sublime_text")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and (("cmd" in p) or ("prompt" in p))):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! command prompt for you!!") 
			os.system("start cmd")
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and (("calculator" in p) or ("calc" in p))):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not open for you.")
		else:
			py.speak("opening!! calculator for you!!")
			subprocess.Popen('C:\\Windows\\System32\\calc.exe')
	
	elif ((("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("take" in p)) and ("paint" in p)):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will nopt open for you")
		else:
			py.speak("opening!! paint for you")
			os.system("%windir%\system32\mspaint.exe")
	
	elif ("date" in p):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not show")
		else:
			py.speak("Todays date is")
			os.system('date')
	
	elif ("time" in p):
		if (("dont" in p) or ("don't" in p) or ("not" in p)):
			py.speak("okay!! it will not show")
		else:
			py.speak("Current time on PC is")
			os.system('time')

	elif (("exit" in p) or ("quite" in p) or ("stop" in p) or ("close" in p) or ("end" in p) or ("finish" in p)):
		py.speak("program execution is going to stop")
		py.speak("Thank you for using my tool")
		break
	
	else:
		py.speak("this requirement is not available!! sorry for that!! go for next requirement")
		print("Don't support")









 
