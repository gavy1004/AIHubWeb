import gradio as gr

ko2enDict = {
    "사과": "apple",
    "사자": "lion",
    "사랑": "love",
    "가비" : "gavy",
    "코코" : "coco",
    "보리" : "bory"
}

def trans_ko_en(ko):
    return ko2enDict[ko]

app = gr.Interface(
    fn=trans_ko_en,
    inputs=gr.Textbox(placeholder="한국어"),
    outputs="text",
)
app.launch(debug=True)



