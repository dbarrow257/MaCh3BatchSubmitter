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
        MaCh3Install = os.environ['MACH3']
    except:
        print("MaCh3 install not found. Please source setup.sh in MaCh3 install or export $MACH3=/path/to/MACH3")
        quit()

    if (os.path.exists(MaCh3Install) == False):
        print("MaCh3 install not found. Given:"+MaCh3Install)
        quit()

    try:
        nJobs = int(input("How many jobs?: "))
    except:
        print("Invalid number of jobs")
        quit()

    try:
        nGPUsPerJob = int(input("How many GPUs per job?: "))
    except:
        print("Invalid number of GPUs")
        quit()

    try:
        nChainsPerJob = int(input("How many chains per job?: "))
    except:
        print("Invalid number of chains per job")
        quit()        

    try:
        nThreads = int(input("How many threads per job?: "))
    except:
        print("Invalid number of threads")
        quit()

    try:
        nSteps = int(input("How many steps per chain?: "))
    except:
        print("Invalid number of steps")
        quit()

    if (nThreads == 0):
        print("\tDefaulting to use 1 thread")
        nThreads = 1
    
    try:
        JobNumber = int(input("Job Number? [0 for starting new job, other for continuing job]: "))
    except:
        print("Invalid Job Number")
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
        SampleConfigDir = input("Sample Config Direcotry:")
    except:
        print("Invalid sample config directory string")
        quit()

    if (os.path.exists(WorkDirectory+"/"+SampleConfigDir) and (SampleConfigDir != '')):
        SampleConfigDir = WorkDirectory+"/"+SampleConfigDir
    else:
        print("SampleConfigDir: "+SampleConfigDir+" not found in current working directory: "+WorkDirectory)
        SampleConfigDir = WorkDirectory+"/SampleConfigs/"

        if (os.path.exists(SampleConfigDir)):
            print("\tDefaulting to use: "+SampleConfigDir)
        else:
            print("Not found valid run script")
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

    try:
        SubmitJobs = int(input("Submit jobs to queue? [1 for yes, 0 for no]: "))
    except:
        print("Invalid answer")
        quit()
        
    print("\n\n")
    print("Summary: ---------")
    print("\tMaCh3 Install:"+MaCh3Install)
    print("\tNumber of Jobs:"+str(nJobs))
    print("\tNumber of GPUs per Job:"+str(nGPUsPerJob))
    print("\tNumber of chains per Job:"+str(nChainsPerJob))
    print("\tNumber of Steps per Job:"+str(nSteps))
    print("\tNumber of Threads per Job:"+str(nThreads))
    print("\tJob Number:"+str(JobNumber))
    print("\tExecutable:"+ExecName)
    print("\tBase Config:"+ConfigName)
    print("\tSample Config Directory:"+SampleConfigDir)
    print("\tBase RunScript:"+RunScriptName)
    print("\tBase SubmitScript:"+SubmitScriptName)
    print("\tOutput Directory:"+OutDirectory)

    if (SubmitJobs == 1):
        SubmitJobs = True
    else:
        SubmitJobs = False

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
        
    for iJob in range(nJobs):
        JobNum_iJob = str(iJob)
        FileNameBase_iJob = "Job_"+JobNum_iJob
        OutDir_iJob = OutDirectory+"/Output_"+FileNameBase_iJob+"/"
        JobName_iJob = "MaCh3_"+FileNameBase_iJob+"_JobNumber_"+str(JobNumber)
        ScriptDir_iJob = WorkDirectory+"/Script_"+FileNameBase_iJob+"/"
        ScriptDir_Log_iJob = ScriptDir_iJob+"/SubmitLog"
        ScriptDir_Error_iJob = ScriptDir_iJob+"/SubmitError"
        ScriptDir_Output_iJob = ScriptDir_iJob+"/SubmitOutput"
        ScriptDir_Submit_iJob = ScriptDir_iJob+"/SubmitScript"
        RunScriptName_iJob = ScriptDir_Submit_iJob+"/RunScript_"+str(iJob)+"_JobNumber_"+str(JobNumber)+".sh"
        SubmitScriptName_iJob = ScriptDir_Submit_iJob+"/SubmitScript_"+str(iJob)+"_JobNumber_"+str(JobNumber)+".sh"
        ScriptDirFileName_Error_iJob = ScriptDir_Error_iJob+"/SubmitError+"+str(iJob)+"_JobNumber_"+str(JobNumber)+".log"
        ScriptDirFileName_Log_iJob = ScriptDir_Log_iJob+"/SubmitLog+"+str(iJob)+"_JobNumber_"+str(JobNumber)+".log"

        OutputName_iJob = []
        for iChain in range(nChainsPerJob):
            OutputName_iJob.append(OutDir_iJob+JobName_iJob+"_Chain_"+str(iChain)+".root")

        OutputName_iJob_m1 = []
        for iChain in range(nChainsPerJob):
            OutputName_iJob_m1.append(OutDir_iJob+"MaCh3_"+FileNameBase_iJob+"_JobNumber_"+str(JobNumber-1)+"_Chain_"+str(iChain)+".root")

        ConfigName_iJob = []
        for iChain in range(nChainsPerJob):
            ConfigName_iJob.append(ScriptDir_Submit_iJob+"/Config_"+str(iJob)+"_JobNumber_"+str(JobNumber)+"_Chain_"+str(iChain)+".cfg")

        ConsoleOutputName_iJob = []
        for iChain in range(nChainsPerJob):
            ConsoleOutputName_iJob.append(ScriptDir_Output_iJob+"/ConsoleOutput_"+str(iJob)+"_JobNumber_"+str(JobNumber)+"_Chain_"+str(iChain)+".log")
        
        MkdirCommand  = "mkdir -p "+ScriptDir_iJob
        os.system(MkdirCommand)
        
        MkdirCommand  = "mkdir -p "+ScriptDir_Log_iJob
        os.system(MkdirCommand)

        MkdirCommand  = "mkdir -p "+ScriptDir_Error_iJob
        os.system(MkdirCommand)

        MkdirCommand  = "mkdir -p "+ScriptDir_Output_iJob
        os.system(MkdirCommand)

        MkdirCommand  = "mkdir -p "+ScriptDir_Submit_iJob
        os.system(MkdirCommand)
        
        MkdirCommand = "mkdir -p "+OutDir_iJob
        os.system(MkdirCommand)

        for iChain in range(nChainsPerJob):
            if (StartFromFile and os.path.exists(OutputName_iJob_m1[iChain]) == False):
                print("Starting from previous job but did not find:" + OutputName_iJob_m1[iChain])
                quit()
                
            Temp_ConfigName = WorkDirectory+"/Config_Temp.cfg"
            CopyCommand = "cp "+ConfigName+" "+Temp_ConfigName
            os.system(CopyCommand)
            
            SedCommand = "sed -i 's|OUTPUTNAME.*|OUTPUTNAME = \""+OutputName_iJob[iChain]+"\"|' "+Temp_ConfigName
            os.system(SedCommand)
            
            if (StartFromFile):
                SedCommand = "sed -i 's|STARTFROMPOS.*|STARTFROMPOS = true|' "+Temp_ConfigName
            else:
                SedCommand = "sed -i 's|STARTFROMPOS.*|STARTFROMPOS = false|' "+Temp_ConfigName
            os.system(SedCommand)
            
            if (StartFromFile):
                SedCommand = "sed -i 's|POSFILES.*|POSFILES = \""+OutputName_iJob_m1[iChain]+"\"|' "+Temp_ConfigName
                os.system(SedCommand)

            SedCommand = "sed -i 's|NSTEPS.*|NSTEPS = "+str(nSteps)+"|' "+Temp_ConfigName
            os.system(SedCommand)

            SedCommand = "sed -i 's|ATMCONFIGDIR.*|ATMCONFIGDIR = \""+SampleConfigDir+"\"|' "+Temp_ConfigName
            os.system(SedCommand)

            SedCommand = "sed -i 's|BEAMCONFIGDIR.*|BEAMCONFIGDIR = \""+SampleConfigDir+"\"|' "+Temp_ConfigName
            os.system(SedCommand)

            mvCommand = "mv "+Temp_ConfigName+" "+ConfigName_iJob[iChain]
            os.system(mvCommand)

        Temp_RunScriptName = WorkDirectory+"/RunScript_Temp.sh"
        CopyCommand = "cp "+RunScriptName+" "+Temp_RunScriptName
        os.system(CopyCommand)

        replaceText(Temp_RunScriptName,"MACH3INSTALL",MaCh3Install)
        replaceText(Temp_RunScriptName,"NTHREADS",str(nThreads/nChainsPerJob))

        for iChain in range(nChainsPerJob):
            iGPU = int(iChain/(nChainsPerJob/nGPUsPerJob))
            SedCommand = "sed -i -e '/^#INSERTJOB/abackground_pid_"+str(iChain)+"=$!' "+Temp_RunScriptName
            os.system(SedCommand)
            SedCommand = "sed -i -e '/^#INSERTJOB/a CUDA_VISIBLE_DEVICES=\""+str(iGPU)+"\" "+ExecName+" "+ConfigName_iJob[iChain]+" > "+ConsoleOutputName_iJob[iChain]+" &' "+Temp_RunScriptName
            os.system(SedCommand)

        for iChain in range(nChainsPerJob):
            SedCommand = "sed -i -e '/^#INSERTWAIT/await ${background_pid_"+str(iChain)+"} ' "+Temp_RunScriptName
            os.system(SedCommand)

        mvCommand = "mv "+Temp_RunScriptName+" "+RunScriptName_iJob
        os.system(mvCommand)

        Temp_SubmitScriptName = WorkDirectory+"/SubmitScript_Temp.sh"
        CopyCommand = "cp "+SubmitScriptName+" "+Temp_SubmitScriptName
        os.system(CopyCommand)

        replaceText(Temp_SubmitScriptName,"JOBNAME",JobName_iJob)
        replaceText(Temp_SubmitScriptName,"EXECUTABLENAME",RunScriptName_iJob)
        replaceText(Temp_SubmitScriptName,"SUBMITSCRIPTOUTPUT",ScriptDirFileName_Log_iJob)
        replaceText(Temp_SubmitScriptName,"ERRORFILE",ScriptDirFileName_Error_iJob)

        mvCommand = "mv "+Temp_SubmitScriptName+" "+SubmitScriptName_iJob
        os.system(mvCommand)

        if (SubmitJobs):
            Submitted = False
            
            SubmitCommand = "sbatch "+SubmitScriptName_iJob
            #SubmitCommand = "condor_submit "+SubmitScriptName_iJob
            try:
                os.system(SubmitCommand)
                Submitted = True
            except:
                print("sbatch command not available")
                
            if (Submitted == False):
                SubmitCommand = "qsub "+SubmitScriptName_iJob
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
