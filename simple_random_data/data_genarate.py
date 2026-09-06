import csv
import random
from datetime import datetime , timedelta
random.seed(42)

countries = ["Canada", "UK", "UAE", "Germany", "USA"]
plans = ["Free", "Basic", "Pro", "Enterprise"]
gender = ['Male' , 'Female']

def random_signup_date():
    start = datetime(2024 , 1 , 1)
    end = datetime(2026 , 1 , 1)
    delta_days = (end - start).days
    return(start + timedelta(days=random.randint(0 , delta_days))).date().isoformat()

rows = []
for i in range(1 , 1001):
    age = random.randint(18 , 70)
    country = random.choice(countries)
    plan = random.choice(plans)
    gender_ = random.choice(gender)
    monthly_spend = round(random.uniform(0,500) , 2)

    rows.append({
        'customer_id' : f'CUST{i:05d}' , 
        'age' : age ,
        'country' :country,
        'gender' : gender_ , 
        'plan' : plan , 
        'monthly_spend' : monthly_spend,
        'signup_date' : random_signup_date()

    })
with open('D:\python_data_genaration_script\simple_random_data\customer.csv' , 'w' , 
          newline='' , encoding='utf-8') as f :
    writer = csv.DictWriter(f , fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print('saved customer.csv')

# it will generate simple randome data

# emp_id , emp_name , department , 
# joined_date , salary , gender 