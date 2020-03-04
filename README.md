# Job_REST_API

Instruction to run Job_server application
This application is made in python 3.8 ( compitable for python 3.7 and 3.6). I have used pep8 and pylint to check coding standards.

Installation: Use tox to run the application
Tox installation:

Browse to the project location in the command prompt and run

python -m tox

This command will install the application in python 3.7 and python 3.8. For any specific version please run

tox -e py38

Application will be running in localhost:5000

I installed this in my personal windows machine for python 3.7 and 3.8

Tox will run first job_insertion.py to insert the jobs listed in job_listing.csv. Then it will run Job_server.py to start the REST API for the job server.



Usage:

Application has two part,

1. Insert the available jobs listed in job_listing.csv
2. Start RESTful APi for job server

job_insertion.py file read the csv file and insert all the listed job offer in sqlite3 database.

Then Job_server.py will start REST API for the job server. Server will start at localhost:5000

a) POST a job:

Use the following curl command to post a job

curl -X POST -H "Content-Type: application/json" -d "{ \"Title\": \"Python developer\", \"Description\": \"Backend Developer\",\"Company\": \"Google\",\"Location\": \"Frankfurt\",\"Job_Catagory\": \"Engineering\" }" http://localhost:5000/postjob

b) SHOW all available job:

Open browser and type

http://localhost:5000/showjob

This will show all the stored job offer along with pagination


c) Update a specific job:

Lets assume we want to update the job id 2

Use the following curl command to update the job offer

curl -X PATCH -H "Content-Type: application/json" -d "{ \"Id\": \"2\", \"Title\": \"Python developer\", \"Description\": \"Backend Developer\"}" http://localhost:5000/updatejob

d) Retrieve locations and categories with most of jobs:

Open browser and type the following

http://localhost:5000/location

This will show you job offer group by location and job category




