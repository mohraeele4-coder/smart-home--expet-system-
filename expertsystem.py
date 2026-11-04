# expert_system.py

def evaluate_home_state(facts):
    decisions = []
    
    # قاعدة 1: الحرارة عالية
    if facts.get("temperature") >= 30:
        decisions.append({
            "rule": "Rule 1: IF Temperature >= 30°C",
            "action": "Turn ON AC",
            "reason": "Temperature is too hot. AC is needed for comfort."
        })

    # قاعدة 2: الحرارة منخفضة
    elif facts.get("temperature") <= 18:
        decisions.append({
            "rule": "Rule 2: IF Temperature <= 18°C",
            "action": "Turn ON Heater",
            "reason": "Temperature is too cold. Heater is needed for comfort."
        })
    else:
        decisions.append({
            "rule": "Rule 3: IF 18°C < Temperature < 30°C",
            "action": "No heating/cooling needed",
            "reason": "Temperature is moderate."
        })

    # قاعدة 4: الأمان - الغاز
    if facts.get("gas_leak"):
        decisions.append({
            "rule": "Rule 4: IF Gas Leak == True",
            "action": "Send WhatsApp Alert & Close Valve",
            "reason": "Safety First. Gas leak detected."
        })

    # قاعدة 5: الأمان - الحريق
    if facts.get("fire"):
        decisions.append({
            "rule": "Rule 5: IF Fire == True",
            "action": "Call Fire Dept & Evacuate",
            "reason": "Safety First. Fire detected."
        })

    return decisions