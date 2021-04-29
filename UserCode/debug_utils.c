#include "debug_utils.h"
void write_to_file_(char* IPC, char* LIBRARY, char* ENVIRONMENT, double AVG_TIME, int ITERATIONS){
    FILE *store_results;
    store_results = fopen(DATA_LOC, "a");
    fprintf(store_results,"%s,%s,%s,%f,%d\n", IPC, LIBRARY, ENVIRONMENT, AVG_TIME, ITERATIONS);
    fclose(store_results);
}

void write_to_file_pathed_(char* path, char* IPC, char* LIBRARY, char* ENVIRONMENT, double AVG_TIME, int ITERATIONS){
    FILE *store_results;
    store_results = fopen(path, "a");
    fprintf(store_results,"%s,%s,%s,%f,%d\n", IPC, LIBRARY, ENVIRONMENT, AVG_TIME, ITERATIONS);
    fclose(store_results);
}