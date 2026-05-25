import sys
import ctypes
import utils


def main():
    # Limpa o terminal e exibe o cabeçalho
    print(
        f"{utils.CIANO}=== ASSISTENTE DE OTIMIZAÇÃO (NETWORK BOOSTER) ==={utils.RESET}"
    )

    utils.fazer_backup_registro()
    utils.desativar_network_throttling()
    utils.limpar_e_configurar_regedit()
    utils.aplicar_ajustes_tcp()

    print(
        f"\n{utils.CIANO}Deseja otimizar o DNS (Google/Cloudflare)? (S/N){utils.RESET}"
    )
    if input("> ").upper() == "S":
        utils.configurar_dns()

    print(f"\n{utils.VERDE}SUCESSO! Reinicie o PC para aplicar.{utils.RESET}")
    input("Pressione Enter para sair...")


if __name__ == "__main__":
    if utils.eh_administrador():
        main()
    else:
        # Elevação de privilégios correta
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
