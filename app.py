import os
import math
import gradio as gr

EN_US = os.getenv("LANG") != "zh_CN.UTF-8"

ZH2EN = {
    "状态栏": "Status",
    "分割步长": "Split step",
    "分割结果": "Split result",
    "字符串分割": "String Splitter",
    "待分割字符串": "String to be split",
}


def _L(zh_txt: str):
    return ZH2EN[zh_txt] if EN_US else zh_txt


def infer(txt: str, step: int):
    status = "Success"
    output = ""
    try:
        text = txt.strip().strip("\n")
        if not text:
            raise ValueError("请输入 txt !")

        md_lines = []
        size = len(text)
        count = math.ceil(size / step)
        for i in range(count):
            md_lines.append(f"```txt\n{text[i * step: min((i + 1) * step, size)]}\n```")

        output = "\n".join(md_lines)

    except Exception as e:
        status = f"{e}"

    return status, output


if __name__ == "__main__":
    gr.Interface(
        fn=infer,
        inputs=[
            gr.TextArea(label=_L("待分割字符串")),
            gr.Slider(
                label=_L("分割步长"),
                minimum=1,
                maximum=255959,
                step=1,
                value=1024,
            ),
        ],
        outputs=[
            gr.Textbox(label=_L("状态栏"), buttons=["copy"]),
            gr.Markdown(label=_L("分割结果"), container=True, buttons=["copy"]),
        ],
        flagging_mode="never",
        title=_L("字符串分割"),
    ).launch(css="#gradio-share-link-button-0 { display: none; }")
