from Generator import Recognizer
from words_generator import words_generator
import os,sys
def mid_results_writer(i):
    result_file=open(os.path.join(sys.path[0],f'../results/Results{i}.txt'),'w+',errors='ignore')
    result_file.write(f"--------------Slide No {i}---------------\n")
    words=words_generator(i)
    timestamps=Recognizer(i)
    result_file.write(str(words)+'\n')
    filter=0
    for j in timestamps:
        if filter%2==0:
            append=''
        else:
            append='\n'
        result_file.write(f"[{j['word']} , {j['end']}]".ljust(30,' ')+append)
        filter+=1
    
    result_file.close()
    return (words,timestamps)