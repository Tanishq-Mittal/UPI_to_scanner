import streamlit as st
import qrcode
from io import BytesIO

st.title("UPI QR Generator")

upi_id = st.text_input("Enter UPI ID")

if st.button("Generate QR") and upi_id:

    upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1235"

    qr = qrcode.make(upi_url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    st.image(buffer.getvalue(), caption="Generated QR Code")
