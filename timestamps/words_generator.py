import os,sys
from test import extract_word
no_to_text_map={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
def words_generator(i):
    words={'first':[],'last':[]}
    read_handler=open(os.path.join(sys.path[0],f'../media/rawtext/Media{i}.txt'),'r+',encoding='cp437',errors='ignore')
    for j in read_handler:
        print('line',j)
        if len(j.strip())>0:
            last_word=j.split()[-1]
            first_word=j.split()[0]
            try:
                last_word=extract_word(last_word)
            except Exception as e:
                print(f'{type(e).__name__}:{e}, last word=',last_word)
                if input('Do you want to take second last word y/n: ')=='y':
                    last_word=extract_word(j.split()[-2])
                else:
                    sys.exit()

            try:
                first_word=extract_word(first_word)
            except Exception as e:
                print(f'{type(e).__name__}:{e}, first word=',first_word)
                if input('Do you want to take second second word y/n:')=='y':
                    first_word=extract_word(j.split()[1])
                else:
                    sys.exit()
            
            if first_word.isnumeric():
                first_word=no_to_text_map[first_word[0]]
            elif first_word=='e.g':
                first_word='words'

            if last_word.isnumeric():
                last_word=no_to_text_map[last_word[-1]]
            elif last_word=='e.g':
                last_word='words'

            words['first'].append(first_word)
            words['last'].append(last_word)
    if words['last']!=[]:
        words['last'].pop()
        words['first'].pop(0)
    read_handler.close()
    return words

