import sys
import ctypes
import utils


def main():
    utils.inicializar_cores_terminal()

    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )
    print(
        f"{utils.CIANO}          ASSISTENTE DE OTIMIZAÇÃO DE REDE (NETWORK BOOSTER)         {utils.RESET}"
    )
    print(
        f"{utils.CIANO}====================================================================={utils.RESET}"
    )
    print(
        f"{utils.BRANCO}Esta ferramenta otimiza o registro e os parâmetros do Windows para\nmelhorar a latência e o desempenho geral da sua conexão.{utils.RESET}"
    )

    utils.fazer_backup_registro()
    utils.desativar_network_throttling()
    utils.limpar_e_configurar_regedit()

    print(
        f"\n{utils.CIANO}---------------------------------------------------------------------{utils.RESET}"
    )
    print(f"{utils.BRANCO}Qual é o tipo da sua conexão com a internet?{utils.RESET}")
    print("1 - Fibra Óptica / Cabo de Rede")
    print("2 - Via Rádio / Satélite / Wi-Fi Distante")
    tipo_conexao = input("> ")

    if tipo_conexao == "2":
        print(
            f"\n{utils.BRANCO}Qual é a velocidade aproximada do seu plano?{utils.RESET}"
        )
        print("1 - Plano menor (Até 50 Mbps)")
        print("2 - Plano maior (Acima de 50 Mbps)")
        velocidade = input("> ")

        if velocidade == "1":
            perfil_tcp = "highlyrestricted"
        else:
            perfil_tcp = "restricted"
    else:
        perfil_tcp = "normal"
    print(
        f"{utils.CIANO}---------------------------------------------------------------------\n{utils.RESET}"
    )

    utils.aplicar_ajustes_tcp(perfil_tcp)
    utils.testar_e_aplicar_mtu()

    print(
        f"\n{utils.CIANO}Deseja otimizar sua resolução de DNS (Google 8.8.8.8 + Cloudflare 1.1.1.1)?{utils.RESET}"
    )
    print(
        f"{utils.BRANCO}Essa configuração reduz a latência ao carregar sites e melhora a estabilidade.{utils.RESET}"
    )
    print("Pressione [S] para aplicar ou [N] para manter a configuração atual.")

    if input("> ").upper() == "S":
        utils.configurar_dns()

    print(
        f"\n{utils.VERDE}====================================================================={utils.RESET}"
    )
    print(f"{utils.VERDE}[SUCESSO] OTIMIZAÇÃO CONCLUÍDA!{utils.RESET}")
    print(f"{utils.VERDE}MTU Final: 1492{utils.RESET}")
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
