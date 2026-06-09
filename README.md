# 🌍 Projeto InovaWare - Plataforma de Mobilidade Urbana

## Sobre a InovaWare

A **InovaWare** é uma startup fundada há 4 anos em Florianópolis com foco em **soluções de mobilidade urbana**. Nosso principal produto é uma plataforma que integra dados de:

- 📊 **Trânsito** - Monitoramento em tempo real
- 🚌 **Transporte Público** - Integração com sistemas de transporte
- 🌤️ **Clima** - Dados meteorológicos em tempo real

A plataforma é voltada para **prefeituras de médio porte**, auxiliando na tomada de decisões sobre mobilidade urbana.

## 🏢 Estrutura Organizacional

A empresa possui uma equipe jovem e multidisciplinar, organizada em **squads** com autonomia para desenvolver e testar soluções. Com esse modelo, crescemos rapidamente, mas enfrentamos desafios de padronização.

## 🚨 Desafios Atuais

- ❌ Falta de padrões entre as equipes (squads desenvolvem de forma heterogênea)
- ❌ Pipelines simples e deploys manuais
- ❌ Ausência de política de revisão de código
- ❌ Métricas de qualidade não formalizadas
- ❌ Alta rotatividade de desenvolvedores
- ❌ Acúmulo de dívidas técnicas
- ❌ Dificuldade na manutenção da base de código

## 🎯 Objetivos de Melhoria

Nosso objetivo é:

1. **Melhorar a previsibilidade das entregas** através de processos mais robustos
2. **Consolidar uma cultura de qualidade** sem burocratizar o processo criativo
3. **Adotar um modelo de maturidade** que guie o crescimento progressivo das práticas de qualidade e DevOps

## 📁 Estrutura do Repositório

```
/workspaces/Projeto-InovaWare/
├── README.md                      # Este arquivo
├── Códigos_Legado/               # Código atual com dívidas técnicas
│   ├── app.py                    # Aplicação principal (versão legada)
│   ├── clima.csv                 # Dados de clima
│   ├── transito.csv              # Dados de trânsito
│   ├── transporte.csv            # Dados de transporte
│   └── templates/
│       └── index.html            # Interface de apresentação
└── Códigos_Corrigidos/           # Versão refatorada e melhorada
    ├── app.py                    # Aplicação refatorada
    ├── clima.csv
    ├── transito.csv
    ├── transporte.csv
    └── templates/
        └── index.html
```

## 📊 Comparação: Legado vs. Corrigido

Este repositório serve como referência para o processo de **refatoração e modernização** da base de código:

- **Códigos_Legado**: Representa o estado atual com dívidas técnicas acumuladas
- **Códigos_Corrigidos**: Demonstra as melhorias aplicadas em padrões, qualidade e manutenibilidade

## 🔄 Próximos Passos

- [ ] Implementar pipeline de CI/CD
- [ ] Estabelecer padrões de código entre as squads
- [ ] Criar política de revisão de código
- [ ] Definir métricas de qualidade (cobertura de testes, code smells, etc.)
- [ ] Implementar testes automatizados
- [ ] Documentar arquitetura e padrões
- [ ] Capacitar equipes em DevOps e boas práticas

## 📝 Contribuindo

As squads devem seguir os padrões estabelecidos neste repositório ao submeter novo código.

---

**InovaWare** - Mobilidade Urbana Inteligente 🚀