import requests
from datetime import datetime

def run_program():
    id_invoice = input("Masukkan ID Invoice: ")
    url = 'https://afvr.my.id/api/cek_status'
    data = {'id_invoice': id_invoice}

    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=data)

    result = response.json()

    if 'error' in result:
        print(result['error'])
    else:
        invoices = result['id_invoice']
        for invoice in invoices:
            print("===============================")
            print("ID Invoice      : ", invoice['id_invoice'])
            transaksi_tanggal = datetime.strptime(invoice['transaksi_tanggal'], '%Y-%m-%d %H:%M:%S')
            print("Tanggal         : ", datetime.strftime(transaksi_tanggal, '%d %B %Y'))
            print("Jasa dipilih    : ", invoice['nama_produk'])
            print("Nama Pelanggan  : ", invoice['nama_konsumen'])
            print("Status          : ", invoice['status_transaksi'])
        print("===============================")

    command = input("Ketik 'jalankan' untuk menjalankan program atau 'berhenti' untuk berhenti (tekan enter jika sudah menuliskan perintah): ")
    if command == "jalankan":
        run_program()
    elif command == "berhenti":
        print("Program dihentikan.")
    else:
        print("Perintah tidak dikenali. Program dihentikan.")

if __name__ == '__main__':
    run_program()
