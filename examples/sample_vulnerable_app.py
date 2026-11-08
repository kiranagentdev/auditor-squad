import os
import sqlite3
import logging

# Configuration & Secrets
DATABASE_URL = "sqlite:///app.db"
# ❌ RISK 1: Hardcoded API key
PAYMENT_GATEWAY_KEY = "sk_live_99823489234892348239"

logging.basicConfig(level=logging.INFO)

def authenticate_user(username, password):
    # ❌ RISK 2: SQL Injection vector
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        # ❌ RISK 3: Logging sensitive PII (email & plaintext password) to logs
        logging.info(f"User authenticated: {username}, Password: {password}, Email: {user[2]}")
        return True
    return False

def execute_user_script(user_input_code):
    # ❌ RISK 4: Unsafe dynamic code execution
    print("Executing user script...")
    eval(user_input_code)