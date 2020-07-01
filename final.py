import PyPDF2


def check_if_type(data):
    try:
        if data[:5] == "TYPEŒ":
            return data.replace(chr(338), '-')
    except Exception as e:
        print(e)
    return 'No Type'


def check_if_answers(data):
    return '(*)' in data or '(1)' in data or '(2)' in data or '(3)' in data or '(4)' in data


pdfFileObj = open('pdf_reader/Arihant-general_knowledge.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

result = {}

for page in range(pdfReader.numPages):
    if page == 65:
        print("hello")
    details_on_this_page = {
        'questions': [],
        'answers': []
    }
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText().split('\n')
    chapter_name, type_, question_no = data[0], '', 1
    question = ''
    option = ''
    if result.get(chapter_name, None) is None:
        result[chapter_name] = {}
    i = 2

    while i < len(data):
        temp = check_if_type(data[i])
        if temp != "No Type":
            type_ = temp
            print(temp)
            i += 1
        else:
            if result[chapter_name].get(type_, None) is None:
                result[chapter_name][type_] = {}
            try:
                if int(data[i][:-1]):
                    question_no = data[i][:-1]
                    if result[chapter_name][type_].get(question_no, None) is None:
                        result[chapter_name][type_][question_no] = {}
                    i += 1
                    if not check_if_answers(data[i]):
                        while data[i][:3] != '(1)':
                            question += data[i]
                            if question[-1] == '-':
                                question = question[:-1]
                            else:
                                question += " "
                            i += 1
                        while data[i] != '(' and ('(SSC' not in data[i]):
                            option += data[i]
                            i += 1
                        option.replace(chr(338), '-')
                        # print(question)
                        # print(option)
                        # questions.append(question)
                        # options.append(option)
                        details_on_this_page['questions'].append(question_no)
                        result[chapter_name][type_][question_no]['question'] = question
                        result[chapter_name][type_][question_no]['options'] = option
                        question, option = '', ''
                    else:
                        # print("Answers Found")
                        details_on_this_page['answers'].append(data[i])
                        result[chapter_name][type_][question_no]['answers'] = data[i]
                        i += 1
                else:
                    i += 1
            except Exception as e:
                i += 1

    print(f"Question found on page no {page+1}: ", end=' ')
    print(*details_on_this_page['questions'])
    print(f"Answers found on page no {page+1}: ", end=' ')
    print(*details_on_this_page['answers'])
    # x = input("Do you want to move to next page: (y/n)")
    # if x == "n":
    #     print(result)
    #     break