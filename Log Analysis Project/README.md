Log Analysis Project Readme
=======

Background
------

This code is written for a project for my Udacity Introduction to Web Programming Nanodegree. The project is to write python code that will return information from an PostreSQL database. This information relates to the fictional records of a newspaper. 

There are three questions that need to be answered by this code: 

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

The project specifies that the answers are returned in a certain format, and that only one PostreSQL query is used. 


How to run the Log Analysis Project python code
------

Udacity have a vagrant virtual machine. The first step to running this code is to install that virtual machine to your computer. Udacity have provided some dummy data for this project in a file called newsdata.sql. This needs to be downloaded and saved to your computer. 

In order to run the Log_Analysis_Project.py you must first save it into the vagrant file on your computer. This must be the same place where you have saved newsdata.sql.

Then you load your vagrant virtual machine by running vagrant up and then vagrant ssh from the command line when you are in the vagrant directory. 

You then write 'cd \vagrant' into the command line of the virtual machine.

You can run test PostreSQL queries from here by running 'psql -d news -f newsdata.sql' in the command line and then 'psql -d news'.

In order to run the python file that I have written for this project type 'python Log_Analysis_Project.py' into your command line. This should give you the same answers as I got, which you can see in 'Example_Output.txt'. 

About the code
------

It is used to present information relating to multiple tables in a database in a clear and easy to read manner. The information that it pulls out is the type of information that would be useful to someone with an online media presence. 

I have check the code with Pep8 and no issues arise. 

I have had one review from a Udacity reviewer who made some suggestions to 'Log_Analysis_Project.py'. You can see the changes is the version history of that file. They also recommended that I expanded this Readme.
