# Impor tkinter
import tkinter as tk

# Membuat objek utama untuk GUI
button = tk.Tk()

# Mengatur judul halaman web
button.title("Ratna Nur Maulidya - Latihan Button")

# Membuat label
label = tk.Label(button, text="Masukkan Nama:")
label.pack()

# Membuat entry (input text)
entry = tk.Entry(button)
entry.pack()

# Fungsi yang akan dijalankan saat tombol ditekan
def on_button_click():
    nama = entry.get()
    label.config(text=f"Nama Anda: {nama}")

# Membuat tombol
button = tk.Button(button, text="Klik", command=on_button_click)
button.pack()

# Menjalankan GUI
button.mainloop()