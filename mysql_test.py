#!/usr/bin/python
import sys
import logging
import rds_config
import pymysql
import os

rds_host = os.environ['DB_ENDPOINT']
name = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)

conn = pymysql.connect(rds_host, user=name,
                     passwd=password, db=db_name, connect_timeout=5)


logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

def lambda_handler(event, context):
    """
    This function inserts content into mysql RDS instance
    """
    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table Employee3 (EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        cur.execute('insert into Employee3 (EmpID, Name) values(1, "Joe")')
        cur.execute('insert into Employee3 (EmpID, Name) values(2, "Bob")')
        cur.execute('insert into Employee3 (EmpID, Name) values(3, "Mary")')
        conn.commit()
        cur.execute("select * from Employee3")
        for row in cur:
            item_count += 1
            logger.info(row)
    return "Added %d items to RDS MySQL table" %(item_count)
