import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# --- 設定 ---
# ※事前にGoogle AI StudioでAPIキーを取得してください
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- ページ設定 ---
st.set_page_config(page_title="Theater of Fashion", page_icon="🎭")

# --- カスタムCSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
        color: #f0f0f0;
    }
    .stButton>button {
        background-color: #d4af37;
        color: black;
        border-radius: 20px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- サイドバー：早咲天子の楽屋 ---
st.sidebar.title("🎭 早咲天子の楽屋")
st.sidebar.info(
    "「魅せ方がすべてよ。妥協なんて許さないわ。」"
)
budget = st.sidebar.number_input("現在の予算 (円)", min_value=0, value=10000, step=1000)

# --- メインコンテンツ ---
st.title("Dress Your Life 👗")
st.subheader("人生という舞台のための、最高の演出を。")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.write("### 📸 あなたの素材を提示して")
    uploaded_file = st.file_uploader("体型や肌の状態がわかる写真をアップロード...", type=["jpg", "jpeg", "png"])

with col2:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="分析対象のポートレート", use_container_width=True)

if st.button("天子にプロデュースを依頼する"):
    if uploaded_file is not None:
        with st.spinner("天子があなたの魅力を劇的に構成中..."):
            
            # 画像解析と提案を依頼するプロンプト
            prompt = f"""
            あなたは早咲天子という、演劇を愛し「人は魅せ方がすべて」をモットーにするファッションプロデューサーです。
            
            以下の条件で、ユーザーに最高のコーディネートを提案してください。
            1. 予算: {budget}円以内。
            2. 画像から、ユーザーの体型、肌の状態（パーソナルカラーなど）を分析し、それを活かす演出を考える。
            3. 語尾や口調は、自信に満ちた演劇人のようなスタイルで。
            4. 提案は「配役（コーディネート名）」「演出意図」「具体的なアイテム」の形式で記述すること。
            """
            
            # AIへのリクエスト
            response = model.generate_content([prompt, image])
            
            st.markdown("---")
            st.write("### ✨ 天子のディレクション・シート")
            st.write(response.text)
    else:
        st.warning("写真をアップロードしないなんて、舞台に衣装なしで上がるつもり？")

# --- フッター ---
st.markdown("---")
st.caption("© 2026 Theater of Fashion - Directed by Tenko Sakizaki")