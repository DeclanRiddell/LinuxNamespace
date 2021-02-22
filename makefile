CXX = gcc
CXXFLAGS = -Wall -w -g

OUT_DIR = bin
LAUNCHER_NAME = LinuxIPC
SRC_DIR = src
ENTRY_POINT = $(SRC_DIR)/main.c


INC_INTERNAL = -I $(SRC_DIR)
INC=-I $(SRC_DIR)/ 

OBJS = #list of objects
OUT_OBJECTS = $(patsubst %.o, $(OUT_DIR)/%.o, $(OBJS))



all: main

main: $(ENTRY_POINT) $(OBJS)
	$(CXX) $(CXXFLAGS) $(LIBS) $(INC) -o $(OUT_DIR)/$(LAUNCHER_NAME) $(OUT_OBJECTS) $(ENTRY_POINT)

run: $(OUT_DIR)/$(LAUNCHER_NAME).exe
	./$(OUT_DIR)/$(LAUNCHER_NAME).exe



example.o: $(SRC_DIR)/examplefolder/cfile.c

