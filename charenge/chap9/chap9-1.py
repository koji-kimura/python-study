# coding: UTF-8
answer = input("何か文言を入力してください")

st = open("st.txt","w",encoding="utf-8")
st.write(answer)
st.close()