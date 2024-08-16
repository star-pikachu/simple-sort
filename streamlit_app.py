import streamlit as st
import numpy as np

def main():
    # hide button
    hide_menu = """
    <style>
    header {
        visibility: hidden;
    }
    # MainMenu {
        visibility: hidden;
    }
    
    footer {
        visibility: hidden;
    }
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)
    
# Функции сортировок: Выбором Вставками Обменами
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Title
st.title("Простейшие алгоритмы сортировки")

# Input
user_input = st.text_input("Enter a list of numbers separated by commas:", "5, 3, 8, 6, 2")
numbers = list(map(int, user_input.split(',')))

# Tabs
tabs = st.tabs(["Selection Sort", "Insertion Sort", "Bubble Sort"])

# Tab0 Сортировка Выбором
with tabs[0]:
    st.header("Selection Sort")
    if st.button("Sort", key="selection_sort_button"):
        sorted_numbers = selection_sort(numbers.copy())
        st.write("Sorted List:", sorted_numbers)
    st.code("""
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
""")

# Tab1 Сортировка Вставками
with tabs[1]:
    st.header("Insertion Sort")
    if st.button("Sort", key="insertion_sort_button"):
        sorted_numbers = insertion_sort(numbers.copy())
        st.write("Sorted List:", sorted_numbers)
    st.code("""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
""")

# Tab2 Сортировка Обменом
with tabs[2]:
    st.header("Bubble Sort")
    if st.button("Sort", key="bubble_sort_button"):
        sorted_numbers = bubble_sort(numbers.copy())
        st.write("Sorted List:", sorted_numbers)
    st.code("""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""")


if __name__ == "__main__":
    main()
