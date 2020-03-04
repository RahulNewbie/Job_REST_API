from flask import Flask, render_template
from flask import request
import json
import logging
from logging.handlers import RotatingFileHandler
import datetime
import os
import ast
import constants
import db_api

app = Flask(__name__)


@app.route('/postjob', methods=['POST'])
def insert_job():
    """
    This method is responsible for posting new job offer into the database
    """
    if request.is_json:
        # Get the json data from request
        content = request.get_json()
        # Insert the job offer into database
        db_api.insert_to_db(content['Title'], content['Description'],
                            content['Company'], content['Location'],
                            content['Job_Catagory'])

        return 'New Job offer with title ' + content['Title'] + \
            ' posted successfully', constants.SUCCESS_STATUS
    else:
        return 'Please post new job offer in Json format'


@app.route('/showjob')
def show_all_jobs():
    """
    Function to show the all the job offer from table data
    """
    try:
        data = db_api.select_all_job_offer()
    except Exception as excep:
        app.logger.error('Error occurred while showing screenshot data'
                         + str(excep))
    return render_template('index.html', rows=data)


@app.route('/updatejob', methods=['PATCH'])
def update_job():
    """
    Updating a job offer using Job id as key
    """
    if request.is_json:
        content = request.get_json()
        try:
            if 'Title' in content.keys():
                db_api.update_job_offer(content['Id'], content['Title'])
            if 'Description' in content.keys():
                db_api.update_job_offer(content['Id'], None, content['Description'])
            if 'Company' in content.keys():
                db_api.update_job_offer(content['Id'], None, None,
                                        content['Company'])
            if 'Location' in content.keys():
                db_api.update_job_offer(content['Id'], None, None,
                                        None, content['Location'])
            if 'Job_Category' in content.keys():
                db_api.update_job_offer(content['Id'], None, None, None,
                                        None, content['Job_Category'])

            return "Job offer updating successful"
        except Exception as excep:
            return "Error happened while updating job offer " + str(excep)
    else:
        return 'Job updating unsuccessful, Please use proper json format'


@app.route('/location')
def get_location_of_max_job_offers():
    """
    Get the comprehensive list of job offers grouped by locations
    and category
    """
    location_dict = {}
    location_data = db_api.get_location_category()
    # Converting result into a list
    location_list = ast.literal_eval(location_data)
    # Accessing each item and forming dictionary
    for item in location_list:
        location_dict.setdefault(item[0], []).append(item[1])
    # COnverting into json format
    location_data_json = json.dumps(location_dict)
    return location_data_json


if __name__ == '__main__':
    # Logging
    handler = RotatingFileHandler('app_logger.log', maxBytes=10000,
                                  backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)