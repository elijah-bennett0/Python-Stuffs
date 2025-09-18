import re

# Open and read files
roster = open("ROSTER.prn", 'r')
emailList = open("emails.txt", 'r')

# Initialize variables
newLines = []
emails = emailList.readlines()

# Add the correct header row to the CSV output
header = ""
newLines.append(header)

# Process each line from the roster
for line in roster.readlines():
    # Skip the original header line in the ROSTER.prn file
    if line.startswith("") or line.strip() == "":
        continue
    
    # Split the line into items
    items = re.split(r'\s+', line.strip())
    
    # Ensure the line has enough fields; pad missing fields with "MISSING"
    while len(items) < 6:  # Assuming 6 fields are expected (before inserting email)
        items.append("MISSING")
    
    matched_email = None  # Initialize variable to track matching email
    
    # Iterate through each email in the email list
    for email in emails:
        email = email.strip()  # Remove any trailing whitespace or newline characters
        
        # Check if the email matches the user's first and last name
        if (email.startswith(items[2].lower())) and ((email.endswith(items[3].lower() + "")) or (email.endswith(items[3].lower() + ""))):
            matched_email = email
            break  # Exit the email loop as we've found a match for this user
    
    # Insert matched email or placeholder
    if matched_email:
        items.insert(5, matched_email)  # Email goes in position 5 (after )
    else:
        items.insert(5, "NO_MATCH")  # Insert placeholder if no email is found
    
    # Ensure all columns are present; pad missing fields with "MISSING"
    while len(items) < 7:  # Final expected number of fields after inserting email
        items.append("MISSING")
    
    # Convert the items list to a CSV row, ensuring the order matches the header
    reordered_items = [items[0], items[1], items[2], items[3], items[4], items[5], items[6]]
    newLines.append(",".join(reordered_items))

# Write updated lines to the CSV file
with open('test.csv', 'w+') as newFile:
    for line in newLines:
        newFile.write(line + '\n')  # Write each line as a CSV row

# Close the files
roster.close()
emailList.close()