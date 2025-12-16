import requests
import sqlite3
import datetime
import logging

# Setup logging
logging.basicConfig(filename="error.log", level=logging.ERROR)

API_URL = "https://fakestoreapi.com/products"
DB_NAME = "database.db"

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"API fetch failed: {e}")
        return None

def transform_data(products):
    transformed = []
    for p in products:
        transformed.append((
            p["id"],
            p["title"],
            p["price"],
            round(p["price"] * 83, 2),  # USD → INR
            p["category"],
            datetime.datetime.now()
        ))
    return transformed

def store_data(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price_usd REAL,
            price_inr REAL,
            category TEXT,
            last_updated TIMESTAMP
        )
    """)

    cursor.executemany("""
        INSERT OR REPLACE INTO products
        VALUES (?, ?, ?, ?, ?, ?)
    """, data)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pipeline_status (
            id INTEGER PRIMARY KEY,
            last_run TIMESTAMP,
            status TEXT
        )
    """)

    cursor.execute("""
        INSERT OR REPLACE INTO pipeline_status
        VALUES (1, ?, ?)
    """, (datetime.datetime.now(), "SUCCESS"))

    conn.commit()
    conn.close()

def main():
    products = fetch_data()
    if products:
        data = transform_data(products)
        store_data(data)
    else:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO pipeline_status
            VALUES (1, ?, ?)
        """, (datetime.datetime.now(), "FAILED"))
        conn.commit()
        conn.close()

if __name__ == "__main__":
    main()
