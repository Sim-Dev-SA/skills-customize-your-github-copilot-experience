# 📘 Assignment: Algorithmic Thinking with Search and Sorting

## 🎯 Objective

Students will practice algorithmic problem solving by implementing and comparing search and sorting approaches, then reflecting on efficiency.

## 📝 Tasks

### 🛠️	Implement Search Strategies

#### Description
Write two functions to search for a target number in a list: linear search and binary search. Test both functions with sample inputs.

#### Requirements
Completed program should:

- Implement `linear_search(numbers, target)` that returns the index of `target` or `-1`
- Implement `binary_search(sorted_numbers, target)` that returns the index of `target` or `-1`
- Include at least 3 test cases that show found and not-found results
- Print clear output showing which algorithm was used and the result


### 🛠️	Sort Data and Compare Performance

#### Description
Implement a sorting algorithm and compare execution time of your search functions on a larger dataset.

#### Requirements
Completed program should:

- Implement `bubble_sort(numbers)` or another sorting algorithm discussed in class
- Sort a random dataset and verify the result is in ascending order
- Measure and print runtime for linear search and binary search on the same dataset
- Explain in comments or output why binary search requires sorted input and is usually faster on large lists
