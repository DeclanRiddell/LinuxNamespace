#ifndef PSEMAPHORE_H
#define PSEMAPHORE_H


#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <sys/time.h>
#include <math.h>


#include <debug_utils.h>

//This program willl use the POSIX implementation of semaphores



void* thread(void* arg);

#define MIN_TIME_EXE 0.00001

//float times [iteration_count]; // This array will hold the elapsed time of each wait()/post() executed by the threads while looping

int count; //Will count how many wait()/post() are executed by the threads while looping

float avg_time;
static int p_iteration_count = 2048;


#endif