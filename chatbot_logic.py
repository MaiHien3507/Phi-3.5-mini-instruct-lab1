import torch
from omegaconf import OmegaConf
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
)

class Phi3Chatbot:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.config.model_path,
            device_map="auto",
            torch_dtype="auto",
            quantization_config=bnb_config,
            trust_remote_code=True
        )
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )

    def __call__(self, user_message):
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message},
        ]

        generation_args = {
            "max_new_tokens": self.config.max_new_tokens,
            "return_full_text": False,
            "temperature": self.config.temperature,
            "top_p": self.config.top_p,
            "do_sample": True,
        }

        output = self.pipe(messages, **generation_args)
        return output[0]['generated_text']
