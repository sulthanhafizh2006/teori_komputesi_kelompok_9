def validasi_nama_variabel(teks: str) -> tuple[bool, list]:
    final_states = {"q1"}
    state = "q0"
    jejak = [state]

    if not teks:
        state = "q_trap"
        jejak.append(state)

    for char in teks:
        if state == "q0":
            state = "q1" if (char.isalpha() or char == "_") else "q_trap"
        elif state == "q1":
            state = "q1" if (char.isalnum() or char == "_") else "q_trap"
        
        jejak.append(state)
        if state == "q_trap":
            break

    return (state in final_states), jejak