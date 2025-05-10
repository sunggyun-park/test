import streamlit as st

# HTML 스타일로 텍스트 출력
st.markdown("<h2 style='color:green;'>안녕 성균</h2>", unsafe_allow_html=True)

# 제목 및 텍스트 출력
st.write('## 😄 안녕 성균')

# 두 개의 열 생성
col1, col2 = st.columns(2)
with col1:
    st.write('하이 성균')
with col2:
    st.write('##### 헬로우 성균')

# 이미지 출력
st.image("111.png", caption="성균이의 사진", use_column_width=True)

# 라디오 버튼
color = st.radio('색상 선택', ('blue', 'red'))