def mix_up(a,b):
   s = a[:2]+b[2:]+ " " +b[:2]+a[2:]
   return s
print(mix_up("Mix","Pod"))
