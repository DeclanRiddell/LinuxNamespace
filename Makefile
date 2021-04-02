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
both: 
	rm -rf build
	./kill_ipcs.sh
	./run_alex.script
	./kill_ipcs.sh
	./run_vincent.script


all_namespace:
	rm -rf build
	./kill_ipcs.sh
	./run_all_namespace.script 

eric_namespace:
	rm -rf build
	./kill_ipcs.sh
	./run_eric_namespace.script 

vincent_namespace:
	rm -rf build
	./kill_ipcs.sh
	./run_vincent_namespace.script 


declan_namespace:
	rm -rf build
	./kill_ipcs.sh
	./run_declan_namespace.script 

alex_namespace:
	rm -rf build
	./kill_ipcs.sh
	./run_alex_namespace.script 
both_namespace: 
	rm -rf build
	./kill_ipcs.sh
	./run_alex.script
	./kill_ipcs.sh
	./run_vincent_namespace.script

clean:
	rm -rf build
