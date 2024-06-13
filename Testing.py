import streamlit as st

# 제목
st.title("롤 챔피언 목록")

# 롤 챔피언 얼굴 이미지를 표시
champions = {
    "아리": "https://ddragon.leagueoflegends.com/cdn/12.2.1/img/champion/Ahri.png",
    "아트록스": "https://ddragon.leagueoflegends.com/cdn/12.2.1/img/champion/Aatrox.png",
    "애쉬": "https://ddragon.leagueoflegends.com/cdn/12.2.1/img/champion/Ashe.png",
    "가렌": "https://ddragon.leagueoflegends.com/cdn/12.2.1/img/champion/Garen.png",
    "다리우스": "https://ddragon.leagueoflegends.com/cdn/12.2.1/img/champion/Darius.png",
}

# 챔피언 이름과 이미지를 목록으로 표시
for name, url in champions.items():
    st.image(url, caption=name, width=100)

# 공통 기능 추가 가능
st.write("공통 기능이나 추가 정보를 이곳에 넣을 수 있습니다.")