# Algorithm

## Sorting Algorithm

### Bubble Sort

* Python

  ```python
  def BubbleSort(nums):
      lastIdx = len(nums) - 1
      for cnt in range(lastIdx):
          for idx in range(lastIdx - cnt):
              if nums[idx] > nums[idx + 1]:
                  nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
  
      return nums
  ```

  

* Java

* C++

