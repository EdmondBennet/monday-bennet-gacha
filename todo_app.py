import streamlit as st
import random
from datetime import date

# 도파민 유발 작업 목록 (작업명, 확률, 희귀도)
tasks = [
    ("50자 쓰기", 0.25, "일반"),
    ("100자 쓰기", 0.20, "일반"),
    ("150자 쓰기", 0.15, "고급"),
    ("200자 쓰기", 0.12, "고급"),
    ("250자 쓰기", 0.08, "희귀"),
    ("300자 쓰기", 0.06, "희귀"),
    ("10분 휴식", 0.09, "희귀"),
    ("30분 휴식", 0.04, "영웅"),
    ("500자 쓰기", 0.01, "전설")
]

# 희귀도별 컬러
rarity_colors = {
    "일반": "gray",
    "고급": "green",
    "희귀": "blue",
    "영웅": "violet",
    "전설": "red"
}

# 항목별 감정선 멘트
reactions = {
    "50자 쓰기": "짧고 굵게, 바로 써보자!",
    "100자 쓰기": "좋아, 손 좀 풀리겠는데?",
    "150자 쓰기": "집중력 모드 슬슬 시동 걸자.",
    "200자 쓰기": "지금부터는 몰입 구간이야.",
    "250자 쓰기": "이 정도면 도파민 흐른다.",
    "300자 쓰기": "작가님 폭주 시작하나요?",
    "500자 쓰기": "전설 등장! 진심 쏟을 차례.",
    "10분 휴식": "살짝 숨 돌리고 와!",
    "30분 휴식": "진짜 아무것도 하지 마. 이것도 일임."
}

# 귀여운 랜덤 이모지
emojis = ["🌱", "🌟", "🍀", "🌀", "💫", "🎈", "🧸", "📚", "☕"]

# 페이지 제목
today = date.today().strftime("%Y-%m-%d")
st.set_page_config(page_title="작가님의 도파민 뽑기", page_icon="🌀")
st.title(f"🌀 {today}의 작업 뽑기")
st.write("버튼을 누르면 오늘의 운명 같은 할 일이 도착합니다.")

# 뽑기 버튼
if st.button("✨ 할 일 뽑기 ✨"):
    items, weights, rarities = zip(*tasks)
    chosen = random.choices(list(zip(items, rarities)), weights=weights, k=1)[0]
    task, rarity = chosen
    color = rarity_colors.get(rarity, "gray")
    emoji = random.choice(emojis)

    st.success(f"{emoji} 오늘의 할 일: {task}")
    st.badge(rarity, color=color)  # ✅ 이거 드디어 넣었다
    st.caption(reactions.get(task, "오늘도 힘내자!"))

# 하단 문구
st.write("---")
st.write("오늘 하루도 천천히, 단단하게.")
