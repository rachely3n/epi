def pivot(a, l, r, pivot_idx):
  pivot_val = a[pivot_idx]
  a[r], a[pivot_idx] = a[pivot_idx], a[r]
  new_piv_idx = l

  for i in xrange(l, r):
    if a[i] > pivot_val:
      a[new_piv_idx], a[i] = a[i], a[new_piv_idx]
      new_piv_idx += 1

  a[new_piv_idx], a[r] = a[r], a[new_piv_idx]

  return new_piv_idx

def findKth(a, k):
  l = 0
  n = len(a)
  r = n - 1

  while l <= r:
    pivot_idx = l + (r - l)/2
    new_piv_idx = pivot(a, l, r, pivot_idx)

    if new_piv_idx == k - 1:
      return a[k - 1]
    elif new_piv_idx > k - 1:
      r = new_piv_idx - 1
    else: # new_piv_idx < k - 1
      l = new_piv_idx + 1
    
  return -1

arr = [1,4,5,3,2]
print findKth(arr, 2) == 4
print findKth(arr, 1) == 5
print findKth(arr, 3) == 3
print findKth(arr, 4) == 2
print findKth(arr, 5) == 1
