text_file_path = "/Users/leesukcheol/Desktop/gitTest/pythonground/assignment/record.txt"
new_text_content = ''
target_word = '참석자 4'
new_word = '\n석철)'
with open(text_file_path,'r') as f:
    print("file load")
    lines = f.readlines()
    for i, l in enumerate(lines):
        new_string = l.strip().replace(target_word,new_word)
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'
                
with open(text_file_path,'w') as f:
    f.write(new_text_content)
print("Finish")
