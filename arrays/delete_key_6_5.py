def delete_key(A, el):
  write_idx = 0
  n = len(A)

  for entry in A:
    if entry != el:
      A[write_idx] = entry 
      write_idx += 1

  return A 

print delete_key([1,3,5,9,4,3], 3) == [1,5,9,4,4,3]
print delete_key([1,2,3,7,8,3,9,5], 3) == [1,2,7,8,9,5,9,5]