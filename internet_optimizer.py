import sys
import ctypes
import utils


def main():
    utils.inicializar_cores_terminal()

    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )
    print(
        f"{utils.CIANO}          ASSISTENTE DE OTIMIZAÇÃO DE REDE (STABLE MODE)             {utils.RESET}"
    )
    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )
    print(
        f"{utils.BRANCO}Otimizando registro e parâmetros TCP para máxima estabilidade e latência.{utils.RESET}"
    )

    utils.fazer_backup_registro()
    utils.desativar_network_throttling()
    utils.limpar_e_configurar_regedit()

    # Ajustes aplicados de forma consistente para evitar erros em jogos
    utils.aplicar_ajustes_tcp()
    utils.testar_e_aplicar_mtu()

    print(
        f"\n{utils.CIANO}Deseja otimizar sua resolução de DNS (Google 8.8.8.8 + Cloudflare 1.1.1.1)?{utils.RESET}"
    )
    print("Pressione [S] para aplicar ou [N] para ignorar.")

    if input("> ").upper() == "S":
        utils.configurar_dns()

    print(
        f"\n{utils.VERDE}====================================================================={utils.RESET}"
    )
    print(f"{utils.VERDE}[SUCESSO] OTIMIZAÇÃO CONCLUÍDA!{utils.RESET}")
    print(f"{utils.VERDE}REINICIE O PC PARA APLICAR AS MUDANÇAS.{utils.RESET}")
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
