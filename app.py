from flask import Flask, request, jsonify 

app = Flask(__name__) 

# Sample data 
catalog = [] 

@app.route('/') 
def welcome(): 
	return "Welcome to the 107 Final Report API!" 

@app.route('/api/catalog', methods=['GET'])
def get_catalog(): 
	return jsonify(catalog) 

@app.route('/api/catalog', methods=['POST']) 
def add_product(): 
	product = request.get_json() 
	catalog.append(product) 
	return jsonify({"message": "Product added successfully!"}), 201 

@app.route('/api/reports/total', methods=['GET']) 
def get_total_value(): 
	total_value = sum(product['price'] * product['quantity'] for product in catalog) 
	return jsonify({"total_value": total_value}) 

@app.route('/api/products/<category>', methods=['GET']) 
def get_products_by_category(category): 
	products = [product for product in catalog if product['category'].lower() == category.lower()] 
	return jsonify(products)


if __name__ == '__main__': 
	app.run(debug=True)