---
title: 基础算法
order: 1
---

## 1. 排序算法

排序是算法中最基础且最常用的部分，掌握不同排序方法的原理和实现是关键。

### 1.1 冒泡排序（Bubble Sort）

- 核心思想：**重复遍历数组，依次比较相邻元素，若顺序错误则交换**。

- 时间复杂度：平均和最坏情况 O(n²)，最好情况 O(n)（已排序时）。

- 代码示例：

  ```python
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n):
          swapped = False
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
                  swapped = True
          if not swapped:  # 提前终止（优化）
              break
      return arr
  ```

### **1.2 快速排序 (Quick Sort)**

- 核心思想：**分治法**。选择一个基准元素，将数组分为“小于基准”和“大于基准”两部分，递归排序子数组。

- 时间复杂度：平均 O(n log n)，最坏 O(n²)（已排序且基准选择不当）。

- 代码示例：

  ```python
  def quick_sort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[len(arr) // 2]  # 选择中间元素为基准
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quick_sort(left) + middle + quick_sort(right)
  ```

### **1.3 归并排序 (Merge Sort)**

- 核心思想：**分治法**。将数组分成两半，分别排序后合并。

- 时间复杂度：稳定 O(n log n)。

- 代码示例：

  ```python
  def merge_sort(arr):
      if len(arr) <= 1:
          return arr
      mid = len(arr) // 2
      left = merge_sort(arr[:mid])
      right = merge_sort(arr[mid:])
      return merge(left, right)
  
  def merge(left, right):
      result = []
      i = j = 0
      while i < len(left) and j < len(right):
          if left[i] < right[j]:
              result.append(left[i])
              i += 1
          else:
              result.append(right[j])
              j += 1
      result += left[i:]
      result += right[j:]
      return result
  ```



## 2. 搜索算法

### **2.1 线性搜索 (Linear Search)**

- **核心思想**：逐个遍历数组元素，直到找到目标。

- **时间复杂度**：O(n)。

- **代码示例**：

  ```python
  def linear_search(arr, target):
      for i in range(len(arr)):
          if arr[i] == target:
              return i
      return -1
  ```

### **2.2 二分查找 (Binary Search)**

- **核心思想**：仅适用于**已排序数组**。每次比较中间元素，缩小搜索范围。

- **时间复杂度**：O(log n)。

- **代码示例**：

  ```python
  def binary_search(arr, target):
      left, right = 0, len(arr) - 1
      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
      return -1
  ```

### **二分查找变种问题**

- **旋转排序数组搜索**（如 [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)）
- **寻找峰值**（如 [LeetCode 162](https://leetcode.com/problems/find-peak-element/)）