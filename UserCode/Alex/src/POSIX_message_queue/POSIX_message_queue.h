#ifndef POSIX_MQ_H
#define POSIX_MQ_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>

#include "POSIX_message_queue_driver.h"

#define QUEUE_NAME "/queue"

mqd_t mqdes;

//Receives and removes message from message queue
void * posix_message_queue_receive();

//Adds message to message queue
void * posix_message_queue_send();


#endif
