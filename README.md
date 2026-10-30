# DSE Physics Topic Classifier

A simple Streamlit app that lets users upload DSE Physics past papers (PDF) and automatically classifies the questions into official topics.

## Features
- Upload multiple PDF past papers
- Automatic question splitting
- Keyword-based topic classification
- Grouped view by topic
- Download results as JSON

## Official Topics Supported
- Heat and Gases
- Force and Motion
- Wave Motion
- Electricity and Magnetism
- Radioactivity and Nuclear Energy
- Astronomy and Space Science
- Atomic World
- Energy and Use of Energy
- Medical Physics

## How to Run

```bash
git clone https://github.com/YOUR_USERNAME/dse-physics-topic-classifier.git
cd dse-physics-topic-classifier
pip install -r requirements.txt
streamlit run app.py
