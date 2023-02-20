import time
from sql_queries import create_table, complete_loan

create_table()

if __name__ == '__main__':
    while True:
        complete_loan()
        print("completed")
        time.sleep(20)
