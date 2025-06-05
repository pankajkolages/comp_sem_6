from datetime import datetime, timedelta

def get_symptom_input(symptom):
    response = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
    if response == "yes":
        days = int(input(f"How many days have you had {symptom}? "))
        return True, days
    return False, 0

def diagnose(symptoms):
    # Basic Rule-Based Conditions
    if symptoms['fever'][0] and symptoms['runny_nose'][0] and symptoms['sore_throat'][0]:
        return "Common Cold", ["Rest", "Paracetamol", "Stay Hydrated"], ["No test needed"]
    elif symptoms['fever'][0] and symptoms['chills'][0] and symptoms['sweating'][0] and symptoms['headache'][0]:
        return "Malaria", ["Consult doctor", "Antimalarial medication"], ["Blood Test (Malaria Parasite)", "CBC"]
    elif symptoms['vomiting'][0] and symptoms['diarrhea'][0] and symptoms['stomach_pain'][0]:
        return "Food Poisoning", ["ORS", "Antiemetic", "Avoid solid food"], ["Stool Test", "Electrolyte Test"]
    else:
        return "Unknown Condition", ["Visit general physician"], ["Basic Blood Test", "Urine Test"]

def schedule_next_appointment():
    today = datetime.today()
    next_date = today + timedelta(days=3)
    return next_date.strftime("%d-%m-%Y")

def main():
    print("---- Medical Expert System ----\n")
    symptom_list = [
        "fever", "runny_nose", "sore_throat",
        "chills", "sweating", "headache",
        "vomiting", "diarrhea", "stomach_pain"
    ]

    symptoms = {}
    for symptom in symptom_list:
        has_symptom, days = get_symptom_input(symptom.replace("_", " "))
        symptoms[symptom] = (has_symptom, days)

    condition, recommendations, tests = diagnose(symptoms)
    
    print("\n-----------------------------")
    print(f"Diagnosis: {condition}")
    print("Recommendations:")
    for item in recommendations:
        print(f"- {item}")

    print("\nRecommended Medical Tests:")
    for test in tests:
        print(f"- {test}")

    appointment_date = schedule_next_appointment()
    print(f"\nNext Appointment Scheduled On: {appointment_date}")
    print("-----------------------------")

if __name__ == "__main__":
    main()
