import streamlit as st

def show_supporters_with_images():
    supporters = [
        {"name": "Alistar", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Alistar.png"},
        {"name": "Bard", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Bard.png"},
        {"name": "Blitzcrank", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Blitzcrank.png"},
        {"name": "Braum", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Braum.png"},
        {"name": "Janna", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Janna.png"},
        {"name": "Karma", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Karma.png"},
        {"name": "Leona", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Leona.png"},
        {"name": "Lulu", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Lulu.png"},
        {"name": "Lux", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Lux.png"},
        {"name": "Morgana", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Morgana.png"},
        {"name": "Nami", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Nami.png"},
        {"name": "Nautilus", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Nautilus.png"},
        {"name": "Rakan", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Rakan.png"},
        {"name": "Senna", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Senna.png"},
        {"name": "Seraphine", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Seraphine.png"},
        {"name": "Sona", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Sona.png"},
        {"name": "Soraka", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Soraka.png"},
        {"name": "Tahm Kench", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/TahmKench.png"},
        {"name": "Taric", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Taric.png"},
        {"name": "Thresh", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Thresh.png"},
        {"name": "Yuumi", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Yuumi.png"},
        {"name": "Zilean", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Zilean.png"},
        {"name": "Zyra", "image_url": "https://ddragon.leagueoflegends.com/cdn/12.11.1/img/champion/Zyra.png"}
    ]

    st.header("League of Legends Supporters")
    st.write("서포터 챔피언을 선택하세요:")

    # 선택된 챔피언의 이름을 저장할 변수
    selected_champion = None

    # 각 챔피언의 이름과 이미지를 함께 출력하고, 클릭 시 선택되었다는 메시지를 출력
    for supporter in supporters:
        image = st.image(supporter['image_url'], width=200)
        if image.image_clicked:
            selected_champion = supporter['name']
            st.success(f"{selected_champion}가 선택되었습니다!")

    # 선택된 챔피언 출력
    if selected_champion:
        st.write(f"선택된 챔피언: {selected_champion}")

if __name__ == "__main__":
    show_supporters_with_images()