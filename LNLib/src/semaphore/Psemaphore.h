#ifndef PSEMAPHORE_H
#define PSEMAPHORE_H


#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <sys/time.h>


//This program willl use the POSIX implementation of semaphores

sem_t semaphore;

void* thread2_function(void* arg);
void* thread1_function(void* arg);



#endif