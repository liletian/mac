from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# dbname is the database name
# user_id and user_password are what you put in above

engine = create_engine("mysql+pymysql://%s:%s@localhost:3306/%s"
                       %(user_id,user_password,dbname),echo=False)
if not database_exists(engine.url): 
    create_database(engine.url)			# Create database if it doesn't exist.
    
con = engine.connect() # Connect to the MySQL engine
table_name = 'new_table'
command = "DROP TABLE IF EXISTS new_table;" # Drop if such table exist
con.execute(command)
