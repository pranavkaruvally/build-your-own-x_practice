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

int fetch() {
    return program[ip];
}

void eval(int instr) {
    switch(instr) {
        case HLT:
            running = false;
            break;
    }
}

int main() {
    bool running = true;
    while (running) {
        eval(fetch());
        ip++
    }
    return 0;
}
