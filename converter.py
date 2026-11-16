from emoji_data import EMOJI

def nahrad_emoji(text):
    for kod, znak in EMOJI.items():
        text = text.replace(kod, znak)
    return text

