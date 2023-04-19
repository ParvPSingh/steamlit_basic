import streamlit as st
def find_max(a,b,c):
  l=list([a,b,c])
  return max(l)
a = st.number_input("First number", min_value=0, step=1)
b = st.number_input("Second number", min_value=0, step=1)
c = st.number_input("Third number", min_value=0, step=1)

if st.button("Largest No"):
  res = find_max(a,b,c)
  st.write(res)
