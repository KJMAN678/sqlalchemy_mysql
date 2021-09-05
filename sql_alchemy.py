import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os
import json

def lambda_handler(event, context):

    user = 'admin'
    password = '8HuGC7RC4OuXS61hdOPv'
    db_name = 'database-1'
    db_host = 'database-1.cuvi12eaaleh.ap-northeast-1.rds.amazonaws.com'
    program_name = os.getenv('AWS_LAMBDA_FUNCTION_NAME')

    engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{db_host}/{db_name}?charset=utf8;program_name={program_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute('select * from information_schema.tables')
    session.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }