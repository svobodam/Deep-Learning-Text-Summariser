#!/usr/bin/env python
# Author: Matej Svoboda
# Python Script to create SQLITE Database

TopicNo = 'D0701A'
TopicName = 'Southern Poverty Law Center'
TopicDesc = 'Describe the activities of Morris Dees and the Southern Poverty Law Center.'
DocumentNo1 = 'APW19990612.0141'
DocumentName1 = 'Supremacist Wanted Everyone Dead'
Docurl1 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW19990612.txt.txt')
Document1 = Docurl1.read()
DocumentNo2 = 'APW19991013.0008'  
DocumentName2 = 'City Calls KKK a Terrorist Group'
Docurl2 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW19991013.txt.txt')
Document2 = Docurl2.read()
DocumentNo3 = 'APW20000824.0204'
DocumentName3 = 'Aryan Nations Threatened by Lawsuit'
Docurl3 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW20000824.txt.txt')
Document3 = Docurl3.read()
DocumentNo4 = 'APW20000831.0201'
DocumentName4 = 'Aryan Nations Guards Testify'
Docurl4= open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW20000831.txt.txt')
Document4 = Docurl4.read()
DocumentNo5 = 'APW20000907.0208' 
DocumentName5 = 'Jury: Aryans To Pay $6.3M in Suit'
Docurl5 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW20000907.txt.txt')
Document5 = Docurl5.read()
DocumentNo6 = 'APW20000908.0184'
DocumentName6 = 'Idahos Racist Image May Change'
Docurl6 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW20000908.txt.txt')
Document6 = Docurl6.read()
DocumentNo7 = 'APW20000909.0144'
DocumentName7 = 'Butler: Racists To Stay in Idaho'
Docurl7 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW20000909.txt.txt') 
Document7 = Docurl7.read()
DocumentNo8 = 'APW20000915.0189' 
DocumentName8 = 'Aryan Nations May Meet in Pa.'
Docurl8 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/APW20000915.txt.txt')
Document8 = Docurl8.read()
DocumentNo9 = 'NYT19980715.0137'
DocumentName9 = 'SINEADS RAGE; GUILT-FREE GUYNESS'
Docurl9 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19980715.txt.txt')
Document9 = Docurl9.read()
DocumentNo10 = 'NYT19990227.0130'
DocumentName10 = 'HT'
Docurl10 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990227.txt.txt')
Document10 = Docurl10.read()
DocumentNo11 = 'NYT19990227.0073'
DocumentName11 = 'COMMENTARY: STARING AT HATRED'
Docurl11 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990228.txt.txt')
Document11 = Docurl11.read()
DocumentNo12 = 'NYT19990302.0069'
DocumentName12 = 'STOPPING HATE BEFORE IT KILLS'
Docurl12 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990302.txt.txt')
Document12 = Docurl12.read()
DocumentNo13 = 'NYT19990304.0376'
DocumentName13 = 'Neo-Nazis next target of lawyer who broke Klan'
Docurl13 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990304.txt.txt')
Document13 = Docurl13.read()
DocumentNo14 = 'NYT19990822.0227'
DocumentName14 = 'WILBERT OLIVER, 89, WHO INFLUENCED FUNERAL-HOME POLICY'
Docurl14 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990822.txt.txt')
Document14 = Docurl14.read()
DocumentNo15 = 'NYT19990825.0042'
DocumentName15 = 'ATTENTION EDITORS: The following material is for use only by'
Docurl15 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990825.txt.txt')
Document15 = Docurl15.read()
DocumentNo16 = 'NYT19990827.0030'
DocumentName16 = 'RICHARD BUTLER SPAWNS RACISM FROM HIS IDAHO COMPOUND'
Docurl16 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990827.txt.txt')
Document16 = Docurl16.read()
DocumentNo17 = 'NYT19990920.0232'
DocumentName17= 'IN EAST PEORIA, AN INTOLERANCE FOR HATE'
Docurl17 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19990920.txt.txt')
Document17 = Docurl17.read()
DocumentNo18 = 'NYT19991031.0076'
DocumentName18 = 'CALIFORNIA JUDGE RULES REPORTER CAN REFUSE TO DISCLOSE MATERIALS'
Docurl18 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19991031.txt.txt')
Document18 = Docurl18.read()
DocumentNo19 = 'NYT19991107.0075'
DocumentName19 = 'UNRESOLVED RACIAL MURDERS ARE BEING RE-EXAMINED'
Docurl19 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT19991107.txt.txt')
Document19 = Docurl19.read()
DocumentNo20 = 'NYT20000711.0211'
DocumentName20 = 'DISTURBING LOOKS AT THE SPREAD OF HATRED ON THE WEB'
Docurl20 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT20000711.txt.txt')
Document20 = Docurl20.read()
DocumentNo21 = 'NYT20000828.0403'
DocumentName21 = 'COURTHOUSE KLAN-FIGHTER TAKES ON ARYAN NATIONS'
Docurl21 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT20000828.txt.txt')
Document21 = Docurl21.read()
DocumentNo22 = 'NYT20000902.0043'
DocumentName22 = 'NEWS OF THE WEEK IN REVIEW'
Docurl22 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT20000902.txt.txt')
Document22 = Docurl22.read()
DocumentNo23 = 'NYT20000907.0438'
DocumentName23 = 'LEADERS OF ARYAN NATIONS FOUND NEGLIGENT IN ATTACK'
Docurl23 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT20000907.txt.txt')
Document23 = Docurl23.read()
DocumentNo24 = 'NYT20000908.0026'
DocumentName24 = 'LEADERS OF ARYAN NATIONS FOUND NEGLIGENT IN ATTACK'
Docurl24 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/NYT20000908.txt.txt')
Document24 = Docurl24.read()
DocumentNo25 = 'XIE19980304.0061'
DocumentName25 = 'Report: Hate Groups Growing in United States'
Docurl25 = open('/home/mathias/Desktop/summCode/Data/Topics/D0701A/XIE19980304.txt.txt')
Document25 = Docurl25.read()
Sumurl1 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.10.txt')
Sum1 = Sumurl1.read()
Sumurl2 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.11.txt')
Sum2 = Sumurl2.read()
Sumurl3 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.12.txt')
Sum3 = Sumurl3.read()
Sumurl4 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.13.txt')
Sum4 = Sumurl4.read()
Sumurl5 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.14.txt')
Sum5 = Sumurl5.read()
Sumurl6 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.15.txt')
Sum6 = Sumurl6.read()
Sumurl7 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.16.txt')
Sum7 = Sumurl7.read()
Sumurl8 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.17.txt')
Sum8 = Sumurl8.read()
Sumurl9 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.18.txt')
Sum9 = Sumurl9.read()
Sumurl10 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.19.txt')
Sum10 = Sumurl10.read()
Sumurl11 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.20.txt')
Sum11 = Sumurl11.read()
Sumurl12 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.21.txt')
Sum12 = Sumurl12.read()
Sumurl13 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.22.txt')
Sum13 = Sumurl13.read()
Sumurl14 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.23.txt')
Sum14 = Sumurl14.read()
Sumurl15 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.24.txt')
Sum15 = Sumurl15.read()
Sumurl16 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.25.txt')
Sum16 = Sumurl16.read()
Sumurl17 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.26.txt')
Sum17 = Sumurl17.read()
Sumurl18 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.27.txt')
Sum18 = Sumurl18.read()
Sumurl19 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.28.txt')
Sum19 = Sumurl19.read()
Sumurl20 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.29.txt')
Sum20 = Sumurl20.read()
Sumurl21 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.2.txt')
Sum21 = Sumurl21.read()
Sumurl22 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.30.txt')
Sum22 = Sumurl22.read()
Sumurl23 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.31.txt')
Sum23 = Sumurl23.read()
Sumurl24 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.32.txt')
Sum24 = Sumurl24.read()
Sumurl25 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.3.txt')
Sum25 = Sumurl25.read()
Sumurl26 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.4.txt')
Sum26 = Sumurl26.read()
Sumurl27 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.5.txt')
Sum27 = Sumurl27.read()
Sumurl28 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.6.txt')
Sum28 = Sumurl28.read()
Sumurl29 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.7.txt')
Sum29 = Sumurl29.read()
Sumurl30 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.8.txt')
Sum30 = Sumurl30.read()
Sumurl31 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.9.txt')
Sum31 = Sumurl31.read()
Sumurl32 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.A.txt')
Sum32 = Sumurl32.read()
Sumurl33 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.G.txt')
Sum33 = Sumurl33.read()
Sumurl34 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.H.txt')
Sum34 = Sumurl34.read()
Sumurl35 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D0701.M.250.A.I.txt')
Sum35 = Sumurl35.read()
Sumurl36 = open('/home/mathias/Desktop/summCode/Data/Summaries/D0701A/D070.txt')
Sum36 = Sumurl36.read()
 
# Import libraries
import sqlite3
sqlConnection = sqlite3.connect('/home/mathias/Desktop/summCode/Data/DUCDataset.db')

c = sqlConnection.cursor()

# Create table summDUC
c.execute('''CREATE TABLE summDUC(TopicNo, TopicName, TopicDesc, DocumentNo1, DocumentName1, Document1, DocumentNo2, DocumentName2, Document2, DocumentNo3, DocumentName3, Document3, DocumentNo4, DocumentName4, Document4, DocumentNo5, DocumentName5, Document5, DocumentNo6, DocumentName6, Document6, DocumentNo7, DocumentName7, Document7, DocumentNo8, DocumentName8, Document8, DocumentNo9, DocumentName9, Document9, DocumentNo10, DocumentName10, Document10, DocumentNo11, DocumentName11, Document11, DocumentNo12, DocumentName12, Document12, DocumentNo13, DocumentName13, Document13, DocumentNo14, DocumentName14, Document14, DocumentNo15, DocumentName15, Document15, DocumentNo16, DocumentName16, Document16, DocumentNo17, DocumentName17, Document17, DocumentNo18, DocumentName18, Document18, DocumentNo19, DocumentName19, Document19, DocumentNo20, DocumentName20, Document20, DocumentNo21, DocumentName21, Document21, DocumentNo22, DocumentName22, Document22, DocumentNo23, DocumentName23, Document23, DocumentNo24, DocumentName24, Document24, DocumentNo25, DocumentName25, Document25, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7, Sum8, Sum9, Sum10, Sum11, Sum12, Sum13, Sum14, Sum15, Sum16, Sum17, Sum18, Sum19, Sum20, Sum21, Sum22, Sum23, Sum24, Sum25, Sum26, Sum27, Sum28, Sum29, Sum30, Sum31, Sum32, Sum33, Sum34, Sum35, Sum36)''')

# Insert data
c.execute("INSERT INTO summDUC (TopicNo, TopicName, TopicDesc, DocumentNo1, DocumentName1, Document1, DocumentNo2, DocumentName2, Document2, DocumentNo3, DocumentName3, Document3, DocumentNo4, DocumentName4, Document4, DocumentNo5, DocumentName5, Document5, DocumentNo6, DocumentName6, Document6, DocumentNo7, DocumentName7, Document7, DocumentNo8, DocumentName8, Document8, DocumentNo9, DocumentName9, Document9, DocumentNo10, DocumentName10, Document10, DocumentNo11, DocumentName11, Document11, DocumentNo12, DocumentName12, Document12, DocumentNo13, DocumentName13, Document13, DocumentNo14, DocumentName14, Document14, DocumentNo15, DocumentName15, Document15, DocumentNo16, DocumentName16, Document16, DocumentNo17, DocumentName17, Document17, DocumentNo18, DocumentName18, Document18, DocumentNo19, DocumentName19, Document19, DocumentNo20, DocumentName20, Document20, DocumentNo21, DocumentName21, Document21, DocumentNo22, DocumentName22, Document22, DocumentNo23, DocumentName23, Document23, DocumentNo24, DocumentName24, Document24, DocumentNo25, DocumentName25, Document25, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7, Sum8, Sum9, Sum10, Sum11, Sum12, Sum13, Sum14, Sum15, Sum16, Sum17, Sum18, Sum19, Sum20, Sum21, Sum22, Sum23, Sum24, Sum25, Sum26, Sum27, Sum28, Sum29, Sum30, Sum31, Sum32, Sum33, Sum34, Sum35, Sum36) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (TopicNo, TopicName, TopicDesc, DocumentNo1, DocumentName1, Document1, DocumentNo2, DocumentName2, Document2, DocumentNo3, DocumentName3, Document3, DocumentNo4, DocumentName4, Document4, DocumentNo5, DocumentName5, Document5, DocumentNo6, DocumentName6, Document6, DocumentNo7, DocumentName7, Document7, DocumentNo8, DocumentName8, Document8, DocumentNo9, DocumentName9, Document9, DocumentNo10, DocumentName10, Document10, DocumentNo11, DocumentName11, Document11, DocumentNo12, DocumentName12, Document12, DocumentNo13, DocumentName13, Document13, DocumentNo14, DocumentName14, Document14, DocumentNo15, DocumentName15, Document15, DocumentNo16, DocumentName16, Document16, DocumentNo17, DocumentName17, Document17, DocumentNo18, DocumentName18, Document18, DocumentNo19, DocumentName19, Document19, DocumentNo20, DocumentName20, Document20, DocumentNo21, DocumentName21, Document21, DocumentNo22, DocumentName22, Document22, DocumentNo23, DocumentName23, Document23, DocumentNo24, DocumentName24, Document24, DocumentNo25, DocumentName25, Document25, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7, Sum8, Sum9, Sum10, Sum11, Sum12, Sum13, Sum14, Sum15, Sum16, Sum17, Sum18, Sum19, Sum20, Sum21, Sum22, Sum23, Sum24, Sum25, Sum26, Sum27, Sum28, Sum29, Sum30, Sum31, Sum32, Sum33, Sum34, Sum35, Sum36))


# Save changes
sqlConnection.commit()

# Retrieve data from DB
t = ('RHAT',)
for row in c.execute('SELECT * FROM summDUC'):
 print(row)

# Close connection to DB
sqlConnection.close()
