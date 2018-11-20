##Taken Semesters
##working hours: a collection mapping course to hours of each semester
sem0_hr = {'cs101':15, 'cs125':20, 'cs173':15}
sem1_hr = {'cs225':22, 'cs223':17, 'cs374':35}
##semesterDict: a collection storing info of a semester
sem0 = {'workload':6, 'hours':sem0_hr}
sem1 = {'workload':9, 'hours':sem1_hr}
##semester booklet: a collection of semesters within one booklet
sem = {}
sem[0]=sem0
sem[1]=sem1
#e.g. sem[1][hours]['cs233'] = 17 means that cs233 was taken in 1-th (second) semester and costed 17 hours per week

##Courses planned to take
courseList = ['cs241','cs411','cs421','ece489']

##Input tuple
inputTuple = (sem, courseList)

##output: collection maping courses to (expected_hours, if_exists_in_our_db)
outputTuple={'cs241':(24,True),'cs411':(14,True),'cs421':(20,True),'ece489':(15,False)}
#note that outputTuple['ece489'] = (15, False) as ece489 is not in our db
