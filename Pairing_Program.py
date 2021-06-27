import csv
from os import name

mentee = [] # global list to keep track of mentess, 
mentor = []
            # they will be added to the list in the order that they apear in the csv

class student:

    def __init__(self, name, field, major, responses):
        # field will be the broader catagory of their major, like chem bio micro bio all fall into lifescience
        # and stat math cpsc would all fall into computation
        # data structure fro responses will be a set of enumerations, atleast for now
        # sets have O(1) lookup time so we dont need to iterate through the list every time
        self.name = name
        self.field = field
        self.major = major
        self.responses = set()
        for s in responses:
            self.responses.add(s)
    
    def get_name(self):
        return self.name

    def get_field(self):
        return self.field

    def get_responses(self):
        return self.responses


def read(filename, formentee):
    # void function bc all is a global variable 
    # for mentee is a bool, true means we are adding to list of mentee
    # mentor otherwise

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile) # turns the spreadsheet into a reader object
        next(reader) # skip header line

    if (formentee):
        for row in reader:
            s = student("generic", "somefield", "major", ["list", "of", "question", "resposnes"])
            # choose the correct row for example student(row[2], row[6].....[row[7], row[8]...] )
            mentee.append(s)
    else: 
        for row in reader:
            s = student("generic", "somefield", "major", ["list", "of", "question", "resposnes"])
            mentor.append(s)


def compare(mentee, mentor):
    '''
    Here is why I decided to add a field parameter to student. Imagine a situation where a mentee is CPSC eng
    and mentor is software eng. If you compared firectly they wouldnt match but if u compared fields they would
    so thats why.

    Also change the numbers that I use in this implementation to fit you wieghtings
    '''
    score = 0

    if (mentee.get_field() == mentor.get_field()): # prob needs a getter funciton in student
        # not sure why my getter doesnt work
        score += 80
    score += 10*len(mentee.get_responses() - (mentee.get_responses() - mentor.get_responses()))\

    return score 


def get_matches(threshhold):
    '''
    get matches will run similar to a dating app where each mentee will be compared to everysingle mentor
    bases on the matches with their majors and answers they will be assigned a score 
    
    for example:
    mentor: Maria, life sci, chemm, [q1, q5, q8]
    mentee: James, life sci, microbio, [q5, q7, q10]

    since major is important we can asisgn maria a 80, then we see the questions, since they only match to 
    q5 and questions are les important then we assign 10. Thus 80+10 = 90 so their match score is 90

    specific numbers are mutable and you can change the parameters as u wish

    ...

    prints all of a mentees pairings above a certain score threshhold: 
    
    if threshhold is 80 then: James -> [Maria90 .......... others]
    '''

    for current in mentee:
        possible = [] # list of menotrs for this mentee, gets reset every iteration
        for mentor in mentor:
            if (threshhold <= compare(current, mentor)): # compare will return the score
                possible.append(mentor.get_name() + str(compare(current, mentor)))
        print(possible)


def main(mentee, mentor, threashold):
    read(mentee, True)
    read(mentor, False)
    get_matches(threashold)

