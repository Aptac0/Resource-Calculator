# RSS STORE APTAC - Calculadora de Recursos

**[Español](README_es.md) | [English](README_en.md) | Português | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Français](README_fr.md)**

Aplicativo desktop para extrair automaticamente recursos de reino a partir de capturas de tela usando OCR com geração inteligente de apelidos.

---

## 📖 Índice

1. [Guia Rápido](#-guia-rápido)
2. [Como Tirar Capturas](#-como-tirar-capturas)
3. [Formatos de Entrada](#-formatos-de-entrada)
4. [Botões e Funções](#-botoes-e-funcoes)
5. [Resultados e Arquivos Salvos](#-resultados-e-arquivos-salvos)
6. [Solução de Problemas](#-solucao-de-problemas)
7. [Sistema de Atualização](#-sistema-de-atualizacao)

---

## 🚀 Guia Rápido

### Passo a Passo

1. **Abra o aplicativo**
   - Execute `RSS STORE APTAC.exe`
   - Selecione o idioma no menu principal

2. **Adicione imagens**
   - Clique no botão `Adicionar Imagens`
   - Selecione suas capturas de tela
   - As imagens carregam na lista

3. **Configure o reino**
   - Escolha o `Reino` no menu suspenso
   - Os reinos disponíveis se atualizam do servidor

4. **Preencha os números**
   - `Número de início`: primeiro número de conta (ex: 1)
   - `Número de fim`: último número de conta (ex: 30)
   - `Números bloqueados` (opcional): contas a pular (ex: 3,5,7)

5. **Defina os níveis**
   - `Nível de cidade`: nível do Mercado (1–25)
   - `Nível de depósito`: nível do Armazém (1–25)

6. **Processe recursos**
   - Clique no botão de recurso que você precisa:
     - `Recursos Totais`: Total por conta
     - `Recursos de Conta`: Valores líquidos
     - `Recursos da Mochila`: Apenas inventário

7. **Encontre os resultados**
   - Salvo automaticamente em `GUARDADOS/`
   - Nome: `KINGDOM_results_YYYYMMDD_HHMMSS.txt`

## 📸 Como Tirar Capturas

### Do PC (Recomendado)

✅ **Forma correta:**
- Abra o jogo em modo janela
- Capture claramente a janela de Recursos
- Garanta que os números não fiquem cortados
- A imagem deve estar nítida sem sombras

![Captura do PC](../../images/app/Foto-desde-PC.png)

**Dicas:**
- Use a ferramenta de captura do Windows (Win + Shift + S)
- Inclua apenas o diálogo de recursos
- Números e etiquetas devem ser legíveis

### Do Mobile

⚠️ **Importante:**
1. Tire a captura no celular
2. **Transfira para o PC** (USB, Google Drive, Telegram, etc.)
3. Evite fotos tortas ou borradas
4. A captura deve estar nítida e clara

![Captura do Mobile](../../images/app/Foto-desde-Movil.png)

**Recomendações:**
- Use screenshot nativo do celular (melhor que foto)
- Boa iluminação
- Sem reflexos ou sombras
- Transfira sem compressão

## 🔢 Formatos de Entrada

### Número de Início e Número de Fim

- **Apenas números**: `1` a `30` (ex: início=1, fim=30)
- **Devem ser inteiros positivos**
- **A quantidade de imagens deve corresponder** às contas válidas

### Números Bloqueados (Opcional)

**Dois formatos permitidos:**

**Formato 1: Intervalo**
```
1-10      → 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
3-5       → 3, 4, 5
```

**Formato 2: Lista**
```
1,3,5,7   → 1, 3, 5, 7
3, 5, 8   → 3, 5, 8 (espaços permitidos)
```

**Formato 3: Misto**
```
1-5,8,10-15  → 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15
```

### Exemplo Prático

| Campo | Valor | Resultado |
|-------|-------|-----------|
| Início | 1 | Conta 1 |
| Fim | 10 | Conta 10 |
| Bloqueados | 3,5 | Processa: 1,2,4,6,7,8,9,10 |
| Imagens | 8 | ✅ Válido (corresponde) |

⚠️ Se a quantidade de imagens ≠ contas válidas, você verá um erro.

### Níveis

- `Nível de cidade` (Mercado): 1-25
- `Nível de depósito` (Armazém): 1-25



## 🎯 Botões e Funções

### Adicionar Imagens
- Abre o seletor de arquivos
- Selecione várias capturas
- Adiciona à lista de processamento

### Adicionar Pasta
- Carrega todas as imagens válidas de uma pasta
- Mais rápido para lotes grandes
- Recomendado ao processar muitas contas

### Excluir Imagem
- Remove uma imagem selecionada da lista
- Útil para corrigir uma captura errada sem limpar tudo
- Ajuda a validar o lote final antes do processamento

### Limpar Lista
- Esvazia todas as imagens carregadas
- Remove dados temporários
- Útil para iniciar um novo lote

### Nova Janela
- Abre outra instância do aplicativo
- Útil para várias tarefas

### Atualizar Dados
- Baixa `kingdoms/` e `Iconos/` mais recentes da fonte de atualização
- Substitui os dados locais
- Se usar o .exe, exibe a página de releases para novo instalador

### Recursos Totais
- Processa imagens para cada conta
- Salva: Comida, Madeira, Pedra, Ouro
- Mostra o total por conta
- Útil para rastrear o inventário

### Recursos de Conta
- Calcula recursos líquidos (total - inventário)
- Subtrai itens da mochila
- Mostra os recursos reais da conta
- Melhor para gestão de contas

### Recursos da Mochila
- Mostra apenas itens de inventário
- Extrai valores "de objetos"
- Útil para análise da mochila

## 💾 Resultados e Arquivos Salvos

### Localização dos Arquivos

```
GUARDADOS/
├── KINGDOM_results_20260602_143022.txt
├── KINGDOM_results_20260602_145015.txt
└── KINGDOM_results_20260603_101530.txt
```

### Formato do Arquivo

```
Nickname: Account_1
Nível de cidade: 15
Nível de depósito: 18
Comida: 45.0K
Madeira: 35.1K
Pedra: 26.8K
Ouro: 6.1K
---
Nickname: Account_2
Nível de cidade: 15
Nível de depósito: 18
Comida: 41.2K
Madeira: 35.1K
Pedra: 26.8K
Ouro: 6.1K
---
```

### Como Usar os Resultados

1. Abra o arquivo `.txt` em um editor
2. Copie os dados que você precisa
3. Cole na sua ferramenta de gestão
4. Os apelidos são gerados automaticamente

---

## 🆘 Solução de Problemas

### "Não foi possível detectar 4 valores"
- Problema de qualidade da imagem - tente uma imagem mais clara
- Os números devem ser legíveis
- Tente recortar ou refazer a captura
- Ajuste o brilho se os números estiverem escuros

### "Erro: X imagens selecionadas mas Y contas válidas"
- A quantidade de imagens não corresponde às contas válidas
- Verifique os números de início/fim e os bloqueados
- Use a fórmula: (fim - início + 1) - bloqueados = total necessário
- Adicione ou remova imagens para corresponder

### "Erro de atualização"
- Verifique a conexão com a Internet
- Tente novamente em alguns minutos
- Reinicie o aplicativo se o erro persistir
- Verifique as configurações do firewall

### As imagens não são processadas
- Verifique se o reino está selecionado
- Verifique se todos os campos numéricos estão preenchidos
- Garanta que a quantidade de imagens corresponda às contas esperadas
- Tente visualizar a imagem para verificar a qualidade do OCR

### "Não é possível abrir a janela"
- Outra instância pode estar em execução
- Feche as janelas existentes e tente novamente
- Tente executar como Administrador

---

## 🔄 Sistema de Atualização

### Automático
- O aplicativo **verifica novas versões na inicialização**
- Se uma atualização estiver disponível, aparece uma notificação
- Download automático do servidor configurado
- Instalação sem intervenção

### Manual
- Execute `actualizar.bat` na pasta de instalação
- Ele atualiza diretamente da fonte configurada

### O que é atualizado
- `kingdoms/` → novos templates
- `Iconos/` → novos ícones
- versão .exe → das Releases

---

## 📋 Níveis Disponíveis

### Nível de Cidade (Mercado)
- Intervalo: 1 a 25
- Aplica-se a todos os recursos
- Salvo nos resultados



### Nível do Depósito (Armazém)
- Intervalo: 1 a 25
- Armazenamento disponível
- Salvo nos resultados



### Tecnologia Máxima
- Afeta a capacidade de recursos
- Referência no aplicativo



---

## 🎯 Exemplo Completo

**Cenário:** Você tem 5 contas, quer recursos totais

1. **Prepare as capturas**
   - Tire 5 capturas de tela (uma por conta)
   - Transfira para o PC
   - Salve em uma pasta acessível

2. **Configure o app**
   - Adicionar Imagens → selecione 5
   - Reino → escolha o correto
   - Número de início: 1
   - Número de fim: 5
   - Números bloqueados: (vazio)
   - Nível de cidade: 15
   - Nível de depósito: 18

3. **Processe**
   - Clique em `Recursos Totais`
   - Aguarde a conclusão
   - Você verá o progresso em %

4. **Resultados**
   - Arquivo salvo automaticamente
   - Abra `GUARDADOS/REINO_results_*.txt`
   - Copie os dados para sua ferramenta
