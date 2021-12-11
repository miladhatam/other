#convert mocha to 3dequalizer
#coded by MiladHatam
import os

#start_frame
startFrame = 1

n=startFrame
ok=1
#export your track layer of Mocha to 'Nuke ascii' in 'c:/temp' dir with 't' prefix
addr = ["C:/temp/t_Tracker1.txt","C:/temp/t_Tracker2.txt","C:/temp/t_Tracker3.txt","C:/temp/t_Tracker4.txt"]
for i in addr:
    ff = open(i,'r')
    fileline = ff.readlines()
    if ok==1:
        s =  '4\n1\n0\n' + str(len(fileline)) + '\n'
        ok=1
    else:
        s+=str(ok)+'\n0\n' + str(len(fileline)) + '\n'
    for x in fileline:
        s+=str(n)+ ' '+x
        n+=1
        print s
    ff.close()
    n=1
    ok+=1
    print s

f = open("C:/temp/3de.txt",'w')
f.write(s)
f.close()
#'3de.txt' is the final file        
os.startfile("C:/temp" )
