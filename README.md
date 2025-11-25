# Elf Gifts – Educational Game in Python

![Autor: Max Muller](https://img.shields.io/badge/Autor-Max%20Muller-1e90ff?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.x-ffd43b?style=for-the-badge&logo=python)

**Elf Gifts** é um jogo interativo desenvolvido em Python com Pygame, criado especialmente para fins educacionais. A proposta foi adaptar conceitos de desenvolvimento de jogos para uma linguagem acessível a crianças de 9 anos, proporcionando uma experiência prática, visual e divertida para introduzir lógica de programação.

---

## Objetivo do Projeto

Este projeto foi construído para apresentar aos alunos uma aplicação real de programação, unindo sprites, interações, áudio, eventos e elementos gráficos. A experiência permite que crianças aprendam lógica, repetição, coordenadas, colisões e fluxo de execução enquanto jogam e exploram o código.

---

## Conceitos Técnicos Demonstrados

- **Sprites personalizados** para o jogador (elfo) e itens coletáveis  
- **Eventos temporizados** para geração dinâmica de presentes  
- **Detecção de colisões** usando grupos de sprites  
- **Plano de fundo gráfico personalizado**, ajustado dinamicamente  
- **Trilha sonora contínua**, com mixer e sons individuais de coleta  
- **Atualização em tempo real** conforme movimentos do mouse  
- **Estrutura de loop principal sólida**, garantindo fluidez e desempenho  
- **Orientação a objetos**, organizando o comportamento de cada entidade do jogo  

---

## Como o jogo funciona

O jogador controla um elfo utilizando o movimento do mouse. Presentes surgem pela tela em intervalos ajustados dinamicamente, aumentando o ritmo conforme a coleta. Ao encostar em um presente, o item desaparece, a pontuação aumenta e um efeito sonoro é reproduzido.

Quando muitos presentes se acumulam na tela, o jogo termina — incentivando agilidade e raciocínio rápido.

---

## Estrutura e Recursos Utilizados

O jogo faz uso de:

- imagens externas (elfo, presente, background, ícone da janela)  
- efeitos sonoros individuais  
- música de fundo em loop  
- organização clara de arquivos usando `pathlib`  

Estes elementos ajudam a transformar programação em uma atividade visual, intuitiva e engajadora para crianças.

---

## Execução

Instale o Pygame:

```bash
pip install pygame
```

Execute o arquivo principal:
python elf-gifts.py

## Autor

Max Muller
Professor de Informática e desenvolvedor com foco em ensino de programação, projetos educacionais e criação de jogos simples e interativos para formação de novos talentos em tecnologia.

Se este projeto ajudou você a evoluir, deixe uma ⭐ e compartilhe o conhecimento. Obrigado por usar este repositório!
