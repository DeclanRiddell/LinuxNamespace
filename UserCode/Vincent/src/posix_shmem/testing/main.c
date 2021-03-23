#include "posix_shmem_driver.h"

int main(int argc, char* argv[]){
    for(int i = 0; i < 50; i++){
        shmem_driver_posix(argc, argv);
    }
    return 0;
}