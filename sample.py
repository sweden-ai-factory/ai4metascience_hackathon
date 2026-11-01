import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():

    model_name = "Qwen/Qwen2.5-1.5B-Instruct"

    print("Loading Qwen model...")

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        use_fast=True
    )

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )

    print("Model loaded successfully!")

    # Define question
    question = (
        "Explain how quantum computing works "
        "and describe its potential applications "
        "in scientific research."
    )

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    print("\nQuestion:", question)
    print("\nGenerating response...\n")

    # Apply chat template
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt"
    )

    inputs = inputs.to(model.device)

    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=1024,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    # Extract generated tokens
    generated_tokens = outputs[0][
        inputs["input_ids"].shape[1]:
    ]

    # Decode response
    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    print("=" * 60)
    print("QWEN RESPONSE")
    print("=" * 60)
    print(response)
    print("=" * 60)

    # Save response to text file
    with open("qwen_response.txt", "w", encoding="utf-8") as f:
        f.write("Question:\n")
        f.write(question + "\n\n")
        f.write("Qwen Response:\n")
        f.write(response)

    print("\nResponse saved to qwen_response.txt")

if __name__ == "__main__":
    main()
