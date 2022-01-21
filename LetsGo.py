import os
import sys

def replaceText(File,oldText,newText):
    with open(File) as f:
        newText=f.read().replace(oldText,newText)
    with open(File,"w") as f:
        f.write(newText)

def main():
    print("\n")

    WorkDirectory = os.environ['PWD']
    
    try:
        nChains = int(input("How many chains?: "))
    except:
        print("Invalid number of chains")
        quit()
        
    try:
        nSteps = int(input("How many steps per chain?: "))
    except:
        print("Invalid number of steps")
        quit()

    try:
        nThreads = int(input("How many threads per chain?: "))
    except:
        print("Invalid number of threads")
        quit()

    if (nThreads == 0):
        print("\tDefaulting to use 1 thread")
        nThreads = 1
        
    try:
        MaCh3Install = os.environ['MACH3']
    except:
        print("MaCh3 install not found. Please source setup.sh in MaCh3 install or export $MACH3=/path/to/MACH3")
        quit()

    if (os.path.exists(MaCh3Install) == False):
        print("MaCh3 install not found. Given:"+MaCh3Install)
        quit()
    
    try:
        JobNumber = int(input("Job Number? [0 for starting new chain, other for continuing chain]: "))
    except:
        print("Invalid Job Number")
        quit()

    try:
        SubmitJobs = int(input("Submit jobs to queue? [1 for yes, 0 for no]: "))
    except:
        print("Invalid answer")
        quit()

        
    ExecName = ""
    try:
        ExecName = input("Executable to run? [Given in relative path to MaCh3 Install, e.g. ./bin/jointFit]: ")
    except:
        print("Invalid executable name")

    if ((os.path.exists(MaCh3Install+"/"+ExecName) == False) or (ExecName == "")):
        
        print("\tExecutable:"+ExecName+" not found in MaCh3 install:"+MaCh3Install)
        ExecName = "./AtmJointFit_Bin/JointAtmFit"
        if (os.path.exists(MaCh3Install+"/"+ExecName) == True):
            print("\tDefaulting to use: "+ExecName)
        else:
            print("Invalid executable name")
            quit()
        
    try:
        ConfigName = input("Base Config Name:")
    except:
        print("Invalid config name string")
        quit()

    if (os.path.exists(WorkDirectory+"/"+ConfigName) and (ConfigName != '')):
        ConfigName = WorkDirectory+"/"+ConfigName
    else:
        print("\tConfig: "+ConfigName+" not found in current working directory: "+WorkDirectory)
        ConfigName = WorkDirectory+"/Config.cfg"

        if (os.path.exists(ConfigName)):
            print("\tDefaulting to use: "+ConfigName)
        else:
            print("Not found valid config")
            quit()

    try:
        RunScriptName = input("Run Script Name:")
    except:
        print("Invalid run script name string")
        quit()

    if (os.path.exists(WorkDirectory+"/"+RunScriptName) and (RunScriptName != '')):
        RunScriptName = WorkDirectory+"/"+RunScriptName
    else:
        print("\tRunScript: "+RunScriptName+" not found in current working directory: "+WorkDirectory)
        RunScriptName = WorkDirectory+"/RunScript.sh"

        if (os.path.exists(RunScriptName)):
            print("\tDefaulting to use: "+RunScriptName)
        else:
            print("Not found valid run script")
            quit()
            
    try:
        SubmitScriptName = input("Submit script to run? [Given in relative path to $PWD, e.g. ./SubmitScript.sh]: ")
    except:
        print("Invalid submit script name")

    if ((os.path.exists(WorkDirectory+"/"+SubmitScriptName) == False) or (SubmitScriptName == "")):
        print("\tSubmitScript: "+SubmitScriptName+" not found in current working directory: "+WorkDirectory)

        SubmitScriptName = "./SubmitScript.sh"
        if (os.path.exists(WorkDirectory+"/"+SubmitScriptName)):
            print("\tDefaulting to use: "+SubmitScriptName)
        else:
            print("Not found valid SubmitScript")            
    
    try:
        OutDirectory = os.environ['OUTDIR']
    except:
        print("Output directory not found. Using current directory. If this is not acceptable, export OUTDIR=/path/to/output")
        OutDirectory = os.environ['PWD']

    if (SubmitJobs == 1):
        SubmitJobs = True
    else:
        SubmitJobs = False
        
    print("\n\n")
    print("Summary: ---------")
    print("\tMaCh3 Install:"+MaCh3Install)
    print("\tNumber of Chains:"+str(nChains))
    print("\tNumber of Steps per Chain:"+str(nSteps))
    print("\tNumber of Threads per Chain:"+str(nThreads))
    print("\tJob Number:"+str(JobNumber))
    print("\tExecutable:"+ExecName)
    print("\tBase Config:"+ConfigName)
    print("\tBase RunScript:"+RunScriptName)
    print("\tBase SubmitScript:"+SubmitScriptName)
    print("\tOutput Directory:"+OutDirectory)

    if (SubmitJobs):
        print("\tSubmitting jobs to queue")
    else:
        print("\tNot submitting jobs to queue")

    print("\n")
    Check = int(input("Continue? [0 for no, 1 for yes]: "))
    if (Check == 0):
        print("Quiting..")
        quit()

    if (JobNumber == 0):    
        StartFromFile = False
    else:
        StartFromFile = True
        
    for iChain in range(nChains):
        ChainNum_iChain = str(iChain)
        FileNameBase_iChain = "Chain_"+ChainNum_iChain
        OutDir_iChain = OutDirectory+"/Output_"+FileNameBase_iChain+"/"
        JobName_iChain = "MaCh3_"+FileNameBase_iChain+"_JobNumber_"+str(JobNumber)
        OutputName_iChain = OutDir_iChain+JobName_iChain+".root"
        OutputName_iChain_m1 = OutDir_iChain+"MaCh3_"+FileNameBase_iChain+"_JobNumber_"+str(JobNumber-1)+".root"
        ScriptDir_iChain = WorkDirectory+"/Script_"+FileNameBase_iChain+"/"
        ScriptDir_Log_iChain = ScriptDir_iChain+"/SubmitLog"
        ScriptDir_Error_iChain = ScriptDir_iChain+"/SubmitError"
        ScriptDir_Output_iChain = ScriptDir_iChain+"/SubmitOutput"
        ScriptDir_Submit_iChain = ScriptDir_iChain+"/SubmitScript"
        ConfigName_iChain = ScriptDir_Submit_iChain+"/Config_"+str(iChain)+"_JobNumber_"+str(JobNumber)+".cfg"
        RunScriptName_iChain = ScriptDir_Submit_iChain+"/RunScript_"+str(iChain)+"_JobNumber_"+str(JobNumber)+".sh"
        SubmitScriptName_iChain = ScriptDir_Submit_iChain+"/SubmitScript_"+str(iChain)+"_JobNumber_"+str(JobNumber)+".sh"
        ConsoleOutputName_iChain = ScriptDir_Output_iChain+"/ConsoleOutput_"+str(iChain)+"_JobNumber_"+str(JobNumber)+".log"
        ScriptDirFileName_Error_iChain = ScriptDir_Error_iChain+"/SubmitError+"+str(iChain)+"_JobNumber_"+str(JobNumber)+".log"
        ScriptDirFileName_Log_iChain = ScriptDir_Log_iChain+"/SubmitLog+"+str(iChain)+"_JobNumber_"+str(JobNumber)+".log"
        
        if (StartFromFile and os.path.exists(OutputName_iChain_m1) == False):
            print("Starting from previous chain but did not find:" + OutputName_iChain_m1)
            quit()
        
        MkdirCommand  = "mkdir -p "+ScriptDir_iChain
        os.system(MkdirCommand)
        
        MkdirCommand  = "mkdir -p "+ScriptDir_Log_iChain
        os.system(MkdirCommand)

        MkdirCommand  = "mkdir -p "+ScriptDir_Error_iChain
        os.system(MkdirCommand)

        MkdirCommand  = "mkdir -p "+ScriptDir_Output_iChain
        os.system(MkdirCommand)

        MkdirCommand  = "mkdir -p "+ScriptDir_Submit_iChain
        os.system(MkdirCommand)
        
        MkdirCommand = "mkdir -p "+OutDir_iChain
        os.system(MkdirCommand)

        Temp_ConfigName = WorkDirectory+"/Config_Temp.cfg"
        CopyCommand = "cp "+ConfigName+" "+Temp_ConfigName
        os.system(CopyCommand)

        SedCommand = "sed -i 's|OUTPUTNAME.*|OUTPUTNAME = \""+OutputName_iChain+"\"|' "+Temp_ConfigName
        os.system(SedCommand)

        if (StartFromFile):
            SedCommand = "sed -i 's|STARTFROMPOS.*|STARTFROMPOS = True|' "+Temp_ConfigName
        else:
            SedCommand = "sed -i 's|STARTFROMPOS.*|STARTFROMPOS = False|' "+Temp_ConfigName
        os.system(SedCommand)

        if (StartFromFile):
            SedCommand = "sed -i 's|POSFILES.*|POSFILES = "+OutputName_iChain_m1+"|' "+Temp_ConfigName
            os.system(SedCommand)

        SedCommand = "sed -i 's|NSTEPS.*|NSTEPS = "+str(nSteps)+"|' "+Temp_ConfigName
        os.system(SedCommand)

        mvCommand = "mv "+Temp_ConfigName+" "+ConfigName_iChain
        os.system(mvCommand)

        Temp_RunScriptName = WorkDirectory+"/RunScript_Temp.sh"
        CopyCommand = "cp "+RunScriptName+" "+Temp_RunScriptName
        os.system(CopyCommand)

        replaceText(Temp_RunScriptName,"MACH3INSTALL",MaCh3Install)
        replaceText(Temp_RunScriptName,"NTHREADS",str(nThreads))
        replaceText(Temp_RunScriptName,"CONFIGNAME",ConfigName_iChain)
        replaceText(Temp_RunScriptName,"EXECNAME",ExecName)
        replaceText(Temp_RunScriptName,"CONSOLELOG",ConsoleOutputName_iChain)

        mvCommand = "mv "+Temp_RunScriptName+" "+RunScriptName_iChain
        os.system(mvCommand)

        Temp_SubmitScriptName = WorkDirectory+"/SubmitScript_Temp.sh"
        CopyCommand = "cp "+SubmitScriptName+" "+Temp_SubmitScriptName
        os.system(CopyCommand)

        replaceText(Temp_SubmitScriptName,"JOBNAME",JobName_iChain)
        replaceText(Temp_SubmitScriptName,"EXECUTABLENAME",RunScriptName_iChain)
        replaceText(Temp_SubmitScriptName,"SUBMITSCRIPTOUTPUT",ScriptDirFileName_Log_iChain)
        replaceText(Temp_SubmitScriptName,"ERRORFILE",ScriptDirFileName_Error_iChain)

        mvCommand = "mv "+Temp_SubmitScriptName+" "+SubmitScriptName_iChain
        os.system(mvCommand)

        if (SubmitJobs):
            Submitted = False
            
            SubmitCommand = "sbatch "+SubmitScriptName_iChain
            try:
                os.system(SubmitCommand)
                Submitted = True
            except:
                print("sbatch command not available")
                
            if (Submitted == False):
                SubmitCommand = "qsub "+SubmitScriptName_iChain
                try:
                    os.system(SubmitCommand)
                    Submitted =	True
                except:
                    print("qsub command not available")

Version = sys.version_info[0]
if (Version != 3):
    print("Python3 required")
    quit()
    
main()
