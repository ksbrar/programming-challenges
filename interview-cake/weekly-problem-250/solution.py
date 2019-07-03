def merge_lists_easy(lst1, lst2):
  '''
  Easy pythonic answer (let the greats do all the work). Probably closer to what you would find in most
  engineering scenarios in which list size is not a big deal. (But it does not take advantage of the
  fact that each list is individually sorted before being passed).
  '''
  return sorted(lst1 + lst2)

def merge_lists(lst1, lst2):
  '''
  Use two walkers to compile the merged list in O(n) time.
  '''
  mergedLength = len(lst1) + len(lst2)
  result = [None] * mergedLength
  w1 = 0
  w2 = 0
  while (w1 + w2) < mergedLength:
    if lst1[w1] <= lst2[w2]:
      

def main():
  my_list = [3, 4, 6, 10, 11, 15]
  alices_list = [1, 5, 8, 12, 14, 19]

  # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
  print(merge_lists_easy(my_list, alices_list))
  print(merge_lists(my_list, alices_list))  

if __name__ == "__main__":
  main()
