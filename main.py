import sqlalchemy as db
from fastapi import FastAPI

app = FastAPI()

engine = db.create_engine('postgresql://postgres:shamim237x@localhost/zibew_chatbot')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('chatbot_2', metadata, autoload=True, autoload_with=engine)

query = db.select([census]) 

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()

# 

@app.get('/')
def simple():
    return "Hello World!"

@app.get('/data')
def get_data():
    return ResultSet

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='8888', debug=True)





# # Print the column names
# # print(census.columns.keys())

# # Print full table metadata
# print(repr(metadata.tables['chatbot']))