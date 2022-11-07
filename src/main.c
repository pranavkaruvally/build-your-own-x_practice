#include <stdio.h>
#define MAX 1000

typedef enum {
    PSH,
    ADD,
    POP,
    SET,
    HLT
}InstructionSet;

int ip = 0; //The instruction pointer
int sp = -1; //The stack pointer

int stack[MAX];

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

        case PSH:
            sp++;
            stack[sp] = program[++ip];
            break;

        case POP:
            int val_popped = stack[sp--];
            printf("Popped %d\n", val_popped);
            break;

        case ADD:
            int a = stack[sp--];
            int b = stack[sp--];
            int result = b + a;
            sp++;
            stack[sp] = result;
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
