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
    return sorted(names)

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

def interpolation_search_iterative(data, target, limit=10):
    results = []
    low, high = 0, len(data) - 1
    while low <= high and data[low] <= target <= data[high]:
        if data[low] == data[high]:
            if data[low] == target:
                results.append((low, data[low]))
            break
        pos = low + ((high - low) * (ord(target[0]) - ord(data[low][0]))) // (ord(data[high][0]) - ord(data[low][0]))
        pos = max(min(pos, high), low)
        if data[pos] == target:
            results.append((pos, data[pos]))
            i = pos - 1
            while i >= 0 and data[i] == target and len(results) < limit:
                results.insert(0, (i, data[i]))
                i -= 1
            i = pos + 1
            while i < len(data) and data[i] == target and len(results) < limit:
                results.append((i, data[i]))
                i += 1
            break
        elif data[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return results

def str_weight(s):
    return sum(ord(c) for c in s)


def interpolation_search_recursive(data, target, low, high, limit=10, results=None, depth=0):
    if results is None:
        results = []
    if depth > 1000 or low > high or not data or target < data[low] or target > data[high]:
        return results

    if low == high:
        if data[low] == target:
            results.append((low, data[low]))
        return results
    if data[low] == data[high]:
        if data[low] == target:
            results.append((low, data[low]))
        return results

    pos = low + ((high - low) * (ord(target[0]) - ord(data[low][0]))) // (ord(data[high][0]) - ord(data[low][0]))
    pos = max(min(pos, high), low)

    if data[pos] == target:
        results.append((pos, data[pos]))
        i = pos - 1
        while i >= 0 and data[i] == target and len(results) < limit:
            results.insert(0, (i, data[i]))
            i -= 1
        i = pos + 1
        while i <= high and data[i] == target and len(results) < limit:
            results.append((i, data[i]))
            i += 1
        return results
    elif data[pos] < target:
        return interpolation_search_recursive(data, target, pos + 1, high, limit, results, depth + 1)
    else:
        return interpolation_search_recursive(data, target, low, pos - 1, limit, results, depth + 1)

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
    print(f"Лінійний пошук: {len(results_linear)} знайдено за {time.time() - start:.6f} сек")
    for i, val in results_linear:
        print(f"  [{i}] {val}")

    start = time.time()
    results_binary = binary_search_all(data, target)
    print(f"\nБінарний пошук: {len(results_binary)} знайдено за {time.time() - start:.6f} сек")
    for i, val in results_binary:
        print(f"  [{i}] {val}")

    start = time.time()
    results_interp_iter = interpolation_search_iterative(data, target)
    print(f"\nІнтерполяційний пошук (ітеративний): {len(results_interp_iter)} знайдено за {time.time() - start:.6f} сек")
    for i, val in results_interp_iter:
        print(f"  [{i}] {val}")

    start = time.time()
    results_interp_rec = interpolation_search_recursive(data, target, 0, len(data) - 1)
    print(f"\nІнтерполяційний пошук (рекурсивний): {len(results_interp_rec)} знайдено за {time.time() - start:.6f} сек")
    for i, val in results_interp_rec:
        print(f"  [{i}] {val}")

    start = time.time()
    results_sql = sql_search_all(target)
    print(f"\nSQL-запит: {len(results_sql)} знайдено за {time.time() - start:.6f} сек")
    for i, val in enumerate(results_sql):
        print(f"  [{i}] {val}")

data = fetch_student_names()
if not data:
    print("Немає даних у таблиці Students.")
else:
    random_target = random.choice(data)
    compare_search_methods(data, random_target)
    results = interpolation_search_recursive(data, random_target, 0, len(data) - 1)
    print(f"Результати: {results}")
