import csv
from os import name

mentee = [] # global list to keep track of mentess, 
mentor = []
            # they will be added to the list in the order that they apear in the csv

class student:

    def __init__(self, name, field, major, first, career, skill, hobby, online, second):
        # data structure for responses will be a set of enumerations, atleast for now
        # sets have O(1) lookup time so we dont need to iterate through the list every time
        self.name = name
        self.field = field
        self.major = major
        self.first = list()
        for s in first:
            self.first.append(s)
        self.career = career
        self.skill = skill
        self.hobby = hobby
        self.online = online
        self.second = list()
        for s in second:
            self.second.append(s)
    
    def get_name(self):
        return self.name

    def get_field(self):
        return self.field

    def get_major(self):
        return self.major

    def get_first(self):
        return self.first
    
    def get_career(self):
        return self.career

    def get_skill(self):
        return self.skill

    def get_hobby(self):
        return self.hobby

    def get_online(self):
        return self.online

    def get_second(self):
        return self.second


def read(filename, formentee):
    # void function bc all is a global variable 
    # for mentee is a bool, true means we are adding to list of mentee
    # mentor otherwise

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile) # turns the spreadsheet into a reader object
        next(reader) # skip header line
        # CHECK YOUR INDENTS
    
        if formentee:
            for row in reader:

                s = student(row[0], row[2], row[3], [row[5], row[6], row[7], row[8], row[9]], row[10], row[11], row[12], row[13], 
                    [row[14], row[15], row[16], row[17]])
                # choose the correct row for example student(row[2], row[6].....[row[7], row[8]...] )
                mentee.append(s)
        else: 
            for row in reader:
                s = student(row[0], row[2], row[3], [row[5], row[6], row[7], row[8], row[9]], row[10], row[11], row[12], row[13], 
                    [row[14], row[15], row[16], row[17]])
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
        score += 10
    if (mentee.get_major() == mentor.get_major()):
        score += 7
    for i in range(5):
        if (mentee.get_first()[i] == 1 and mentee.get_first()[i] == mentor.get_first()[i]):
            score += 5
    if (mentee.get_career() == mentor.get_career()):
        score += 7
    if (mentee.get_skill() == mentor.get_skill()): 
        score += 2
    if (mentee.get_online() == mentor.get_online()): # online
        score += 2
    for i in range(4): # workshops
        if (mentee.get_second()[i] == 1 and mentee.get_second()[i] == mentor.get_second()[i]):
            score += 2
    
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
        for m in mentor:
            score = compare(current, m)
            if (threshhold <= score): # compare will return the score
                possible.append(m.get_name() + str(score))
        
        print("--------")
        print(current.get_name())
        print(possible)
        print("--------")


def main(menteecsv, mentorcsv, threashold):
    read(menteecsv, True)
    read(mentorcsv, False)
    get_matches(threashold)

main("Mentee.csv", "Mentor.csv", 13)
