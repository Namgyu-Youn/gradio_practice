import gradio as gr

"""
[Interface]
- ML models에 활용 가능한 high-level API (빠르다!)
- fn: 실행할 함수 (main 역할)
- inputs: "fn"에 입력할 input (parser 역할)
- outputs: the outputs of the function

# Keyword
- 입력 함수를 다양하게 응용이 가능하다. (ex. Model Inference, 이미지 시각화, ..)
- 입출력 함수에 None을 활용 가능하다.
- Model inference를 활용해 사용자가 Image를 집어넣으면, rle를 출력해줄 수도 있음 -> 시각화까지 연계 가능
- slider를 활용하면 숫자를 조절 가능 -> 증강의 정도 조절처럼 다양하게 응용 가능함.

# 입출력 함수 변형 예시
- Inputs-Only : Data collecting -> 사용자가 입력한 데이터를 기록하는 방식으로 응용 가능
- Outputs-Only : GAN -> 무작위로 생성된 이미지를 출력해주는 방식
"""

def text_repeater(name, num:int):
    return name * int(num)

demo = gr.Interface(
    fn=text_repeater,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch(share=True) # share을 활용해 외부로 공유 가능함.