import gradio as gr

def greet(name, intensity):
    return name * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

''' [Interface]
- Create demos for ML models -> Interface로 구현
- fn: the function to run
- inputs: "fn"에 입력할 input (parser 역할)
- outputs: the outputs of the function
'''

demo.launch(share=True) # 외부로 공유 가능함.