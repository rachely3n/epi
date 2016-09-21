# https://discuss.leetcode.com/topic/27840/ac-python-clean-solution-using-stack-76ms

#genius, stack has -1, height has 0, handles the boundary, flush on right...
def largestRectangleArea(heights):
  """
  :type heights: List[int]
  :rtype: int
  """
      # print len(heights)
  if len(heights) == 0:
    return 0

  S = []
  max_area = 0
  ## TODO: do i have to do the equal building thing, i might just change hte invariant
  
  for i in xrange(len(heights)):
     # invariant is that stack is always monotonically increasing
    while len(S) > 0 and heights[S[-1]] > heights[i]:
      cand = heights[S.pop()]
      w = i # empty stack, we are blocked by no one until element i appeared
      if len(S) > 0: 
        w -=(S[-1] + 1) 
        max_area = max(cand * w, max_area)
    S.append(i) # add yourself 

  ##### handle after iteration is done ####
  n = len(heights)
  while len(S) > 0 :

    cand = heights[S.pop()]
    w = n
    if len(S) > 0:
      w -= (S[-1] + 1)
      print cand*w
      max_area = max(cand * w, max_area) 


  return max_area

print largestRectangleArea([2,4])