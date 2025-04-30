import streamlit as st

st.set_page_config(
    page_title="사진첩",
    page_icon="📷"
)

st.title("📸 나만의 사진첩")
st.markdown("**사진**을 하나씩 추가해서 앨범을 채워보세요!")

photo_type_options = ["인물", "풍경", "여행", "접사", "패션", "음식", "거리", "스포츠", "연예인", "기타"]

initial_photos = [
    {
        "name": "동해바다",
        "types": ["풍경"],
        "year": "2023",
        "image_url": "https://picsum.photos/id/1018/400/300"
    },
    {
        "name": "친구와 여행",
        "types": ["여행", "인물"],
        "year": "2022",
        "image_url": "https://picsum.photos/id/1015/400/300"
    },
    {
        "name": "맛있는 음식",
        "types": ["음식"],
        "year": "2024",
        "image_url": "https://picsum.photos/id/1035/400/300"
    },
    {
        "name": "하늘",
        "types": ["풍경"],
        "year": "2021",
        "image_url": "https://picsum.photos/id/1040/400/300"
    },
]

example_photo = {
    "name": "예시 사진",
    "types": ["풍경", "여행"],
    "year": "2020",
    "image_url": "https://picsum.photos/id/1025/400/300"
}

if "photos" not in st.session_state:
    st.session_state.photos = initial_photos

auto_complete = st.toggle("예시 사진으로 자동 채우기")

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("사진 이름", value=example_photo["name"] if auto_complete else "")
        year = st.text_input("사진 연도", value=example_photo["year"] if auto_complete else "")
    with col2:
        types = st.multiselect(
            "사진 종류 (최대 2개 선택)",
            options=photo_type_options,
            max_selections=2,
            default=example_photo["types"] if auto_complete else []
        )
    image_url = st.text_input("사진 URL", value=example_photo["image_url"] if auto_complete else "")
    submit = st.form_submit_button("추가하기")

    if submit:
        if not name:
            st.error("사진 이름을 입력해주세요.")
        elif not year:
            st.error("사진 연도를 입력해주세요.")
        elif len(types) == 0:
            st.error("사진 종류를 최소 1개 선택해주세요.")
        else:
            st.success("사진이 추가되었습니다!")
            st.session_state.photos.append({
                "name": name,
                "types": types,
                "year": year,
                "image_url": image_url if image_url else "https://picsum.photos/400/300"
            })

delete_index = None

for i in range(0, len(st.session_state.photos), 4):
    row_photos = st.session_state.photos[i:i+4]
    cols = st.columns(len(row_photos))
    for j in range(len(row_photos)):
        with cols[j]:
            photo = row_photos[j]
            with st.expander(f"📷 {photo['name']} ({photo['year']})", expanded=True):
                st.image(photo["image_url"], use_column_width=True)
                st.caption(" / ".join(photo["types"]))
                if st.button("삭제", key=f"delete_{i+j}", use_container_width=True):
                    delete_index = i + j

if delete_index is not None:
    del st.session_state.photos[delete_index]
    st.experimental_rerun()