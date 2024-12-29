
file = input("File name: ")

if '.' in file:
    text = file.rsplit(".", 1)
    extension = text[1].lower()

    if extension == 'jpg':
        print("image/jpeg")
    elif extension in ['pdf', 'zip']:
        print(f"application/{extension}")
    elif 'PDF' in text[1] or 'pdf' in text[1]:
        print(f"application/pdf")
    elif extension == 'bin':
        print("application/octet-stream")
    elif extension == 'txt':
        print("text/plain")
    elif extension == '':
        print("application/octet-stream")
    else:
        print(f"image/{extension}")
else:
    print("application/octet-stream")
