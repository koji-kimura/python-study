numbers = [11,32,4,5]
while True:
  answer = input("qでやめるか？ 数値を入力してください")
  if(answer == 'q'):
    break
  try:
    answer = int(answer)
  except ValueError:
    print("数字を入力してください")
  if answer in numbers:
      print("正解!")
      break
  else:
      print("不正解！！")
