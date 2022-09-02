import sys
no_of_lines=[]
for i in range(2,11):
    file=open(sys.path[0]+f'/slides/Lesson14/Media{i}.txt','r+',encoding='cp437',errors='ignore')
    count=0
    for line in file.readlines():
        if line !='\n':
            count+=1
    no_of_lines.append(count)
    file.close()
print(no_of_lines)