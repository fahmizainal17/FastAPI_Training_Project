from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # @app. - path operation decorator
def say_hello():
    return {"output":"success"}

# this is for fetching data

# @app.get("/car/{car_id}")
# def read_db(car_id: int):
#     get_db()
#     car_info =(
#         dd.sql(f"SELECT * FROM car_price.csv WHERE car_id ={car_id}")
#         .fetchdf()
#         .to_dict("index")
#     )
# So you will get that car_info in response 

# data validation using pydantic
# contoh nak string kan dia 
#kalau basemodel send dalam json kat 
# post ni bila kita nak hantar body Json
# get kalau hantar parameter 
# Data Type Data Validation , type hint yang int and str '
# Typing ada Union[str,None] ada multiple type hint 
# semua untuk basemodel dan 
# using BaseModel #annotated kita juga boleh letak Path Parameter (Title : balalal
# Query Parameter (boleh letak max length))
# Field (response Body)

# dalam class include model_confiq and create auto schemas

#security : yang username masuk 

# middle ware boleh access berapa lama kita execute the endpont

# tulah router 
# bila banyak endpoint , kita nak folderkan dia

# metadata

# Endpoint tested 
# less potentioal to break down 
# scalable development 
# safe dia akan [pass] the same ohh ambik masa mula2 je sebb time tulis code 
# mindset 
