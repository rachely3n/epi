# we wish to partition a list/array of numbers around a single element
# hence "dutch national flag" (3 stripes)
# e is the element we are partitioning around
# a is an list of elements
# we will output a list/array with elements lesser than
# e to the left of e and those greater than e will be
# on the right
def dutch_flag(e, a): 
  # 3 pointers
  l = -1
  m = 0
  h = len(a)

  # invariant: anything between the middle and greater exclusive
  # pointers need to be sorted
  while m < h :
    if a[m] < e :
      l += 1
      #swap
      a[l], a[m] = a[m] , a[l]
      m += 1
    elif a[m] == e :
      m += 1
    else :
      h -= 1
      a[h], a[m] = a[m] , a[h]
  return a 

# following epi solutions
# fun fact: in c++, i++ requires a temporary variable
def dutch_flag2(e, a):
  # e pointers
  l = 0
  m = 0
  h = len(a) - 1

  #everything between m and h inclusive is unclassified
  while m <= h :
    if a[m] < e :
      #swap a[l] and a[m]
      a[l], a[m] = a[m], a[l]
      l += 1
      m += 1
    elif a[m] == e : 
      m += 1
    else : # h + 1 to len(a) is > e
      a[m], a[h] = a[h], a[m]
      h -= 1 
  return a 