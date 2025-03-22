# SassySolver 🤖📚 - Correcting Wrong Math Memes with AI

SassySolver is a fun and educational AI-powered project designed to correct incorrect math memes and provide accurate explanations. By using a fine-tuned Qwen1.5-4B-Chat model, SassySolver aims to address common math misconceptions and errors with sass and precision.

## 📌 Overview
### SassySolver is built with the following features:

- Fine-tuned Qwen1.5-4B-Chat model using LoRA (Low-Rank Adaptation) technique.
- Memory-efficient quantization using bitsandbytes.
- Model deployment via Streamlit with an interactive UI.
- Trained on a diverse dataset of incorrect math memes and correct explanations.
- Provides entertaining yet informative explanations for a wide variety of math-related mistakes.

  ## 📁 Directory Structure

  ```
  ├── math_memes_dataset123.csv     # Dataset for training the model
  ├── app.py                        # Streamlit deployment script
  ├── your_script.py                # Script for testing the model with new inputs
  ├── requirements.txt              # Dependencies for the project
  ├── Output.png                    # Sample output of the model
  ├── Output2.png                   # Sample output of the model
  ├── Output3.png                   # Sample output of the model
  └── README.md                     # Project README (this file)
  ```

## 🚀 Installation
**To get started, clone this repository and install the required packages:**
```
git clone https://github.com/AbsarRaashid3/SassySolver.git
cd SassySolver
```

**Install the dependencies from requirements.txt:I**
```
pip install -r requirements.txt
```

## 📚 Dataset
The dataset (math_memes_dataset123.csv) consists of pairs of incorrect math memes and their corresponding correct explanations. Example entries:
```
input,output
8 ÷ 2(2+2) = 1?,Incorrect! Correct solution: 8 ÷ 2×(2+2) = 8 ÷ 2×4 = 4×4 = 16. PEMDAS requires performing multiplication and division left‐to‐right after parentheses.
1/2 + 1/3 = 2/5. Just add numerators and denominators!,Fraction error! The correct method is to find a common denominator: 1/2 = 3/6 and 1/3 = 2/6; so the sum is 5/6.

```

## 🧩 Model Training
**The model is fine-tuned using LoRA (Low-Rank Adaptation) with quantization enabled to reduce memory usage. The training script is written in Jupyter Notebook.**

### Training Configuration
- Model: Qwen1.5-4B-Chat
- LoRA Configuration: r=16, lora_alpha=16, lora_dropout=0.05
- Quantization: 4-bit quantization using BitsAndBytesConfig
- Training Epochs: 9
- Evaluation Strategy: epoch
- Optimized for both GPU and CPU compatibility.


## 🌐 Deployment
The model is deployed using Streamlit with app.py.

## Run the App Locally
```
streamlit run app.py
```

Once deployed, the UI will be accessible at:
```
http://localhost:8501
```

## Ngrok Deployment (Optional)
If you want to make your app publicly accessible, you can use ngrok.

```
ngrok authtoken YOUR_NGROK_AUTH_TOKEN  # Set your ngrok auth token
```

Then, in your terminal:
```
python -m streamlit run app.py
```

## 📄 Usage
- Open the Streamlit app.
- Enter a wrong math meme.
- Click "Fix Math Meme" button.
- Receive a corrected explanation with a touch of sass!

## 📦 Requirements
The required packages are listed in the requirements.txt file:
```
torch
streamlit
datasets
transformers
bitsandbytes
```

Install them using:
```
pip install -r requirements.txt
```

## 📌 Testing The Model
Use the your_script.py file to test the model with more incorrect math memes.

```
python your_script.py
```

## 📷 Sample Outputs

![Output](https://github.com/user-attachments/assets/fac32dae-467d-414b-b285-acb57989bd18)
![Output2](https://github.com/user-attachments/assets/f5e01305-9ab9-42ef-9d5e-788f8dfe5d01)
![Output3](https://github.com/user-attachments/assets/3bfe1213-ef55-4ab4-8305-84ec92f4f6cd)

## 🔥 Future Improvements
- Enhancing the dataset with more common misconceptions.
- Improving the UI for better user experience.
- Deploying the model as a web API for easier integration.


## 💬 Acknowledgments
**Special thanks to the developers of Qwen1.5-4B-Chat, Streamlit, and bitsandbytes for making this project possible.**


