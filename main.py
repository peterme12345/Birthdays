import json
import datetime

def main():

    menu=input("Please select an option:\n" 
    "1. Start\n" \
    "2. Display\n"
    "3. Enter birthday\n" \
    "4. Delete birthday\n" \
    "5. Find person\n" \
    "6. Quit\n" \
        "Answer: ")
    
    if int(menu)==1:
        showNearest()
        main()

    elif int(menu)==2:
        showBirthday()
        main()

    elif int(menu)==3:
        addBirthday()
        choice=input("Add another?: ").lower()
        while choice=="y":
            addBirthday()
            choice=input("Add another?: ").lower()
        main()
        
        
    elif int(menu)==4:
        removeBirthday()
        choice=input("Remove another?: ").lower()
        while choice=="y":
            removeBirthday()
            choice=input("Remove another?: ").lower()
        main()
    
    elif int(menu)==5:
        user=input("Checking for who?: ")
        findPerson(user)
        main()

    elif int(menu)==6:
        print("Program terminated")

    elif menu.isalpha():
        print("Please type a number!")
        main()
        


def showNearest():
    
    result=[]
    with open("Birthdays.json","r") as file:
        database=json.load(file)
    

    for b in database["birthdays"]:
        if datetime.datetime.today()<=datetime.datetime(2026, int(b["month"]), int(b["day"])):
            diff=datetime.datetime(2026, int(b["month"]), int(b["day"]))-datetime.datetime.today()
            temp={}
            temp["name"]=b["name"]
            temp["time"]=diff
            result.append(temp)

    sortedList = sorted(result, key=lambda x: x["time"],reverse=False)
    print()
    print("The next birthdays are:")
    print()
    for i in range(10):
        print(sortedList[i]["name"],"in",sortedList[i]["time"])
    
    print()




def addBirthday():
    person={}
    person["name"]=name=input("Enter name: ").capitalize()
    person["month"]=month=int(input("Enter month as a number: "))
    while month<=0 or month>12:
        month=int(input("Try again. Please choose a valid month: "))
    person["day"]=day=int(input("Enter day as a number: "))
    while day<=0 or day>31:
        day=int(input("Try again. Please choose a valid day: "))

    
    with open("Birthdays.json","r+") as file:
        database = json.load(file)
        database["birthdays"].append(person)
        file.seek(0)
        json.dump(database,file,indent=4)
    

    print("Successfully added: ",person["name"])

def removeBirthday():
    remove=input("Who do you want to remove?: ")

    with open("Birthdays.json","r") as file:
        database=json.load(file)
    
    for b in database["birthdays"]:
        if b["name"]==remove:
            database["birthdays"].remove(b)
            print("Successfully removed",remove)


   
    with open("Birthdays.json","w") as file:
        json.dump(database,file, indent=4)


def showBirthday():
    with open("Birthdays.json","r") as file:
        database=json.load(file)

    sortedList = sorted(database["birthdays"], key=lambda x: x["name"])
    
    for p in range(len(database["birthdays"])):
        print(sortedList[p]["name"],end=" ")

    print()
    print("There are",len(database["birthdays"]),"records")
    print()


def findPerson(user):
    with open("Birthdays.json","r") as file:
        database=json.load(file)
    
    target=user.lower()

    for x in range(len(database["birthdays"])):
        if database["birthdays"][x]["name"].lower()==target:
            print()
            print("Yes they are added")
            print()



main()