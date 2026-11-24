# Hospital Billing and Patient Classification
patient_name = "Robert Smith"
age = 65
consultation = 150.0
diagnostic = 300.0
treatment = 1200.0

subtotal = consultation + diagnostic + treatment
discount = 0.15 if age >= 60 else 0.0
total_bill = subtotal * (1 - discount)

classification = (
    "Senior Concession Tier" if age >= 60 else "Standard General Tier"
)

print(f"Patient: {patient_name} (Age: {age})")
print(f"Classification: {classification}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount Applied: {discount*100}%")
print(f"Final Payable Amount: ${total_bill:.2f}")