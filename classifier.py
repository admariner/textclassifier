# -*- coding: utf-8 -*-
"""A lightweight classifier, have input.txt in the current folder. See sample file for the format"""
import os.path
mapping = {}
#print data
def readInput():
    if not os.path.exists('training.txt'):
        print("training.txt file not present in the currrent folder")
        quit()
    f = open ('training.txt')
    with f as ins:
        for row in ins:
            det = row.split(" ")
            #print det
            if det[0] and det[0] != "\n":
                k = det[0].replace("__label__",'')
                if k not in mapping:
                    mapping[k] = []
                mapping[k].append(det[1].lower().strip("\n").strip("\r"))

def classify(subject, default):
    matches = {}
    for category,row in mapping.items():        
        #Check subject                 
        for word in subject.lower().split(" "):
            #Check if the word in the subject is there in a training row
            if word in row:
                if category in matches:
                    matches[category] = matches[category] + 1
                else:
                    matches[category] = 1    
    if matches:
        #Sort by value
        sortedResult = sorted(matches.items(), key = lambda kv:kv[1])
        #Get descending order
        sortedResult.reverse()
        return sortedResult
    return default


#Load the input file and assign category for each row
readInput()

#Run if invked from command line directly
if __name__ == "__main__":
    results = classify("offer linkedin linkedin", "somerandomcategory")
    if results != 'somerandomcategory':
        print results[0][0], "is the top category"
    else:
        print "somerandomcategory"