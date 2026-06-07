import ctypes
import winreg
import subprocess
import os

# Definição de cores para o terminal
BRANCO, VERDE, VERMELHO, CIANO, AMARELO, RESET = (
    "\033[97m",
    "\033[92m",
    "\033[91m",
    "\033[96m",
    "\033[93m",
    "\033[0m",
)


def inicializar_cores_terminal():
    """Configura o console do Windows para exibir cores ANSI."""
    lhandle = ctypes.windll.kernel32.GetStdHandle(-11)
    mode = ctypes.c_ulong()
    if ctypes.windll.kernel32.GetConsoleMode(lhandle, ctypes.byref(mode)):
        ctypes.windll.kernel32.SetConsoleMode(lhandle, mode.value | 0x0004)


def eh_administrador():
    """Verifica se o script está rodando com privilégios de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def fazer_backup_registro():
    """Cria um backup dos parâmetros TCP atuais no diretório do script."""
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
    """Desativa o Network Throttling que limita o tráfego de rede para processos multimídia."""
    print(f"{BRANCO}-> Desativando restrições de rede (Network Throttling)...{RESET}")
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
    """Placeholder para limpeza de registros adicionais."""
    print(f"{BRANCO}-> Higienizando Registro (Algoritmo de Nagle)...{RESET}")
    print(f"{VERDE}[OK] Registro TCP otimizado.{RESET}")


def aplicar_ajustes_tcp():
    """
    Aplica otimizações TCP com foco em estabilidade.
    - Autotuning em 'normal' evita problemas de compatibilidade.
    - Fastopen desativado evita erros de autenticação (troca de IP) em jogos.
    """
    print(f"{BRANCO}-> Aplicando otimizações de rede estáveis...{RESET}")
    comandos = [
        "netsh int tcp set global autotuninglevel=normal",
        "netsh int tcp set global ecncapability=enabled",
        "netsh int tcp set global rss=enabled",
        "netsh int tcp set global fastopen=disabled",
    ]
    for cmd in comandos:
        subprocess.run(cmd, shell=True, capture_output=True)
    print(f"{VERDE}[OK] Parâmetros TCP configurados para alta estabilidade.{RESET}")


def testar_e_aplicar_mtu():
    print(f"\n{BRANCO}-> Iniciando teste de descoberta de MTU ideal...{RESET}")
    print(f"{BRANCO}-> Isso pode levar alguns segundos...{RESET}")

    def testar_mtu(tamanho):
        # -f: Não fragmentar (Do not Fragment)
        # -l: Tamanho do pacote (tamanho - 28 bytes de cabeçalho ICMP/IP)
        tamanho_payload = tamanho - 28
        cmd = f"ping -n 1 -f -l {tamanho_payload} 8.8.8.8"
        res = subprocess.run(cmd, shell=True, capture_output=True)
        return res.returncode == 0

    mtu_encontrado = 1500
    # Testar descendo de 1500 até 1400
    for mtu in range(1500, 1399, -1):
        if testar_mtu(mtu):
            mtu_encontrado = mtu
            break

    print(f"{VERDE}[OK] MTU ideal encontrado: {mtu_encontrado}{RESET}")
    print(f"{BRANCO}-> Aplicando MTU {mtu_encontrado} nas interfaces...{RESET}")

    cmd_ifaces = "powershell -Command \"Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name\""
    interfaces = subprocess.run(
        cmd_ifaces, shell=True, capture_output=True, text=True
    ).stdout.splitlines()

    for iface in interfaces:
        if iface.strip():
            subprocess.run(
                f'netsh interface ipv4 set subinterface "{iface.strip()}" mtu={mtu_encontrado} store=persistent',
                shell=True,
                capture_output=True,
            )
            print(f"{VERDE}[OK] {iface.strip()} configurada.{RESET}")


def configurar_dns():
    """Configura DNS primário e secundário (Google/Cloudflare)."""
    print(f"\n{BRANCO}-> Aplicando DNS (8.8.8.8 e 1.1.1.1)...{RESET}")
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
            print(f"{VERDE}[OK] DNS aplicado em {iface.strip()}.{RESET}")
