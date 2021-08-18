#  {{}} -> for the passage
# [[]] -> macqs
# ##-> for the year and month
# && -> for the source

import re
import json
# import uuid
strr = ""
with open(r'Comprehensions_jan_12.txt', encoding="utf8") as op:
    for line in op:
        strr += line
        # print( line)
    p = re.findall(r'{{([\s\S]*?)}}', strr)  # {{text}}
    id = 1
    passage_dict = {}
    year = re.findall(r'##([\s\S]*?)##', strr)  # text##
    print(year)
    source = re.findall(r'&&([\s\S]*?)&&', strr)  # &&text&&
    print(len(source))
    mcqs = re.findall(r'\[\[([\s\S]*?)\]\]', strr)  # [[text]]
    for i in range(len(mcqs)):
        mcqs[i] += "\n9"
        # [num]text(1) -> to find questions
        q = re.findall(r'[0-9] ([\s\S]*?)\(1\)', mcqs[i])
        p_dict = {"id": id, "passage": p[i].strip(), "source": source[i], "year": year[i], "no_of_questions": len(q)}
        # (num)text(num) -> to find all options
        opt = re.findall(r'\([0-9]\) ([\s\S]*?)\n[0-9]', mcqs[i])
        # print(len(opt))
        for j in range(len(opt)):
            p_dict[f'question_{j+1}'] = q[j].replace("\n", " ").strip()
            opt_arr = (re.compile(r'\([0-9]\)').split(opt[j])) # split the options around (num)
            for k in range(len(opt_arr)):
                p_dict[f'option_{k+1}_question_{j+1}'] = opt_arr[k].replace(
                    "\n", " ").strip()
        passage_dict[id] = p_dict
        id += 1
    # print(passage_dict)
    y = json.dumps(passage_dict)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(passage_dict, f, ensure_ascii=False, indent=4)
