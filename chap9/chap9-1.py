import os
# print(os.path.join("Users","bob","st.txt"))

st = open("chap9/st.txt","w")
st.write("Hi from python!!!!!")
st.close()

with open("chap9/st2.txt","w") as f:
  f.write("test")

with open("chap9/st.txt","r") as f:
  print(f.read())
