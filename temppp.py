import pandas as pd

# Path to the input Excel file
input_excel_file = 'data/attendance.xlsx'

data = pd.read_excel(input_excel_file)

# Filter rows where the student name matches the given name
filtered_data = data[data['NAME'] == "22CS168"]

# Path to the output Excel file where the filtered data will be saved
output_excel_file = 'filtered_output.xlsx'

# Save the filtered data to a new Excel file
filtered_data.to_excel(output_excel_file, index=False)
