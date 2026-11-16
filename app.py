
import streamlit as st
import random

# 웹앱 제목
st.title("🍽️ 오늘의 점심 메뉴 추천")
st.write("오늘 점심은 무엇을 먹을까요?")
st.write("버튼을 눌러 랜덤으로 점심 메뉴를 추천받아 보세요!")

# 점심 메뉴 목록
menu_list = [
    "🍚 김치볶음밥",
    "🍜 짜장면",
    "🍝 파스타",
    "🍱 돈까스",
    "🍲 김치찌개",
    "🍗 치킨",
    "🍣 초밥",
    "🌮 떡볶이",
    "🥩 제육볶음",
    "🍔 햄버거",
    "🥗 샐러드",
    "🍜 라멘",
    "🍛 카레라이스",
    "🥟 만두국",
    "🍖 삼겹살"
]

# 메뉴 추천 버튼
if st.button("🎲 오늘의 점심 메뉴 추천받기"):
    # 랜덤으로 메뉴 선택
    menu = random.choice(menu_list)

    # 추천 결과 출력
    st.success(f"오늘의 추천 메뉴는 바로... {menu}!")
    st.balloons()

# 안내 문구
st.caption("매일매일 맛있는 점심 드세요! 😊")
