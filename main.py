import json


def main():

    menu=int(input("Please select an option:\n" 
    "1. Start\n" \
    "2. Display\n"
    "3. Enter birthday\n" \
    "4. Delete birthday\n" \
    "5. Quit\n"))

    if menu==2:
        showBirthday()
        main()

    elif menu==3:
        addBirthday()
        choice=input("Add another?: ")
        while choice=="y":
            addBirthday()
            choice=input("Add another?: ")
        main()
        
    elif menu==4:
        removeBirthday()
        while choice=="y":
            addBirthday()
            choice=input("Remove another?: ")
        main()

    elif menu==5:
        print("Program terminated")


def addBirthday():
    person={}
    person["name"]=name=input("Enter name: ")
    person["month"]=month=int(input("Enter month as a number: "))
    person["day"]=day=int(input("Enter day as a number: "))

    
    with open("Birthdays.json","a") as f:
        json.dump(person, f, indent=4)
    

    print("Successfully added: ",person["name"])

def removeBirthday():
    remove=input("Who do you want to remove?: ")

def showBirthday():
    with open("Birthdays.json","r") as f:
        data=json.loads(f)
    print(json.dumps(data, indent=4))

main()