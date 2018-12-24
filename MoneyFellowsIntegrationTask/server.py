from flask import Flask, request
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db=client.pymongo_sim
age_config=db.pymongo_coll
age_records=db.pymongo_ageRecords
age=""
age_cat_doc=""
app=Flask(__name__)
@app.route('/', methods=['POST'])
def result():
	req_data = request.get_json()
	age=req_data['Age']
	print(age)
	for rec in age_config.find({
		"upper_bound":{ "$gte": age}, 
		"lower_bound":{ "$lte": age}
		}, {"age_category":1,"_id": False}):
		age_cat_doc=rec
		age_cat=age_cat_doc['age_category']
		#print(age_cat)
	try:
		age_cat
	except NameError:
		print("Error. Category not found")
		return "Error. Category not found"
	updateDB(age,age_cat)
	return age_cat
def updateDB(age,age_cat):
	age_records.update_one({},{"$set":{
	"age":age,
	"age_category":age_cat
	}})
app.run(host='127.0.0.1',debug=True, port=3101)