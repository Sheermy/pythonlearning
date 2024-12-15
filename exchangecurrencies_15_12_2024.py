import tkinter as tk
from tkinter import messagebox
import requests


def pobierz_kursy(waluta_poczatkowa):
    waluta_poczatkowa = entry_waluta_poczatkowa.get().upper()
    url = f"https://api.exchangerate-api.com/v4/latest/{waluta_poczatkowa}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json() 
        return data['rates']  
    else:
        messagebox.showerror("Błąd", "Nie udało się pobrać danych z API.")
        return None

def przelicz_walute():
    try:
        kwota = float(entry_kwota.get())
        waluta_poczatkowa = entry_waluta_poczatkowa.get().upper()
        waluta_docelowa = entry_waluta_docelowa.get().upper()
        kursy = pobierz_kursy(waluta_poczatkowa)
        if kursy and waluta_docelowa in kursy:
                kurs = kursy[waluta_docelowa] 
                wynik = kwota * kurs
                label_wynik.config(text=f"{kwota} {waluta_poczatkowa} = {wynik:.2f} {waluta_docelowa}")
        else:
            messagebox.showerror("Błąd", "Niepoprawna waluta docelowa!")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawną kwotę")

okno = tk.Tk()
okno.title("Przelicznik Walut")

okno.configure(bg="#0E0D0D")

tk.Label(okno, bg="#0E0D0D", fg="#ffffff", text="Kwota:").grid(row=0, column=0, padx=10, pady=5)
entry_kwota = tk.Entry(okno, bg="#191919", fg="#ffffff")
entry_kwota.grid(row=0, column=1, padx=10, pady=5)

tk.Label(okno, bg="#0E0D0D", fg="#ffffff", text="Waluta początkowa (np. USD):").grid(row=1, column=0, padx=10, pady=5)
entry_waluta_poczatkowa = tk.Entry(okno, bg="#191919", fg="#ffffff")
entry_waluta_poczatkowa.grid(row=1, column=1, padx=10, pady=5)

tk.Label(okno, bg="#0E0D0D", fg="#ffffff", text="Waluta docelowa (np. EUR):").grid(row=2, column=0, padx=10, pady=5)
entry_waluta_docelowa = tk.Entry(okno, bg="#191919", fg="#ffffff")
entry_waluta_docelowa.grid(row=2, column=1, padx=10, pady=5)


button_przelicz = tk.Button(okno, bg="#191919", fg="#ffffff", text="Przelicz", command=przelicz_walute)
button_przelicz.grid(row=3, column=0, columnspan=2, pady=10)


label_wynik = tk.Label(okno, bg="#0E0D0D", fg="#ffffff", text="", font=("", 14))
label_wynik.grid(row=4, column=0, columnspan=2, pady=10)

okno.mainloop()