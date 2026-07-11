import ctypes
import winreg
import subprocess
import os

# Definição de Cores
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


def aplicar_ajustes_tcp():
    print(f"{BRANCO}-> Aplicando otimizações TCP...{RESET}")

    # Lista de ajustes: (nome, comando, valor_alvo)
    ajustes = [
        (
            "AUTOTUNINGLEVEL",
            "netsh int tcp set global autotuninglevel=normal",
            "normal",
        ),
        (
            "ECNCAPABILITY",
            "netsh int tcp set global ecncapability=disabled",
            "disabled",
        ),
        ("RSS", "netsh int tcp set global rss=enabled", "enabled"),
        ("FASTOPEN", "netsh int tcp set global fastopen=disabled", "disabled"),
    ]

    for nome, cmd, valor in ajustes:
        # Executa o comando
        resultado = subprocess.run(cmd, shell=True, capture_output=True)

        # Verifica se o comando retornou sucesso (returncode 0)
        if resultado.returncode == 0:
            print(f"   {CIANO}[OK] {nome} definido para: {VERDE}{valor}{RESET}")
        else:
            print(f"   {CIANO}[ERRO] {nome} não pôde ser alterado.{RESET}")


def desativar_network_throttling():
    print(f"{BRANCO}-> Desativando Network Throttling...{RESET}")
    path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile"
    with winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE
    ) as key:
        winreg.SetValueEx(
            key, "NetworkThrottlingIndex", 0, winreg.REG_DWORD, 0xFFFFFFFF
        )
        winreg.SetValueEx(key, "SystemResponsiveness", 0, winreg.REG_DWORD, 15)
    print(f"{VERDE}[OK] Network Throttling desativado.{RESET}")


def testar_e_aplicar_mtu():
    print(f"{BRANCO}-> Testando MTU ideal (ping diagnóstico)...{RESET}")
    mtu_ideal = 1500
    for mtu in range(1500, 1399, -1):
        if (
            subprocess.run(
                f"ping -n 1 -f -l {mtu-28} 8.8.8.8", shell=True, capture_output=True
            ).returncode
            == 0
        ):
            mtu_ideal = mtu
            break
    print(f"{BRANCO}-> Aplicando MTU: {mtu_ideal}{RESET}")

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
    print(f"{VERDE}[OK] MTU configurado com sucesso.{RESET}")
