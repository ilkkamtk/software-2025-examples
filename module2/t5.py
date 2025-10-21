T = float(input("Enter mass in talent:"))
P = float(input("Enter mass in pounds:"))
L = float(input("Enter mass in lots:"))
Total_pound = (T * 20) + P
Total_lots = (Total_pound * 32) + L
Total_grams = (Total_lots * 13.3)
Total_kg = Total_grams // 1000
grams = Total_grams % 1000
print(Total_kg, "kilograms", "or", Total_grams, "grams")
print(Total_kg, "kilograms", "and", grams, "grams")