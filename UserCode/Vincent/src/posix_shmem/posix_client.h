#ifndef POSIX_CLIENT_H
#define POSIX_CLIENT_H

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/mman.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/time.h>

#define SHM_SIZE 1024

#define NAME "/POSIX_SHMEM"
struct timeval startClientPosix, endClientPosix;
int clientCountPosix;
int shm_fd;
void * ptr;
float readDeltaPosix;
float longestClientPosix;
float shortestClientPosix;
float averageClientPosix;
float totalClientTimePosix;

void * posix_receive();
void posix_print_msg();
int posix_set_varClient();

#endif