# A CSV import job fails when one row has bad data. How would you handle the error without stopping the whole job?
# rows = [
# {"user": "Amit", "amount": "1200"},
# {"user": "Riya", "amount": ""},
# {"user": "Dev", "amount": "900"},
# ]
# for row in rows:
# amount = int(row["amount"])
# print(row["user"], amount)
rows = [
    {"user": "Amit", "amount": "1200"},
    {"user": "Riya", "amount": ""},
    {"user": "Dev", "amount": "900"},
]

for row in rows:
    try:
        amount = int(row["amount"])
        print(row["user"], amount)
    except ValueError:
        print(f"Skipping row for {row['user']} due to invalid amount: {row['amount']}")



# A REST API returns inconsistent errors to the client. How would you redesign the endpoint behavior?
# @app.route("/orders/<order_id>")
# def get_order(order_id):
# order = db.get(order_id)
# return order
from flask import jsonify

@app.route("/orders/<order_id>")
def get_order(order_id):
    try:
        order = db.get(order_id)
        if order is None:
            return jsonify({"error": "Order not found"}), 404
        return jsonify(order), 200
    except ValueError:
        return jsonify({"error": "Invalid order ID"}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500



# A service calls many independent APIs and is slow. How would you use multithreading to improve the total response time?
# urls = [
# "https://api.example.com/users/1",
# "https://api.example.com/users/2",
# "https://api.example.com/users/3",
# ]
import requests
import concurrent.futures
import time

urls = [
    "https://api.example.com/users/1",
    "https://api.example.com/users/2",
    "https://api.example.com/users/3",
]

def fetch_url(url):
    response = requests.get(url)
    return url, response.status_code, response.json()

def main():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_url, urls))
    end = time.time()

    for url, status, data in results:
        print(f"{url} -> {status}, {data}")
    print(f"Total time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()


# A CPU-heavy transformation freezes the application. How would you move this work to multiprocessing?
# def transform(record):
# # CPU-heavy calculation
# return record * record
# records = list(range(10_000_000))
import multiprocessing
import time

def transform(record):
    return record * record

if __name__ == "__main__":
    records = list(range(10_000_000))

    start = time.time()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(transform, records)

    end = time.time()
    print(f"Processed {len(records)} records in {end - start:.2f} seconds")



# Multiple functions need the same audit behavior: log function name, start time, end time, execution duration, and exceptions.How 
# would you implement this using a decorator?
# def generate_report(user_id):
# # expensive report logic
# return {"status": "done"}
import logging
import time
from functools import wraps

# Configure logging once
logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
)

def audit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error("Exception in %s: %s", func.__name__, e)
            raise
        finally:
            end_time = time.time()
            duration = end_time - start_time
    return wrapper



# A Python script uses `print()` everywhere, and the client wants logs written to a file with timestamps and error details. Howwould 
# you improve this?
# def process_payment(payment_id):
# print("Processing payment", payment_id)
# result = call_gateway(payment_id)
# print("Gateway response", result)
# return resul
import logging

logging.basicConfig(
    filename="payments.log",          
    level=logging.INFO,               
)

def process_payment(payment_id):
    logging.info("Processing payment:", payment_id)
    try:
        result = call_gateway(payment_id)
        logging.info("Gateway response:", result)
        return result
    except Exception as e:
        logging.error("Error processing payment %s: %s", payment_id, e)
        return None
