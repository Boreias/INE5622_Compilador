#Makefile

.PHONY: run clean

clean:
	rm -rf __pycache__

run:
	python3 ./main.py