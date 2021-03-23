#ifndef POSIX_SHMEM_DRIVER_H
#define POSIX_SHMEM_DRIVER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
#include "posix_client.h"
#include "posix_server.h"


int shmem_driver_posix(int argc, char* argv[]);
int posix_append_results();
void posix_results();

struct timeval startPosix, endPosix;
float elapsedTimePosix;
pthread_t thread1Posix, thread2Posix;

#endif