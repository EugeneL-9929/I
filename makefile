# compiler and compiling options
CC = g++
CFLAGS = -Wall -g

# target and source
TARGET = ./compile/my_program
SOURCES = ./src/main.cpp ./src/Array.cpp
OBJECTS = $(patsubst ./src/%.cpp, ./build/%.o, $(SOURCES)) # patsubst <pattern> <replacement> <text>

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

./build/%.o: ./src/%.cpp # ensure every .o corresponds to respective .c
	@echo "objects $(OBJECTS), sources $(SOURCES)" 
	$(CC) $(CFLAGS) -c $< -o $@ 
# < means the src files and @ means the dst files
# means single line comment

# clear all
clean: 
	rm -f $(OBJECTS) $(TARGET)