import gradio as gr
import time

""" [max_batch_size]
- 연산량 과부하를 막는 batch_size 개념
- GAN 등 연산량이 많은 모델에서 사용
"""
def trim_words(words, lens):
    trimmed_words = []
    time.sleep(5)
    for w, l in zip(words, lens):
        trimmed_words.append(w[:int(l)])
    return [trimmed_words]

demo = gr.Interface(
    fn=trim_words,
    inputs=["textbox", "number"],
    outputs=["output"],
    batch=True,
    max_batch_size=16 # batch_size
)

demo.launch()