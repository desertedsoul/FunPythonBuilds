# Program for printing daily updated count of coronavirus cases
# Pseudocode:    
# check worldometer website
# fetch through the webpage (inspect html code)
# get desired data (check for tags and their text data)
# print that info
# do similar sequence for the country
# **schedule for daily run at specific time using Windows task scheduler

import requests
from bs4 import BeautifulSoup

print('\n====================================================') # just for layout
print("Today's update on total number of Coronavirus cases:\n") # double quote because single quote is present in the sentence

# function that'll take website url and the name of the country as parameters
# this will save us from writing code for every html page of the country

def covid_cases(url, country):
	 
	resp=requests.get(url)
	
	if resp.status_code==200: # http respone 200 means OK status 
		
		soup = BeautifulSoup(resp.text,'html.parser') # using python built-in HTML parser

		# info should be the list which contains all the text information
		# check carefully through the html code and find tags that contain desired information

		info=soup.find('div',{'style':'margin-top:15px'})
		
                # now we want to print only the text part (i.e the count of cases) of the HTML tag data
		# find all the elements of that particular HTML tag
		
		for i in info.findAll('span'):
			total_cases = i.text # store this data as text into a variable
			
			print(country, total_cases)
			print('====================================================') # just for layout
	else:
		print('Error')

covid_cases('https://www.worldometers.info/coronavirus/', 'Current Worldwide Coronavirus Cases: ')
covid_cases('https://www.worldometers.info/coronavirus/country/india/', 'Coronavirus Cases in India: ')

# single function with multiple urls of multiple countries can be done but this seemed easy to me
# now, display date and time of updation so that we know the data is latest

import datetime

now = datetime.datetime.now()
print('Updated on: ', now.strftime('%d/%m/%Y %H:%M:%S'))
input('\nPress ENTER to exit') # old technique
