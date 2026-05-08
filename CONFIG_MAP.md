# CONFIG_MAP - Itens de Configuração (ICs)

Este documento lista os Itens de Configuração (ICs) do projeto e define a política de versionamento.

1) Código fonte
- `src/main.py` — Aplicação de exemplo (Python).

2) Arquivos de configuração
- `config.env` — Variáveis de ambiente usadas pela aplicação.

3) Documentação
- `README.md` — Instruções e descrição do projeto.

4) Dependências / Plataforma
- Linguagem: Python 3.11 (recomendado)
- Bibliotecas externas: Nenhuma (arquivo `requirements.txt` vazio)

5) Ferramentas de build/execução
- Git — controle de versão e baseline/tag

Política de Versionamento
- Usamos Versionamento Semântico (SemVer): MAJOR.MINOR.PATCH
  - MAJOR: mudanças incompatíveis na API
  - MINOR: adição de funcionalidades compatíveis
  - PATCH: correções e pequenas alterações

Exemplos:
- `v1.0.0` — baseline inicial (tag criada neste repositório)
- `v1.1.0` — nova feature compatível
- `v2.0.0` — alteração incompatível

Observações
- O `config.env` contém valores de exemplo; em ambientes reais, segredos não devem ser comitados.
- Todos os ICs devem ser listados e versionados; binários e artefatos gerados ficam fora do repositório.
