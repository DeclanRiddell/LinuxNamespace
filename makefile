
CXX = gcc
CFLAGS = -Wall -w -g

OUT_DIR = bin
LAUNCHER_NAME = LinuxIPC
SRC_DIR = src
ENTRY_POINT = $(SRC_DIR)/main.c


INC_INTERNAL = -I $(SRC_DIR)
INC=-I $(SRC_DIR)/ 

EXAMPLE_OBJS = example.o
OBJS = $(EXAMPLE_OBJS)#list of objects
OUT_OBJECTS = $(patsubst %.o, $(OUT_DIR)/%.o, $(OBJS))



all: main

main: $(ENTRY_POINT) $(OBJS)
	$(CXX) $(CXXFLAGS) $(INC) -o $(OUT_DIR)/$(LAUNCHER_NAME) $(OUT_OBJECTS) $(ENTRY_POINT)

run: $(OUT_DIR)/$(LAUNCHER_NAME).exe
	./$(OUT_DIR)/$(LAUNCHER_NAME).exe



example.o: $(SRC_DIR)/example/example.c
	$(CXX) $(CFLAGS) -c $(SRC_DIR)/example/example.c -o $(OUT_DIR)/example.o

