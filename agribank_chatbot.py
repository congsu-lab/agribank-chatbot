import streamlit as st
from openai import OpenAI

# === CẤU HÌNH CƠ BẢN ===
client = OpenAI(api_key="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")

st.set_page_config(page_title="Trợ lý Agribank 24/7", page_icon="💬", layout="centered")

# === GIAO DIỆN PHẦN ĐẦU ===
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Agribank_logo.svg", width=120)
st.title("Trợ lý Agribank 24/7")
st.markdown("#### 💬 Trợ lý Agribank thân thiện, chuyên nghiệp, tư vấn dịch vụ và hỗ trợ khách hàng 24/7.")
st.divider()

# === NÚT GỢI Ý CHỦ ĐỀ ===
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏦 Tư vấn vay vốn"):
        st.session_state["preset"] = "Tư vấn vay vốn tại Agribank"
with col2:
    if st.button("💰 Gửi tiết kiệm"):
        st.session_state["preset"] = "Tư vấn gửi tiền tiết kiệm tại Agribank"
with col3:
    if st.button("📱 Mở tài khoản"):
        st.session_state["preset"] = "Hướng dẫn mở tài khoản và App Agribank"
with col4:
    if st.button("❓ Thắc mắc / hỗ trợ"):
        st.session_state["preset"] = "Giải đáp thắc mắc và hỗ trợ khách hàng"

st.divider()

# === KHỞI TẠO BỘ NHỚ HỘI THOẠI ===
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Bạn là trợ lý Agribank, tư vấn và hỗ trợ khách hàng bằng tiếng Việt chuyên nghiệp."}
    ]

# === Ô NHẬP LIỆU NGƯỜI DÙNG ===
user_input = st.chat_input("Nhập câu hỏi của bạn tại đây...")

if user_input or "preset" in st.session_state:
    if "preset" in st.session_state:
        user_input = st.session_state["preset"]
        del st.session_state["preset"]

    st.session_state.messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-5",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# === HIỂN THỊ HỘI THOẠI ===
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
