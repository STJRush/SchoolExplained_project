from time import sleep
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
print("REMEMBER all choices have to be made with capital letters.")
print("lets start!!!")


subjects=["Religion", "History", "Irish", "Science", "Maths", "English", "Geography", "Spanish", "German", "French", "Business", "Coding", "Homec", "Woodwork", "T.G", "P.E", "Art", "Music",]

print("So, what subject do you want to learn about?")
subject=input()
sleep(1)

if subject=="Maths":
    print("What would you like to know on the subject of maths!")
    sleep(2)

else:
    print("ERROR!")

topic=input()

if topic=="Algebra":
    print(1)
    print("Jobs requiring a knowledge of Algebra include; Market Research Analyst, Animation, Industrial Engineer!")

elif topic=="Trigonomatry":
    sleep(1)
    print("Jobs requiring a knowledge of Trigonometry include; Architect, Navigator, Radiologist")

else:
    print("ERROR!")

