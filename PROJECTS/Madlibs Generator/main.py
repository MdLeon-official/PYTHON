# Mar 2, 2025


def main():
    with open("story.txt", "r") as file:
        story = file.read()

    keywords = set()
    wordstart = "<"
    wordend = ">"

    start_point = -1

    for i, chars in enumerate(story):
        if chars == wordstart:
            start_point = i

        if chars == wordend and start_point != -1:
            words = story[start_point:i+1]
            keywords.add(words)
            start_point = -1

    answers = {}

    for word in keywords:
        answer = input("Enter a word for " + word + " : ")
        answers[word] = answer

    for word in keywords:
        story = story.replace(word, answers[word])

    print(story)

if __name__ == "__main__":
    main()
