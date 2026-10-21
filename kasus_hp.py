def validasi_nomor_hp(teks: str) -> tuple[bool, list]:
    final_states = {"q10", "q11", "q12", "q13"}
    state = "q0"
    jejak = [state]

    for char in teks:
        if state == "q0":
            state = "q1" if char == "0" else "q_trap"
        elif state == "q1":
            state = "q2" if char == "8" else "q_trap"
        elif state in {f"q{i}" for i in range(2, 13)}:
            if char.isdigit():
                current_num = int(state[1:])
                state = f"q{current_num + 1}"
            else:
                state = "q_trap"
        elif state == "q13":
            state = "q_trap"

        jejak.append(state)
        if state == "q_trap":
            break

    return (state in final_states), jejak