
def save_file(f):
    with open('/home/dk/PycharmProjects/test_warg/text_t/upload/upload_files/your_file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)




def read_file(f):
    with open('/home/dk/PycharmProjects/test_warg/text_t/upload/upload_files/your_file.txt') as resource:
        text = []
        text_line = resource.readline()
        while text_line:
            if text_line == '\n':
                pass
            else:
                text_line = text_line.strip()
                if text_line == '':
                    pass
                else:
                    text.append(text_line)
            text_line = resource.readline()
        print(text)


