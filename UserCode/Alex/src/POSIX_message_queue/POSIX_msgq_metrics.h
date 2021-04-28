#ifndef POSIX_MSG_Q_METRICS_H
#define POSIX_MSG_Q_METRICS_H

#include <unistd.h>
#include "POSIX_message_queue.h"
#include <debug_utils.h>

void POSIX_msgq_outputDataFile(double times[], char methodName[], int iterations);

double POSIX_msgq_averageTime(double times[], int iterations);

double POSIX_msgq_minimum(double times[], int iterations);

double POSIX_msgq_maximum(double times[], int iterations);

#endif