import gradio as gr

''' [Interface]
- Radio : 단일 선택
- CheckboxGroup : 다중 선택
- flagged : I/O 결과를 CSV로 저장해준다.
'''

def select_options(choices):
    return f"You selected: {', '.join(choices)}"

demo = gr.Interface(
    fn=select_options,
    inputs=gr.CheckboxGroup(
        ["Option X", "Option Y", "Option Z"],
        label="Select Multiple Options"
    ),
    outputs="text"
)

demo.launch()