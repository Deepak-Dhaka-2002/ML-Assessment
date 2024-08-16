# ML-Assessment
This repository contains solutions for the following tasks:
1. Password Strength Evaluation
2. Prime Factorization
3. SQL Query for Retrieving Posts from Friends

## Requirements
To run the Python scripts in this project, ensure you have the following installed:
- Python 3.6 or higher

## Setup Instructions
Q1 - 
   1. Clone the Repository:
      
     git clone https://github.com/Deepak-Dhaka-2002/ML-Assessment.git
     cd ML-Assessment
   2. Create a Virtual Environment (optional but recommended):
   
     python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate
   3. Install req libary(No need to run this here):

     pip install -r requirements.txt
   4. Run the script -

     python password_strength.py

Q2 - Run second que script - 

       python prime_factorization.py

Q3 - The SQL query to retrieve posts made by friends can be found in the retrieve_posts.sql file. You can run this query in your SQL database environment.

     SELECT p.*
     FROM posts p
     JOIN friends f ON p.user_id = f.friend_id
     WHERE f.user_id = 'current_user_id';
