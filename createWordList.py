import re
import sys

def process_text(url):
    """Removes unnecessary parts from URLs and splits them into words."""
    url = re.sub(r'^https?://', '', url, flags=re.IGNORECASE)
    url = re.sub(r'\?.*$', '', url)
    
    words = re.split(r'\W+', url)
    
    return [word for word in words if word]

def generate_wordlist(file_path):
    """Generates a wordlist from the provided file."""
    word_list = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    words = process_text(line.strip())
                    word_list.extend(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    unique_words = sorted(set(word_list))
    
    return unique_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python createWordList.py [input_file]")
        sys.exit(1)

    input_file = sys.argv[1]

    wordlist = generate_wordlist(input_file)
    
    for word in wordlist:
        print(word)

if __name__ == "__main__":
    main()
