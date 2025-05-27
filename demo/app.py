
import gradio as gr
from gradio_goodtabs import GoodTabs


with gr.Blocks() as demo:
    with GoodTabs():
        with gr.Tab("Tab 1"):
            gr.Textbox(value="foo", interactive=True)
        with gr.Tab("Tab 2"):
            gr.Number(value=10, interactive=True)


if __name__ == "__main__":
    demo.launch()
