import gradio as gr
dict = {
    "ko2en" : {
        "사과" : "apple",
        "사자" : "tiger",
        "사랑" : "love"
    },
    "en2ko" : {
        "apple" : "사과",
        "lion" : "사자",
        "love" : "사랑"
    }
}
def trans(type, word):
    return dict[type][word]
app = gr.Interface(
    fn=trans,
    inputs=[
        gr.Radio(['ko2en', 'en2ko']),
        gr.Textbox(placeholder="한국어")
    ],
    outputs="text",
)
app.launch(debug=True)
