def validasi_email(teks: str) -> tuple[bool, list]:
    final_states = {"q6"}
    state = "q0"
    jejak = [state]

    for char in teks:
        if state == "q0":
            state = "q1" if char.isalnum() else "q_trap"
        elif state == "q1":
            if char.isalnum():
                state = "q1"
            elif char == "@":
                state = "q2"
            else:
                state = "q_trap"
        elif state == "q2":
            state = "q3" if char.isalnum() else "q_trap"
        elif state == "q3":
            if char.isalnum():
                state = "q3"
            elif char == ".":
                state = "q4"
            else:
                state = "q_trap"
        elif state == "q4":
            state = "q5" if char.isalpha() else "q_trap"
        elif state == "q5":
            state = "q6" if char.isalpha() else "q_trap"
        elif state == "q6":
            state = "q6" if char.isalpha() else "q_trap"

        jejak.append(state)
        if state == "q_trap":
            break

    return (state in final_states), jejak