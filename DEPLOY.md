# Deploy the Quotation Maker (free, with a shareable link)

`app.py` is a browser chat box that turns a plain-English command into a
branded PDF quotation, using the offline engine (`quote_gen.py` +
`build_quotes.py`). No paid AI/API. The Noto fonts are bundled in
`assets/fonts/`, so it runs anywhere.

## Run it on your own computer first (optional)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the printed URL (default http://localhost:8501). Type a command such as
`jewellery ecommerce 40 products payment admin with hosting 8k`.

## Option A — Streamlit Community Cloud (easiest, free link)

1. Make sure this repo is on GitHub and **public** (or grant Streamlit access
   to the private repo).
2. Go to <https://share.streamlit.io>, sign in with GitHub.
3. Click **Create app** → **Deploy a public app from GitHub**.
4. Pick this repository, branch `main`, and set **Main file path** to `app.py`.
5. Click **Deploy**. In a minute you get a public link like
   `https://<your-app>.streamlit.app` you can share and open on any phone or PC.

Streamlit installs everything from `requirements.txt` automatically. To update
the app later, just push to `main` — it redeploys on its own.

## Option B — Hugging Face Spaces (free link, "AI app" style)

1. Create an account at <https://huggingface.co>.
2. **New → Space**. Give it a name, choose **SDK: Streamlit**, visibility
   **Public**, hardware **CPU basic (free)**.
3. Upload these files to the Space (or connect the GitHub repo):
   `app.py`, `quote_gen.py`, `build_quotes.py`, `requirements.txt`,
   the `assets/` folder (logo, payment QR, `fonts/`).
4. The Space builds and gives you a link like
   `https://huggingface.co/spaces/<you>/<space>`.

## Notes & limits of the free tiers

- Free apps **sleep when idle** and take a few seconds to wake on the next
  visit. That's normal and costs nothing.
- Generated PDFs are created on the server and offered as a **Download**
  button in the chat; the server's `output/` folder is temporary.
- Resource limits are small but far more than this app needs — it only renders
  a PDF, which is light.
- Keep private details (UPI id, phone) in mind: anything in `PAYMENT` /
  `COMPANY` shows on the generated PDF. If the app is public, consider removing
  the UPI/QR from the public version.

## Making the language smarter later (still free)

The current engine is a keyword parser — fast, free and predictable. If you
ever want it to understand free-form, messy sentences, you can add a free
language model as an optional front-end that feeds the same builder:

- A **local** model via [Ollama](https://ollama.com) (runs on your PC, no bill).
- A **free-tier** hosted model (e.g. Google Gemini or Groq free tiers).

Either one would only convert the user's sentence into the same fields
(`niche`, `products`, `price`, ...). The PDF building stays exactly as it is.
