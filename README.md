# Plataforma de Línguas Indígenas

Portal oficial da **Plataforma de Línguas Indígenas** — um projeto de revitalização, fortalecimento e documentação de línguas indígenas brasileiras através de plataformas digitais, dicionários, corpus linguísticos, dados etnobotânicos e materiais pedagógicos, com governança comunitária e ética.

## Visite

- **Portal**: [terradoc.org](https://terradoc.org)
- **Instagram**: [@plataformasindigenas](https://instagram.com/plataformasindigenas)

### Plataformas

- **Bororo (Boe Eno Moto)**: [boeenomoto.terradoc.org](https://boeenomoto.terradoc.org)
- **Enawenê-Nawê**: [enawenenawe.terradoc.org](https://enawenenawe.terradoc.org)
- **Xavante**: [xavante.terradoc.org](https://xavante.terradoc.org)
- **Akuntsu**: [akuntsu.terradoc.org](https://akuntsu.terradoc.org)
- **Paresi**: [paresi.terradoc.org](https://paresi.terradoc.org)
- **Bakairi**: [bakairi.terradoc.org](https://bakairi.terradoc.org)

## Objetivos

- Documentar e preservar línguas indígenas em risco de extinção
- Criar materiais didáticos para escolas indígenas
- Desenvolver plataformas digitais acessíveis (dicionários, corpus, materiais)
- Capacitar professores indígenas
- Garantir governança comunitária e respeito aos direitos de dados

## Tecnologias

- **Vite** — Build tool
- **Tailwind CSS** — Framework CSS utilitário
- **JavaScript (ES6+)** — Interatividade sem frameworks
- **Google Fonts** — Inter + Playfair Display

As plataformas individuais são geradas com [terradoc](https://pypi.org/project/terradoc/), [aptoro](https://pypi.org/project/aptoro/) e [kodudo](https://pypi.org/project/kodudo/).

## Executando Localmente

```bash
npm install
npm run dev       # servidor de desenvolvimento
npm run build     # build para produção (saída em dist/)
```

## Estrutura do Projeto

```
├── index.html            # Página inicial (PT)
├── plataformas.html      # Detalhes das plataformas
├── equipe.html           # Equipe
├── contato.html          # Contato
├── en/                   # Páginas em inglês
├── es/                   # Páginas em espanhol
├── src/
│   └── styles.css        # Estilos Tailwind
├── public/
│   ├── js/main.js        # JavaScript principal
│   ├── logo.svg          # Logo do projeto
│   ├── patterns/         # Padrões SVG decorativos
│   └── images/           # Fotos e logos
├── vite.config.js        # Configuração do Vite
├── tailwind.config.js    # Configuração do Tailwind
└── package.json          # Dependências
```

## Equipe

- **Fabrício Ferraz Gerardi** — Linguística Computacional
- **Gustavo Polleti** — Engenharia e Coordenação
- **Michel Correa da Silva** — Diretor Escolar Indígena
- **Maria Eduarda Correr** — Pedagogia
- **José Ícaro Bezerra Clemente** — Engenharia de IA e ML
- **Fernando Orphão de Carvalho** — Linguística/Antropologia
- **Carolina Aragon** — Linguística Antropológica
- **Tiago Tresoldi** — Linguística Histórica Computacional / Análise de Dados

## Contato

- **Email**: info@plataformasindigenas.org
- **Localização**: Mato Grosso, Brasil ↔ Alemanha

## Licença

Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).
