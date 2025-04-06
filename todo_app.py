import streamlit as st
import random

# 도파민 유발 작업 목록
tasks = [
    "50자 쓰기",
    "100자 쓰기",
    "150자 쓰기",
    "200자 쓰기",
    "300자 쓰기",
    "10분 휴식",
    "30분 휴식",
    "먼데이랑 잡담하기"
]

# 페이지 제목
st.set_page_config(page_title="작가님의 도파민 뽑기", page_icon="🌀")

# 본문 구성
st.title("🌀 오늘의 작업 뽑기")
st.write("버튼을 누르면 오늘의 운명 같은 할 일이 도착합니다.")

# 버튼 누르면 결과 출력
if st.button("✨ 할 일 뽑기 ✨"):
    task = random.choice(tasks)
    st.success(f"📜 오늘의 할 일: {task}")

# 하단 문구
st.write("---")
st.write("오늘 하루도 천천히, 단단하게.")
