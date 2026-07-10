with open("sample.txt", encoding="utf-8") as f:
    content = f.read()

    start = 0
    chunks = []

    while start < len(content):
        piece = content[start:start + 200]
        chunks.append(piece)
        start += 160

print(len(chunks))
print("a\n"+ chunks[0] + "\n")
print("b\n" + chunks[1] + "\n")