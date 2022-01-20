import os
from sys import argv

def replaceText(File,oldText,newText):
    with open(File) as f:
        newText=f.read().replace(oldText,newText)
    with open(File,"w") as f:
        f.write(newText)

if (len(argv)==1):
    print("How many chains? python run.py N")
    print("Quitting")
    quit()

try:
    n = int(argv[1])
except:
    print("How many chains? python run.py N - needs to be an integer")
    print("Quitting")
    quit()

StartFromFile = False
StartingFileBase = ""
OutDirBase = "/scratch/barrow/M3-Output/"
JobNum = "0"

for i in range(n):
    ChainNum = str(i)
    FileName = "Chain"+ChainNum+"/"
    OutDir = OutDirBase+FileName+"/"
    
    CopyCommand  = "cp -a ChainBase "+FileName
    os.system(CopyCommand)

    MkdirCommand = "mkdir -p "+OutDir
    os.system(MkdirCommand)

    ScriptName = FileName+"/submit.py"

    SUBMITDIRECTORYPrefix = os.getcwd()+"/Chain"+str(i)+"/"
    DATADIRECTORYPrefix = OutDir = OutDirBase+"/Chain"+ChainNum+"/"
    
    replaceText(ScriptName,"ChainNumBASE",ChainNum)
    replaceText(ScriptName,"SUBMITDIRECTORYPrefixBASE",SUBMITDIRECTORYPrefix)
    replaceText(ScriptName,"DATADIRECTORYPrefixBASE",DATADIRECTORYPrefix)
    replaceText(ScriptName,"JobNumBASE",JobNum)

    if (StartFromFile==True):
        StartingFileBase = OutDirBase+FileName+"MaCh3Output_"+str((int(JobNum)-1))+".root"
        
    replaceText(ScriptName,"STARTINGFILEBASE",StartingFileBase)

    if (JobNum=="0"):
        os.system("python "+FileName+"/submit.py")
    
print("Submitted "+str(n)+" jobs")
