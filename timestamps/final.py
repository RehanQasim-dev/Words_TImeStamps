import sys,os
from itertools import chain
import results_writer as rw
write_handler=open(os.path.join(sys.path[0],f'../results/Results.txt'),'w+',encoding='cp437',errors='ignore')
write_handler.write('[')
for i in range(3,43):
    (words,timestamps,line_words_count)=rw.mid_results_writer(i)
    word_index=0
    iterations=0
    results=[]
    for timestamp_item in timestamps:
        if iterations >= (line_words_count[word_index]-1):
            if timestamp_item['word']==words['last'][word_index]:
                results.append(timestamp_item['end'])
                word_index+=1
                iterations=0
                if word_index>=len(words['first']):
                    break
            elif timestamp_item['word']==words['first'][word_index]:
                results.append(timestamp_item['start'])
                word_index+=1
                iterations=0
                if word_index>=len(words['first']):
                    print(results)
                    break
        iterations+=1
    write_handler.write(str(results)+','+'\n')
write_handler.write(']')
write_handler.close()
