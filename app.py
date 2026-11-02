"""
Bhama Vision - quotation chat app (web UI around the offline quote bot).

A chat box in the browser: type a plain-English command and get a branded
A4 PDF quotation to download, in seconds. It reuses the SAME engine as the
command line (`quote_gen.py` + `build_quotes.py`) - no external AI / API,
nothing paid. Deploy it free on Streamlit Community Cloud or Hugging Face
Spaces and share the link.

Run locally:

    pip install -r requirements.txt
    streamlit run app.py

Then open the URL it prints (default http://localhost:8501).
"""
import os

import streamlit as st

import quote_gen

st.set_page_config(page_title="Bhama Vision - Quotation Maker", page_icon="📝")

EXAMPLES = [
    "jewellery ecommerce 40 products payment integration no domain with hosting admin 8k",
    "apparel ecommerce 25 products payment admin 8k reference lukaoriginals.com",
    "perfume ecommerce 30 products payment integration admin no domain with hosting 7k",
]

st.title("📝 Bhama Vision — Quotation Maker")
st.caption(
    "Type what the client needs and get a ready PDF quotation in seconds. "
    "Runs fully offline — no paid AI or API."
)

with st.expander("How to write the command (click for examples)"):
    st.markdown(
        "Mention the **niche**, **number of products**, **price** and which "
        "features you want. Order and punctuation don't matter.\n\n"
        "- Niche: jewellery, apparel, perfume, grocery, optical, footwear, "
        "beauty, electronics, furniture, food (or leave blank for generic)\n"
        "- Products: `25 products`\n"
        "- Price: `8k` or `rs 8000` or `₹6,000`\n"
        "- Payment: `payment integration` / `no payment`\n"
        "- Admin: `admin` / `no admin`\n"
        "- Domain: `with domain` / `no domain`\n"
        "- Hosting: `with hosting` / `no hosting`\n"
        "- Support: `1 year support`\n"
        "- Reference site: `reference lukaoriginals.com`"
    )
    for ex in EXAMPLES:
        st.code(ex, language=None)

# Chat history lives in the session.
if "history" not in st.session_state:
    st.session_state.history = []  # list of dicts: role, text, pdf(bytes), pdf_name

# Replay history.
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
        if msg.get("pdf"):
            st.download_button(
                "⬇️ Download PDF",
                data=msg["pdf"],
                file_name=msg["pdf_name"],
                mime="application/pdf",
                key="dl-" + msg["pdf_name"],
            )

command = st.chat_input("e.g. jewellery ecommerce 40 products payment admin with hosting 8k")

if command:
    st.session_state.history.append({"role": "user", "text": command})
    with st.chat_message("user"):
        st.markdown(command)

    with st.chat_message("assistant"):
        slots = quote_gen.parse_command(command)

        if slots["price"] is None:
            reply = (
                "I couldn't find a **price** in that. Add the amount, e.g. "
                "`8k` or `rs 8000`, and send it again."
            )
            st.markdown(reply)
            st.session_state.history.append({"role": "assistant", "text": reply})
        else:
            data = quote_gen.build_quote_data(slots)
            quote_gen.build_quotes.data = data
            outputs = quote_gen.build_quotes.build()
            path = outputs[0]
            with open(path, "rb") as fh:
                pdf_bytes = fh.read()
            q = data.QUOTATIONS[0]
            reply = (
                "Done ✅ **{title}**\n\n"
                "- Quotation no.: `{id}`\n"
                "- Price: ₹{price:,} ({note})\n"
                "- Timeline: {timeline}\n\n"
                "Here's what I understood:\n```\n{parsed}\n```"
            ).format(
                title=q["title"], id=q["id"], price=q["price"],
                note=q["price_note"], timeline=q["timeline"],
                parsed=quote_gen.summarize(slots),
            )
            st.markdown(reply)
            pdf_name = os.path.basename(path)
            st.download_button(
                "⬇️ Download PDF",
                data=pdf_bytes,
                file_name=pdf_name,
                mime="application/pdf",
                key="dl-" + pdf_name,
            )
            st.session_state.history.append({
                "role": "assistant", "text": reply,
                "pdf": pdf_bytes, "pdf_name": pdf_name,
            })
