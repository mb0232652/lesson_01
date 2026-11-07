from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "51","+79011011010"),
    Smartphone("Honor", "8", "+79022022020"),
    Smartphone("Honor", "10", "+79033033030"),
    Smartphone("Honor", "15", "+79044040404"),
    Smartphone("Honor", "25", "+79055055050")
]
for smartphone in catalog:
    print(f"{smartphone.smart_name} - {smartphone.modele} - {smartphone.phone_number}")
