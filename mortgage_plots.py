'''

Mortgage plots script.
This script generates plots related to mortgage data, including the distribution of interest rates and the relationship between interest rates and loan amounts and monthly payments.

'''

import matplotlib.pyplot as plt
import numpy as np

# User inputs
# Range of interest rates
i_rates = np.linspace(0.065, 0.07, 3)

house_prices = np.linspace(650000, 800000, 10)  

# Downpayment percentage
downpayment_percentage = 0.2  # Example downpayment of 20%

# Load term
term = 30  # Example term in years

# Property tax rate
property_tax_rate = 0.015  # Example property tax rate of 1%

# Home owner's insurance rate
home_owner_insurance_rate = 0.0064  # Example home owner's insurance rate of 0.5%

# Calculate the monthly payment as a function of interst rate, loan amount, downpayment, term, property tax rate, and home owner's insurance rate
def calculate_monthly_payment(interest_rate, house_price, downpayment_percentage, term, property_tax_rate, home_owner_insurance_rate):
    downpayment = house_price * downpayment_percentage
    principal = house_price - downpayment
    monthly_interest_rate = interest_rate / 12
    number_of_payments = term * 12

    # Monthly payment formula for principal and interest
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    # Add property tax and insurance
    monthly_property_tax = (house_price * property_tax_rate) / 12
    monthly_insurance = (house_price * home_owner_insurance_rate) / 12

    total_monthly_payment = monthly_payment + monthly_property_tax + monthly_insurance
    return total_monthly_payment


# Generate a plot of house prices vs monthly payments with a different curve for each interest rate
plt.figure(1, figsize=(10, 6))
plt.clf()

for interest_rate in i_rates:
    monthly_payments = [calculate_monthly_payment(interest_rate, price, downpayment_percentage, term, property_tax_rate, home_owner_insurance_rate) for price in house_prices]
    plt.plot(house_prices, monthly_payments, '-o', label=f'Interest Rate: {interest_rate:.2%}')

plt.title('House Prices vs Monthly Payments')
plt.xlabel('House Price ($)')
plt.ylabel('Monthly Payment ($)')
plt.legend()
plt.grid(True)
plt.show()

