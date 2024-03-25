def merge_sort(arr, level=0):
  # Base case: if the list is one element long, just return it
  if len(arr) <= 1:
      return arr

  # Divide the list in half and merge sort recursively
  mid = len(arr) // 2
  left_half = merge_sort(arr[:mid], level+1)
  right_half = merge_sort(arr[mid:], level+1)

  # Merge the sorted halves
  merged = merge(left_half, right_half, level)

  # If we're at the top level, we're done, so print the sorted list
  if level == 0:
      print(f"Sorted array: {merged}")
  return merged

def merge(left, right, level):
  merged = []
  left_index = right_index = 0

  # Print the current step of merging
  print(f"{'  '*level}Merging {left} and {right}")

  # Compare the first elements of each half
  while left_index < len(left) and right_index < len(right):
      if left[left_index] < right[right_index]:
          merged.append(left[left_index])
          left_index += 1
      else:
          merged.append(right[right_index])
          right_index += 1

  # Once one half is exhausted, append the rest of the other half
  merged.extend(left[left_index:])
  merged.extend(right[right_index:])

  # Print the result of the merge
  print(f"{'  '*level}Result of merge: {merged}")
  return merged

# Example usage
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Original array:", arr)
merge_sort(arr)
