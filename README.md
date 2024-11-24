# Gerador de Escala de Dança

![Ícone do Aplicativo](icone_danca.ico)

## Descrição

O **Gerador de Escala de Dança** é um aplicativo desktop desenvolvido em Python que ajuda a organizar e gerar automaticamente uma escala de dança mensal com base em regras de negócio específicas. O aplicativo permite que usuários gerem a escala e salvem-na em formato PDF diretamente na pasta Downloads do seu computador.

## Funcionalidades

- **Geração Automática de Escalas:** Cria escalas de dança mensais considerando adultos e crianças, com regras de rotação e participação específica.
- **Interface Gráfica Intuitiva:** Desenvolvido com Tkinter, oferece uma interface amigável para interação fácil.
- **Exportação para PDF:** Salva a escala gerada automaticamente na pasta Downloads do usuário em formato PDF.
- **Personalização de Ícone:** Possui um ícone personalizado para uma melhor identificação visual.

## Pré-requisitos

Antes de executar o aplicativo, certifique-se de que seu sistema atende aos seguintes requisitos:

- **Sistema Operacional:** Windows, macOS ou Linux
- **Python:** Versão 3.6 ou superior instalada no sistema
- **Git:** Para clonar o repositório

## Instalação

Siga os passos abaixo para configurar e executar o **Gerador de Escala de Dança** no seu computador.

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu computador usando o Git. Abra o terminal ou prompt de comando e execute:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
Substitua https://github.com/seu-usuario/seu-repositorio.git pelo URL real do seu repositório.

### 2. Navegar até o Diretório do Projeto
Acesse o diretório clonado:

```bash
cd seu-repositorio
```
### 3. Criar um Ambiente Virtual (venv)
É recomendável criar um ambiente virtual para gerenciar as dependências do projeto. Execute os seguintes comandos:

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No macOS e Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Instalar as Dependências
Com o ambiente virtual ativado, instale as dependências necessárias usando o requirements.txt:

```bash
pip install -r requirements.txt
```
### 5. Gerar o Executável
Para criar um executável do aplicativo, utilize o PyInstaller. Certifique-se de que o PyInstaller está instalado no seu ambiente virtual. Se não estiver, instale-o:

```bash
pip install pyinstaller
```
Em seguida, execute o comando abaixo para gerar o executável:

```bash
pyinstaller --onefile --windowed --icon=icone_danca.ico escala_danca.py
```

### Uso
Após a conclusão, o executável estará disponível na pasta dist que será gerada no diretório do projeto.
