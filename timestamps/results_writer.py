from Generator import Recognizer
from words_generator import words_generator
import os,sys
'''writes last and first words of each line of the slide to the file and also all [word,ending_timeStamp] of each word in audio to the voice
 and also returns the last and first words of a slide or text file and starting and ending time stamps of each word of the slide'''
def mid_results_writer(i):
    result_file=open(os.path.join(sys.path[0],f'../results/Results{i}.txt'),'w+',errors='ignore')
    result_file.write(f"--------------Slide No {i}---------------\n")
    (words,line_words_count)=words_generator(i)
    timestamps=Recognizer(i)
    # print(timestamps)
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
    return (words,timestamps,line_words_count)
# mid_results_writer(2)
