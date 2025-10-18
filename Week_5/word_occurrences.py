"""
File: word_occurrences.py
Estimate of time to complete: 20 minutes

Description:
Count the occurrences of each word in a user-provided string.
Then display the results in alphabetical order, aligned using f-strings.
"""

def main():
    text = input("Text: ").strip()
    words = text.split()

    # Count word occurrences
    word_counts = {}
    for word in words:
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort words alphabetically
    sorted_words = sorted(word_counts.keys())

    # Find longest word for column alignment
    max_length = max(len(word) for word in sorted_words)

    # Display neatly aligned results
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")


if __name__ == "__main__":
    main()