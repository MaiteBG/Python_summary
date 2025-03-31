# Email generator (activity 36)
print("*** Email generator ***")

# Variable definition: Define the user name, company name, and domain extension.
name = " Maite Bernaus Gimeno  "
company = "Global Mento"
domain_extencion = ".es"

# Data normalization: Process the input data to standardize it.
# Normalize the user name: Remove extra spaces, replace spaces with dots, and convert to lowercase.
norm_name = name.strip().replace(" ",".").lower()

# Normalize the company name: Remove extra spaces and convert to lowercase without any spaces.
norm_company = company.strip().replace(" ","").lower()

# Create the email domain: Combine the normalized company name and the domain extension.
email_domain = f"@{norm_company}{domain_extencion}"

# Generate the final email address: Combine the normalized user name and email domain.
final_email = norm_name + email_domain

# Print results: Display the original and normalized values.
print(f"Nombre usuario: {name}")  # Original user name.
print(f"Nombre usuario normalizado: {norm_name}")  # Normalized user name.
print()  # Print a blank line for better readability.

print(f"Nombre empresa: {company}")  # Original company name.
print(f"Extensión del dominio: {domain_extencion}")  # Domain extension.
print(f"Dominio de email normalizado: {email_domain}")  # Normalized email domain.
print()  # Print a blank line for better readability.

print(f"Email final generado: {final_email}")  # Final email address.

