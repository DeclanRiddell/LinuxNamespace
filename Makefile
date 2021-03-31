all: main

main:
	rm -rf build
	./kill_ipcs.sh
	./run_all.script 

eric:
	rm -rf build
	./kill_ipcs.sh
	./run_eric.script 

vincent:
	rm -rf build
	./kill_ipcs.sh
	./run_vincent.script 


declan:
	rm -rf build
	./kill_ipcs.sh
	./run_declan.script 

alex:
	rm -rf build
	./kill_ipcs.sh
	./run_alex.script 
	
clean:
	rm -rf build
