import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import random
import time
import numpy as np
from matplotlib.animation import FuncAnimation

# Sorting Algorithms

def bubble_sort(arr, ax, color_scheme, pause_time):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ax.clear()
                ax.bar(range(len(arr)), arr, color=color_scheme)
                ax.bar(j, arr[j], color='orange')  # Highlight swapped bar
                ax.bar(j+1, arr[j+1], color='red')  # Highlight swapped bar
                plt.draw()
                plt.pause(pause_time)  # Adjust the pause time for slower sorting
    return arr


def merge_sort(arr, ax, color_scheme, pause_time):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, ax, color_scheme, pause_time)
        merge_sort(right, ax, color_scheme, pause_time)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        ax.clear()
        ax.bar(range(len(arr)), arr, color=color_scheme)
        plt.draw()
        plt.pause(pause_time)
    return arr


def quick_sort(arr, ax, color_scheme, pause_time):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                ax.clear()
                ax.bar(range(len(arr)), arr, color=color_scheme)
                ax.bar(j, arr[j], color='orange')  # Highlight compared bar
                ax.bar(i, arr[i], color='red')  # Highlight compared bar
                plt.draw()
                plt.pause(pause_time)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

    quick_sort_rec(0, len(arr) - 1)
    return arr


def insertion_sort(arr, ax, color_scheme, pause_time):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        ax.clear()
        ax.bar(range(len(arr)), arr, color=color_scheme)
        ax.bar(i, arr[i], color='orange')  # Highlight inserted element
        plt.draw()
        plt.pause(pause_time)
    return arr


def selection_sort(arr, ax, color_scheme, pause_time):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        ax.clear()
        ax.bar(range(len(arr)), arr, color=color_scheme)
        ax.bar(i, arr[i], color='orange')  # Highlight current element
        ax.bar(min_idx, arr[min_idx], color='red')  # Highlight minimum element
        plt.draw()
        plt.pause(pause_time)
    return arr


def heapify(arr, n, i, ax, color_scheme, pause_time):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        ax.clear()
        ax.bar(range(len(arr)), arr, color=color_scheme)
        ax.bar(i, arr[i], color='orange')  
        ax.bar(largest, arr[largest], color='red')  
        plt.draw()
        plt.pause(pause_time)
        heapify(arr, n, largest, ax, color_scheme, pause_time)


def heap_sort(arr, ax, color_scheme, pause_time):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, ax, color_scheme, pause_time)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        ax.clear()
        ax.bar(range(len(arr)), arr, color=color_scheme)
        ax.bar(i, arr[i], color='orange')  
        ax.bar(0, arr[0], color='red')  
        plt.draw()
        plt.pause(pause_time)
        heapify(arr, i, 0, ax, color_scheme, pause_time)
    return arr


def counting_sort(arr, exp, ax, color_scheme, pause_time):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
        ax.clear()
        ax.bar(range(len(arr)), arr, color=color_scheme)
        plt.draw()
        plt.pause(pause_time)


def radix_sort(arr, ax, color_scheme, pause_time):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp, ax, color_scheme, pause_time)
        exp *= 10
    return arr


def create_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

# UI Class
class SortVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.config(bg='#f0f0f0')  
        
        self.size = 50
        self.speed = 0.2
        self.algorithm_1 = "Merge Sort"
        self.algorithm_2 = "Quick Sort"
        self.array = create_random_array(self.size)

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20)

        # Labels and Buttons 
        self.algorithm_label = tk.Label(main_frame, text="Select Sorting Algorithms:", bg='#4CAF50', fg='white', font=('Arial', 14, 'bold'))
        self.algorithm_label.grid(row=0, column=0, padx=10, pady=10)

        self.algorithm_dropdown_1 = ttk.Combobox(main_frame, values=["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort", "Selection Sort", "Heap Sort", "Radix Sort"])
        self.algorithm_dropdown_1.set("Merge Sort")
        self.algorithm_dropdown_1.grid(row=0, column=1, padx=10, pady=10)

        self.algorithm_dropdown_2 = ttk.Combobox(main_frame, values=["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort", "Selection Sort", "Heap Sort", "Radix Sort"])
        self.algorithm_dropdown_2.set("Quick Sort")
        self.algorithm_dropdown_2.grid(row=0, column=2, padx=10, pady=10)

        # Array size input 
        self.size_label = tk.Label(main_frame, text="Array Size:", bg='#4CAF50', fg='white', font=('Arial', 12))
        self.size_label.grid(row=1, column=0, padx=10, pady=10)

        self.size_slider = tk.Scale(main_frame, from_=10, to=100, orient="horizontal", bg='#4CAF50', fg='white', sliderlength=20)
        self.size_slider.set(self.size)
        self.size_slider.grid(row=1, column=1, padx=10, pady=10)

        # Speed control slider
        self.speed_label = tk.Label(main_frame, text="Animation Speed:", bg='#4CAF50', fg='white', font=('Arial', 12))
        self.speed_label.grid(row=2, column=0, padx=10, pady=10)

        self.speed_slider = tk.Scale(main_frame, from_=0.05, to=0.5, resolution=0.05, orient="horizontal", bg='#4CAF50', fg='white', sliderlength=20)
        self.speed_slider.set(self.speed)
        self.speed_slider.grid(row=2, column=1, padx=10, pady=10)

        # Start button 
        self.start_button = tk.Button(main_frame, text="Start", command=self.start_sorting, bg='#0000ff', fg='white', font=('Arial', 12, 'bold'), relief="raised", activebackground="#218838")
        self.start_button.grid(row=3, column=0, padx=10, pady=10)

        # Reset button 
        self.reset_button = tk.Button(main_frame, text="Reset", command=self.reset, bg='#dc3545', fg='white', font=('Arial', 12, 'bold'), relief="raised", activebackground="#c82333")
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)

        # Result Text Box for showing sorting time and sorted array
        self.result_box_label = tk.Label(main_frame, text="Results time:", bg='#4CAF50', fg='white', font=('Arial', 12))
        self.result_box_label.grid(row=4, column=0, padx=10, pady=10)

        self.result_box = tk.Text(main_frame, height=4, width=80, bg='#2e3b4e', fg='white', font=('Courier', 10), wrap="word")
        self.result_box.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        # Description Text Box for Algorithm Explanation
        self.description_label = tk.Label(main_frame, text="Description of Algorithm:", bg='#4CAF50', fg='white', font=('Arial', 12))
        self.description_label.grid(row=5, column=0, padx=10, pady=10)

        self.description_box = tk.Text(main_frame, height=8, width=60, bg='#2e3b4e', fg='white', font=('Courier', 12, 'bold'), wrap="word")
        self.description_box.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

        # Update description when algorithm is selected
        self.algorithm_dropdown_1.bind("<<ComboboxSelected>>", self.update_description)
        self.algorithm_dropdown_2.bind("<<ComboboxSelected>>", self.update_description)

        # Display initial description
        self.update_description()

    def update_description(self, event=None):
        descriptions = {
            "Bubble Sort": "Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. The process continues until no swaps are needed.",
            "Merge Sort": "Merge Sort is a divide-and-conquer algorithm that splits the array into halves, recursively sorts them, and then merges the sorted halves.",
            "Quick Sort": "Quick Sort is a divide-and-conquer algorithm that selects a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays.",
            "Insertion Sort": "Insertion Sort builds the final sorted array one element at a time by repeatedly picking the next element and placing it in the correct position.",
            "Selection Sort": "Selection Sort repeatedly selects the minimum element from the unsorted portion and swaps it with the first unsorted element.",
            "Heap Sort": "Heap Sort builds a binary heap from the input array and then repeatedly extracts the maximum element, rearranging the heap until the array is sorted.",
            "Radix Sort": "Radix Sort processes digits of the numbers in place, starting with the least significant digit and moving to the most significant, repeatedly using counting sort."
        }
        description_1 = descriptions.get(self.algorithm_dropdown_1.get(), "No description available.")
        description_2 = descriptions.get(self.algorithm_dropdown_2.get(), "No description available.")
        self.description_box.delete(1.0, tk.END)
        self.description_box.insert(tk.END, f"Algorithm 1: {description_1}\n\nAlgorithm 2: {description_2}\n")

    def start_sorting(self):
        # Check if the window is closed
        if not self.root.winfo_exists():
            return
        try:
            self.size = self.size_slider.get()
            self.speed = self.speed_slider.get()
            self.algorithm_1 = self.algorithm_dropdown_1.get()
            self.algorithm_2 = self.algorithm_dropdown_2.get()
            self.array = create_random_array(self.size)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

            color_schemes = {
                "Bubble Sort": 'skyblue',
                "Merge Sort": 'green',
                "Quick Sort": 'purple',
                "Insertion Sort": 'orange',
                "Selection Sort": 'yellow',
                "Heap Sort": 'red',
                "Radix Sort": 'blue'
            }

            color_scheme_1 = color_schemes.get(self.algorithm_1, 'skyblue')
            color_scheme_2 = color_schemes.get(self.algorithm_2, 'green')

            ax1.bar(range(len(self.array)), self.array, color=color_scheme_1)

            plt.ion()
            plt.show()
            start_time_1 = time.time()
            pause_time = self.speed  

            if self.algorithm_1 == "Bubble Sort":
                self.array = bubble_sort(self.array, ax1, color_scheme_1, pause_time)
            elif self.algorithm_1 == "Merge Sort":
                self.array = merge_sort(self.array, ax1, color_scheme_1, pause_time)
            elif self.algorithm_1 == "Quick Sort":
                self.array = quick_sort(self.array, ax1, color_scheme_1, pause_time)
            elif self.algorithm_1 == "Insertion Sort":
                self.array = insertion_sort(self.array, ax1, color_scheme_1, pause_time)
            elif self.algorithm_1 == "Selection Sort":
                self.array = selection_sort(self.array, ax1, color_scheme_1, pause_time)
            elif self.algorithm_1 == "Heap Sort":
                self.array = heap_sort(self.array, ax1, color_scheme_1, pause_time)
            elif self.algorithm_1 == "Radix Sort":
                self.array = radix_sort(self.array, ax1, color_scheme_1, pause_time)

            elapsed_time_1 = time.time() - start_time_1

            if self.result_box.winfo_exists():
                self.result_box.delete(1.0, tk.END)
                self.result_box.insert(tk.END, f"Algorithm 1 ({self.algorithm_1}) completed in {elapsed_time_1:.5f} seconds.\n")

            # Repeat sorting for second algorithm
            self.array = create_random_array(self.size) 
            ax2.clear()
            ax2.bar(range(len(self.array)), self.array, color=color_scheme_2)

            start_time_2 = time.time()

            if self.algorithm_2 == "Bubble Sort":
                self.array = bubble_sort(self.array, ax2, color_scheme_2, pause_time)
            elif self.algorithm_2 == "Merge Sort":
                self.array = merge_sort(self.array, ax2, color_scheme_2, pause_time)
            elif self.algorithm_2 == "Quick Sort":
                self.array = quick_sort(self.array, ax2, color_scheme_2, pause_time)
            elif self.algorithm_2 == "Insertion Sort":
                self.array = insertion_sort(self.array, ax2, color_scheme_2, pause_time)
            elif self.algorithm_2 == "Selection Sort":
                self.array = selection_sort(self.array, ax2, color_scheme_2, pause_time)
            elif self.algorithm_2 == "Heap Sort":
                self.array = heap_sort(self.array, ax2, color_scheme_2, pause_time)
            elif self.algorithm_2 == "Radix Sort":
                self.array = radix_sort(self.array, ax2, color_scheme_2, pause_time)

            elapsed_time_2 = time.time() - start_time_2

            if self.result_box.winfo_exists():
                self.result_box.insert(tk.END, f"Algorithm 2 ({self.algorithm_2}) completed in {elapsed_time_2:.5f} seconds.\n")
        except Exception as e:
            print(f"Error during sorting: {e}")

    def reset(self):
        try:
            if self.result_box.winfo_exists():
                self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, "Results cleared. Ready to start new sorting.\n")
        except Exception as e:
            print(f"Error during reset: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizerApp(root)
    root.mainloop()
