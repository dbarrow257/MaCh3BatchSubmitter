import sys
import os

def main():
    nMaxChains = 1000
    nMaxJobs = 1000

    for iChain in range(0,nMaxChains):
        if (os.path.exists("Output_Chain_"+str(iChain))):

            Start = 0
            Stop = nMaxJobs
            if (len(sys.argv) > 1):
                Start = int(sys.argv[1])
                Stop = Start+1
            
            for iJob in range(Start,Stop):
                FileName = "Output_Chain_"+str(iChain)+"/MaCh3_Chain_"+str(iChain)+"_JobNumber_"+str(iJob)+".root.log"
                if (os.path.exists(FileName)):
                    print(FileName+":")

                    Command = "cat "+FileName+" | grep \"logLProp\" | wc -l"
                    os.system(Command)
                else:
                    break

main()
