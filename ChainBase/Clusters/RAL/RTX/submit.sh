input                   = /dev/null
executable              = EXECUTABLENAME
output                  = SUBMITSCRIPTOUTPUT
error                   = ERRORFILE
log                     = LOGFILE
notification            = never
request_cpus            = 4
request_memory          = 16 GB
request_GPUs            = 1
requirements            = (CUDADeviceName =?= "TITAN RTX")

queue 1
