input                   = /dev/null
executable              = EXECUTABLENAME
output                  = SUBMITSCRIPTOUTPUT
error                   = ERRORFILE
log                     = LOGFILE
notification            = never
request_cpus            = 48
request_memory          = 170 GB
request_GPUs            = 2
requirements            = (CUDADeviceName =?= "NVIDIA TITAN RTX")

queue 1
