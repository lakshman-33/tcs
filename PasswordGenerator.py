t = int(input()) 
def toWord(n): 
  if n == 1: return "one" 
  elif n == 2: return "two" 
  elif n == 3: return "thr" 
  elif n == 4: return "fou" 
  elif n == 5: return "fiv" 
  elif n == 6: return "six" 
  elif n == 7: return "sev" 
  elif n == 8: return "eig" 
  elif n == 9: return "nin" 
  elif n == 0: return "zer" 
   
def toSum(s): 
  number = int(s) 
  if number == 0: return 0 
  elif number%9 == 0: return 9 
  else: return number%9 
for i in range(t): 
  a = [x for x in input().split()] 
  n = a[0] 
  name = a[1] 
  d1 = 0 
  if "." in n: 
    d1 = n.index('.') 
  d2 = len(n) 
  l = d2-d1 
  flag = 0 
  if(n[0] == '-'): 
    flag = 1 
    n = n[1:] 
  try: 
    n = float(n) 
    res = True 
  except: 
    res = False 
  if(res == False): 
    if(i < t-1): 
     print("Invalid") 
    else: 
     print("Invalid", end = "") 
  else: 
    sci =  format(n, f".{l}e") 
    part = sci.split('e') 
    num = part[0].split('.') 
    k = int(part[1]) 
    if(flag == 1): res = "-" 
    else: res = "" 
    res += toWord(int(num[0])) +"."+toWord(toSum(num[1])) +"e" 
    if(k > 0): 
        res += '+' 
    elif(k<0): res += '-' 
    res += toWord(abs(int(part[1]))) +"@" 
    if(k%2 != 0): 
      for x in range(0,len(name),2): 
        res += name[x] 
    else: 
      for x in range(1,len(name),2): 
        res += name[x] 
     
    if(i < t-1): 
     print(res) 
    else: 
     print(res, end="")