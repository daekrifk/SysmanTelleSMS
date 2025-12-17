import os
import glob
from datetime import datetime

def process_csv_files(folder_path):
    # Finner alle CSV filene i mappen
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in: {folder_path}")
        return
    
    total_sms_2025 = 0
    
    print(f"\nProcessing folder: {os.path.basename(folder_path)}")
    print(f"Found {len(csv_files)} CSV file(s)\n")
    
    for csv_file in csv_files:
        print(f"Processing: {os.path.basename(csv_file)}")
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Filtrerer linjener for < 2025
        lines_2025 = [line for line in lines if '-2025 ' in line]
        
        sms_count = len(lines_2025)
        total_sms_2025 += sms_count
        
        print(f"  SMS in 2025: {sms_count}")
        
        # Fjerner alle linjer som ikke har dato 2025
        with open(csv_file, 'w', encoding='utf-8') as f:
            f.writelines(lines_2025)
    
    print(f"\n{'='*50}")
    print(f"TOTAL SMS in {os.path.basename(folder_path)} (Jan 1 - Dec 11, 2025): {total_sms_2025}")
    print(f"{'='*50}")

# mappe den skal lese csv filer fra, - husk å endre mappe hvis du henter inn mapper fra flere løsninger.
folder = r"c:\Users\daekri\Documents\Sysman\ADM01(ADM1)"
process_csv_files(folder)


#Hvis du vil rydde og telle flere mapper samtidig bruk denne i stedet. 
#folders = [
#    r"c:\Users\daekri\Documents\Sysman\mappe1",
#    r"c:\Users\daekri\Documents\Sysman\mappe2",
#    r"c:\Users\daekri\Documents\Sysman\mappe3",
#    r"c:\Users\daekri\Documents\Sysman\mappe4"
#]
#
#for folder in folders:
#    process_csv_files(folder)
#