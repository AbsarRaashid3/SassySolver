
import subprocess
import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from pyngrok import ngrok



model_path = "./math_meme_repair_model"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token  # Ensure padding token

# Set quantization to reduce memory usage
quantization_config = BitsAndBytesConfig(load_in_8bit=True)  # Change to load_in_4bit=True if needed

# Load model with device auto-detection and offloading
try:
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",  # Automatically selects best device (GPU if available)
        offload_folder="./offload_dir",  # Offloads large layers to disk if needed
        quantization_config=quantization_config  # Apply quantization
    )
except Exception as e:
    print(f"Failed to load on GPU, switching to CPU: {e}")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="cpu"  # Fallback to CPU if necessary
    )

# ✅ Streamlit UI
st.title("🤖 SASSY SOLVER")
st.write("Enter a wrong math meme, and the AI will correct it!")

prompt = st.text_input("Enter an incorrect math meme:", "")

if st.button("Fix Math Meme"):
    if prompt:
        input_text = f"Wrong Math Meme: {prompt}\nCorrect Explanation:"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        inputs = tokenizer(input_text, return_tensors="pt").to(device)

        # ✅ Generate response
        output = model.generate(
            **inputs, max_length=60, num_return_sequences=1,
            do_sample=True, temperature=0.7, top_p=0.9
        )
        result = tokenizer.decode(output[0], skip_special_tokens=True)

        st.success(f"📖 Correct Explanation: {result}")
    else:
        st.warning("Please enter a valid math meme.")
