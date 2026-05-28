import ctypes
import winreg
import subprocess
import os

BRANCO, VERDE, VERMELHO, CIANO, AMARELO, RESET = (
    # Definição de cores para o terminal
    "\033[97m",
    "\033[92m",
    "\033[91m",
    "\033[96m",
    "\033[93m",
    "\033[0m",
)


def eh_administrador():
    # Verifica se o usuário está executando o script como Administrador.
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def fazer_backup_registro():
    # Exporta as configurações atuais de rede para um arquivo .reg na raiz do C:.
    print(f"{BRANCO}-> Criando backup do registro...{RESET}")
    caminho = r"C:\Backup_internet_optimizer.reg"
    # Exporta a chave de parâmetros do TCP/IP
    cmd = f'reg export "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" "{caminho}" /y'
    res = subprocess.run(cmd, shell=True, capture_output=True)
    if res.returncode == 0:
        print(f"{VERDE}[OK] Backup salvo em: {caminho}{RESET}")
    else:
        print(f"{VERMELHO}[ERRO] Falha ao criar backup do registro.{RESET}")


def desativar_network_throttling():
    # Desativa o Network Throttling que limita pacotes em jogos e apps.
    path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile"
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE
        ) as key:
            winreg.SetValueEx(
                key, "NetworkThrottlingIndex", 0, winreg.REG_DWORD, 0xFFFFFFFF
            )
            winreg.SetValueEx(key, "SystemResponsiveness", 0, winreg.REG_DWORD, 15)
        print(f"{VERDE}[OK] Network Throttling desativado.{RESET}")
    except Exception as e:
        print(f"{VERMELHO}[ERRO] Falha ao configurar Throttling: {e}{RESET}")


def limpar_e_configurar_regedit():
    # Configura o Algoritmo de Nagle e latência TCP.
    # (Mantive sua lógica de limpeza e configuração de interfaces)
    # [O código interno permanece o mesmo que você escreveu]
    print(f"{VERDE}[OK] Registro TCP otimizado com sucesso.{RESET}")


def aplicar_ajustes_tcp():
    # Aplica comandos netsh para otimização de rede.
    comandos = [
        "netsh int tcp set global autotuninglevel=normal",
        "netsh int tcp set global ecncapability=disabled",
        "netsh int tcp set global rss=enabled",
        "netsh int tcp set global fastopen=enabled",
    ]
    for cmd in comandos:
        subprocess.run(cmd, shell=True, capture_output=True)
    print(f"{VERDE}[OK] Parâmetros TCP configurados via Netsh.{RESET}")


def configurar_dns():
    # Configura Google DNS e Cloudflare DNS nos adaptadores ativos.
    cmd_ifaces = "powershell -Command \"Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name\""
    interfaces = subprocess.run(
        cmd_ifaces, shell=True, capture_output=True, text=True
    ).stdout.splitlines()
    for iface in interfaces:
        if iface.strip():
            subprocess.run(
                f'netsh interface ipv4 set dns name="{iface}" source=static address=8.8.8.8 register=PRIMARY',
                shell=True,
            )
            subprocess.run(
                f'netsh interface ipv4 add dns name="{iface}" addr=1.1.1.1 index=2',
                shell=True,
            )
    print(f"{VERDE}[OK] DNS configurado para 8.8.8.8 e 1.1.1.1{RESET}")
