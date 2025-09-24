def detect_spikes(twins):
    results = []
    for twin in twins.values():
        if twin["spike"] == "Yes":
            results.append(f"[SPIKE] {twin['device']} (Delay: {twin['delay']}s)")
        else:
            results.append(f"[OK] {twin['device']} (Delay: {twin['delay']}s)")
    return results