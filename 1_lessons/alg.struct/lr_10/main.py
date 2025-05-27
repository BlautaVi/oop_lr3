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

def quick_sort(arr, pivot_strategy='first'):
    if len(arr) <= 1:
        return arr

    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'random':
        pivot = random.choice(arr)
    elif pivot_strategy == 'median3':
        first = arr[0]
        middle = arr[len(arr) // 2]
        last = arr[-1]
        pivot = sorted([first, middle, last])[1]
    else:
        raise ValueError("Невідома стратегія опорного елемента")
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less, pivot_strategy) + equal + quick_sort(greater, pivot_strategy)
def selection_sort(data):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(data):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(data):
    arr = data[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def sql_order_by():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT last_name FROM Students ORDER BY last_name")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

def test_all():
    data = fetch_data()
    print(f"Кількість елементів: {len(data)}")

    strategies = ['first', 'last', 'random', 'median3']
    for strategy in strategies:
        start = time.time()
        sorted_data = quick_sort(data, strategy)
        end = time.time()
        print(f"Quick Sort ({strategy} pivot): {end - start:.6f} секунд")

    for name, sort_func in [
        ("Сортування вибором", selection_sort),
        ("Сортування бульбашкою", bubble_sort),
        ("Сортування вставки", insertion_sort)
    ]:
        start = time.time()
        sorted_data = sort_func(data)
        end = time.time()
        print(f"{name}: {end - start:.6f} секунд")

    start = time.time()
    sorted_sql = sql_order_by()
    end = time.time()
    print(f"SQL ORDER BY: {end - start:.6f} секунд")

test_all()