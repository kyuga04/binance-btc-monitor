import ccxt
import time
from datetime import datetime

# Inisialisasi Bursa (Binance)
exchange = ccxt.binance()
SYMBOL = 'BTC/USDT'

def monitor_harga():
    print(f"--- Memulai Pemantauan Real-time {SYMBOL} di Binance ---")
    print("Tekan Ctrl+C untuk berhenti.\n")
    
    harga_sebelumnya = None

    while True:
        try:
            # Ambil data ticker
            ticker = exchange.fetch_ticker(SYMBOL)
            harga_sekarang = ticker['last']
            waktu = datetime.now().strftime('%H:%M:%S')

            # Tentukan arah pergerakan harga
            if harga_sebelumnya is not None:
                perubahan = harga_sekarang - harga_sebelumnya
                simbol = "🔺" if perubahan > 0 else "🔻" if perubahan < 0 else "➖"
                # Warna terminal (Hijau untuk naik, Merah untuk turun)
                warna = "\033[92m" if perubahan > 0 else "\033[91m" if perubahan < 0 else "\033[0m"
                reset = "\033[0m"
                print(f"[{waktu}] {SYMBOL}: {warna}${harga_sekarang:,.2f} {simbol}{reset}")
            else:
                print(f"[{waktu}] {SYMBOL}: ${harga_sekarang:,.2f}")

            harga_sebelumnya = harga_sekarang
            
            # Tunggu 5 detik sebelum update lagi
            time.sleep(5)

        except KeyboardInterrupt:
            print("\n\nPemantauan dihentikan.")
            break
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e}")
            time.sleep(10)

if __name__ == '__main__':
    monitor_harga()