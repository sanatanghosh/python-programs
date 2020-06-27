def linear_search(A, k):
      for element in A:
        if element == k:
          return 'k is found'
      return 'k is not found'
A = [3, 5, 11, 6, 9, 23, 12, 13, 4]
k = 12
print (linear_search(A, k))