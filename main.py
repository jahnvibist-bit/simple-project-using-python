import csv
import os

student="students.csv"

def csvfile():
    if not os.path.exists(student) or os.stat(student).st_size==0:
        with open(student,'w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["Name","Roll","DOB","Age","Marks","Stream"])

def add():
    try:
        name=input("Enter your name:").capitalize()
        rollno=input("Enter your roll.no:")
        dob=input("Enter your birthdate:")
        age=input("Enter your age:")
        marks=input("Enter your total percentile marks:")
        stream=input("Enter your stream:")
        with open(student,"a",newline='')as a:
            csv.writer(a).writerow([name,rollno,dob,age,marks,stream])
        print("Student added successfully")
    except Exception as e:
        print("Error:",e)

def view():
    with open(student,'r',newline='')as r:
        read=csv.reader(r)
        for i in read:
            print(i)

def search():
    try:
        a=input("Do you want to search?(yes/no):").lower()
        while a=="yes":
            rollno=input("Enter roll number:")
            found=False
            with open(student,'r',newline='')as f:
                read=csv.reader(f)
                next(read)
                for i in read:
                    if i[1]==rollno:
                        print("Found:",i)
                        found=True
                        break
            if not found:
                print("Not found")
            a=input("Search again?(yes/no):").lower()
    except Exception as e:
        print("Error:",e)

def update():
    name=input("Enter name to update:").capitalize()
    found=False
    new=[]
    with open(student,'r',newline='')as f:
        read=csv.reader(f)
        for i in read:
            if i[0]==name:
                print("1.Name 2.Roll 3.Age 4.Marks 5.Stream 6.DOB 7.Exit")
                while True:
                    c=int(input("Choice:"))
                    if c==1:i[0]=input("New name:").capitalize()
                    elif c==2:i[1]=input("New roll:")
                    elif c==3:i[3]=input("New age:")
                    elif c==4:i[4]=input("New marks:")
                    elif c==5:i[5]=input("New stream:")
                    elif c==6:i[2]=input("New dob:")
                    elif c==7:break
                found=True
            new.append(i)
    with open(student,'w',newline='')as f:
        csv.writer(f).writerows(new)
    if not found:
        print("Not found")

def delete():
    name=input("Enter name to delete:").capitalize()
    found=False
    new=[]
    with open(student,'r',newline='')as f:
        read=csv.reader(f)
        for i in read:
            if i[0]==name:
                found=True
                continue
            new.append(i)
    with open(student,'w',newline='')as f:
        csv.writer(f).writerows(new)
    if found:print("Deleted")
    else:print("Not found")

csvfile()

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.View 6.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:add()
    elif ch==2:search()
    elif ch==3:update()
    elif ch==4:delete()
    elif ch==5:view()
    elif ch==6:break
    else:print("Invalid")