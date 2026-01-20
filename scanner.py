import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    135: "RPC",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}
#dictionary açtık Eğer port 80 ise, karşılığındaki 'HTTP' yazısını al.

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")

    # range fonksiyonu son sayıyı dahil etmediği için +1 ekliyoruz
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)  # Hızlandırmak için süreyi iyice kıstım

        result = s.connect_ex((target, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            print(f"[+] Port {port} is OPEN ({service})")
#.get(port, "Unknown") şunu der: "Port numarasını sözlükte ara. Bulursan ismini getir. Buverme, sadece 'Unklamazsan hata nown' (Bilinmiyor) yaz. .get olmasaydı hangisi unknown bulamazdık"
        s.close()  # Her denemeden sonra kapatıyoruz


if __name__ == "__main__":
    target_ip = input("Target IP address: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    scan_ports(target_ip, start_port, end_port)

""" 
s = socket.socket(...): Burada s adında bir soket nesnesi oluşturuyoruz
socket.AF_INET: "Address Family - Internet" demektir. Bu, IPv4 adreslerini (örneğin 192.168.1.1 gibi) kullanacağımızı belirtir.
socket.SOCK_STREAM: Bu, TCP (Transmission Control Protocol) kullanacağımızı belirtir. TCP, verinin sırayla ve güvenli bir şekilde gittiğinden emin olan bir protokoldür. Port taramalarında genellikle TCP bağlantısı kurmaya çalışırız.
s.settimeout(1) Soketin cevap bekleme süresini 1 saniye ile sınırlandırıyor.soket normalde dakikalarca cevap bekleyebilir. Kodun donmasını (hang) engellemek ve işlemi hızlandırmak için
Normal s.connect() fonksiyonu, bağlantı başarısız olursa programı durduran bir hata (Exception) fırlatır. Bunu yönetmek için try-except bloğu gerekir.
s.connect_ex() ise hata fırlatmaz, bunun yerine bir hata kodu (sayı) döndürür.
Eğer sonuç 0 ise: Bağlantı başarılıdır.
Eğer sonuç 0 değilse bir hata oluşmuştur
127.0.0.1 localhosttur kendi bilgisayarın
bu bilgiler kodun eski ilk hali içindir kafa karışıklığı olmasın
"""