import pandas as pd

df = pd.read_csv('employees.csv')


# Display Data
def display_data():
    print("\nEmployee Data:")
    print(df)


while True:
    print("\nMenu:")
    print("1. Display Employee Data")
    print("2. Add New Employee")
    print("3. Update Employee Designation")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        display_data()
    elif choice == '2':
        new_employee = {
           
            'empname': input("Enter Employee Name: "),
             'empno': int(input("Enter EmployeeID: ")),
            'dept': input("Enter Department: "),
            'designation': input("Enter Designation: ")
        }
        df = df._append(new_employee, ignore_index=True)
        print("New employee added.")
        display_data()
    elif choice == '3':
        employee_id = int(input("Enter EmployeeID to update Designation: "))
        new_desg = input("Enter the updated Designation: ")
        df.loc[df['empno'] == employee_id, 'designation'] = new_desg
        print("Designation updated.")
        display_data()
    elif choice == '4':
        employee_id = int(input("Enter EmployeeID to delete: "))
        df = df[df['empno'] != employee_id]
        print("Employee deleted.")
        display_data()
    elif choice == '5':
        # Saving the updated data back to the CSV file and exit
        df.to_csv('employees.csv', index=False)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
