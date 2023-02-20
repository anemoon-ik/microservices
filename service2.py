import time
from sql_queries import create_table, update_loan

create_table()

if __name__ == '__main__':
    while True:
        update_loan()
        print("updated")
        time.sleep(20)
