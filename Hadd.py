import sys
import os

def main():
    nMaxChains = 1000
    nMaxJobs = 1000

    FilesToDelete = []
    Files = []

    for iChain in range(0,nMaxChains):
        if (os.path.exists("Output_Chain_"+str(iChain))):

            Start = 0
            Stop = nMaxJobs
            if (len(sys.argv) > 1):
                Start = int(sys.argv[1])
                Stop = Start+1

            CombFileName = "Output_Chain_"+str(iChain)+"/MaCh3_MCMC_"+str(iChain)+".root"
            HaddCommand = "hadd -n 10 "+CombFileName+" "
                
            for iJob in range(Start,Stop):
                FileName = "Output_Chain_"+str(iChain)+"/MaCh3_Chain_"+str(iChain)+"_JobNumber_"+str(iJob)+".root"
                if (os.path.exists(FileName)):
                    NewFileName = FileName+".tmp"
                    Command = "cp "+FileName+" "+NewFileName
                    os.system(Command)
                    #print(Command)

                    FilesToDelete.append(NewFileName)
                    HaddCommand += NewFileName+" "
                else:
                    break

            FilesToDelete.append(CombFileName)
            Files.append(CombFileName)
            os.system(HaddCommand)
            #print(HaddCommand)

    Command = "hadd MaCh3_MCMC.root "
    for File in Files:
        Command += File+" "

    os.system(Command)
    #print(Command)

    for	File in	FilesToDelete:
        Command = "rm "+File

        os.system(Command)
        #print(Command)
    
main()
