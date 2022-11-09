#include <stdio.h>
#include <stdbool.h>
#define MAX 1000

typedef enum {
    PSH,
    ADD,
    POP,
    SET,
    HLT
}InstructionSet;

typedef enum {
    A, B, C, D, E, F,
    NUM_OF_REGISTERS
}Registers;

int ip = 0; //The instruction pointer
int sp = -1; //The stack pointer
bool running = true;

int stack[MAX];
int registers[NUM_OF_REGISTERS];

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

        case SET:
            ip++;
            int reg = program[ip];
            registers[reg] = program[++ip];
            break;
    }
}

int main() {
    while (running) {
        eval(fetch());
        ip++;
    }
    return 0;
}
