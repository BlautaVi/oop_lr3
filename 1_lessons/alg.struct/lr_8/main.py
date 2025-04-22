import mysql.connector
import time

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678L",
        database="studentcoursemanagement"
    )

def fetch_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT grade FROM Grades LIMIT 10")
    data = [row[0] for row in cursor.fetchall()]
    conn.close()
    return data

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def sql_sorted_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT grade FROM Grades ORDER BY grade ASC LIMIT 10")
    sorted_data = [row[0] for row in cursor.fetchall()]
    conn.close()
    return sorted_data

# --- Основна логіка ---
original_data = fetch_data()

print("Оригінальні дані:", original_data)

# Bubble sort
start = time.time()
bubble_result = bubble_sort(original_data)
bubble_time = time.time() - start
print("\nСортування бульбашкою:", bubble_result)
print("Час сортування бульбашкою:", bubble_time)

# Insertion sort
start = time.time()
insertion_result = insertion_sort(original_data)
insertion_time = time.time() - start
print("\nСортування вставками:", insertion_result)
print("Час сортування вставками:", insertion_time)

# SQL sort
start = time.time()
sql_result = sql_sorted_data()
sql_time = time.time() - start
print("\nСортування SQL (ORDER BY):", sql_result)
print("Час SQL-сортування:", sql_time)

# Порівняння
print("\n--- Порівняння часу ---")
print(f"Bubble sort: {bubble_time:.6f} сек")
print(f"Insertion sort: {insertion_time:.6f} сек")
print(f"SQL ORDER BY: {sql_time:.6f} сек")
