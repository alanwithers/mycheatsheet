#replace ch's in string without using a list
def alt_str(str,index=-1,existing_char='',new_char='',no_of_replacements=2):
    new_str=''
    for i,ch in enumerate(str):
        if i==index:
            new_str+=new_char
            continue
        elif ch==existing_char:
            new_str+=new_char
            if no_of_replacements==1:
                existing_char=''
            continue
        new_str+=ch   
    return new_str