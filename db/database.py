import sqlite3

def get_db_connection():
    conn = sqlite3.connect('scraping_system.db')
    conn.row_factory = sqlite3.Row  # 將結果轉換為字典類型
    return conn

def get_website_info():
    """從資料庫中獲取所有網站信息"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, url, types, headers FROM websites")
    websites = cursor.fetchall()
    conn.close()
    return websites
