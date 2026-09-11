import gradio as gr
import os
from dotenv import load_dotenv

# Tải cấu hình từ .env
load_dotenv()

from template import chat_with_system_prompt, OPENAI_MODEL

def respond(message, history, system_prompt, temperature):
    try:
        response, latency = chat_with_system_prompt(
            system_prompt=system_prompt,
            user_prompt=message,
            model=OPENAI_MODEL,
            temperature=temperature
        )
        return f"{response}\n\n*(Đã trả lời trong {latency:.2f} giây)*"
    except Exception as e:
        return f"Lỗi gọi API: {str(e)}"

demo = gr.ChatInterface(
    fn=respond,
    additional_inputs=[
        gr.Textbox(value="Bạn là một trợ lý AI thông minh, nhiệt tình. Hãy trả lời ngắn gọn.", label="System Prompt (Vai trò)"),
        gr.Slider(minimum=0.0, maximum=2.0, value=0.7, step=0.1, label="Temperature (Độ sáng tạo)"),
    ],
    title=f"Chatbot UI - Đang chạy {OPENAI_MODEL}",
    description="Giao diện Web UI để kiểm thử các hàm AI bạn đã viết trong template.py",
)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
