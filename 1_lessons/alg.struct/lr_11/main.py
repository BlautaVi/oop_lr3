import pymysql
import time
import random

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "12345678L",
    "database": "StudentCourseManagement"
}

def fetch_data():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT last_name FROM Students LIMIT 100")
    rows = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return rows

def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)

def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    result = arr[:]
    while width < n:
        for i in range(0, n, 2*width):
            left = result[i:i+width]
            right = result[i+width:i+2*width]
            result[i:i+2*width] = merge(left, right)
        width *= 2
    return result

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def bubble_sort(arr):
    data = arr[:]
    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def insertion_sort(arr):
    data = arr[:]
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def selection_sort(arr):
    data = arr[:]
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def sql_order_by():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT last_name FROM Students ORDER BY last_name")
    rows = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return rows

def test_sorts():
    data = fetch_data()
    print(f"\nКількість елементів: {len(data)}")

    sort_algorithms = [
        ("Merge Sort (рекурсивний)", merge_sort_recursive),
        ("Merge Sort (ітеративний)", merge_sort_iterative),
        ("Quick Sort", quick_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort)
    ]

    for name, func in sort_algorithms:
        start = time.time()
        result = func(data)
        end = time.time()
        print(f"{name}: {end - start:.6f} секунд")

    start = time.time()
    sql_result = sql_order_by()
    end = time.time()
    print(f"SQL ORDER BY: {end - start:.6f} секунд")
test_sorts()
