#include "posix_shmem_driver.h"

/**
 * This program is used to demonstrate Shared Memory using POSIX API
 */

int POSIX_shared_memory_execute(int iteration_count){


    gettimeofday(&startPosix, NULL);
    while(posixCounter < iteration_count){
        posixCounter++;
        
        //Create pthread and send the message
        pthread_create(&thread1Posix, NULL, posix_send, __msg);
        pthread_join(thread1Posix, NULL);

        //Create pthread and read the message
        pthread_create(&thread2Posix, NULL, posix_receive, NULL);
        pthread_join(thread2Posix, NULL);
    }
    gettimeofday(&endPosix, NULL); //end timer
    elapsedTimePosix += abs(((endPosix.tv_usec - startPosix.tv_usec) / 1000.0)); //converts from microseconds to milliseconds

    //Averages time spent for Server and Client
    averageClientPosix = totalClientTimePosix/clientCountPosix;
    averageServerPosix = totalServerTimePosix/serverCountPosix;
    msgPerSecondPosix = posixCounter/(elapsedTimePosix/1000.0); //Go from millisecond to second

    
    //Print results and append results to file
    posix_results();
    posix_append_results(__msg);
    db();
    return 0;
}

//prints results
void posix_results(){        
   LOG("\n");
   LOG("Shared Memory POSIX findings\n");
   LOG("-----------------------------------\n");
   LOG("Number of Iterations : %d\n", posixCounter);
   LOG("Total time spent : %f ms\n", elapsedTimePosix);
   LOG("Message rate : %f messages per second\n", msgPerSecondPosix);
   LOG("\n");
   LOG("Operation: Shared Memory Read\n");
   LOG("Average Access Time : %f ms\n", averageClientPosix);
   LOG("Minimum Access Time : %f ms\n", shortestClientPosix);
   LOG("Longest Access Time : %f ms\n", longestClientPosix);
   LOG("\n");

   LOG("Operation: Shared Memory Write\n");
   LOG("Average Access Time : %f ms\n", averageServerPosix);
   LOG("Minimum Access Time : %f ms\n", shortestServerPosix);
   LOG("Longest Access Time : %f ms\n", longestServerPosix);
   LOG("\n");
}

/**
 * Write results to file
 * The file is located in the "build" folder
 * Time is recorded in ms
 * First value is Read Average
 * Second value is Write Average
 */
int posix_append_results(){
    
    FILE *store_results;
    store_results = fopen("../UserCode/Vincent/src/posix_shmem/SHM_POSIX_Output.txt", "a");
    fprintf(store_results,"%f\n", averageClientPosix);
    fprintf(store_results,"%f\n", averageServerPosix);
    fprintf(store_results, "\n");

    fclose(store_results);

}


/**
 * Connect to the DB here, then use the stored procedures to add the values.
 * After the values are added, then call the procedure to generate a CSV.
 *
 *
 */

void db() {
    int count = 0;
    if(mysql_library_init(-1, NULL, NULL)){
        fprintf(stderr, "MYSQL INIT FAILED\n");
    }
	MYSQL *conn = NULL;
	MYSQL_RES *res = NULL;
	MYSQL_ROW row = NULL;
	
	const char *server = "localhost";
	const char *user = "namespace";
	const char *password = "password"; /* set me first */
	const char *database = "sys";
    int* c = NULL;
	if( conn == NULL) printf("NULL LMAO\n");
    printf("%p\n", conn);
	conn = mysql_init(NULL);
    conn->db = database;
    conn->user = user;
    conn->passwd = password;
    printf("db: %s\n", conn->db);
    fprintf(stderr, "%s\n", mysql_error(conn));
    printf("%p\n", conn);
	if(conn == NULL) printf("NULL LMAO\n");
    printf("Version, %s\n", mysql_get_client_info());
	LOG("%d", count++);
    LOG("%s, %s, %s, %s", server, user, password, database);
	/* Connect to database */
    mysql_real_connect(conn, server, user, password, database, 0, "", 0);
	if(conn == ((void*) 0) || conn == NULL) printf("NULL LMAO\n");

	// if (!mysql_real_connect(conn, server, user, password, 
    //                                   database, 0, 0, 0)) {
	// LOG("%d", count++);
	// 	fprintf(stderr, "%s\n", mysql_error(conn));
	// 	exit(1);
	// }
	LOG("%d", count++);
	
	/* send SQL query */
	if (mysql_query(conn, "call sys.addSharedMemory(.0021, .8762)")) {
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}
   
	res = mysql_use_result(conn);
	
	/* output table name */
	printf("MySQL Tables in mysql database:\n");
   
	while ((row = mysql_fetch_row(res)) != NULL)
		printf("%s \n", row[0]);
   
	/* close connection */
	mysql_free_result(res);
	mysql_close(conn);
}

