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

    else:
        print("ERROR!")



def english():

    topic=input("What topic in this subject would you like to know about?")

    if topic=="Poetry":
        sleep(1)
        print("jobs requiring a knowledge of Poetry include; Poet, Freelance poetry, musician")

    elif topic=="creative writting":
        sleep(1)
        print("jobs that require a knowledge f poetry are; an author, Comunications director, digital copywriter")

    elif topic=="media studies":
        sleep(1)
        print("jobs that require a knowledge of media studies are; journalist, news anchour, web contact manager")

    else:
        print("ERROR!")
        
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


subjects=["Maths", "English", "Irish", "Geography", "History", "Coding", "Science", "Business"]


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

else:
    print("Error")
