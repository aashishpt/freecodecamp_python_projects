def evaluate(s:str)->str:
  """
  This function takes arithmatic expression of addition or subtraction and returns its evaluaten in string format.
  ------------------------------------------------------------
  input -> "a + b" or "a - b"
  output -> result in str format
  constraints -> -9999<= a,b <= 9999
  """
  t = s.split()
  res = ''

  # Check valid operator  
  if t[1] not in ['+','-']:
      return "Error: Operator must be '+' or '-'."

  # check valid number  
  try:
      t1 = int(t[0])
      t2 = int(t[2])
       
  except ValueError:
      return "Error: Numbers must only contain digits."

  # check if numbers are 4 digits  
  if (t1>9999 or t1 < -9999 or t2>9999 or t2<-9999):
      return "Error: Numbers cannot be more than four digits."
  
  # addition  
  if t[1] == '+':
      res = t1 + t2
      return str(res)
  
  # subtraction 
  elif t[1] == '-':
      res = t1 -t2
      return str(res)
    