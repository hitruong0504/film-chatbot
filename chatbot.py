import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "HiTruong/Llama-2-chat-finetuned"
# model_name = "NousResearch/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

def chat(question):
    inputs = tokenizer(f"<s>[INST] {question} [/INST]", return_tensors="pt", truncation=True, max_length=100).to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_length=75, eos_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return response.replace(f"[INST] {question} [/INST]", "").strip().split('.')[0]

# Gradio UI
iface = gr.Interface(fn=chat, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860)
