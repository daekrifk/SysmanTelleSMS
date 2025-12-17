# SysmanTelleSMS
-------COUNT_SMS.PY-------
SMS Counter Script
Dette scriptet teller og filtrerer SMS-meldinger fra CSV-filer basert på dato.

Viktig å endre før bruk
📅 Oppdater dato
Endre datofilteret i koden for hver måned:

📁 Mappestruktur
Sikre at CSV-filene ligger i riktig mappe som definert i koden:

Funksjonalitet
Leser alle CSV-filer i den spesifiserte mappen
Filtrerer SMS-meldinger basert på dato
Teller totalt antall SMS
VIKTIG: Overskriver originalfilene med kun filtrerte data
Bruk
Flere mapper
Kommenter ut enkeltmappe-koden og bruk flermappe-seksjonen nederst i filen for å prosessere flere mapper samtidig.

⚠️ Advarsel
Scriptet endrer originalfilene permanent. Ta backup før kjøring!

-------COUNT_BY_SENDER.PY-------

SMS Counter by Sender
Dette scriptet analyserer SMS-trafikk fra spesifikke e-postadresser i CSV-filer.

Funksjonalitet
Leser CSV-filer og filtrerer kun MAILtoSMS-trafikk fra 2025
Teller SMS per spesifikk e-postadresse
Viser prosentfordeling av SMS-bruk
Kun read-only - endrer ikke originalfilene
Viktig å endre før bruk
📅 Oppdater datofilter
Endre datofilteret for hver måned/år

📁 Mappestruktur
Sikre riktig mappebane

📧 E-postadresser som overvåkes
Scriptet teller SMS fra disse adressene:

ca06@fredrikstad.kommune.no
gericasms@fredrikstad.kommune.no
ikkesvar@fredrikstad.kommune.no
maskinsentralen@fredrikstad.kommune.no
servicetorget@fredrikstad.kommune.no
Output
Viser:

Antall SMS per e-postadresse
Prosentandel av total trafikk
Total SMS-count fra alle overvåkede adresser
