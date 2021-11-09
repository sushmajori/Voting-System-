from datetime import date
import datetime 
import pytz 
import csv
import mysql.connector

# database connection
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "VotingSystem")
mycursor = db.cursor(buffered=True)


#Defining Functions
# Function for adding voter details
def AddVoterDetails():
    ch = int(input("How many Voter Do You want to Add: "))
    for i in range(1,ch+1):
        while(True):
            id = input('Enter Voter ID : ')
            while(len(id) != 6 or id.isnumeric() == False or id == None):
                print("Enter 6 Digit Unique Number Only")
                id = input('Enter Voter ID : ')

            query = "select VoterId from Voter where VoterId =%s" %(id)
            val = (id)
            mycursor.execute(query,val)
            # result = mycursor.fetchall()
            # for i in result:
            #     print(i[0])
            count = str(mycursor.rowcount)
            cnt = int(count)
            if(cnt>=1):
                print("Voter is already Present")
                continue

            name = input('Enter Voter Name :')
            location = input('Enter Voter Location :')
            dob = input('Enter Voter Date of Birth(DOB) :')
            todays_date = date.today()
            age = int(todays_date.year) - int(dob.split("-")[0])
            #print(age)
            if(age<18):
                print("Your Not allowed to Vote Because your age is less than 18")
                continue
            query = '''Insert Into Voter(VoterId,VoterName,VoterLocation,DOB) values(%s, %s, %s, %s)'''
            # Execute the sql query
            mycursor.execute(query,[id,name,location,dob])
            # Commit the data
            db.commit()
            print(' Voter Data Saved Successfully')
            break


# Function for Updating Voter details
def UpdateVoterDetails():
    while(True):
        id = input('Enter Voter ID : ')
        while(len(id) != 6 or id.isnumeric() == False or id == None):
            print("Enter 6 Digit Unique Number Only")
            id = input('Enter Voter ID : ')

        sql = "select * from Voter where VoterId = %s"
        mycursor.execute(sql, [id])
        item = mycursor.fetchone()
        count = str(mycursor.rowcount)
        cnt = int(count)
        if(cnt<1):
            print("Voter is Not Present")
            continue

        print("------------------------------------------------------------- Update Voter Details -------------------------------------------------------------------")  
        print('ID\t\t Voter Name\t\tVoter Location\t\tDate of Birth\t\t\t')
        print('{}\t\t {}\t\t\t {} \t\t{} '.format(item[0], item[1], item[2], item[3]))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")  
        print('Enter New Data To Update Voter Record ')
        name = input('Enter Voter Name :')
        location = input('Enter Voter Location :')
        dob = input('Enter Voter Date of Birth(DOB) :')
        todays_date = date.today()
        age = int(todays_date.year) - int(dob.split("-")[0])
        #print(age)
        if(age<18):
            print("Your Not allowed for Vote Because your age is less than 18")
            continue
        query = """Update Voter Set VoterName=%s, VoterLocation=%s, DOB=%s Where VoterId=%s"""
        mycursor.execute(query, (name,location,dob,id))
        #print("Row(s) were updated :" +  str(mycursor.rowcount))
        db.commit()
        print('Data Updated Successfully')
        break


#  Function for adding Nominee data
def AddNominee():
    ch = int(input("How many Nominee Do You want to Add: "))
    for i in range(1,ch+1):
        while(True):
            id = input('Enter Nominee ID : ')
            while(len(id) != 6 or id.isnumeric() == False or id == None):
                print("Enter 6 Digit Unique Number Only")
                id = input('Enter Nominee Voter ID : ')

            query = "select nominee_voterId from Nominee where nominee_voterId =%s" %(id)
            val = (id)
            mycursor.execute(query,val)
            # result = mycursor.fetchall()
            # for i in result:
            #     print(i[0])
            count = str(mycursor.rowcount)
            cnt = int(count)
            if(cnt>=1):
                print("Nominee is already Present")
                continue

            name = input('Enter Nominee Name :')
            location = input('Enter Nominee Location :')
            dob = input('Enter Nominee Date of Birth(DOB) :')
            todays_date = date.today()
            age = int(todays_date.year) - int(dob.split("-")[0])
            #print(age)
            if(age<28):
                print("Your Not allowed Because your age is less than 28")
                continue
            query = '''Insert Into Nominee(nominee_voterId,nominee_name,nominee_location,DOB) values(%s, %s, %s, %s)'''
            # Execute the sql query
            mycursor.execute(query,[id,name,location,dob])
            # Commit the data
            db.commit()
            print(' Nominee Data Saved Successfully')
            break

# function for Update Nominee Details
def UpdateNominee():
    while(True):
        id = input('Enter Nominee Voter ID : ')
        while(len(id) != 6 or id.isnumeric() == False or id == None):
            print("Enter 6 Digit Unique Number Only")
            id = input('Enter Nominee Voter ID : ')

        sql = "select * from Nominee where nominee_voterId = %s"
        mycursor.execute(sql, [id])
        item = mycursor.fetchone()
        count = str(mycursor.rowcount)
        cnt = int(count)
        if(cnt<1):
            print("Nominee is Not Present")
            continue

        print("------------------------------------------------------------- Update Voter Details -------------------------------------------------------------------")  
        print('ID\t\t Nominee Name\t\tNominee Location\t\tDate of Birth\t\t\t')
        print('{}\t\t {}\t\t\t {} \t\t{} '.format(item[0], item[1], item[2], item[3]))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")  
        print('Enter New Data To Update Nominee Record ')
        name = input('Enter Nominee Name :')
        location = input('Enter Nominee Location :')
        dob = input('Enter Nominee Date of Birth(DOB) :')
        todays_date = date.today()
        age = int(todays_date.year) - int(dob.split("-")[0])
        #print(age)
        if(age<28):
            print("Your Not allowed Because your age is less than 28")
            continue
        query = """Update Nominee Set nominee_name=%s, nominee_location=%s, DOB=%s Where nominee_voterId=%s"""
        mycursor.execute(query, (name,location,dob,id))
        #print("Row(s) were updated :" +  str(mycursor.rowcount))
        db.commit()
        print(' Nominee Data Updated Successfully')
        break


#function for voting 
def votingdetails():
    while(True):
        id = input("Enter your Voter ID: ")
        while(len(id) != 6 or id.isnumeric() == False or id == None):
            print("Enter 6 Digit Unique Number Only")
            id = input('Enter your Voter ID : ')
        query = "select voterid from voting_details where voterid =%s" %(id)
        val = (id)
        mycursor.execute(query,val)
                # result = mycursor.fetchall()
                # for i in result:
                #     print(i[0])
        count = str(mycursor.rowcount)
        cnt = int(count)

        if(cnt>=1):
            print("You have already voted ,re-voting is not allowed")
            print("Thanks for your valuable vote")
            break
        query = "select VoterId from Voter where voterid =%s" %(id)
        val = (id)
        mycursor.execute(query,val)
        count = str(mycursor.rowcount)
        cnt = int(count)
        if(cnt<1):
            print("Invalid Voting Id")
            break

        print("Select one of below Nominee for voting: ")
        statement = "select nominee_name from Nominee"
        mycursor.execute(statement)
        result = mycursor.fetchall()
        for i in result:
            print(i[0])
        Choose_nominee = input("Type the Name of Nominee that you want to vote")
        stmt = "select nominee_voterId from Nominee where nominee_name ='%s'" %(Choose_nominee)
        val = (Choose_nominee)
        mycursor.execute(stmt,(val))
        result = mycursor.fetchall()
        for i in result:
            nid = i[0]

        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 

        query = '''Insert Into voting_details(voterid,nominee_voter_id,voting_time) values(%s, %s, %s)'''
        # Execute the sql query
        mycursor.execute(query,[id,nid,current_time])
        # Commit the data
        db.commit()
        print('Thanks for your valuable vote')
        break


# function for displaying result of voting
def Result():
    stmt = "select count(voterid) from voting_details"
    mycursor.execute(stmt)
    result = mycursor.fetchall()
    for i in result:
        Total_voter_voted = i[0]
    
    # Count number of votes got by each Nominee
    statement = "select nominee_name as Nominee_Name, count(voterid) as Total_Number_of_Votes from Nominee n inner join voting_details v on n.nominee_voterId = v.nominee_voter_id group by nominee_name order by count(voterid) desc"
    mycursor.execute(statement)
    result = mycursor.fetchall()

    # Getting Winner in election
    query = "select nominee_name as Nominee_Name, count(voterid) as Total_Number_of_Votes from Nominee n inner join voting_details v on n.nominee_voterId = v.nominee_voter_id group by nominee_name order by count(voterid) desc"
    mycursor.execute(query)
    res = mycursor.fetchone()
   
    print("------------------------------------------------------------- Voting  Result -----------------------------------------------------------------------------------------")  
    print("Total Number Of Voter Voted: ",Total_voter_voted,"\n")
    print('Nominee Name\t\tTotal Number of Votes')
    for i in result:
        print(' {}\t\t                 {}\t\t'.format(i[0], i[1]),"\n")

    print("Winner of this election: ",res[0])

 # function for downloading result   
def DownloadResult():
    query = "select v.VoterName,n.nominee_name,vd.voting_time from Voter v inner join voting_details vd on v.VoterId = vd.voterid inner join Nominee n on vd.nominee_voter_id = n.nominee_voterId"
    mycursor.execute(query)
    result = mycursor.fetchall()
    voternames,nomineenames,times=[i[0] for i in result],[i[1] for i in result],[str(i[2]).split(' ')[1] for i in result]
    result=[]
    for i,j,k in zip(voternames,nomineenames,times):
        result.append((i,j,k))
    with open('Result_of_voting.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(['Voter','Nominee','time'])
        write.writerows(result)
    print("Your Voting Result CSV file is downloaded")
  
# creating options  
while True:  
    print("------------------------------------------------------------- Welcome to Voting System --------------------------------------------------------------------------------")  

    print("\nEnter Your Role: ")  
    print("1. Voter")  
    print("2. Election Commissioner")  
    print("3. Exit")  
    choice1 = int(input("Enter the Choice:"))  
  
    if choice1 == 1:  
        votingdetails()  

    elif choice1 == 2:  
        print("\n Choose the Operations that you want to Perform")  
        print("1. Add Voter")  
        print("2. Update Voter")  
        print("3. Add Nominee")
        print("4. Update Nominee")  
        print("5. See Result")  
        print("6. Download voting Result in CSV File")  
        print("7. Exit")  
        choice3 = int(input("Enter the Choice:"))  
  
        if choice3 == 1:  
            AddVoterDetails()  
        elif choice3 == 2:  
            UpdateVoterDetails()              
        elif choice3 == 3:  
            AddNominee()

        elif choice3 == 4:  
            UpdateNominee()
        
        elif choice3 == 5:  
            Result()

        elif choice3 == 6:  
            DownloadResult()  
            
        elif choice3 == 7:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 3:  
        break  
      
    else:  
        print("Oops! Incorrect Choice.")  
