import csv
from multiprocessing.dummy import Manager
import random
from datetime import datetime , timedelta
random.seed(42)
import pandas as pd
from faker import Faker

random.seed(42)
Faker.seed(42)
fake = Faker()
faker_in = Faker('en_IN')


gender = ['Male' , 'Female']
departments = ['IT' , 'Marketing' , 'Research and Development']
IT_job_roles = ['software engineer' , 'data scientist', 
             'ML engineer' , 'data analytics']
marketing_job_roles = ['Marketing Manager' , 'Digital Marketing Specialist' , 'Marketing Analyst' , 'SEO Specialist' , 'Content Marketing Manager']
research_job_roles = ['Research Scientist' , 'R&D Engineer' , 'Research Analyst' , 'Product Development Engineer' , 'R&D Project Manager']

def random_joined_date():
    start = datetime(2025 , 1 , 1)
    end = datetime(2025 , 12 , 31)
    delta_days = (end - start).days
    return(start + timedelta(days=random.randint(0 , delta_days))).date().isoformat()

def random_names(gender_) :
    if  gender_ == 'Male':
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
    last_name = fake.last_name()
    return f"{first_name} {last_name}"

def random_job_role(department):
    if department == 'IT':
        return random.choice(IT_job_roles)
    elif department == 'Marketing':
        return random.choice(marketing_job_roles)
    else:
        return random.choice(research_job_roles)

def monthly_salary():
    return round(random.randint(10000 , 50000),)

def email_address(first_name , last_name , i):
    email = f"{first_name.lower()}.{last_name.lower()}{i}@meta.com"
    return email

def random_phone_number():
    first_digit = random.choice(['6', '7', '8', '9'])
    rest = ''.join(random.choices('0123456789', k=9))
    number = first_digit + rest
    return f"+91-{number[:5]}-{number[5:]}"

rows = []

for i in range(1 , 5001):

    gender_ =  random.choice(gender)
    department_ = random.choice(departments)

    first_name, last_name = random_names(gender_)      # generated ONCE
    full_name = f"{first_name} {last_name}"

    email = email_address(first_name , last_name , i)  
    phone = random_phone_number()
    
    rows.append({
        'emp_id' : f'EMP{i:05d}' , 
        'emp_name' : random_names(gender_) , 
        'gender' : gender_,
        'department' : department_ , 
        'job_role' : random_job_role(department_) , 
        'salary' : monthly_salary() , 
        'email' : email ,
        'phone' : phone,
        'city' : faker_in.city() , 
        'join_date' : random_joined_date()
    })
    
pd.DataFrame(rows).to_csv(r'D:\python_data_genaration_script\simple_random_data\employee.csv', index=False)
print('saved employee.csv')

