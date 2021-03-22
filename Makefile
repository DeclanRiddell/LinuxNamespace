all: main

main:
	rm -rf build
	./kill_ipcs.sh
	./run.script 
	
clean:
	rm -rf build