from transformers import pipeline


def translate_to_french(text):
    translator = pipeline("translation_en_to_fr")
    translated_text = translator(text, max_length=40)[0]['translation_text']
    return translated_text


if __name__ == "__main__":
    # Example English text for translation
    english_text = "Hello, how are you?"

    # Translate English text to French
    translated_text = translate_to_french(english_text)
    print(f"English: {english_text}")
    print(f"French: {translated_text}")
