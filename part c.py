def fix_start(s):
   print("\n")
   a = s[1:].replace(s[0],"*")
   a=s[0]+a
   return a
print(fix_start("bubble"))
