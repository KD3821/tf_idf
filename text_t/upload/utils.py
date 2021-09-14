from .models import Word


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
                    text_line = text_line.replace('!', '\n')
                    text_line = text_line.replace(',', '\n')
                    text_line = text_line.replace('.', '\n')
                    text_line = text_line.replace(':', '\n')
                    text_line = text_line.replace('-', '\n')
                    text_line = text_line.replace('?', '\n')
                    text_line = text_line.replace(' ', '\n')
                    text_line = text_line.replace(';', '\n')
                    text_line = text_line.replace('_', '\n')
                    text_line = text_line.replace('(', '\n')
                    text_line = text_line.replace(')', '\n')
                    text_line = text_line.replace('[', '\n')
                    text_line = text_line.replace(']', '\n')
                    text_line = text_line.replace('{', '\n')
                    text_line = text_line.replace('}', '\n')
                    text_line = text_line.replace('`', '\n')
                    text_line = text_line.replace('"', '\n')

                    if text_line == '\n':
                        pass
                    else:
                        text_line = text_line.lower()
                        text_line = text_line.splitlines()
                        text += text_line
            text_line = resource.readline()


        print(text)
        word_dict = {}
        word_count = 0

        for i in range(len(text)):
            if text[i] == '':
                continue
            for j in range(len(text)):
                if text[j] == '':
                    continue
                elif text[i] == text[j]:
                    word_count += 1
                else:
                    pass
            word_dict[text[i]] = word_count
            word_count = 0

        total_w = len(word_dict)
        for key, value in word_dict.items():
            w = Word(word_text=key, tf_amount=(float(value/total_w))*100)
            w.save()




        print(word_dict)

        with open('/home/dk/PycharmProjects/test_warg/text_t/upload/upload_files/mid_file.txt', 'w') as destination2:
            # destination2.writelines(word_dict)
            destination2.write(str(word_dict))




