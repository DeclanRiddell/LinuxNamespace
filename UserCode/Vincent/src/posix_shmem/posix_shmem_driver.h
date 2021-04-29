#ifndef POSIX_SHMEM_DRIVER_H
#define POSIX_SHMEM_DRIVER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
#include "posix_client.h"
#include "posix_server.h"
#include <debug_utils.h>


int POSIX_shared_memory_execute(int iteration_count, int native);
int posix_append_results();
void posix_results();

struct timeval startPosix, endPosix;
float elapsedTimePosix;
pthread_t thread1Posix, thread2Posix;
float msgPerSecondPosix;
int posixCounter = 0;

#endif