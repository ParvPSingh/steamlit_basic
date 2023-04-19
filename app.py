!pip install streamlit -q
import streamlit as st
def find_max(a,b,c):
  l=list([a,b,c])
  return max(l)
a = st.number_input()
b = st.number_input()
c = st.number_input()
res = find_max(a,b,c)
if st.button("Largest No"):
  st.write(res)
