#################### IMPORT PUSTAKA ####################
# import pustaka tkinter untuk membuat gui
import tkinter as tk
import tkinter.ttk as ttk



################### PENDAFTARAN ITEM ###################
### Kode oleh Raditya

# daftar item yang tersedia
a = {'nama' : 'Aqua', 'harga' : 5000, 'stok' : 4, 'jmlbeli': 0}
b = {'nama' : 'Mizone', 'harga' : 10000, 'stok' : 6, 'jmlbeli': 0}
c = {'nama' : 'Pocari', 'harga' : 10000, 'stok' : 2, 'jmlbeli': 0}
d = {'nama' : 'Tebs', 'harga' : 15000, 'stok' : 3, 'jmlbeli': 0}
e = {'nama' : 'Minute Maid', 'harga' : 10000, 'stok' : 3, 'jmlbeli': 0}
f = {'nama' : 'Kopiko 78C', 'harga' : 10000, 'stok' : 8, 'jmlbeli': 0}
g = {'nama' : 'Coca Cola', 'harga' : 10000, 'stok' : 9, 'jmlbeli': 0}
h = {'nama' : 'Vit', 'harga' : 5000, 'stok' : 5, 'jmlbeli': 0}
# masih bisa ditambah lagi, nama perlu diganti, harga juga, stok juga

items = [a, b, c, d, e, f, g, h] # masih bisa ditambah lagi




#################### VARIABEL GLOBAL ###################
saldo = 0
logbelanja = ""
totalbelanja = 0




##################### WINDOW UTAMA #####################
### Kode oleh Andika N.
class VendingMachine:
    ### Inisiasi
    def __init__(self, master=None):
        ### Pembentukan Window Utama
        master.title("Vending Machine - Tugas Besar")
        master.geometry("600x500")
        master.minsize(600, 500)
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        ### Pembentukan Frame Utama untuk membingkai semua komponen
        self.mainFrame = ttk.Frame(master)
        self.mainFrame.grid(sticky="nsew", padx=12, pady=12)
        self.mainFrame.grid_rowconfigure(0, weight=0)
        self.mainFrame.grid_rowconfigure(1, weight=0)
        self.mainFrame.grid_rowconfigure(2, weight=0)
        self.mainFrame.grid_rowconfigure(3, weight=0)
        self.mainFrame.grid_rowconfigure(4, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=0)

        ### Label judul untuk Vending Machine
        self.vendingTitle = ttk.Label(self.mainFrame)
        self.vendingTitle.config(
            text="Vending Machine",
            font="{Segoe UI Light} 20 {}"
        )
        self.vendingTitle.grid(row=0, column=0, columnspan=2, sticky='n')
        self.vendingTitle.rowconfigure('0', pad=3)
        self.vendingTitle.columnconfigure('0', pad=3)

        #=================== CONTAINER GRID ITEM DISPLAY =====================
        self.itemsGrid = ttk.Labelframe(self.mainFrame)
        self.itemsGrid.config(
            text="Items",
            labelanchor="n"
        )
        self.itemsGrid.rowconfigure('1', pad='10')
        self.itemsGrid.columnconfigure('0', pad='10')
        self.itemsGrid.grid(row=1, column=0, rowspan=4, padx=6, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.itemsGrid.grid_columnconfigure((0,1,2,3), weight=1)

        ### BARIS PERTAMA PADA CONTAINER ITEM
        ### Item dengan index 0
        
        # penempatan item0
        self.item0frame = ttk.Frame(self.itemsGrid)
        self.item0frame.grid(row=0, column=0, padx=3)

        # konten item0 dengan tombol Beli
        self.item0nama = tk.StringVar()
        self.item0nama.set(items[0]['nama'])

        self.item0harga = tk.StringVar()
        self.item0harga.set(items[0]['harga'])

        self.item0stok = tk.StringVar()
        self.item0stok.set(f"Stok: {items[0]['stok']}")

        self.item0namalabel = ttk.Label(self.item0frame)
        self.item0namalabel.config(textvariable=self.item0nama)
        self.item0namalabel.pack()

        self.item0hargalabel = ttk.Label(self.item0frame)
        self.item0hargalabel.config(textvariable=self.item0harga)
        self.item0hargalabel.pack()

        self.item0stoklabel = ttk.Label(self.item0frame)
        self.item0stoklabel.config(textvariable=self.item0stok)
        self.item0stoklabel.pack()

        self.item0Button = ttk.Button(self.item0frame)
        self.item0Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[0], self.displaySaldo, self.item0stok),
            state=tk.DISABLED
        )
        self.item0Button.pack()

        ### Item dengan index 1

        # penempatan item1
        self.item1frame = ttk.Frame(self.itemsGrid)
        self.item1frame.grid(row=0, column=1, padx=3)

        # konten item1 dengan tombol Beli
        self.item1nama = tk.StringVar()
        self.item1nama.set(items[1]['nama'])

        self.item1harga = tk.StringVar()
        self.item1harga.set(items[1]['harga'])

        self.item1stok = tk.StringVar()
        self.item1stok.set(f"Stok: {items[1]['stok']}")

        self.item1namalabel = ttk.Label(self.item1frame)
        self.item1namalabel.config(textvariable=self.item1nama)
        self.item1namalabel.pack()

        self.item1hargalabel = ttk.Label(self.item1frame)
        self.item1hargalabel.config(textvariable=self.item1harga)
        self.item1hargalabel.pack()

        self.item1stoklabel = ttk.Label(self.item1frame)
        self.item1stoklabel.config(textvariable=self.item1stok)
        self.item1stoklabel.pack()

        self.item1Button = ttk.Button(self.item1frame)
        self.item1Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[1], self.displaySaldo, self.item1stok),
            state=tk.DISABLED
        )
        self.item1Button.pack()

        ### Item dengan index 2

        # penempatan item2
        self.item2frame = ttk.Frame(self.itemsGrid)
        self.item2frame.grid(row=0, column=2, padx=3)

        # konten item2 dengan tombol Beli
        self.item2nama = tk.StringVar()
        self.item2nama.set(items[2]['nama'])

        self.item2harga = tk.StringVar()
        self.item2harga.set(items[2]['harga'])

        self.item2stok = tk.StringVar()
        self.item2stok.set(f"Stok: {items[2]['stok']}")

        self.item2namalabel = ttk.Label(self.item2frame)
        self.item2namalabel.config(textvariable=self.item2nama)
        self.item2namalabel.pack()

        self.item2hargalabel = ttk.Label(self.item2frame)
        self.item2hargalabel.config(textvariable=self.item2harga)
        self.item2hargalabel.pack()

        self.item2stoklabel = ttk.Label(self.item2frame)
        self.item2stoklabel.config(textvariable=self.item2stok)
        self.item2stoklabel.pack()

        self.item2Button = ttk.Button(self.item2frame)
        self.item2Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[2], self.displaySaldo, self.item2stok),
            state=tk.DISABLED
        )
        self.item2Button.pack()

        ### Item dengan index 3

        # penempatan item3
        self.item3frame = ttk.Frame(self.itemsGrid)
        self.item3frame.grid(row=0, column=3, padx=3)

        # konten item3 dengan tombol Beli
        self.item3nama = tk.StringVar()
        self.item3nama.set(items[3]['nama'])

        self.item3harga = tk.StringVar()
        self.item3harga.set(items[3]['harga'])

        self.item3stok = tk.StringVar()
        self.item3stok.set(f"Stok: {items[3]['stok']}")

        self.item3namalabel = ttk.Label(self.item3frame)
        self.item3namalabel.config(textvariable=self.item3nama)
        self.item3namalabel.pack()

        self.item3hargalabel = ttk.Label(self.item3frame)
        self.item3hargalabel.config(textvariable=self.item3harga)
        self.item3hargalabel.pack()

        self.item3stoklabel = ttk.Label(self.item3frame)
        self.item3stoklabel.config(textvariable=self.item3stok)
        self.item3stoklabel.pack()

        self.item3Button = ttk.Button(self.item3frame)
        self.item3Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[3], self.displaySaldo, self.item3stok),
            state=tk.DISABLED
        )
        self.item3Button.pack()

        ### BARIS KEDUA PADA CONTAINER ITEM
        ### Item dengan index 4
        
        # penempatan item4
        self.item4frame = ttk.Frame(self.itemsGrid)
        self.item4frame.grid(row=1, column=0, padx=3)

        # konten item4 dengan tombol Beli
        self.item4nama = tk.StringVar()
        self.item4nama.set(items[4]['nama'])

        self.item4harga = tk.StringVar()
        self.item4harga.set(items[4]['harga'])

        self.item4stok = tk.StringVar()
        self.item4stok.set(f"Stok: {items[4]['stok']}")

        self.item4namalabel = ttk.Label(self.item4frame)
        self.item4namalabel.config(textvariable=self.item4nama)
        self.item4namalabel.pack()

        self.item4hargalabel = ttk.Label(self.item4frame)
        self.item4hargalabel.config(textvariable=self.item4harga)
        self.item4hargalabel.pack()

        self.item4stoklabel = ttk.Label(self.item4frame)
        self.item4stoklabel.config(textvariable=self.item4stok)
        self.item4stoklabel.pack()

        self.item4Button = ttk.Button(self.item4frame)
        self.item4Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[4], self.displaySaldo, self.item4stok),
            state=tk.DISABLED
        )
        self.item4Button.pack()

        ### Item dengan index 5
        
        # penempatan item5
        self.item5frame = ttk.Frame(self.itemsGrid)
        self.item5frame.grid(row=1, column=1, padx=3)

        # konten item5 dengan tombol Beli
        self.item5nama = tk.StringVar()
        self.item5nama.set(items[5]['nama'])

        self.item5harga = tk.StringVar()
        self.item5harga.set(items[5]['harga'])

        self.item5stok = tk.StringVar()
        self.item5stok.set(f"Stok: {items[5]['stok']}")

        self.item5namalabel = ttk.Label(self.item5frame)
        self.item5namalabel.config(textvariable=self.item5nama)
        self.item5namalabel.pack()

        self.item5hargalabel = ttk.Label(self.item5frame)
        self.item5hargalabel.config(textvariable=self.item5harga)
        self.item5hargalabel.pack()

        self.item5stoklabel = ttk.Label(self.item5frame)
        self.item5stoklabel.config(textvariable=self.item5stok)
        self.item5stoklabel.pack()

        self.item5Button = ttk.Button(self.item5frame)
        self.item5Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[5], self.displaySaldo, self.item5stok),
            state=tk.DISABLED
        )
        self.item5Button.pack()

        ### Item dengan index 6
        
        # penempatan item0
        self.item6frame = ttk.Frame(self.itemsGrid)
        self.item6frame.grid(row=1, column=2, padx=3)

        # konten item6 dengan tombol Beli
        self.item6nama = tk.StringVar()
        self.item6nama.set(items[6]['nama'])

        self.item6harga = tk.StringVar()
        self.item6harga.set(items[6]['harga'])

        self.item6stok = tk.StringVar()
        self.item6stok.set(f"Stok: {items[6]['stok']}")

        self.item6namalabel = ttk.Label(self.item6frame)
        self.item6namalabel.config(textvariable=self.item6nama)
        self.item6namalabel.pack()

        self.item6hargalabel = ttk.Label(self.item6frame)
        self.item6hargalabel.config(textvariable=self.item6harga)
        self.item6hargalabel.pack()

        self.item6stoklabel = ttk.Label(self.item6frame)
        self.item6stoklabel.config(textvariable=self.item6stok)
        self.item6stoklabel.pack()

        self.item6Button = ttk.Button(self.item6frame)
        self.item6Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[6], self.displaySaldo, self.item6stok),
            state=tk.DISABLED
        )
        self.item6Button.pack()

        ### Item dengan index 7
        
        # penempatan item7
        self.item7frame = ttk.Frame(self.itemsGrid)
        self.item7frame.grid(row=1, column=3, padx=3)

        # konten item7 dengan tombol Beli
        self.item7nama = tk.StringVar()
        self.item7nama.set(items[7]['nama'])

        self.item7harga = tk.StringVar()
        self.item7harga.set(items[7]['harga'])

        self.item7stok = tk.StringVar()
        self.item7stok.set(f"Stok: {items[7]['stok']}")

        self.item7namalabel = ttk.Label(self.item7frame)
        self.item7namalabel.config(textvariable=self.item7nama)
        self.item7namalabel.pack()

        self.item7hargalabel = ttk.Label(self.item7frame)
        self.item7hargalabel.config(textvariable=self.item7harga)
        self.item7hargalabel.pack()

        self.item7stoklabel = ttk.Label(self.item7frame)
        self.item7stoklabel.config(textvariable=self.item7stok)
        self.item7stoklabel.pack()

        self.item7Button = ttk.Button(self.item7frame)
        self.item7Button.config(
            text="Beli",
            command=lambda: self.beliBarang(items[7], self.displaySaldo, self.item7stok),
            state=tk.DISABLED
        )
        self.item7Button.pack()
        
        #################################################
        # Notes: untuk item selanjutnya bisa dibuat     #
        # baris lagi, namun diperlukan penambahan dict  #
        # item di bagian awal kode                      #
        #################################################

        # Dibuat sebuah array/list berisi tombol yang ada untuk
        # memudahkan pemanggilan prosedur self.cekSaldo()
        self.itembuttons = [
            self.item0Button,
            self.item1Button,
            self.item2Button,
            self.item3Button,
            self.item4Button,
            self.item5Button,
            self.item6Button,
            self.item7Button
            ]

        #=================== CONTAINER GRID DISPLAY SALDO =====================
        self.saldoGrid = ttk.Labelframe(self.mainFrame)
        self.saldoGrid.config(
            text="Saldo Anda",
            labelanchor="n"
        )
        self.saldoGrid.rowconfigure('1', pad=10, weight='1')
        self.saldoGrid.columnconfigure('1', pad=10, weight='1')
        self.saldoGrid.grid(row=1, column=1, padx=6, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        ### LABEL UNTUK MENAMPILKAN SALDO
        self.displaySaldo = tk.StringVar()
        self.displaySaldo.set(f"Rp{saldo:,}")
        self.saldoLabel = ttk.Label(self.saldoGrid)
        self.saldoLabel.config(
            textvariable=self.displaySaldo,
            font="{Segoe UI Light} 20 {}"
        )
        self.saldoLabel.pack(anchor=tk.E)

        #=================== CONTAINER GRID MEMASUKKAN UANG =====================
        self.insertCashGrid = ttk.Labelframe(self.mainFrame)
        self.insertCashGrid.config(
            text="Masukkan Uang",
            labelanchor="n",
        )
        self.insertCashGrid.grid(row=2, column=1, ipadx=6, padx=6, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.insertCashGrid.grid_rowconfigure(0, weight=1)
        self.insertCashGrid.grid_rowconfigure(1, weight=1)
        self.insertCashGrid.grid_columnconfigure(0, weight=1)
        self.insertCashGrid.grid_columnconfigure(1, weight=1)

        ### TOMBOL TAMBAHKAN 5000
        self.add5kButton = ttk.Button(self.insertCashGrid)
        self.add5kButton.config(text="5.000", command=lambda: self.tambahSaldo(5000, self.displaySaldo))
        self.add5kButton.grid(row=0, column=0, padx=3, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        ### TOMBOL TAMBAHKAN 10000
        self.add10kButton = ttk.Button(self.insertCashGrid)
        self.add10kButton.config(text="10.000", command=lambda: self.tambahSaldo(10000, self.displaySaldo))
        self.add10kButton.grid(row=1, column=0, padx=3, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        ### TOMBOL TAMBAHKAN 20000
        self.add20kButton = ttk.Button(self.insertCashGrid)
        self.add20kButton.config(text="20.000", command=lambda: self.tambahSaldo(20000, self.displaySaldo))
        self.add20kButton.grid(row=0, column=1, padx=3, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        ### TOMBOL TAMBAHKAN 50000
        self.add50kButton = ttk.Button(self.insertCashGrid)
        self.add50kButton.config(text="50.000", command=lambda: self.tambahSaldo(50000, self.displaySaldo))
        self.add50kButton.grid(row=1, column=1, padx=3, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        #=================== CONTAINER TOMBOL SELESAI BELANJA =====================
        self.finishButton = ttk.Button(self.mainFrame)
        self.finishButton.config(
            text="Selesai Belanja",
            command=self.selesaiBelanja
        )
        self.finishButton.grid(row=3, column=1, ipadx=6, padx=6, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        #=================== CONTAINER GRID TEXT OUTPUT =====================
        self.outputGrid = ttk.Labelframe(self.mainFrame)
        self.outputGrid.config(
            text="Output",
            labelanchor="n",
        )
        self.outputGrid.grid(row=4, column=1, ipadx=6, padx=6, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))
        # membuat konten di dalam grid output lebih fleksibel
        self.outputGrid.grid_columnconfigure(0, weight=1)
        self.outputGrid.grid_rowconfigure(0, weight=1)

        ### WIDGET TEXT OUTPUT
        self.outputTxt = tk.Text(self.outputGrid)
        self.outputTxt.config(font=("consolas", 12), undo=True, wrap='word')
        self.outputTxt.config(borderwidth=3, relief="sunken", width=20)
        self.outputTxt.grid(row=0, column=0, ipadx=6, padx=6, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))

        #=================== SETTING SEBAGAI FRAME UTAMA =====================
        self.master = self.mainFrame
    

    ### Fungsi dan Prosedur dalam Class VendingMachine
    # Prosedur menambah saldo
    def tambahSaldo(self, cash: int, displaysaldo: tk.StringVar):
        # akses variabel global
        global saldo

        # menambahkan saldo dan update display saldo
        saldo += cash
        displaysaldo.set(f"Rp{saldo:,}")

        # menjalankan prosedur self.cekSaldo()
        self.cekSaldo()

    # Prosedur membeli barang
    def beliBarang(self, barang: dict, displaysaldo: tk.StringVar, displaystok: tk.StringVar):
        # akses variabel global
        global saldo, logbelanja, totalbelanja

        # mengurangi stok barang dan menambahkan jumlah belanja barang
        barang["stok"] -= 1
        sisa = barang["stok"]
        barang["jmlbeli"] += 1

        # mengurangkan saldo dengan harga serta mengupdate display saldo dan stok
        saldo -= barang["harga"]
        totalbelanja += barang["harga"]
        displaysaldo.set(f"Rp{saldo:,}")
        displaystok.set(f"Stok: {sisa}")
        
        # mengupdate display output dan menghasilkan output
        self.outputTxt.delete("1.0", tk.END)
        self.outputTxt.insert(tk.INSERT, "Anda berhasil membeli {} seharga Rp{:,}.\n".format(barang["nama"], barang["harga"]))
        self.outputTxt.insert(tk.END, "\nSaldo Anda tersisa sebanyak Rp{:,}.".format(saldo))

        # menjalankan prosedur self.cekSaldo()
        self.cekSaldo()

    # Prosedur mengecek saldo
    def cekSaldo(self):
        # akses variabel global
        global saldo, items

        # membuat looping untuk semua item untuk mengecek apakah item sudah bisa dibeli
        for i in range(len(items)):
            # jika stok habis atau saldo tidak cukup maka item tidak bisa dibeli
            if saldo < items[i]['harga'] or items[i].get("stok") == 0:
                self.itembuttons[i].config(state=tk.DISABLED)
            else:
                self.itembuttons[i].config(state=tk.NORMAL)

    # Prosedur mengakhiri proses belanja di vending machine
    def selesaiBelanja(self):
        # akses ke variabel global terlebih dahulu
        global saldo, logbelanja, totalbelanja, items

        # menuliskan riwayat belanja dengan jumlah barang
        for item in items:
            if item['jmlbeli']>0:
                logbelanja = logbelanja + "{} buah {} @ Rp.{:,}\n".format(item['jmlbeli'], item['nama'], item['harga'])

        # membuka form selesai belanja
        formSelesai()

        # mengosongkan jumlah pembelian
        for item in items:
            item['jmlbeli']=0

        # reset semua settingan dan kembali ke awal
        self.outputTxt.delete("1.0", tk.END)
        saldo=0
        totalbelanja=0
        logbelanja=""
        self.displaySaldo.set(f"Rp{saldo:,}")

        # menjalankan prosedur cek saldo yang akan menonaktifkan semua tombol
        # di item vending machine karena saldo sudah nol
        self.cekSaldo()

    # Prosedur memulai dan menjalankan vending machine
    def run(self):
        self.master.mainloop()




############## WINDOW POP-UP SELESAI BELANJA ##############
### Kode oleh Akmal Arifin
class formSelesai:
    ### Inisiasi
    def __init__(self, master=None):
        ### setting sebagai window baru
        self.rootSelesai = tk.Toplevel(master)

        # buat fokusin ke window popup
        self.rootSelesai.focus_force()

        # buat disable main window
        self.rootSelesai.grab_set()

        self.rootSelesai.title("Hasil Belanja")
        self.rootSelesai.geometry("400x400")
        self.rootSelesai.resizable(width=False, height=False)
        self.rootSelesai.grid_rowconfigure(0, weight=1)
        self.rootSelesai.grid_columnconfigure(0, weight=1)

        # konfigurasi grid di dalamnya
        self.selesaiFrame = ttk.Frame(self.rootSelesai)
        self.selesaiFrame.grid(sticky="nsew", padx=12, pady=12)
        self.selesaiFrame.grid_rowconfigure(0, minsize=50)
        self.selesaiFrame.grid_rowconfigure(1, weight=8)
        self.selesaiFrame.grid_rowconfigure(2, weight=0)
        self.selesaiFrame.grid_columnconfigure(0, weight=1)

        ### GRID UNTUK LABEL HASIL BELANJA
        self.selesaiTitle = ttk.Label(self.selesaiFrame)
        self.selesaiTitle.config(
            text="Hasil Belanja",
            font="{Segoe UI Light} 20 {}"
        )
        self.selesaiTitle.grid(row=0, column=0, columnspan=2, sticky='n')
        self.selesaiTitle.rowconfigure('0', pad=3)
        self.selesaiTitle.columnconfigure('0', pad=3)

        ### GRID UNTUK MENAMPILKAN OUTPUT RIWAYAT BELANJA
        self.logtext = tk.Text(self.selesaiFrame)
        self.logtext.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.logtext.config(font=("consolas", 12), undo=True, wrap='word')
        self.logtext.config(borderwidth=3, relief="sunken")
        self.logtext.insert(tk.INSERT, f"Anda berbelanja dengan total Rp{totalbelanja:,}.\n")
        self.logtext.insert(tk.END, f"Kembalian yang Anda dapatkan adalah Rp{saldo:,}.\n")
        self.logtext.insert(tk.END, f"\nAnda telah membeli:\n{logbelanja}")

        ### SETTING SCROLLBAR UNTUK SCROLLING VERTIKAL
        self.scrollbar = tk.Scrollbar(self.selesaiFrame, command=self.logtext.yview)
        self.scrollbar.grid(row=1, column=1, sticky='nsew')
        self.logtext['yscrollcommand'] = self.scrollbar.set

        ### TOMBOL OK UNTUK MENUTUP FORM
        self.okbutton = ttk.Button(self.selesaiFrame)
        self.okbutton.config(text="Selesai", command=self.rootSelesai.destroy)
        self.okbutton.grid(row=2, column=0, columnspan=2, padx=3, pady=6, sticky=(tk.N, tk.W, tk.E, tk.S))




#################### EKSEKUSI KODE UTAMA ####################
root = tk.Tk()
app = VendingMachine(root)
app.run()