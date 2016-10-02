# @ param list of ints
# @ return tuple of beginning and ending indices of maximum sum
# subarray in list a
def max_sum_subarray(a) :
  min_sum = 0
  max_sum = 0
  cur_sum = 0
  min_idx = -1
  max_idx = -1
  # idea is that max subarray at index j is s[j] - min s[i] (given i <= j)
  # why does this work?
  for i in range(0, len(a)) : 
    #need to reset, but how
    cur_sum += a[i]

    # when we see a sum smaller than our minimum sum, that becomes our new minimum sum
    # we can keep summing up to get a min_sum because we have been 
    # checking for a max all this time
    if cur_sum < min_sum :
      min_sum = cur_sum
      min_idx = i

    # see if there are max sum's along the way
    if (cur_sum - min_sum) > max_sum :
      max_sum = cur_sum - min_sum 
      max_idx = i


  return min_idx + 1, max_idx 


# a different way to think about the problem
# more intuitive in the sense that we have a more explicit reset point
# the other problem, try drawing pictures out, we don't explicitly reset
# portions before our "reset" would be canceled out when cur_sum - min_sum 
  def max_sum_subarray2(a) :
    cur_sum = 0
    min_idx_temp = 0
    min_idx = 0
    max_sum = 0
    for i in range(0, len(a)) :
      cur_sum += A[i]
      if cur_sum > max_sum :
        max_sum = cur_sum
        max_idx = i
        min_idx = temp_min_idx
      # if I sum to 0 or a negative number, i basically made no progress, let's reset
      # we can wait til we get to 0 because we've already kept checking
      # for a local max along the way and updating our global max
      if cur_sum < 0 :
        temp_min_idx = i
        cur_sum = 0

    return min_idx + 1, max_idx 