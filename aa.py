import streamlit as st

st.write('color:green; 안녕 성균')
st.write('## 	😄안녕 성균')

col1, col2 = st.columns(2)
with col1:
   '하이 성균'
with col2:
   '##### 헬로우 성균'

st.image("111.png", caption="성균이의 사진", use_column_width=True)



import streamlit as st

import streamlit as st

st.markdown("<h2 style='color:green;'>안녕 성균</h2>", unsafe_allow_html=True)

