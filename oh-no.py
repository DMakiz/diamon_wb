import gradio as gr

block = gr.Blocks()

def run():
  with block:
    gr.Markdown(
    """
    <p>oh no 😐 something wrong with the 🤗 hugging face servers 😐 hopefully, it will be fixed soon</p>
    """)
    block.launch(debug=True, max_threads=True, share=True, inbrowser=True)

if __name__ == "__main__":
    run()
