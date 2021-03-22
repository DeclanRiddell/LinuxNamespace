all: main

main:
	./kill_ipcs.sh
	./clean.script
	./run.script 
	
clean:
	./clean.script