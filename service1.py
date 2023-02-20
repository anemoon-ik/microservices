import time
import random
from sql_queries import create_table, insert_loan
from loan import Loan

create_table()

if __name__ == '__main__':
    while True:
        insert_loan(
            Loan(
                loan=random.randint(100, 1000),
                interest_rate=random.randint(1, 10),
                total=0,
            )
        )
        print("Inserted")
        time.sleep(10)
