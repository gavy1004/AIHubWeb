import gradio as gr
dict = {
    "ko2en" : {
        "사과" : "apple",
        "사자" : "tiger",
        "사랑" : "love"
    },
    "en2ko" : {
        "apple" : "사과",
        "tiger" : "사자",
        "love" : "사랑"
    }
}
def trans(type, word):
    return dict[type][word]
with gr.Blocks() as app:
    result = gr.Textbox(label='결과')
    type = gr.Radio(label='종류', choices=['ko2en', 'en2ko'])
    word = gr.Textbox(label='단어', placeholder="한국어")
    btn = gr.Button(value='실행')
    btn.click(
        fn = trans,
        inputs = [type, word],
        outputs = result
    )
app.launch(debug=True, share=True)
#public URL로 접근하면 전세계 어디서나 내 컴퓨터에 접속 가능
#그러나! 72시간 후에 접속 안됨. 내 컴퓨터를 끄면 접속 안됨
