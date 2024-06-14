import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ensure the Hugging Face access token is set
access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
if not access_token:
    raise ValueError("HUGGINGFACE_ACCESS_TOKEN environment variable not set")

# Model and tokenizer loading
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)
    print("TOKENIZER LOADED")
    model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=access_token)
    print("MODEL LOADED")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    raise

# Use a pipeline for easier text generation
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
print("GENERATOR LOADED")
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        print("PROMPT LOADED "+prompt)
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Generate response using the pipeline
        responses = generator(prompt, max_length=100, num_return_sequences=1)
        result = responses[0]['generated_text']
        print("RESULT LOADED: "+result)
        return jsonify({'response': result})
    except Exception as e:
        print(f"Error in prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

