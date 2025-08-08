
# 🧠 MindTrack

## CURRENT STATUS

This project is currently in progress. The following features are implemented:

- Basic Streamlit app structure
- Journal input functionality
- Emotion and sentiment analysis using TextBlob
- Requirements management

Areas for future improvement include:

- Enhanced emotion model accuracy (using HuggingFace, etc.)
- Visualizing emotion trends over time
- Saving and exporting journal history
- User account management

---

## 📌 Project Title

**MindTrack** – Emotion-Aware AI Journal

---

## 📄 Description

MindTrack is an AI-powered mental health journaling assistant that helps users reflect on their emotions through real-time NLP-based analysis. Built in Python using Streamlit, it offers a minimal and accessible way to track your feelings.

---

## 🚀 Getting Started

### Note for CPU-Only Users

If you run into issues with specific libraries, ensure your `requirements.txt` uses the CPU-compatible versions of dependencies. (MindTrack does not use heavy GPU libraries.)

---

### 📦 Dependencies

Refer to `requirements.txt`

Main packages:
- streamlit
- textblob
- pandas

---

### ⚙️ Installing

Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r mindtrack/requirements.txt
````

---

### ▶️ Executing Program

To launch the Streamlit app:

```bash
streamlit run mindtrack/app.py
```

The app should open in your browser at `http://localhost:8501`

---

## 📂 Dataset Instructions (for future versions)

Currently, the app is text-input only. Future versions may support importing datasets (CSV, JSON, or from journaling apps).

---

## 🤝 Help

Issues or bugs? [Open an issue here](https://github.com/aarjivi1/mindtrack/issues)

---

## 👤 Author

Aarjivi Chandra
[GitHub: @aarjivi1](https://github.com/aarjivi1)

---

## 🪪 License

MIT License – see the `LICENSE` file.

---

## 🙌 Acknowledgments

* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* [Streamlit](https://streamlit.io/)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)

```

