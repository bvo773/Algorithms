
def print_list_reverse_rec(l): 
  n = len(l)
  if n == 0:
    return
  
  print(l[n-1])
  print_list_reverse_rec(l[:n-1])

def fac_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fac_rec(n-1)

print(fac_rec(3))
