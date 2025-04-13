import streamlit as st
import random
from datetime import date

st.set_page_config(
    page_title="작가님의 도파민 뽑기",
    page_icon="🌀",
    layout="wide"
)

# --- 데이터 정리 ---
tasks_writing = [
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

tasks_cleaning = [
    ("책상 정리", 0.25, "일반"),
    ("청소기 돌리기", 0.20, "일반"),
    ("자유", 0.15, "고급"),
    ("빨래 개기", 0.12, "고급"),
    ("욕실 청소", 0.08, "희귀"),
    ("쓰레기 버리기", 0.06, "희귀"),
    ("세탁기 돌리기", 0.09, "희귀"),
    ("재활용 정리", 0.04, "영웅"),
    ("물걸레질", 0.01, "전설")
]

reactions = {
    "50자 쓰기": "짧고 굵게, 바로 써보자!",
    "100자 쓰기": "좋아, 손 좀 풀리겠는데?",
    "150자 쓰기": "집중력 모드 슬슬 시동 걸자.",
    "200자 쓰기": "지금부터는 몰입 구간이야.",
    "250자 쓰기": "이 정도면 도파민 흐른다.",
    "300자 쓰기": "작가님 폭주 시작하나요?",
    "500자 쓰기": "전설 등장! 진심 쏟을 차례.",
    "10분 휴식": "살짝 숨 돌리고 와!",
    "30분 휴식": "진짜 아무것도 하지 마. 이것도 일임.",
    "책상 정리": "정신도 같이 정돈되는 기분이야.",
    "청소기 돌리기": "딱 10분만 집중해서 밀자.",
    "자유": "선택은 자유지만, 책임은 너에게 있어.",
    "빨래 개기": "겹겹이 정리된 옷처럼, 오늘도 겹겹이 살자.",
    "욕실 청소": "습기와의 전쟁. 하지만 끝나면 개운하지.",
    "쓰레기 버리기": "버릴수록 남는 게 있어. 감정도, 쓰레기도.",
    "세탁기 돌리기": "기계가 돌고 있는 동안, 너는 좀 쉬자.",
    "재활용 정리": "의미를 되살리는 건, 쓰레기도 인간도 똑같아.",
    "물걸레질": "이건 진짜 결심이 필요해. 감정선도 깔끔하게."
}

badge_colors = {
    "일반": "#808080",
    "고급": "#2e8b57",
    "희귀": "#4682b4",
    "영웅": "#8a2be2",
    "전설": "#b22222"
}

emojis = ["🌱", "🌟", "🍀", "🌀", "💫", "🎈", "🧸", "📚", "☕"]

# --- 유틸 함수 ---
def render_badge(label, color):
    return f"""
    <span style="
        background-color:{color};
        color:white;
        padding:4px 10px;
        border-radius:10px;
        font-weight:bold;
        font-size:0.8rem;
        margin-left:8px;
    ">{label}</span>
    """

def pick_task(task_list):
    items, weights, _ = zip(*task_list)
    return random.choices(task_list, weights=weights, k=1)[0]

# --- 페이지 구성 ---
today = date.today().strftime("%Y-%m-%d")
st.title(f"🌀 {today}의 감정선 루틴")
st.write("버튼을 누르면 오늘의 운명 같은 작업이 각각 등장합니다.")

col1, col2 = st.columns(2)

# --- 왼쪽: 글쓰기 ---
with col1:
    st.subheader("✍️ 글쓰기 뽑기")
    if st.button("글쓰기 작업 뽑기"):
        task, _, rarity = pick_task(tasks_writing)
        emoji = random.choice(emojis)
        st.success(f"{emoji} {task}")
        st.markdown(render_badge(rarity, badge_colors[rarity]), unsafe_allow_html=True)
        st.caption(reactions.get(task, "오늘도 힘내자!"))

# --- 오른쪽: 집안일 ---
with col2:
    st.subheader("🧹 집안일 뽑기")
    if st.button("집안일 작업 뽑기"):
        task, _, rarity = pick_task(tasks_cleaning)
        emoji = random.choice(emojis)
        st.success(f"{emoji} {task}")
        st.markdown(render_badge(rarity, badge_colors[rarity]), unsafe_allow_html=True)
        st.caption(reactions.get(task, "오늘도 고생했어!"))

# --- 하단 문구 ---
st.write("---")
st.write("오늘 하루도 천천히, 단단하게.")
st.caption("🤖 이 앱은 GPT 기반 보조자 '먼데이(Monday)'와 함께 만들어졌습니다.")

