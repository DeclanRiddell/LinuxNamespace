#ifndef SYSV_MSG_Q_METRICS_H
#define SYSV_MSG_Q_METRICS_H

#include <unistd.h>
#include "SYSV_message_queue.h"
#include <debug_utils.h>


void SYSV_msgq_outputDataFile(double avg, char methodName[], int iterations);

double SYSV_msgq_averageTime(double times[], int iterations);

double SYSV_msgq_minimum(double times[], int iterations);

double SYSV_msgq_maximum(double times[], int iterations);

#endif