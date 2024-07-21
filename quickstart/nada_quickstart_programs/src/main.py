from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")

    # Inputs: age and disease severity
    age = 44
    disease_severity = 1

    # Calculate base premium based on age
    base_premium = If(age <= 20, 10000,
                  If(age <= 30, 24000,
                  If(age <= 40, 30000,
                  If(age <= 50, 35000, 0))))  

    # Adjust premium based on disease severity
    adjusted_premium = If(disease_severity == 0, base_premium,
                      If(disease_severity == 1, base_premium * 1.1, base_premium * 1.3))

    return [Output(adjusted_premium, "premium_output", party1)]
