#ifndef POSIX_SERVER_H
#define POSIX_SERVER_H

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/mman.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <debug_utils.h>

#define SHM_SIZE 1024

#define NAME "/POSIX_SHMEM"
struct timeval startServerPosix, endServerPosix;
int serverCountPosix;
int shm_fd;
void *ptr;
float writeDeltaPosix;
float longestServerPosix;
float shortestServerPosix;
float averageServerPosix;
float totalServerTimePosix;

void * posix_send(void * msg);
int posix_set_varServer();

#endif