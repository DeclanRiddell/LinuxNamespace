#ifndef MSG_Q_DR_H
#define MSG_Q_DR_H

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include "POSIX_msgq_metrics.h"
#include "POSIX_message_queue.h"
#include <debug_utils.h>

#define MIN_POSSIBLE_EXE_TIME 0.00001

//Executes message queue
char* inc_msg;
int POSIX_message_queue_execute(int);

#endif