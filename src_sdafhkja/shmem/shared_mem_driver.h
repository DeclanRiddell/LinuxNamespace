#ifndef SHM_DRIVER_H
#define SHM_DRIVER_H

#include "server.h"
#include "client.h"
#include <sys/time.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * This program is used to demonstrate Shared Memory using SystemV
 * it counts how many times a message is sent and read from Shared
 * Memory in 1 second
 * 
 * An argument is needed to be able to print the message
 * ./shared_mem "Message goes in here"
 */

int shared_mem_execute(int argc, char* argv[]);



#endif