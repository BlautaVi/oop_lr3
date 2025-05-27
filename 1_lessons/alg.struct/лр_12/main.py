import mysql.connector
import time
import random

def fetch_student_names():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678L',
        database='StudentCourseManagement'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT first_name FROM Students")
    names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return names

def linear_search_all(data, target, limit=10):
    results = []
    for i, value in enumerate(data):
        if value == target:
            results.append((i, value))
            if len(results) >= limit:
                break
    return results

def binary_search_all(data, target, limit=10):
    left, right = 0, len(data) - 1
    found_index = -1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            found_index = mid
            break
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if found_index == -1:
        return []

    results = [(found_index, data[found_index])]
    i = found_index - 1
    while i >= 0 and data[i] == target and len(results) < limit:
        results.insert(0, (i, data[i]))
        i -= 1

    i = found_index + 1
    while i < len(data) and data[i] == target and len(results) < limit:
        results.append((i, data[i]))
        i += 1

    return results

def sql_search_all(target, limit=10):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678L',
        database='StudentCourseManagement'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT first_name FROM Students WHERE first_name = %s LIMIT %s", (target, limit))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in results]

def compare_search_methods(data, target):
    print(f"\nПошук елемента '{target}' у {len(data)} елементах:\n")
    start = time.time()
    results_linear = linear_search_all(data, target)
    duration_linear = time.time() - start
    print(f"Лінійний пошук ({len(results_linear)} знайдено за {duration_linear:.6f} сек):")
    for idx, val in results_linear:
        print(f"  [{idx}] {val}")
    sorted_data = sorted(data)
    start = time.time()
    results_binary = binary_search_all(sorted_data, target)
    duration_binary = time.time() - start
    print(f"\nБінарний пошук ({len(results_binary)} знайдено за {duration_binary:.6f} сек):")
    for idx, val in results_binary:
        print(f"  [{idx}] {val}")
    start = time.time()
    results_sql = sql_search_all(target)
    duration_sql = time.time() - start
    print(f"\nSQL SELECT ... WHERE ({len(results_sql)} знайдено за {duration_sql:.6f} сек):")
    for i, val in enumerate(results_sql):
        print(f"  [{i}] {val}")
data = fetch_student_names()
if not data:
    print("Немає даних у таблиці Students.")
else:
    random_target = random.choice(data)
    compare_search_methods(data, random_target)
