# KonfHub

Task Overview: 

There is an API that provides the list of upcoming technical conferences. 
When you do a GET call for this REST API, you will get the list of conferences and their details in JSON format:   

The key and values for the JSON entries are self-explanatory. For example, some of the entries are: 
	… 
"confUrl": "https://futureconevents.com/events/san-antonio/", 
"confStartDate": "06 Nov, 2019", 
"entryType": "Paid",
 … 

 Technology used: Python 
 NOTE: Source code is available in .py file


Task: 

    1.Printing the contents in a human readable format, e.g.: “San Antonio CyberSecurity Conference”, 
    November 6th, 2019, San Antonio, TX, US, Paid. https://futureconevents.com/events/san-antonio/” 

    2.Identifying exact duplicates (if any) and removed it.
    
    3.Identifying semantic duplicates (i.e., the conferences are same but the details provided are slightly different, 
    e.g., “React Conference 2019” in one entry and “ReactConf ‘19” 
    in another entry but the other fields are same or similar). 
