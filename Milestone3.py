import nltk
import os
from transformers import MarianMTModel, MarianTokenizer

nltk.download('punkt')
model_name = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text):
    print("In translate function")
    sentences = nltk.tokenize.sent_tokenize(text)
    translations = []
    for sentence in sentences:
        print(sentence)
        batch = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True, max_length=512)
        gen = model.generate(**batch)
        translation = tokenizer.batch_decode(gen, skip_special_tokens=True)
        print(translation)
        translations.append(translation[0])
    
    return ' '.join(translations)

source_directory = 'videos\\text'
target_directory = 'translated_text'
os.makedirs(target_directory, exist_ok=True)
for filename in os.listdir(source_directory):
    if filename.endswith('.txt'):
        print("In filename loop")
        source_file_path = os.path.join(source_directory, filename)
        target_file_path = os.path.join(target_directory, f"translated_{filename}")

        with open(source_file_path, 'r', encoding='utf-8') as file:
            source_text = file.read()

        translated_text = translate(source_text)
        print(translated_text)
        with open(target_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        
        print(f"Translated '{filename}' to '{target_file_path}'")