
import argparse
from .dronePol import atualizarDronePol
from uploader.core import load_dataframe, connect_mysql, upload_df_mysql  # from uploader-basico (installed or editable)
try:
    from uploader_utils.dronepol_utils import tratarDronepol  # optional
except Exception:
    tratarDronepol = None

def main():
    parser = argparse.ArgumentParser(prog="uploader-dronepol", description="CLI Dronepol")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # Subcomando: atualizar (valor/mês/ano para inserir em tabela resumo)
    p_upd = sub.add_parser("atualizar", help="Atualiza contadores (operacoes/minutos) no banco")
    p_upd.add_argument("--valor", type=int, required=True)
    p_upd.add_argument("--mes", type=int, required=True)
    p_upd.add_argument("--ano", type=int, required=True)
    p_upd.add_argument("--tabela", choices=["dronepol_operacoes","dronepol_minutos"], required=True)

    # Subcomando: tratar (processa planilha e opcionalmente sobe para uma tabela)
    p_trat = sub.add_parser("tratar", help="Trata planilha Dronepol; se --tabela for informado, faz upload")
    p_trat.add_argument("--arquivo", required=True)
    p_trat.add_argument("--tabela", required=False)

    args = parser.parse_args()

    if args.cmd == "atualizar":
        msg = atualizarDronePol(args.valor, args.mes, args.ano, args.tabela)
        print(msg)
        return

    if args.cmd == "tratar":
        if tratarDronepol is None:
            raise SystemExit("O módulo uploader_utils.dronepol_utils não está disponível.")
        df = tratarDronepol(args.arquivo)
        if args.tabela:
            conn = connect_mysql()
            upload_df_mysql(df, args.tabela, conn)
            print(f"Tratado e inserido {len(df)} registros em {args.tabela}.")
        else:
            print(df.head())
