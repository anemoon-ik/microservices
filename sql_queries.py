import psycopg2

from loan import Loan

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS loans (
        id SERIAL PRIMARY KEY,
        loan INTEGER NOT NULL,
        interest_rate INTEGER NOT NULL,
        total INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'taken'
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_loan(loan: Loan):
    query = """
    INSERT INTO loans (loan, interest_rate, total)
    VALUES (%s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (loan.loan, loan.interest_rate, loan.total))
    conn.commit()


def update_loan():
    query = "UPDATE loans SET total=(loan*interest_rate)/10, status='total is calculated' WHERE status='taken';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def complete_loan():
    query = "UPDATE loans SET status='paid' WHERE status='total is calculated';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

