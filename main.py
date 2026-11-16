from converter import nahrad_emoji

def main():
    text = input("Zadejte text s emoji kódy: ")
    prevedeny_text = nahrad_emoji(text)
    print(prevedeny_text)

if __name__ == "__main__":
    main()

