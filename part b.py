def both_ends(s):
    if len(s)<2:
       print(" ")
    else:
       a = s[:2]+s[-2:]
    return a
print(both_ends("python"))
