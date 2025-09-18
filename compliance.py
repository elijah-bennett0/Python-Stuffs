import csv
import datetime
'''
ROWS:
0 
1 
2 
3 

COLUMNS:
0 	
1 
2 
3 
4 	
5 
6 

'''
expiredCA = 0
totalCA = 0

expiredAUP = 0
totalAUP = 0

with open("") as file:
	format = "%d-%b-%Y"
	companies = {}
	companiesAUP = {}
	for row in csv.reader(file):
		# CA exp date: col 4
		# AUP date signed: 2
		
		if len(row) < 7:
			pass
		else:
			try:
				
				company = row[6]
				if company == "" or company == "":
					pass
				else:
					if company in companies:
						companies[company] = {list(companies[company].items())[0][0]:list(companies[company].items())[0][1] + 1}
					else:
						companies[company] = {0:1} # expired:total
					if company in companiesAUP:
						companiesAUP[company] = {list(companiesAUP[company].items())[0][0]:list(companiesAUP[company].items())[0][1] + 1}
					else:
						companiesAUP[company] = {0:1} # expired:total
				
				
				object1 = datetime.datetime.strptime(row[4], format)
				#print(datetime.datetime.today())
				if object1 > datetime.datetime.today():
					#print("Not Expired")
					pass # dont really need to do anything
				else:
					#print("%s : Expired" % object)
					expiredCA += 1
					companies[company] = {list(companies[company].items())[0][0] + 1:list(companies[company].items())[0][1]}
				totalCA += 1
				object2 = datetime.datetime.strptime(row[2], format)
				if object2 > (datetime.datetime.today() - datetime.timedelta(365)):
					pass
				else:
					expiredAUP += 1
					companiesAUP[company] = {list(companiesAUP[company].items())[0][0] + 1:list(companiesAUP[company].items())[0][1]}
				totalAUP += 1
					
				#print(companies)
				
			except:
				pass
	
	
	
	
	
	
	
	