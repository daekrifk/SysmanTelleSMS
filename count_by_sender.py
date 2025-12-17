import os
import glob
from collections import defaultdict

def count_sms_by_email(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in: {folder_path}")
        return
    
    # Dictionary for å telle per e-post
    email_counts = defaultdict(int)
    total_sms = 0
    
    # E-postadressene vi skal telle
    target_emails = [
        "ca06@fredrikstad.kommune.no",
        "gericasms@fredrikstad.kommune.no",
        "ikkesvar@fredrikstad.kommune.no",
        "maskinsentralen@fredrikstad.kommune.no",
        "servicetorget@fredrikstad.kommune.no"
    ]
    
    print(f"\n{'='*70}")
    print(f"Analyserer mappe: {os.path.basename(folder_path)}")
    print(f"{'='*70}\n")
    
    for csv_file in csv_files:
        print(f"Leser: {os.path.basename(csv_file)}")
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Hopp over hvis ikke 2025
                if '-2025 ' not in line:
                    continue
                
                # Split linjen på semikolon
                parts = line.split(';')
                
                # Sjekk om det er en MAILtoSMS linje (kolonne 1)
                if len(parts) > 3 and parts[1] == 'MAILtoSMS':
                    email = parts[3]  # E-post er i kolonne 3
                    
                    # Tell hvis e-posten er i listen vår
                    if email in target_emails:
                        email_counts[email] += 1
                        total_sms += 1
    
    # Vis resultater
    print(f"\n{'='*70}")
    print(f"RESULTAT - SMS per e-postadresse (2025)")
    print(f"{'='*70}\n")
    
    for email in target_emails:
        count = email_counts[email]
        if count > 0:
            percentage = (count / total_sms * 100) if total_sms > 0 else 0
            print(f"{email:50} : {count:6} SMS ({percentage:5.1f}%)")
        else:
            print(f"{email:50} : {count:6} SMS")
    
    print(f"\n{'='*70}")
    print(f"TOTALT antall SMS fra disse e-postene: {total_sms}")
    print(f"{'='*70}\n")

# Kjør for ADM01 mappen
folder = r"c:\Users\daekri\Documents\Sysman\ADM01(ADM1)"
count_sms_by_email(folder)