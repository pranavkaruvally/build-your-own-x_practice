#include <stdio.h>

typedef enum {
    PSH,
    ADD,
    POP,
    SET,
    HLT
}InstructionSet;

int ip = 0; //The instruction pointer

const int program[] = {
    PSH, 5,
    PSH, 6,
    ADD,
    POP,
    HLT
};

int main() {
    int instruction = program[ip];
    return 0;
}
