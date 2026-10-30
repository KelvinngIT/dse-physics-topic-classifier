import streamlit as st
from collections import defaultdict
from utils import extract_text_from_pdf, split_into_questions
from classifier import classify_question, TOPICS

st.set_page_config(
    page_title="DSE Physics Topic Classifier",
    page_icon="📘",
    layout="wide"
)

st.title("📘 DSE Physics Past Paper → Topic Classifier")
st.markdown("Upload DSE Physics past papers (PDF) and automatically separate questions by topic.")

# Sidebar
with st.sidebar:
    st.header("Settings")
    show_full_text = st.checkbox("Show full question text", value=False)
    min_score = st.slider("Minimum keyword score", 0, 5, 1)

# File uploader
uploaded_files = st.file_uploader(
    "Upload one or more DSE Physics Past Papers (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    all_results = defaultdict(list)

    progress = st.progress(0)
    status = st.empty()

    for idx, file in enumerate(uploaded_files):
        status.write(f"Processing **{file.name}** ...")
        try:
            text = extract_text_from_pdf(file)
            questions = split_into_questions(text)

            for i, q in enumerate(questions, 1):
                topic, score = classify_question(q)
                if score >= min_score:
                    all_results[topic].append({
                        "q_num": i,
                        "text": q,
                        "score": score,
                        "source": file.name
                    })
        except Exception as e:
            st.error(f"Error processing {file.name}: {e}")

        progress.progress((idx + 1) / len(uploaded_files))

    status.success("Done!")

    # Summary
    st.subheader("📊 Summary")
    cols = st.columns(3)
    total_q = sum(len(v) for v in all_results.values())
    cols[0].metric("Total Questions", total_q)
    cols[1].metric("Topics Found", len(all_results))
    cols[2].metric("Files Processed", len(uploaded_files))

    # Display by Topic
    st.subheader("📂 Questions by Topic")

    # Sort topics: official order first, then Unclassified
    ordered_topics = [t for t in TOPICS if t in all_results] + \
                     [t for t in all_results if t not in TOPICS]

    for topic in ordered_topics:
        items = all_results[topic]
        with st.expander(f"**{topic}**  ({len(items)} questions)", expanded=False):
            for item in items:
                st.markdown(f"**Q{item['q_num']}** · `{item['source']}` · score: {item['score']}")
                if show_full_text:
                    st.write(item["text"])
                else:
                    st.write(item["text"][:400] + ("..." if len(item["text"]) > 400 else ""))
                st.divider()

    # Download option
    if st.button("Prepare Download (JSON)"):
        import json
        result_json = {
            topic: [
                {"question": item["text"], "source": item["source"], "score": item["score"]}
                for item in items
            ]
            for topic, items in all_results.items()
        }
        st.download_button(
            label="Download Classified Questions (JSON)",
            data=json.dumps(result_json, indent=2, ensure_ascii=False),
            file_name="dse_physics_classified.json",
            mime="application/json"
        )

else:
    st.info("👆 Please upload one or more DSE Physics past paper PDFs to start.")
