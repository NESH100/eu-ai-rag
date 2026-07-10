with open("sample.txt", encoding="utf-8") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(word_count)

    
    start = 0
    chunks = []

    while start < len(content):
        piece = content[start:start + 200]
        chunks.append(piece)
        start += 160