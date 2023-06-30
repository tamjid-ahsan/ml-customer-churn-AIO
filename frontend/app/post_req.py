import requests
import json

URL = "http://localhost:5000/predict"
headers = {'Content-Type':'application/json'}
# data = {"Customer_Age": 45, "Gender": "M", "Dependent_count": 3, "Education_Level": "High School", "Marital_Status": "Married", "Income_Category": "60K_to_80K", "Card_Category": "Blue", "Months_on_book": 39, "Total_Relationship_Count": 5, "Months_Inactive_12_mon": 1, "Contacts_Count_12_mon": 3, "Credit_Limit": 12691.0, "Total_Revolving_Bal": 777, "Avg_Open_To_Buy": 11914.0, "Total_Amt_Chng_Q4_Q1": 1.335, "Total_Trans_Amt": 1144, "Total_Trans_Ct": 42, "Total_Ct_Chng_Q4_Q1": 1.625, "Avg_Utilization_Ratio": 0.061}
data = {"Customer_Age":45,"Gender":"M","Dependent_count":3,"Education_Level":"High School","Marital_Status":"Married","Income_Category":"60K_to_80K","Card_Category":"Blue","Months_on_book":39,"Total_Relationship_Count":3,"Months_Inactive_12_mon":3,"Contacts_Count_12_mon":3,"Credit_Limit":12000,"Total_Revolving_Bal":777,"Avg_Open_To_Buy":11900,"Total_Amt_Chng_Q4_Q1":1.3,"Total_Trans_Amt":1144,"Total_Trans_Ct":39,"Total_Ct_Chng_Q4_Q1":1.6,"Avg_Utilization_Ratio":0.06}
data = json.dumps(data)
response = requests.post(url=URL, headers=headers, data=data)

print(response.text)
