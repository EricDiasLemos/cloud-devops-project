# DevOps Cloud Observability Project

Projeto prático de **DevOps e automação de infraestrutura** utilizando Infraestrutura como Código, CI/CD, containers e monitoramento.

O objetivo deste projeto é demonstrar um **pipeline completo de automação**, desde o provisionamento da infraestrutura até o deploy automático da aplicação e monitoramento do ambiente.

---

# Arquitetura do Projeto

Este ambiente automatiza todo o fluxo de deploy de uma aplicação containerizada.

Componentes principais:

- Provisionamento de infraestrutura com Terraform
- Containerização da aplicação com Docker
- Pipeline CI/CD automatizado
- Deploy automático em VM
- Monitoramento de infraestrutura e containers

---

# Fluxo de Automação

O fluxo do pipeline segue o seguinte processo:

1. Desenvolvedor realiza commit no repositório
2. Pipeline CI/CD é disparado automaticamente
3. A imagem Docker da aplicação é construída
4. A imagem é enviada para o registry
5. A pipeline conecta na VM via SSH
6. A VM realiza pull da nova imagem
7. O container é reiniciado automaticamente
8. Prometheus coleta métricas da infraestrutura
9. Grafana exibe dashboards de monitoramento

---

# Fluxograma da Arquitetura


flowchart TD

A[Developer Commit] --> B[GitHub Repository]

B --> C[CI/CD Pipeline]

C --> D[Build Docker Image]

D --> E[Push Image to Docker Hub]

E --> F[SSH Deploy to VM]

F --> G[Docker Pull Latest Image]

G --> H[Run Application Container]

H --> I[Prometheus Collect Metrics]

I --> J[Grafana Dashboards]

Provisionamento da Infraestrutura

A infraestrutura é criada automaticamente utilizando Terraform.

Recursos provisionados:

Máquina virtual em cloud

Instalação automática do Docker

Configuração inicial do ambiente

Executar:

terraform init
terraform plan
terraform apply
Pipeline CI/CD

O pipeline automatizado executa as seguintes etapas:

Checkout do repositório

Login no Docker Hub

Build da imagem Docker

Push da imagem para o registry

Deploy automático na VM

Fluxo resumido:

Commit → Build → Push Image → Deploy → Container Running
Monitoramento

O ambiente inclui monitoramento completo da infraestrutura.

Métricas coletadas:

CPU da VM

Uso de memória

Utilização de disco

Containers em execução

Ferramentas utilizadas:

Prometheus → coleta de métricas
Grafana → visualização e dashboards

Estrutura do Projeto
project-root
│
├── terraform
│   ├── main.tf
│   ├── variables.tf
│   ├── provider.tf
│
├── docker
│   └── Dockerfile
│
├── api
│   └── application source
│
├── monitoring
│   ├── prometheus.yml
│   └── grafana dashboards
│
└── .github
    └── workflows
        └── pipeline.yml
Stack Tecnológica

Infraestrutura

Terraform

Cloud VM

Containers

Docker

Docker Hub

CI/CD

GitHub Actions

Observabilidade

Prometheus

Grafana

Objetivo do Projeto

Este projeto foi desenvolvido para praticar e demonstrar conceitos fundamentais de DevOps:

Infraestrutura como código

Automação de deploy

CI/CD pipelines

Containerização

Observabilidade

Melhorias Futuras

Possíveis evoluções do projeto:

Deploy utilizando Kubernetes

Auto Scaling da infraestrutura

Monitoramento de métricas da aplicação

Centralização de logs

Alertas automatizados


---

### Sugestão importante para seu repositório

Se quiser deixar o projeto **mais profissional no GitHub**, adicione no topo do README:


print do pipeline rodando

print do dashboard do Grafana

print do terraform apply criando a VM


Isso transforma o README em **portfólio DevOps real**, algo que recruta dores técnicos valorizam muito.

---

Se quiser, também posso te gerar **uma versão muito mais profissional desse README (nível projeto open-source)** com:

- badges de status  
- arquitetura visual  
- seção de deploy rápido  
- GIF do pipeline  

que deixa o repositório **bem mais forte para LinkedIn e recrutadores DevOps**.

