import gradio as gr
from predict import predict_sentiment_review

demo = gr.Interface(
    fn=predict_sentiment_review,
    inputs=["textbox"],
    outputs=["textbox"],
)

demo.launch()