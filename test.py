import pandas as pd


data = pd.read_csv("emp_data.csv")

def display_data():
    print(data)


while True:
    print("Menu")
    print("1. Display data")
    print("2. Add data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Save and Exit!")

    ch=int(input("Enter your choice: "))

    if ch==1:
        display_data()
    
    elif ch==2:
        new_emp={
            'emp_id' : int(input("Enter emp_id: ")),
            'emp_name' : input("Enter emp_name: "),
            'dob' : input("Enter dob: "),
            'doj' : input("Enter doj: ")
        }
        data.append(new_emp,ignore_index=True)
        data.to_csv('emp_data.csv', index=False)
        print("New Employee data added Successfully!")

    elif ch==3:
        emp_id=int(input("Enter emp_id to update data: "))
        up=input("Enter what you want to update (emp_name/doj/dob): ")

        if(up=='emp_name'):
            new_name=input("Enter new emp_name: ")
            data.loc[data['emp_id']==emp_id,'emp_name']=new_name
            data.to_csv('emp_data.csv', index=False)
        
        elif up=='dob':
            new_dob=input("Enter new dob: ")
            data.loc[data['emp_id']==emp_id,'dob']=new_dob
            data.to_csv('emp_data.csv', index=False)

        elif up=='doj':
            new_doj=input("Enter new doj: ")
            data.loc[data['emp_id']==emp_id,'doj']=new_doj
            data.to_csv('emp_data.csv', index=False)
        
        else:
            print("Enter valid option!")
    
    elif ch==4:
        emp_id=int(input("Enter emp_id to delete: "))
        data = data[data['emp_id']!=emp_id]
        data.to_csv('emp_data.csv', index=False)
        print("Employee deleted succesfully!")
    
    elif ch==5:
        data.to_csv('emp_data.csv', index=False)
        print("Data saved. Exiting program.")
        break

    else:
        print("Invalid choice! Enter valid choice!")
