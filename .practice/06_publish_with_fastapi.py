import gradio as gr
from fastapi import FastAPI

app = FastAPI()

def my_function(input):
    return f"Processed: {input}"

demo = gr.Interface(
    fn=my_function,
    inputs="text",
    outputs="text"
)

# FastAPI와 통합
app = gr.mount_gradio_app(app, demo, path="/")

# Uvicorn 등으로 서버 실행
# uvicorn main:app --host 0.0.0.0 --port 7860