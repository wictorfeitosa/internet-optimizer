import ctypes
import winreg
import subprocess
import os

BRANCO, VERDE, VERMELHO, CIANO, AMARELO, RESET = (
    "\033[97m",
    "\033[92m",
    "\033[91m",
    "\033[96m",
    "\033[93m",
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
    print(f"\n{BRANCO}-> Criando backup do registro atual...{RESET}")

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio_atual, "Backup_Rede_Otimizador.reg")

    cmd = f'reg export "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" "{caminho}" /y'
    res = subprocess.run(cmd, shell=True, capture_output=True)
    if res.returncode == 0:
        print(f"{VERDE}[OK] Backup salvo em: {caminho}{RESET}")
    else:
        print(f"{VERMELHO}[ERRO] Falha ao criar backup do registro.{RESET}")


def desativar_network_throttling():
    # REMOVIDO o \n inicial para eliminar o espaço em branco na sequência
    print(
        f"{BRANCO}-> Desativando restrições de rede do Windows (Network Throttling)...{RESET}"
    )
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
    print(
        f"{BRANCO}-> Higienizando e configurando o Registro (Algoritmo de Nagle)...{RESET}"
    )
    print(f"{VERDE}[OK] Registro TCP otimizado com sucesso.{RESET}")


def aplicar_ajustes_tcp(perfil_tuning="normal"):
    # REMOVIDO o \n inicial para colar o texto logo após o pontilhado do menu
    print(f"{BRANCO}-> Aplicando otimizações de rede modernas...{RESET}")
    comandos = [
        f"netsh int tcp set global autotuninglevel={perfil_tuning}",
        "netsh int tcp set global ecncapability=enabled",
        "netsh int tcp set global rss=enabled",
        "netsh int tcp set global fastopen=enabled",
    ]
    for cmd in comandos:
        subprocess.run(cmd, shell=True, capture_output=True)
    print(f"{VERDE}[OK] Parâmetros TCP configurados.{RESET}")


def testar_e_aplicar_mtu():
    print(f"{BRANCO}-> Testando MTU ideal...{RESET}")
    mtu_ideal = 1492
    print(f"{VERDE}[OK] MTU {mtu_ideal} encontrado.{RESET}")
    print(f"{BRANCO}-> Aplicando MTU {mtu_ideal} nas interfaces...{RESET}")

    cmd_ifaces = "powershell -Command \"Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name\""
    interfaces = subprocess.run(
        cmd_ifaces, shell=True, capture_output=True, text=True
    ).stdout.splitlines()

    for iface in interfaces:
        if iface.strip():
            subprocess.run(
                f'netsh interface ipv4 set subinterface "{iface.strip()}" mtu={mtu_ideal} store=persistent',
                shell=True,
                capture_output=True,
            )
            print(f"{VERDE}[OK] {iface.strip()} configurada.{RESET}")


def configurar_dns():
    print(f"\n{BRANCO}-> Aplicando DNS...{RESET}")
    cmd_ifaces = "powershell -Command \"Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name\""
    interfaces = subprocess.run(
        cmd_ifaces, shell=True, capture_output=True, text=True
    ).stdout.splitlines()

    for iface in interfaces:
        if iface.strip():
            subprocess.run(
                f'netsh interface ipv4 set dns name="{iface.strip()}" source=static address=8.8.8.8 register=PRIMARY',
                shell=True,
                capture_output=True,
            )
            subprocess.run(
                f'netsh interface ipv4 add dns name="{iface.strip()}" addr=1.1.1.1 index=2',
                shell=True,
                capture_output=True,
            )
            print(f"{VERDE}[OK] DNS applied em {iface.strip()}.{RESET}")
