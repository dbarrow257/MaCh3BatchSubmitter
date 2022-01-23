import os

def main():
    nMaxChains = 1000
    nMaxJobs = 1000
    
    for iChain in range(0,nMaxChains):
        if (os.path.exists("Output_Chain_"+str(iChain))):

            for iJob in range(0,nMaxJobs):
                FileName = "Output_Chain_"+str(iChain)+"/MaCh3_Chain_"+str(iChain)+"_JobNumber_"+str(iJob)+".root.log"
                if (os.path.exists(FileName)):
                    print(FileName+":")

                    Command = "cat "+FileName+" | grep \"logLProp\" | wc -l"
                    os.system(Command)
                else:
                    break

main()
