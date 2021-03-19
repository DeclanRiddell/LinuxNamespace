#ifndef CLIENT_H
#define CLIENT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

/**
 * Shared Memory SystemV Client side
 * 
 * The Client is able to read the data from Shared Memory
 * that was used as an argument in server.c
 */


#define SHM_SIZE 1024

int shmid;
key_t key;
char *shm;

int receive();
void print_msg();
void clean_ipc();

#endif