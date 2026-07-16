"""
search_simulation.py

DTS 304 - Data Management I

Project:
Design and Implementation of a Scalable Information
Management System for a Retail Business

Purpose:
- Perform Sequential Search on unindexed data
- Perform Binary Search on indexed/sorted data
- Compare execution performance
"""


import csv
import time
import os


# DATA LOADING FUNCTION

def load_dataset(filename):
    """
    Load retail dataset from CSV file.

    Parameters:
        filename (str):
            CSV file location

    Returns:
        list:
            List containing customer purchase records
    """

    data = []

    try:

        with open(filename, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                data.append(row)


        return data


    except FileNotFoundError:

        print("Dataset file not found.")

        return []



# SEQUENTIAL SEARCH

def sequential_search(data, product_id):
    """
    Sequential Search Algorithm.

    Searches every record one by one.

    Time Complexity:
        O(n)

    Parameters:
        data:
            Unsorted dataset

        product_id:
            Product ID to search

    Returns:
        Matching record or None
    """

    for record in data:

        if record["product_id"] == product_id:

            return record


    return None



# BINARY SEARCH

def binary_search(data, product_id):
    """
    Binary Search Algorithm.

    Requires sorted data.

    Time Complexity:
        O(log n)

    Parameters:
        data:
            Sorted dataset

        product_id:
            Product ID to search

    Returns:
        Matching record or None
    """

    left = 0

    right = len(data) - 1



    while left <= right:


        middle = (left + right) // 2


        current_id = data[middle]["product_id"]



        if current_id == product_id:

            return data[middle]



        elif current_id < product_id:

            left = middle + 1



        else:

            right = middle - 1



    return None



# SORT DATA FOR BINARY SEARCH

def prepare_binary_search_data(data):
    """
    Sort dataset by product_id.

    Binary search requires sorted data.
    """

    return sorted(
        data,
        key=lambda x: x["product_id"]
    )



# PERFORMANCE TEST FUNCTION

def measure_execution_time(function, data, product_id):
    """
    Measure search execution time.

    Returns:
        result,
        execution time
    """


    start_time = time.perf_counter()


    result = function(
        data,
        product_id
    )


    end_time = time.perf_counter()



    execution_time = (
        end_time - start_time
    )


    return result, execution_time



# DISPLAY RESULT

def display_result(search_type, result, execution_time):
    """
    Display search output.
    """

    print("\n" + "=" * 60)

    print(search_type)

    print("=" * 60)



    if result:

        print("Product Found")

        print("-----------------------------")

        print(
            "Customer ID:",
            result["customer_id"]
        )

        print(
            "Customer Name:",
            result["customer_name"]
        )

        print(
            "Product ID:",
            result["product_id"]
        )

        print(
            "Product Name:",
            result["product_name"]
        )

        print(
            "Category:",
            result["product_category"]
        )

        print(
            "Amount:",
            result["total_amount"]
        )


    else:

        print("Product Not Found")



    print(
        "\nExecution Time:",
        execution_time,
        "seconds"
    )



# MAIN PROGRAM

def main():


    print("=" * 60)

    print(
        "DTS 304 RETAIL MANAGEMENT SEARCH SIMULATION"
    )

    print("=" * 60)



    # Dataset path

    base_dir = os.path.dirname(os.path.abspath(__file__))

    dataset_file = os.path.abspath(
        os.path.join(base_dir, "..", "dataset", "customer_purchases.csv")
    )



    # Load data

    data = load_dataset(dataset_file)



    if not data:

        return



    print(
        "\nDataset Loaded Successfully"
    )


    print(
        "Total Records:",
        len(data)
    )



    # User input

    product_id = input(
        "\nEnter Product ID to search: "
    )



    # Sequential Search


    sequential_result, sequential_time = (
        measure_execution_time(
            sequential_search,
            data,
            product_id
        )
    )



    display_result(
        "SEQUENTIAL SEARCH (Unindexed Data)",
        sequential_result,
        sequential_time
    )



    # Binary Search


    sorted_data = (
        prepare_binary_search_data(data)
    )



    binary_result, binary_time = (
        measure_execution_time(
            binary_search,
            sorted_data,
            product_id
        )
    )



    display_result(
        "BINARY SEARCH (Indexed/Sorted Data)",
        binary_result,
        binary_time
    )



    # Performance Comparison


    print("\n" + "=" * 60)

    print("PERFORMANCE COMPARISON")

    print("=" * 60)



    print(
        "Sequential Search Time:",
        sequential_time,
        "seconds"
    )


    print(
        "Binary Search Time:",
        binary_time,
        "seconds"
    )



    if binary_time < sequential_time:

        print(
            "\nBinary Search performed faster."
        )


    elif sequential_time < binary_time:

        print(
            "\nSequential Search performed faster."
        )


    else:

        print(
            "\nBoth searches had similar performance."
        )



# PROGRAM EXECUTION

if __name__ == "__main__":

    main()