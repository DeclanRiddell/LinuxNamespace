#ifndef MSG_Q_DR_H
#define MSG_Q_DR_H

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <math.h>
#include "SYSV_msgq_metrics.h"
#include "SYSV_message_queue.h"

#define MIN_POSSIBLE_EXE_TIME 0.00001

//void sysv_message_queue_execute(int argc, char* argv[]);
char* inc_msg;
int SYS_V_message_queue_execute(int argc, char* argv[]);

#endif