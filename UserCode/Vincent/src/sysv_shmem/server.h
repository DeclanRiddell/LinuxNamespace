#ifndef SERVER_H
#define SERVER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <errno.h>
#include <sys/time.h>

/**
 * Shared Memory SystemV Server Side
 * 
 * When running the program, it takes a parameter (a message) and copies it
 * into memory so that Client can read it. Running this program will give no
 * output unless there is an error. In order to read the message, run client.c
 */

#define SHM_SIZE 1024

int serverCount;
int shmid;
key_t key;
char *shm;
struct timeval startServer, endServer;
float writeDelta;
float longestServer;
float shortestServer;
float averageServer;
float totalServerTime;


void * send(void * message);
int set_varServer();

#endif