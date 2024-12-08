import gradio as gr

''' [Blocks]
- Interface보다 다양한 custom이 가능하다. (?)
'''

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Name")
    greet_btn = gr.Button("Greet")
    farewell_btn = gr.Button("Farewell")
    output = gr.Textbox(label="Result")

    greet_btn.click(greet, inputs=name_input, outputs=output)
    farewell_btn.click(farewell, inputs=name_input, outputs=output)

demo.launch()