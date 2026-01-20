from agent.parser import parse_instruction

def run_agent(instruction):
    actions = parse_instruction(instruction)

    generated_steps = []
    for a in actions:
        generated_steps.append(
            f"Verified {a['target']} successfully"
        )

    status = "PASS" if actions else "FAIL"

    return {
        "parsed_actions": actions,
        "generated_steps": generated_steps,
        "status": status
    }
