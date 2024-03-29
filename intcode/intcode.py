from typing import List
from collections import defaultdict


def intcode(program, inputs: List[int] = [], i: int = 0, relative_base: int = 0, perpetual_input: bool = False,
            loop_mode: bool = False, print_outputs: bool = True, ):
    assert len(program) > 0

    if type(program) == list:
        p = defaultdict(int, enumerate(program))
    elif type(program) == str:
        p = defaultdict(int, enumerate([int(item.strip()) for item in program.split(",")]))
    else:
        p = program.copy()

    relative_base = 0
    outputs = []

    while p[i] != 99:
        # Extract operation
        op = int(str(p[i])[-2:])
        # Extract modes after zero filling it & inverting
        modes = [int(char) for char in str(p[i])[:-2].zfill(3)][::-1]

        # Map variables/locations based on operation
        variables = [
            i + 1 if modes[0] == 1 else p[i + 1] + relative_base if modes[0] == 2 else p[i + 1],
            i + 2 if modes[1] == 1 else p[i + 2] + relative_base if modes[1] == 2 else p[i + 2],
            i + 3 if modes[2] == 1 else i + 3 + relative_base if modes[2] == 2 else p[i + 3]
        ]

        # Perform operation
        if op == 1:  # Sum
            p[variables[2]] = p[variables[0]] + p[variables[1]]
            i += 4
        elif op == 2:  # Multiplication
            p[variables[2]] = p[variables[0]] * p[variables[1]]
            i += 4
        elif op == 3:  # Input
            p[variables[0]] = p[inputs[0]] if perpetual_input and len(inputs) == 0 else inputs.pop(0)
            i += 2
        elif op == 4:  # Output
            outputs.append(p[variables[0]])
            if print_outputs:
                print(p[variables[0]])
            i += 2
            if loop_mode:
                return {"outputs": outputs, "program": p.copy(), "i":i, "relative_base": relative_base}
        elif op == 5:  # Jump-if-true
            i = p[variables[1]] if p[variables[0]] else i + 3
        elif op == 6:  # Jump-if-false
            i = i + 3 if p[variables[0]] else p[variables[1]]
        elif op == 7:  # Less-than
            p[variables[2]] = int(p[variables[0]] < p[variables[1]])
            i += 4
        elif op == 8:  # Equals
            p[variables[2]] = int(p[variables[0]] == p[variables[1]])
            i += 4
        elif op == 9:  # Relative base adjustment
            relative_base += p[variables[0]]
            i += 2
        else:  # ERROR!!
            print("Oops...")
            return {"outputs": - 1}

    if loop_mode:
        return {"outputs": - 1}
    return {"outputs": outputs, "program": p.copy(), "i": i, "relative_base": relative_base}


def chain_intercodes(program: List[int], phases: List[int] = []):
    output = 0
    for phase in phases:
        outputs, _, _ = intcode(program, [phase, output])
        output = outputs[-1]
    return output


def looping_intcodes(program: List[int], phases: List[int]):
    amps = [program.copy() for i in range(len(phases))]
    amps_i = [0] * len(phases)
    amps_active = list(range(len(phases)))

    output = 0
    result = None

    while len(amps_active) > 0:
        for amp in amps_active:
            program = amps[amp].copy()
            i = amps_i[amp]
            phase = phases[amp]
            program_input = [phase, output] if i == 0 else [output]
            outputs, amp_p, amp_i = intcode(program, program_input, perpetual_input=True,
                                            loop_mode=True, print_outputs=False, i=i)
            if outputs is not None:
                output = outputs[-1]
                result = output
                # print(result)
            if amp_i == -1:
                amps_active.remove(amp)
            else:
                amps[amp] = amp_p.copy()
                amps_i[amp] = amp_i

    return result
