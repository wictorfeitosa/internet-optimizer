import ctypes
import winreg
import subprocess
import os

BRANCO, VERDE, VERMELHO, CIANO, RESET = (
    "\033[97m",
    "\033[92m",
    "\033[91m",
    "\033[96m",
    "\033[0m",
)


def inicializar_cores_terminal():
    lhandle = ctypes.windll.kernel32.GetStdHandle(-11)
    mode = ctypes.c_ulong()
    if ctypes.windll.kernel32.GetConsoleMode(lhandle, ctypes.byref(mode)):
        ctypes.windll.kernel32.SetConsoleMode(lhandle, mode.value | 0x0004)


def eh_administrador():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def fazer_backup_registro():
    print(f"{BRANCO}-> Criando backup do registro atual...{RESET}")
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "Backup_Rede.reg"
    )
    subprocess.run(
        f'reg export "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" "{caminho}" /y',
        shell=True,
    )
    print(f"{VERDE}[OK] Backup criado.{RESET}")


def desativar_network_throttling():
    path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile"
    with winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE
    ) as key:
        winreg.SetValueEx(
            key, "NetworkThrottlingIndex", 0, winreg.REG_DWORD, 0xFFFFFFFF
        )
        winreg.SetValueEx(key, "SystemResponsiveness", 0, winreg.REG_DWORD, 15)
    print(f"{VERDE}[OK] Network Throttling desativado.{RESET}")


def aplicar_ajustes_tcp():
    print(f"{BRANCO}-> Aplicando otimizações TCP estáveis...{RESET}")
    comandos = [
        "netsh int tcp set global autotuninglevel=normal",
        "netsh int tcp set global ecncapability=disabled",  # Desativado para compatibilidade
        "netsh int tcp set global rss=enabled",
        "netsh int tcp set global fastopen=disabled",  # Desativado para evitar IP mismatch
    ]
    for cmd in comandos:
        subprocess.run(cmd, shell=True, capture_output=True)
    print(f"{VERDE}[OK] Parâmetros TCP configurados.{RESET}")


def testar_e_aplicar_mtu():
    print(f"{BRANCO}-> Testando MTU ideal (ping diagnóstico)...{RESET}")

    def testar_mtu(tamanho):
        return (
            subprocess.run(
                f"ping -n 1 -f -l {tamanho-28} 8.8.8.8", shell=True, capture_output=True
            ).returncode
            == 0
        )

    mtu_ideal = 1500
    for mtu in range(1500, 1399, -1):
        if testar_mtu(mtu):
            mtu_ideal = mtu
            break

    print(f"{VERDE}[OK] MTU encontrado: {mtu_ideal}. Aplicando...{RESET}")
    cmd_ifaces = "powershell -Command \"Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name\""
    interfaces = subprocess.run(
        cmd_ifaces, shell=True, capture_output=True, text=True
    ).stdout.splitlines()

    for iface in interfaces:
        if iface.strip():
            subprocess.run(
                f'netsh interface ipv4 set subinterface "{iface.strip()}" mtu={mtu_ideal} store=persistent',
                shell=True,
            )
