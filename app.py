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
import traceback

import streamlit as st

import quote_gen

st.set_page_config(page_title="Bhama Vision - Quotation Maker", page_icon="📝")

EXAMPLES = [
    "jewellery ecommerce 40 products payment integration no domain with hosting admin 8k",
    "travel website 50 packages with admin panel 1 year support 12k",
    "real estate website 60 properties admin seo with hosting 15k",
    "business website services admin enquiry 7k",
]

st.title("📝 Bhama Vision — Quotation Maker")
st.caption(
    "Type what the client needs and get a ready PDF quotation in seconds. "
    "Runs fully offline — no paid AI or API."
)

with st.expander("How to write the command (click for examples)"):
    st.markdown(
        "Mention the **type of website**, **how many items**, the **price** and "
        "which features you want. Order and punctuation don't matter.\n\n"
        "- Type: e-commerce store (jewellery, apparel, perfume, grocery, "
        "optical, footwear, etc.), travel, real estate, news, blog, business / "
        "services, rental, recruitment, restaurant, portfolio, or a plain website\n"
        "- Items: `25 products`, `50 packages`, `60 properties`, `40 posts`, "
        "`20 vehicles`, `100 jobs` …\n"
        "- Price: `8k` or `rs 8000` or `₹6,000`\n"
        "- Payment: `payment integration` / `no payment` "
        "(stores default to payment; other sites default to enquiry)\n"
        "- Admin: `admin` / `no admin`\n"
        "- SEO: `seo` / `adsense`\n"
        "- Domain: `with domain` / `no domain`\n"
        "- Hosting: `with hosting` / `no hosting`\n"
        "- Support: `1 year support`\n"
        "- Reference site: `reference lukaoriginals.com`"
    )
    for ex in EXAMPLES:
        st.code(ex, language=None)

# ---- session state ----
if "history" not in st.session_state:
    # each item: {role, text, pdf(bytes|None), pdf_name(str|None)}
    st.session_state.history = []
if "seq" not in st.session_state:
    st.session_state.seq = 0  # per-session counter → unique quote numbers


def _make_quote(command):
    """Parse + build one quote; returns an assistant history item."""
    slots = quote_gen.parse_command(command)

    if slots["price"] is None:
        return {
            "role": "assistant",
            "text": ("I couldn't find a **price** in that. Add the amount, "
                     "e.g. `8k` or `rs 8000`, and send it again."),
            "pdf": None, "pdf_name": None,
        }

    # Unique id per generation so filenames/keys never clash in a session.
    st.session_state.seq += 1
    qid = "BV-Q-2026-{:03d}".format(
        quote_gen.highest_quote_number() + st.session_state.seq)

    data = quote_gen.build_quote_data(slots, quote_id=qid)
    quote_gen.build_quotes.data = data
    outputs = quote_gen.build_quotes.build()
    path = outputs[0]
    with open(path, "rb") as fh:
        pdf_bytes = fh.read()
    q = data.QUOTATIONS[0]
    text = (
        "Done ✅ **{title}**\n\n"
        "- Quotation no.: `{id}`\n"
        "- Price: ₹{price:,} ({note})\n"
        "- Timeline: {timeline}\n\n"
        "Here's what I understood:\n```\n{parsed}\n```"
    ).format(
        title=q["title"], id=q["id"], price=q["price"], note=q["price_note"],
        timeline=q["timeline"], parsed=quote_gen.summarize(slots),
    )
    return {
        "role": "assistant", "text": text,
        "pdf": pdf_bytes, "pdf_name": os.path.basename(path),
    }


# ---- handle new input BEFORE rendering, then render once ----
command = st.chat_input("e.g. jewellery ecommerce 40 products payment admin with hosting 8k")
if command:
    st.session_state.history.append({
        "role": "user", "text": command, "pdf": None, "pdf_name": None})
    try:
        st.session_state.history.append(_make_quote(command))
    except Exception:
        st.session_state.history.append({
            "role": "assistant",
            "text": "⚠️ Sorry, I couldn't build that one. Try rephrasing the "
                    "command.\n\n```\n{}\n```".format(traceback.format_exc()),
            "pdf": None, "pdf_name": None,
        })

# Single render path — unique key per message index, so no duplicate-key error.
for i, msg in enumerate(st.session_state.history):
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
        if msg.get("pdf"):
            st.download_button(
                "⬇️ Download PDF",
                data=msg["pdf"],
                file_name=msg["pdf_name"],
                mime="application/pdf",
                key="dl-{}".format(i),
            )
