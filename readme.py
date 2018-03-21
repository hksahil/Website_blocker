Between working hours,it will block  ccertain websites(it will write these wesiites on hosts file available at windows/systems/drivers/etc/hosts
and after that working hours,it will delete that websites from hosts file.
-(To run on doule click)To automatically run a script ,save it as filename.pyw  It will automatically executed on double click.no need to go to cmd then typing python filename.py	
-(To run it on every sartup of PC)To run a script on everytime start of computer, search TASK SCHEDULER on windows. Set it there.					       

import time
from datetime import datetime as dt

#hosts_temp=r"D:\Dropbox\pp\block_websites\Demo\hosts"
hosts_path="C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"

#List of banned websites:

"""
1.Facebook
2.Instagram
3.Whatsapp
4.Pornhub
5.youtube
"""
website_list=["www.facebook.com","facebook.com","www.pornhub.com","pornhub.com","www.instagram.com","www.whatsapp.com","whatsapp.com","twitter.com","instagram.com","instagram.com"]

while True:

	#If between working hours,block the websites.(Means write the websites in host file)
	
	
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
            with open(hosts_path,'r+') as file:#open the file
			content=file.read()#read the file 
            for website in website_list:#Iterate through the website-list
                if website in content:#if  allready present in our host file
                    pass#pass
                else:#if not
                    file.write(redirect+" "+ website+"\n")#write the websites in the host file
					
					
	#If between working hours,block the websites.
    else:
	"""
	IF OUT OF TIME,WE HAVE TO DELETE THAT LIST OF WEBSITES.
	THERE IS NO OPTION TO DELETE SOETHING IN FILE.
			SO,TRICK:::
			ITERATE THROUGH THE COMPLETE HOST FILE.WRITE ALL THE CONTENT TILL THERE COMES THE WEBSITE LIST.
			BUT IT WILLWRITE THE COMPLETE CONTENT ON END OF FILE.BUT YOU NEED IT ON START OF WEBSITE.
			THEREFORE FIRST PUT THE POINTER TO THE START OF WEBSITE USING SEEK(0) AND THEN TRUNCATE ALL THE THINGS BELOW IT.
	"""
        with open(hosts_path,'r+') as file: 
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            time.sleep(5)
