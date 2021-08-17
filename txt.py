import re
import json
# import uuid
strr=""
with open(r'Comprehensions_jan_12.txt', encoding="utf8") as op:
    for line in op:
        strr+=line
        # print( line)
    p=re.findall(r'{{([\s\S]*?)}}', strr)
    id=1
    passage_dict={}
    # for i in p1:
    #     print(i+"////////////////////////////////////")
    year=re.findall(r'##([\s\S]*?)##', strr)
    print(year)
    source=re.findall(r'&&([\s\S]*?)&&', strr)
    print(len(source))
    mcqs=re.findall(r'\[\[([\s\S]*?)\]\]', strr)
    for i in range(len(mcqs)):
        mcqs[i]+="\n9"
        q=re.findall(r'[0-9] ([\s\S]*?)\(1\)', mcqs[i])
        p_dict={"id": id, "passage": p[i].strip(), "source": source[i], "year": year[i], "no_of_questions": len(q)}
        # for qs in range(len(q)):
        #     p_dict[f'question_{qs+1}']=q[qs]
        # print(q)
        opt=re.findall(r'\([0-9]\) ([\s\S]*?)\n[0-9]', mcqs[i])
        # print(len(opt))
        for j in range(len(opt)):
            p_dict[f'question_{j+1}']=q[j].replace("\n", " ").strip()
            opt_arr=(re.compile(r'\([0-9]\)').split(opt[j]))
            for k in range(len(opt_arr)):
                p_dict[f'option_{k+1}_question_{j+1}']=opt_arr[k].replace("\n", " ").strip()
        passage_dict[id]=p_dict
        id+=1
    # print(passage_dict)
    y=json.dumps(passage_dict)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(passage_dict, f, ensure_ascii=False, indent=4)
    # print(y)



    # print(mcqs)
    # for mcq in mcqs:
    #     mcq+="\n9"
    #     q=re.findall(r'[0-9] ([\s\S]*?)\(1\)', mcq)
    #     # print(q)
    #     opt=re.findall(r'\([0-9]\) ([\s\S]*?)\n[0-9]', mcq)
    #     for i in opt:
    #         opt_arr=(re.compile(r'\([0-9]\)').split(i))
        
# strip to remove newline charachter
# f = open("Comprehensions_jan_12.txt", "r")
# print(f.read())