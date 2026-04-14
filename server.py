from flask import Flask 

app = Flask (__name__) #instance of Flask

# GET http://127.0.0.1:5000/home
@app.route("/", methods=["GET"])
def home():
    return {"message":"Welcome to Flask ch 65"}

#GET http://127.0.0.1:5000/cohort-65
@app.route("/cohort-65", methods=["GET"])
def get_students_65():
    students_list = ["Parrilla", "Trishon", "Antonio"]
    return students_list



#  ------ Products
products = [
  {
    "_id": 1, 
    "title": "Nintendo Switch", 
    "price": 499.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2, 
    "title": "Smart Refrigerator", 
    "price": 999.99, 
    "category": "Kitchen", 
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3, 
    "title": "Bluetooth Speaker", 
    "price": 79.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/3/300/300"
  },
]

#http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return {"data": products}


# --------- Coupons -------------
coupons = [
        {
            "_id":1,"code":"WELCOME10","discount":10
        },
        {
            "_id":2,"code":"SPOOKY25","discount":25
        },
        {
            "_id":3,"code":"VIP50","discount": 50
        }
    ]


@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return({"data": coupons})

#taking the value of coupons list by using the get_coupons function as a value for the coupon_data variable 
#converted it into a string because using len() by itself was returning information that gave an error
@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return ({"coupons_counter": len(coupons)})
    #counter = 0
    #for coupon in coupons:
    #    counter += 1

    #return str(counter)


if __name__ == "__main__":
    app.run()
#when this file is run directly: __name__ == "__main__"
#when this file is imported as module: __name__ == "server.py"