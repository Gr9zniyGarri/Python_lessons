with open ('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(type(text))
    text.replace('.', '!')
    word_count = len(text.split())
    print(word_count)
    print(len(text))

file1 = open('referat.txt', 'r')
file2 = open('referat2.txt','w')
for line in file1:
    file2.write(line.replace('.', '!'))
file1.close
file2.close