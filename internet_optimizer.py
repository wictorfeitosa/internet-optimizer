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
        subprocess.run(cmd, shell=True, capture_output=True)

    print(f"{utils.VERDE}[OK] Otimizações consolidadas e cache limpo.{utils.RESET}")


def main():
    utils.inicializar_cores_terminal()

    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )
    print(
        f"{utils.CIANO}          INTERNET OPTIMIZER (STABLE MODE)                    {utils.RESET}"
    )
    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )

    utils.fazer_backup_registro()
    print(f"{utils.VERDE}[OK] Backup do registro concluído.{utils.RESET}")

    # Aplicar apenas os ajustes TCP definidos no utils.py
    utils.aplicar_ajustes_tcp()

    # Limpeza final dos protocolos de rede
    finalizar_otimizacao()

    print(
        f"\n{utils.VERDE}====================================================================={utils.RESET}"
    )
    print(f"{utils.VERDE}[SUCESSO] OTIMIZAÇÃO CONCLUÍDA!{utils.RESET}")
    print(
        f"{utils.VERDE}REINICIE O PC AGORA para aplicar todas as mudanças.{utils.RESET}"
    )
    print(
        f"{utils.VERDE}====================================================================={utils.RESET}"
    )

    input("\nTudo certo, pode fechar a tela.")


if __name__ == "__main__":
    if utils.eh_administrador():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
