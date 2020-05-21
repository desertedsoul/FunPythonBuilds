# Program for printing daily updated count of coronavirus cases
# Pseudocode:    check worldometer website
#                fetch through the webpage (inspect html code)
#                get desired data (check for tags and their text data)
#                print that info
#		 do similar sequence for the country
#		 **schedule for daily run at specific time using Windows task scheduler

import requests
from bs4 import BeautifulSoup

def covid_world():
	# the website we want to open	 
	url1='https://www.worldometers.info/coronavirus/'
	
	#data 
	resp1=requests.get(url1) 
	
	#http_respone 200 
	if resp1.status_code==200: 
		print('Successfully connected to the Worldometer website')
		print('\nJust a moment (gathering data)...\n')

		# Using Python built-in HTML parser
		soup1=BeautifulSoup(resp1.text,'html.parser')

		# info should be the list which contains all the text info

		info1=soup1.find('div',{'style':'margin-top:15px'})
		
        #now we want to print only the text part of the HTML tag data
		#find all the elements of that particular HTML tag
		
		for i in info1.findAll('span'):
			#now store this data as text into a variable
			total_cases = i.text
			print('Data gathering complete.')
			print('\n====================================================')
			print('Current Worldwide Coronavirus Cases: ', total_cases)
			print('====================================================')
	else:
		print('Error')

def covid_india(): 
	 
	url2='https://www.worldometers.info/coronavirus/country/india/'
	
	resp2=requests.get(url2) 
	
	if resp2.status_code==200: 
		
		soup2=BeautifulSoup(resp2.text,'html.parser')

		info2=soup2.find('div',{'style':'margin-top:15px'})
		
		for i in info2.findAll('span'):
			
			total_india = i.text
			print('Coronavirus Cases in India: ', total_india)
			print('====================================================')
	else:
		print('Error')

covid_world()
covid_india()

#display date and time of updation
import datetime
now = datetime.datetime.now()
print('Updated on: ', now.strftime('%d/%m/%Y %H:%M:%S'))
input('\nPress ENTER to exit')
