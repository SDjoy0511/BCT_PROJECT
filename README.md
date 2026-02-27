## AI Interview Simulator

This is an interactive **AI Interview Simulator** built with `streamlit` and `langchain-google-genai`. It conducts domain-specific interviews and provides personality-based feedback using Google's Gemini models.

### Features
- **Domain selection**: Choose from Python, Java, Machine Learning, Web Development, and Android.
- **Interviewer role**: Switch between HR, Technical, and Manager-style interviews.
- **Adaptive difficulty**: Starts at Easy and gradually moves to Medium and Hard based on your answers.
- **Answer evaluation**: Scores your response and gives strengths, weaknesses, and improvement tips.
- **Final report**: Generates an overall performance summary with a 7‑day improvement roadmap.

### Requirements
- Python 3.9+
- A Google Gemini API key stored in the `GEMINI_API_KEY` environment variable.

Recommended Python dependencies (add these to `requirements.txt` if you create one):

```txt
streamlit
python-dotenv
langchain-google-genai
```

### Running the App
1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   or manually:
   ```bash
   pip install streamlit python-dotenv langchain-google-genai
   ```
3. Set your Gemini API key (example on Windows PowerShell):
   ```powershell
   setx GEMINI_API_KEY "YOUR_API_KEY_HERE"
   ```
4. From the `Project` directory, run:
   ```bash
   streamlit run app.py
   ```

### Project Structure
- `app.py` – Main Streamlit application.
- `README.md` – Project overview and setup instructions.

