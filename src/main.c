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

int main() {
    bool running = true;
    while (true) {
        x = fetch();
        if (x == HLT) running=false;
        ip++
    }
    return 0;
}
