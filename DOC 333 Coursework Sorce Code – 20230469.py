# Initializing Variables
no_workers = 50
no_projects = 0
upd_dtls = 0
n_workers = 0
s_date=0
end_date=0
proj_codes=0
clt_name=0
pro_status=0
upd_dtls=0
index = 0

# Lists to store project Details
allprojects = []
proj_codes = []
rem_codes = []

# Counters for project statistics
ong_projects = 0
completed = 0
hold_projects = 0

# Main program loop
while True:
    # Display menu options
    print()
    print()
    print()
    print("1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to the available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project Statistics")
    print("6. Exit")

    # User input for menu option
    opt = int(input("Enter an option to continue: "))
    
    # Option 1: Add a new project
    if opt == 1:
        print("XYZ Company".center(75))
        print("Add a New Project".center(75))
        
        # User input for project details
        p_code = int(input("Enter the project code: "))
        if p_code in proj_codes:
            print("This project code already exists. Please enter a new project code.")
        else:
            clt_name = input("Enter the client's Name: ")
            s_date = input("Enter The Starting Date: ")
            end_date = input("Enter the ending date: ")
            n_workers = int(input("Number of workers: "))
            pro_status = str(input("Project Status (ongoing, hold, or completed): "))
            upd_dtls = input("If You Want to Update Details (yes/no)?")

            # Check if there are enough workers
            if no_workers >= n_workers:
                print()
                if upd_dtls == "yes":
                    # Update project details
                    # Update project details
                    projects=[]
                    no_projects += 1
                    no_workers -= n_workers
                    projects.append(p_code)
                    proj_codes.append(p_code)
                    projects.append(clt_name)
                    projects.append(s_date) 
                    projects.append(end_date)
                    projects.append(n_workers)
                    projects.append(pro_status)
                    allprojects.append(projects)


                    # Update project statistics based on status
                    if pro_status == "completed":
                        completed += 1
                    elif pro_status == "hold":
                        hold_projects += 1
                    else:
                        ong_projects += 1

                    print("Project Details Updated, Thank you")
                else:
                    print("Project details not Updated")
            else:
                print("Workers are not sufficient, add workers from option 3")

    # Option 2: Remove a completed project
    elif opt == 2:
        print("XYZ Company".center(75))
        print("Remove Completed Project".center(75))
        
        # User input for project code to remove
        p_code = int(input("Enter The Project code to remove: "))
        upd_dtls = input("If you want to remove project (yes/no)?")

        if upd_dtls == "yes":
            # Check if the project code exists
            if p_code in proj_codes:
                rem_codes.append(p_code)
                index = proj_codes.index(p_code)
                no_workers = no_workers + allprojects[index][4]
                del allprojects[index]
                proj_codes.remove(p_code)
                completed += 1
                ong_projects -= 1
                print()
                print()
                print()
            else:
                print("Project Code not found.")
        else:
            print("Project Not Removed")

    # Option 3: Add workers
    elif opt == 3:
        print("XYZ Company".center(75))
        print("Add Workers".center(75))
        
        # User input for the number of workers to add
        n_workers = int(input("Number of workers to add: "))
        upd_dtls = input("If you want to update the number of workers (yes/no)?")

        # Check if the user wants to update the number of workers
        if upd_dtls == "yes":
            no_workers += n_workers
            print("Number of workers updated, Thank you")
            print("No of Workers available", no_workers)
        else:
            print("Sorry, the number of workers is not updated")
    
    elif opt == 4:
        print("XYZ Company".center(75))
        print("Update Details on ongoing Projects".center(75))
        p_code = int(input("Project Code: "))

        # Check if the project code exists
        if p_code in proj_codes:
            clt_name = input("Enter the client's Name: ")
            s_date = input("Enter The Starting Date: ")
            end_date = input("Enter the ending date: ")
            n_workers = int(input("Number of workers: "))
            pro_status = str(input("Project Status (ongoing, hold, or completed): "))
            upd_dtls = input("If you want to update the project details (yes/no)?")

            if upd_dtls == "yes":
                allprojects[index][1] = clt_name
                allprojects[index][2] = s_date
                allprojects[index][3] = end_date
                allprojects[index][4] = n_workers
                allprojects[index][5] = pro_status

                # Update project statistics based on status
                if (pro_status == "completed"):
                    completed += 1
                    ong_projects -= 1
                    no_workers += n_workers
                if (pro_status == "hold"):
                    hold_projects += 1
                    ong_projects -= 1
                    no_workers += n_workers
                if (pro_status == "ongoing"):
                 print(allprojects)
                 print("Project details updated successfully!")


            elif upd_dtls == "no":
                print("Sorry Project Details Not Updated")
                print(allprojects)
        else:
            print("This project code does not exist. Please enter a valid project code.")

    # Option 5: Display project statistics
    elif opt == 5:
        print("XYZ Company".center(75))
        print("Project Statistics".center(75))
        print("Number of ongoing projects -", ong_projects)
        print("Number of completed projects -", completed)
        print("Number of on-hold projects -", hold_projects)
        print("Number of available workers to assign -", no_workers)

    # Option 6: Exit the program
    elif opt == 6:
        print("Exiting Programme...")
    # Invalid option    
    else:
        print("Invalid choice. Please select a number between 1-6")
