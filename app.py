import streamlit as st

# ページ全体の設定（ブラウザのタブ名など）
st.set_page_config(
    page_title="HAJIMEのStreamlitサンプルアプリ",
    page_icon="📊",
    layout="centered",
)

# ちょっとだけCSSで背景とカードっぽい枠を調整（おまけ）
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7fb;
    }
    .app-card {
        background-color: white;
        padding: 2rem;
        border-radius: 0.8rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.06);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# カードっぽいコンテナ
with st.container():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.title("HAJIMEアプリ②：文字数カウント & BMIチェック")

    st.write("**動作モード1: 文字数カウント ✍️**")
    st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")

    st.write("**動作モード2: BMI値の計算 ⚖️**")
    st.write("身長と体重を入力すると、肥満度を表す体型指数のBMI値を計算します。")

    # 動作モードの選択
    selected_item = st.radio(
        "動作モードを選択してください。",
        ["文字数カウント", "BMI値の計算"],
        horizontal=True,
    )

    st.divider()

    # 動作モードによる分岐
    if selected_item == "文字数カウント":
        input_message = st.text_input(
            label="文字数のカウント対象となるテキストを入力してください。"
        )
        text_count = len(input_message)
    else:
        col1, col2 = st.columns(2)
        with col1:
            height = st.text_input(label="身長（cm）を入力してください。")
        with col2:
            weight = st.text_input(label="体重（kg）を入力してください。")

    # 実行ボタン
    if st.button("実行"):
        st.divider()

        if selected_item == "文字数カウント":
            if input_message:
                st.success(f"文字数は **{text_count}文字** です。")
            else:
                st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")
        else:
            if height and weight:
                try:
                    bmi = round(int(weight) / ((int(height) / 100) ** 2), 1)
                    st.info(f"BMI値は **{bmi}** です。")
                except ValueError:
                    st.error("身長と体重は数値で入力してください。")
            else:
                st.error("身長と体重をどちらも入力してください。")

    st.markdown("</div>", unsafe_allow_html=True)
