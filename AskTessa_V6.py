from time import sleep

def maths():

    topic=input("What topic in this subject would you like to know about?")

    if topic=="Algebra":
        sleep(1)
        print("Jobs requiring a knowledge of Algebra include; Market Research Analyst, Animation, Industrial Engineer!")

    elif topic=="Trigonomatry":
        sleep(1)
        print("Jobs requiring a knowledge of Trigonometry include; Architect, Navigator, Radiologist")

    elif topic=="Geometry":
        sleep(1)
        print("Jobs requiring a knowledge of Geometry include; Artist, Architect and Engineer.")

def english():

    topic=input("What topic in this subject would you like to know about?")

    if topic=="Poetry":
        sleep(1)
        print("Jobs requiring a knowledge of Poetry include; Poet, Freelance poetry, musician")

    elif topic=="Creative Writting":
        sleep(1)
        print("Jobs that require a knowledge f poetry are; an author, Comunications director, digital copywriter")

    elif topic=="Media Studies":
        sleep(1)
        print("Jobs that require a knowledge of media studies are; journalist, news anchour, web contact manager")

def science():
	
	topic=input("What topic in this subject would you like to know about?")
	
	if topic=="Acids":
		sleep(1)
		print("Jobs that require a knowledge in acids are; Plant Operator, Water Treatment, Research Scientist.")
		
	elif topic=="Planets":
		sleep(1)
		print("Jobs requiring a knowledge of planets are; Astronomer, Mission Control Planner, Astrogeologists.")
		
	elif topic=="Energy":
		sleep(1)
		print("Jobs requiring a knowledge of energy are; Electrician, Solar Engineer, Enviromental Specialist.")

def coding():
    topic=input("What topic in this subject would you like to know about?")

    if topic=="HTML":
        sleep(1)
        print("Jobs requiring a knowledge of HTML are; Front End Developer, Freelance Developer, Junior Developer")

    elif topic=="Python":
        sleep(1)
        print("Jobs requiring a knowledge of Python are; Software Engineer, Backend Developer, Data Engineer")

    elif topic=="Javascript":
        sleep(1)
        print("Jobs requiring a knowledge of Javascript are; UI Engineer, Fullstack Engineer, Node Javascript Developer")


print("Welcome to AskTessa©!!")               #print("")
sleep(1)
print("As you probably already know, this is a program to help you find inspiration in school and while doing homework by telling you what it is usefull for")
sleep(1)
print("So no further addue, lets get into it!!!")
sleep(1)
print("e.g; Have you ever been in a class, wondering what good will this do me in the?")
sleep(1.5)
print("This programme will tell you if what you're learning has any real world uses.")
sleep(.5)
print("REMEMBER all choices have to start with capital letters.")
sleep(3)
print("Currently the only subjects available are Maths, English, Coding, Science")
sleep(3)

subjectchoice=input("So, what subject do you want to learn about?")

if subjectchoice=="Maths":
    sleep(1)
    maths()

elif subjectchoice=="English":
    sleep(1)
    english()
    
elif subjectchoice=="Science":
	sleep(1)
	science()
elif subjectchoice=="Coding":
    sleep(1)
    coding()

else:
    print("Error")

