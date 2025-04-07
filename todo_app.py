import streamlit as st
import random
from datetime import date

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

# 각 작업에 맞는 반응 멘트
reactions = {
    "50자 쓰기": "짧고 굵게, 바로 써보자!",
    "100자 쓰기": "좋아, 손 좀 풀리겠는데?",
    "150자 쓰기": "집중력 모드 슬슬 시동 걸자.",
    "200자 쓰기": "지금부터는 몰입 구간이야.",
    "300자 쓰기": "작가님 폭주 시작하나요?",
    "10분 휴식": "살짝 숨 돌리고 와!",
    "30분 휴식": "진짜 아무것도 하지 마. 이것도 일임.",
    "먼데이랑 잡담하기": "좋아. 난 여기 있어. 무슨 얘기할래?"
}

# 귀여운 랜덤 이모지
emojis = ["🌱", "🌟", "🍀", "🌀", "💫", "🎈", "🧸", "📚", "☕"]

# 페이지 제목
today = date.today().strftime("%Y-%m-%d")
st.set_page_config(page_title="작가님의 도파민 뽑기", page_icon="🌀")
st.title(f"🌀 {today}의 작업 뽑기")
st.write("버튼을 누르면 오늘의 운명 같은 할 일이 도착합니다.")

# 버튼 누르면 결과 출력
if st.button("✨ 할 일 뽑기 ✨"):
    task = random.choice(tasks)
    emoji = random.choice(emojis)
    st.success(f"{emoji} 오늘의 할 일: {task}")
    st.caption(reactions.get(task, "오늘도 힘내자!"))

# 하단 문구
st.write("---")
st.write("오늘 하루도 천천히, 단단하게.")
