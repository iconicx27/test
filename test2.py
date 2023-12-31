import pandas as pd

df = pd.read_csv('read.csv')

 

# Display the initial data
def display_data():
    print("\nEmployee Data:")
    print(df)

 

while True:
    print("\nMenu:")
    print("1. Display Employee Data")
    print("2. Add New Employee")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Exit")

 

    choice = input("Enter your choice (1/2/3/4/5): ")

 

    if choice == '1':
        display_data()
    elif choice == '2':
        new_employee = {
           
            'emp_name': input("Enter First Name: "),
             'emp_id': int(input("Enter EmployeeID: ")),
            'salary': float(input("Enter Salary: "))
        }
        df = df.append(new_employee, ignore_index=True)
        print("New employee added.")
        display_data()
    elif choice == '3':
        employee_id = int(input("Enter EmployeeID to update salary: "))
        new_salary = float(input("Enter the new salary: "))
        df.loc[df['emp_id'] == employee_id, 'salary'] = new_salary
        print("Salary updated.")
        display_data()
    elif choice == '4':
        employee_id = int(input("Enter EmployeeID to delete: "))
        df = df[df['emp_id'] != employee_id]
        print("Employee deleted.")
        display_data()
    elif choice == '5':
        # Save the updated data back to the CSV file and exit
        df.to_csv('employee_data.csv', index=False)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
