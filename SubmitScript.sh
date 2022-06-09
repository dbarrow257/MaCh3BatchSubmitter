input                   = /dev/null
executable              = EXECUTABLENAME
output                  = SUBMITSCRIPTOUTPUT
error                   = ERRORFILE
log                     = LOGFILE
notification            = never
request_cpus            = 80
request_memory          = 170 GB
request_GPUs            = 1
requirements            = (CUDADeviceName =?= "NVIDIA A100-PCIE-40GB")

queue 1
