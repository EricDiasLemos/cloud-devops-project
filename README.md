# DevOps Cloud Observability Pipeline

<div align="center">

![Badge Status Pipeline](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square)
![Terraform](https://img.shields.io/badge/Terraform-1.5+-623CE4?style=flat-square&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24+-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-2.45+-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-10+-F46800?style=flat-square&logo=grafana&logoColor=white)

**Projeto prático completo de DevOps: IaC + CI/CD + Containers + Observabilidade**

</div>

<br>

## Visão Geral

Demonstração prática de um **pipeline de entrega contínua** moderno, do provisionamento da infraestrutura até o monitoramento da aplicação em produção.

### O que o projeto faz?

- Cria automaticamente uma VM na cloud usando **Terraform** (IaC)
- Containeriza uma aplicação simples com **Docker**
- Implementa pipeline **CI/CD** com **GitHub Actions**
- Faz deploy automático na VM via SSH + docker pull & restart
- Monitora infraestrutura e containers com **Prometheus** + **Grafana**

<br>

## Arquitetura

![Arquitetura do Pipeline DevOps](<img width="1459" height="660" alt="image" src="https://github.com/user-attachments/assets/4fca6b43-9579-49ad-b018-12381f94d03b" />
![Uploading image.png…]()
)

> *Fluxo completo: commit → build → push image → deploy na VM → coleta de métricas → visualização no Grafana*

<br>

## Fluxo de Automação

1. Desenvolvedor faz commit e push no repositório  
2. GitHub Actions dispara o pipeline automaticamente  
3. Build da imagem Docker  
4. Push da imagem para o Docker Hub  
5. Conexão SSH na VM criada pelo Terraform  
6. Pull da nova imagem na VM  
7. Reinício do container (atualização da aplicação)  
8. Prometheus coleta métricas (Node Exporter + container metrics)  
9. Grafana exibe dashboards em tempo real

<br>

## Tecnologias Utilizadas

| Camada            | Tecnologia              | Finalidade principal                     |
|-------------------|-------------------------|------------------------------------------|
| Infraestrutura    | Terraform               | Provisionamento como código              |
| Cloud             | Google Cloud / AWS / ...| Hospedagem da VM                         |
| Container         | Docker                  | Empacotamento e execução da aplicação    |
| Registry          | Docker Hub              | Armazenamento das imagens                |
| CI/CD             | GitHub Actions          | Automação de build, teste e deploy       |
| Monitoramento     | Prometheus + Node Exporter | Coleta de métricas                    |
| Visualização      | Grafana                 | Dashboards e alertas visuais             |

<br>

```text
.
├── .github
│   └── workflows
│       └── deploy.yml              # Pipeline CI/CD principal (GitHub Actions)
├── terraform
│   ├── main.tf                     # Recursos principais (VM, firewall, etc.)
│   ├── variables.tf                # Variáveis de entrada
│   ├── outputs.tf                  # Saídas úteis (ex: IP da VM)
│   ├── provider.tf                 # Configuração do provedor cloud (opcional)
│   └── cloud-init
│       └── user-data.yaml          # Script de inicialização da VM (instala Docker, Prometheus, etc.)
├── docker
│   └── Dockerfile                  # Definição da imagem da aplicação
├── src                             # Código-fonte da aplicação (api, backend, frontend, etc.)
│   └── ... 
├── monitoring
│   ├── prometheus
│   │   └── prometheus.yml          # Configuração do Prometheus (targets, scrape configs)
│   └── grafana
│       └── provisioning
│           ├── datasources         # Configuração automática do datasource Prometheus
│           └── dashboards          # JSONs dos dashboards pré-configurados
└── docs
    └── images
        └── architecture.png        # Diagrama da arquitetura do pipeline
```

<br>

## Como Usar (Quick Start)

### 1. Provisionar a infraestrutura

```bash
cd terraform
terraform init
terraform plan
terraform apply
```
2. Configurar Secrets no GitHub
No repositório → Settings → Secrets and variables → Actions:

DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
VM_SSH_PRIVATE_KEY     (chave privada SSH – sem senha)
VM_IP                   (IP público da VM)
VM_USER                 (ex: ubuntu, debian, etc.)

3. Testar o deploy
git commit --allow-empty -m "test: trigger pipeline"
git push


Observe o pipeline rodando em Actions → a aplicação será atualizada na VM automaticamente.


Demonstração (recomendado adicionar)
Coloque capturas de tela reais na pasta docs/images/ e referencie aqui:

Pipeline rodando no GitHub Actions
Dashboard principal no Grafana
Output do terraform apply
Prometheus targets mostrando a VM e containers



Melhorias Futuras (roadmap)

 Migração para Kubernetes (kind local ou cluster gerenciado)
 GitOps com ArgoCD ou Flux
 Blue-green / Canary deployment
 Alertas via Alertmanager (Slack, Telegram, e-mail)
 Instrumentação da aplicação (Prometheus client)
 Centralização de logs (Loki + Grafana)
 Auto Scaling da infraestrutura
 Testes automatizados (API, segurança, carga)



Licença
MIT License
Projeto criado com o objetivo de aprendizado e portfólio DevOps.
Se gostou, não esqueça de deixar uma ⭐!
Feito em Contagem/MG 🚀


### Dicas finais para deixar ainda mais profissional

1. **Faça upload da imagem**  
   Coloque a imagem que você enviou na pasta `docs/images/architecture.png` (ou o nome que preferir) e ajuste o caminho no README.

2. **Adicione prints reais**  
   Tire screenshots do:
   - GitHub Actions rodando
   - Grafana dashboard
   - Prometheus targets
   - Terminal com `terraform apply`

3. **Crie o LICENSE**  
   Adicione um arquivo `LICENSE` com o texto da MIT License.

4. **Badges dinâmicos** (opcional)  
   Se quiser badge de status do workflow:
   ```markdown
   <image-card alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/SEU_USUARIO/SEU_REPO/deploy.yml?branch=main?style=flat-square" ></image-card>
