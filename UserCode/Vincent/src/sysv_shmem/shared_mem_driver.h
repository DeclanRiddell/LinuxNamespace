#ifndef SHM_DRIVER_H
#define SHM_DRIVER_H

#include "server.h"
#include "client.h"
#include <sys/time.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <debug_utils.h>

/**
 * This program is used to demonstrate Shared Memory using SystemV
 * it counts how many times a message is sent and read from Shared
 * Memory in 1 second
 * 
 * An argument is needed to be able to print the message
 * ./shared_mem "Message goes in here"
 */

int SYS_V_shared_memory_execute();
int append_results(char* message);
void results();
   
struct timeval start, end;
float elapsedTime = 0;
pthread_t thread1, thread2;
int counterSYSV = 0;
float msgPerSecondSYSV;


#endif