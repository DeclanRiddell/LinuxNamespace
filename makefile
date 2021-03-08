
CXX = gcc
CFLAGS = -Wall -w -g -pthread

OUT_DIR = bin
LAUNCHER_NAME = LinuxIPC
SRC_DIR = src
ENTRY_POINT = $(SRC_DIR)/main.c


INC_INTERNAL = -I $(SRC_DIR)
INC=-I $(SRC_DIR)/ 



SHARED_MEM_OBJS = client.o server.o shared_mem_driver.o
SEMAPHORE_OBJS = Psemaphore.o semaphore_driver.o
OBJS = $(SHARED_MEM_OBJS) $(SEMAPHORE_OBJS)				#list of objects
OUT_OBJECTS = $(patsubst %.o, $(OUT_DIR)/%.o, $(OBJS))



all: main

main: $(ENTRY_POINT) $(OBJS)
	$(CXX) $(CFLAGS) $(INC) -o $(OUT_DIR)/$(LAUNCHER_NAME) $(OUT_OBJECTS) $(ENTRY_POINT)

run: $(OUT_DIR)/$(LAUNCHER_NAME).exe
	./$(OUT_DIR)/$(LAUNCHER_NAME).exe


#to add a file called example.c/example.h in folder src/example you would do the following:
#use ur brain to find/replace ur file names where example and src/example would be, this is for COMPILATION not for pure headers

#example.o: $(SRC_DIR)/example/example.c
	#$(CXX) $(CFLAGS) -c $(SRC_DIR)/example/example.c -o $(OUT_DIR)/example.o


#Shared Memory
client.o: $(SRC_DIR)/shmem/client.c
	$(CXX) $(CFLAGS) -c $(SRC_DIR)/shmem/client.c -o $(OUT_DIR)/client.o

server.o: $(SRC_DIR)/shmem/server.c
	$(CXX) $(CFLAGS) -c $(SRC_DIR)/shmem/server.c -o $(OUT_DIR)/server.o

shared_mem_driver.o: $(SRC_DIR)/shmem/shared_mem_driver.c
	$(CXX) $(CFLAGS) -c $(SRC_DIR)/shmem/shared_mem_driver.c -o $(OUT_DIR)/shared_mem_driver.o

semaphore_driver.o: $(SRC_DIR)/semaphore/semaphore_driver.c
	$(CXX) $(CFLAGS) -c $(SRC_DIR)/semaphore/semaphore_driver.c -o $(OUT_DIR)/semaphore_driver.o

Psemaphore.o: $(SRC_DIR)/semaphore/Psemaphore.c
	$(CXX) $(CFLAGS) -c $(SRC_DIR)/semaphore/Psemaphore.c -o $(OUT_DIR)/Psemaphore.o




clean:
	rm bin/*