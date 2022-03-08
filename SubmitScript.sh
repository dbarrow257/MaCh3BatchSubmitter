input                   = /dev/null
executable              = EXECUTABLENAME
output                  = SUBMITSCRIPTOUTPUT
error                   = ERRORFILE
log                     = LOGFILE
notification            = never
request_cpus            = 40
request_memory          = 200 GB
request_GPUs            = 1
requirements            = (CUDADeviceName =?= "NVIDIA A100-PCIE-40GB")

queue 1
