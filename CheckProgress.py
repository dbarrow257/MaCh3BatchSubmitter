import sys
import os
import subprocess

def main():
    nMax = 1000

    Total = 0

    for iJob in range(0,nMax):
        if (os.path.exists("Output_Job_"+str(iJob))):

            Start = 0
            Stop = nMax
            if (len(sys.argv) > 1):
                Start = int(sys.argv[1])
                Stop = Start+1
            
            for iJobNumber in range(Start,Stop):
                for iChain in range(0,nMax):
                    FileName = "Output_Job_"+str(iJob)+"/MaCh3_Job_"+str(iJob)+"_JobNumber_"+str(iJobNumber)+"_Chain_"+str(iChain)+".root.log"

                    if (os.path.exists(FileName)):
                        print(FileName+":")
                        
                        Command = "cat "+FileName+" | grep \"logLProp\" | wc -l"
                        output = subprocess.getoutput(Command)
                        print(output)

                        Total += int(output)
                    else:
                        if (iChain == 0):
                            break


    print("Total:" + str(Total))

main()
