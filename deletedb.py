import os

try:
    os.remove('db.sqlite3')
    print("db.sqlite3 dosyası başarıyla silindi.")
except FileNotFoundError:
    print("db.sqlite3 dosyası bulunamadı.")