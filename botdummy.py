import os
from huggingface_hub import InferenceClient


os.environ["HF_TOKEN"] = "hf_token_here"  


client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")


output = client.chat.completions.create(
    messages=[
         {"role": "system", "content": "Answer in rude and insulting way."},
        {"role": "user", "content": "hola"},
    ],
    stream=False,
    max_tokens=35,  
)
print(output.choices[0].message.content)



print(output)





