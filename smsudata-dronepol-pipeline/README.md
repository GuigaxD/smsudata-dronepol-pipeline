# Dronepol Operational Pipeline

> Pipeline para consolidação do Dronepol: tratamento de planilhas e atualização de agregados (operações/minutos) diretamente no banco.

### Sugestão de nome do repositório: **smsudata-dronepol-pipeline**

## ▶️ Uso rápido
```bash
# Atualiza contadores agregados (usa .env)
python -m uploader_dronepol.cli atualizar --valor 100 --mes 8 --ano 2025 --tabela dronepol_operacoes

# Trata arquivo e (opcional) envia para o MySQL
python -m uploader_dronepol.cli tratar --arquivo ./dados/drone.xlsx --tabela tb_drone_tratada
```

## ✨ Motivação (Portfólio)
Este repositório fez parte de um conjunto de soluções que desenvolvi na **Secretaria Municipal de Segurança Urbana (SMSU)** para melhorar **produtividade** e **qualidade dos dados**. O objetivo foi transformar processos manuais em **pipelines reproduzíveis**, com **configuração por `.env`**, **padronização de regras de negócio** e foco em **manutenibilidade**.

## 🔒 Credenciais
- Use `.env` localmente; **não** comite esse arquivo. O projeto inclui um `.env.example` para referência.

## 🧪 Requisitos
- Python 3.10+
- `pip install -r requirements.txt`

## 🧭 Estrutura
- `src/` — código-fonte (pacote instalável)
- `.env.example` — template de credenciais
- `requirements.txt` — dependências
- `README.md` — documentação

## 🛡️ Licença
MIT — sinta-se à vontade para usar/estender respeitando a licença.


## 📊 Case Study — Impacto (SMSU)
Antes, diversos tratamentos eram feitos manualmente em planilhas, consumindo horas por semana.
Com este repositório e o ecossistema `smsudata-*`:
- ⏱️ Tempo de processamento caiu de horas para minutos (execução reproduzível).
- 🧼 Melhoria de qualidade: padronização de endereços, rubricas e datas.
- 🔁 Menos erros humanos e pipelines versionados, com CI rodando os testes a cada PR.
