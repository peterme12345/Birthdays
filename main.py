import json


def main():

    menu=input("Please select an option:\n" 
    "1. Start\n" \
    "2. Display\n"
    "3. Enter birthday\n" \
    "4. Delete birthday\n" \
    "5. Quit\n" \
        "Answer: ")

    if int(menu)==2:
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
        print("Program terminated")

    elif menu.isalpha():
        print("Please type a number!")
        main()

    else:
        main()


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

    print(json.dumps(database, indent=4))


main()