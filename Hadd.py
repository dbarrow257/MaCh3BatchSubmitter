import sys
import os

def main():
    nMax = 1000

    FilesToDelete = []
    Files = []

    for iJob in range(0,nMax):
        if (os.path.exists("Output_Job_"+str(iJob))):

            Start = 0
            Stop = nMax
            if (len(sys.argv) > 1):
                Start = int(sys.argv[1])
                Stop = Start+1

            CombFileName = "Output_Job_"+str(iJob)+"/MaCh3_MCMC_"+str(iJob)+".root"
            HaddCommand = "hadd -n 10 "+CombFileName+" "
                
            for iJobNumber in range(Start,Stop):
                for iChain in range(0,nMax):
                    FileName = "Output_Job_"+str(iJob)+"/MaCh3_Job_"+str(iJob)+"_JobNumber_"+str(iJobNumber)+"_Chain_"+str(iChain)+".root"
                    if (os.path.exists(FileName)):
                        NewFileName = FileName+".tmp"
                        Command = "cp "+FileName+" "+NewFileName

                        print(Command)
                        os.system(Command)
                        
                        FilesToDelete.append(NewFileName)
                        HaddCommand += NewFileName+" "
                    else:
                        break
                        
            FilesToDelete.append(CombFileName)
            Files.append(CombFileName)

            print(HaddCommand)
            os.system(HaddCommand)

    Command = "hadd MaCh3_MCMC.root "
    for File in Files:
        Command += File+" "

    print(Command)
    os.system(Command)

    for	File in	FilesToDelete:
        Command = "rm "+File

        print(Command)
        os.system(Command)
    
main()
