def returnFloat(x):
  try:
    float(x)
    return float(x)
  except ValueError:
    return "Please input number"
print(returnFloat(10))
