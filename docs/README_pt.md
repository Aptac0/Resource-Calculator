# RSS STORE APTAC - Calculadora de Recursos

**[Español](README_es.md) | [English](README_en.md) | Português | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Français](README_fr.md)**

---

## 📱 O que é RSS STORE APTAC?

Aplicação de desktop para extrair recursos de reino de capturas de tela usando tecnologia OCR com gerenciamento inteligente de contas.

## ✨ Características

- ✅ Extração automática de recursos com OCR
- 🎯 Interface multiidioma (6 idiomas suportados)
- 🔄 Atualizações automáticas do GitHub
- 📊 Processamento em lote (até 100 imagens)
- 💾 Exportação para arquivos TXT/CSV
- 🌍 Todas as mensagens respeitam seu idioma selecionado

## 🚀 Instalação Rápida

1. Baixe `RSS_STORE_APTAC_Installer.exe` de [Releases](https://github.com/Aptac0/Resource-Calculator/releases)
2. Execute o instalador
3. Pronto! O aplicativo será atualizado automaticamente quando novas versões estiverem disponíveis

## 📖 Guia do Usuário

### Fluxo Rápido

1. **Abrir a aplicação:** Execute `RSS STORE APTAC.exe`
2. **Adicionar imagens:** Clique em "Adicionar Imagens" e selecione suas capturas de tela
3. **Selecionar reino:** Escolha o reino apropriado no menu suspenso
4. **Configurar números:**
   - `Número de início`: Primeiro número de conta (ex: 1)
   - `Número de fim`: Último número de conta (ex: 30)
   - `Números bloqueados`: (opcional) Números para pular (ex: 3,5,7)
5. **Definir níveis:** Selecione "Nível de cidade" e "Nível de depósito" (1-25)
6. **Processar:** Clique no botão de recurso que você precisa

### Como Tirar Capturas de Tela

#### Do PC (Recomendado)
- Abra o jogo no modo janelado
- Tire uma captura de tela clara da janela de Recursos
- Certifique-se que números e rótulos sejam legíveis

![Captura do PC](../Ejemplos/Foto-desde-PC.png)

#### Do Celular
- Transfira a imagem para o PC (USB, Google Drive, etc.)
- Evite fotos inclinadas ou desfocadas
- Certifique-se que a imagem seja nítida

![Captura do Celular](../Ejemplos/Foto-desde-Movil.png)

### Formatos de Entrada

#### Números de Início e Fim
- Apenas números (ex: `1` e `30`)
- Devem ser inteiros positivos válidos

#### Números Bloqueados (Opcional)
Dois formatos disponíveis:
- **Intervalo:** `1-10` (todos os números de 1 a 10)
- **Lista:** `1,3,5,7` (números específicos)
- **Misto:** `1-5,8,10-15`

**Exemplos:**
- `início=1`, `fim=10`, `bloqueados=3,5` → processa: 1,2,4,6,7,8,9,10
- O aplicativo valida que você tem imagens suficientes

#### Níveis
- `Nível de cidade` (Mercado): 1-25
- `Nível de depósito` (Armazém): 1-25

![Níveis de Mercado](../Ejemplos/Niveles-Puesto-de-Venta.png)
![Níveis de Armazém](../Ejemplos/Niveles-de-Almacen.png)

## 🔄 Sistema de Atualização

### Automático
O aplicativo verifica novas versões ao iniciar. Se encontrado:
- Você receberá uma notificação
- Baixe diretamente do aplicativo
- Instalação automática

### Manual
Execute `actualizar.bat` na pasta de instalação

## 💾 Resultados e Arquivos Salvos

### Localização dos Arquivos

```
GUARDADOS/
├── REINO_results_20260602_143022.txt
├── REINO_results_20260602_145015.txt
└── REINO_results_20260603_101530.txt
```

### Formato do Arquivo

```
Nickname: Account_1
Nível de Cidade: 15
Nível de Armazém: 18
Comida: 45.0K
Madeira: 32.5K
Pedra: 28.7K
Ouro: 5.6K
---
Nickname: Account_2
Nível de Cidade: 15
Nível de Armazém: 18
Comida: 41.2K
Madeira: 35.1K
Pedra: 26.8K
Ouro: 6.1K
---
```

### Como Usar os Resultados

1. Abra o arquivo `.txt` no editor
2. Copie os dados que você precisa
3. Cole em sua ferramenta de gerenciamento
4. Os nicknames são gerados automaticamente

---
