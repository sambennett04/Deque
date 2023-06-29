import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  if n == 0: #if n is zero or one disk move from s stack to d
    x = s.pop()
    #print(x)
    d.push(x)
    print(n, s, a, d, '\n')
    return 
    #print('base',n, s, a, d)
  #-------->(n, s, a, d)
  Hanoi_rec(n-1, s, d, a) #swaps dest and aux so that a disc can be moved from source to auxilary
  d.push(s.pop()) #push on to aux the top of s in the context of the line above but in the context of the line below its going to push from aux to destination
  Hanoi_rec(n-1, a, s, d) #swaps source and aux so that a disc can be moved from aux to dest 
    #print('recur',n, s, a, d)
  # TODO replace pass with your base and recursive cases.
  print(n, s, a, d, '\n')
  #print()

def Hanoi(n): 
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)
  #HanoiRec2(n-1, source, dest, aux)

if __name__ == "__main__":
  n=12
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
