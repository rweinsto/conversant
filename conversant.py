#!/usr/bin/python
#Reina Weinstock
#Start Date: August 20, 2107
#Project Name: Conversant Coding Assessment
#Project Description:
#  What conclusions can you programmtically derive based on this data?
#  Trends in data across multiple data centers
#  Trends in data across time
#  Reports results in as much relevant detailsas can you think?
#  Extra- How can you represent your conclusions visually
#Deliverable: GitHub Repository w/ code, run instructions, assumptions, 
# findings, challengers, if any info was missing
#Data File: data.montoya.txt

import numpy as np

#------------------------FUNCTION--------------------------
# processRawData: reads in the data file (data.montoya.txt)
#    strips each piece of data of extraneous spaces/newlines
#    splits each line on the tab (\t) character
#    converts time to an int
#    converts value to a float
#    removes preceeding "dc=" before the data center name
#    parameters: list of data from calling readlines() file
#    returns: a list of each line, with each data point as 
#      an item in that line
#----------------------------------------------------------
def processRawData(inputData):


	for i in range(len(inputData)):
		split = inputData[i].strip().split("\t")
		if i != 0:
			split[1] = int(split[1])
			split[2] = float(split[2])
			split[3] = split[3][-1]
		inputData[i] = split
	return inputData

#------------------------FUNCTION--------------------------
# mean: determines the mean of a list
#    parameters: a list of the same type
#    returns: a single value, the mean
#----------------------------------------------------------

def mean(lst):
	return sum(lst)/len(lst)

#------------------------FUNCTION--------------------------
# main: reads in the raw data, calls the processRawData fn
#    analyzes and outputs results from the data
#    results include: Min, Max, Mean Values along with
#        Trend Line Over Time and Error of that trend
#----------------------------------------------------------
def main():

	#read in the raw data
	f = open("data.montoya.txt", "r")
	inputData = f.readlines()
	f.close()

	#clean unneccessary garbage from that data
	cleanData = processRawData(inputData)

	#create and populate lists for analysis of all data centers
	times =[]
	values = []
	centers = set([])

	for i in range(1,len(cleanData)):
		times.append(cleanData[i][1])
		values.append(cleanData[i][2])
		centers.add(cleanData[i][3])

	#output the results of analysis for all data centers
	print("\nVALUES ACROSS ALL DATA CENTERS")
	print"Min: ",min(values), "@", times[values.index(min(values))]
	print"Max: ",max(values), "@", times[values.index(max(values))]
	print"Mean: ",mean(values)

	print("\nVALUES OVER TIME AT ALL DATA CENTERS")

	#get the coefficents and residuals from a polynomial fitted line
	#coefficents are used to create the y = mx+b trend line
	#residuals are used to determine the error of the line
	coefficients, residuals, _,_,_ = np.polyfit(times, values, 1, full=True)
	nrmse = np.sqrt(residuals[0]/(len(values)))/(max(values) - min(values))
	print"Trend Line: y = ",coefficients[0],"x +",coefficients[1]
	print"Normalize Mean Square Error (0-1): ", nrmse

	print("-------------------------------")
	#ouput the results of analysis for each data cetner
	print("\nVALUES AT EACH DATA CENTER...")
	for each in centers:
		centerTimes = []
		centerValues = []

		for i in range(len(cleanData)):
			if cleanData[i][3] == each:
				centerTimes.append(cleanData[i][1])
				centerValues.append(cleanData[i][2])

		#output the results of analysis for all data centers
		print"\nVALUES AT DATA CENTER:", each
		print"Min: ", min(centerValues), "@", centerTimes[centerValues.index(min(centerValues))]
		print"Max: ", max(centerValues), "@", centerTimes[centerValues.index(max(centerValues))]
		print"Mean: ", mean(centerValues)

		print"\nVALUES OVER TIME AT DATA CENTER: ", each

		#get the coefficents and residuals from a polynomial fitted line
		#coefficients are used to create the y = mx+b trend line
		#residuals are used to determine the error of the line
		coefficients, residuals, _,_,_ = np.polyfit(centerTimes, centerValues, 1, full=True)
		nrmse = np.sqrt(residuals[0]/(len(centerValues)))/(max(centerValues) - min(centerValues))
		print"Trend Line: y = ",coefficients[0],"x +",coefficients[1]
		print"Normalize Mean Square Error (0-1): ", nrmse

		
if __name__ == "__main__":
    main()