import sys
import ctypes
import subprocess
import utils


def finalizar_otimizacao():
    print(
        f"\n{utils.BRANCO}-> Executando limpeza final (isso pode demorar alguns segundos)...{utils.RESET}"
    )

    comandos_limpeza = [
        ("Flush DNS", "ipconfig /flushdns"),
        ("Reset Winsock", "netsh winsock reset"),
        ("Reset IP", "netsh int ip reset"),
    ]

    for nome, cmd in comandos_limpeza:
        print(f"   {utils.CIANO}Executando: {nome}...{utils.RESET}")
        # Removemos o capture_output=True para que o console mostre o feedback do Windows
        subprocess.run(cmd, shell=True)

    print(f"{utils.VERDE}[OK] Otimizações consolidadas.{utils.RESET}")

    print(
        f"\n{utils.BRANCO}-> Executando limpeza final de sockets e cache...{utils.RESET}"
    )
    comandos_limpeza = [
        "ipconfig /flushdns",
        "netsh winsock reset",
        "netsh int ip reset",
    ]
    for cmd in comandos_limpeza:
        subprocess.run(cmd, shell=True, capture_output=True)
    print(f"{utils.VERDE}[OK] Otimizações consolidadas.{utils.RESET}")


def main():
    utils.inicializar_cores_terminal()

    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )
    print(
        f"{utils.CIANO}          INTERNET OPTIMIZER v1.2.1 (STABLE MODE)                    {utils.RESET}"
    )
    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )

    utils.fazer_backup_registro()
    utils.desativar_network_throttling()
    utils.aplicar_ajustes_tcp()
    utils.testar_e_aplicar_mtu()
    utils.configurar_dns()
    finalizar_otimizacao()

    print(
        f"\n{utils.VERDE}====================================================================={utils.RESET}"
    )
    print(f"{utils.VERDE}[SUCESSO] OTIMIZAÇÃO CONCLUÍDA!{utils.RESET}")
    print(f"{utils.VERDE}REINICIE O PC AGORA para aplicar as mudanças.{utils.RESET}")
    print(
        f"{utils.VERDE}====================================================================={utils.RESET}"
    )

    input("\nPressione qualquer tecla para sair...")


if __name__ == "__main__":
    if utils.eh_administrador():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
