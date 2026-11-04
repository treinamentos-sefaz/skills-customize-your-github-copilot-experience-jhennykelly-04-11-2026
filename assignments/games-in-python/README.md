
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras em Python, praticando manipulação de strings, loops, condicionais e seleção aleatória.

## 📝 Tarefas

### 🛠️ Seleção da Palavra e Estado Inicial

#### Descrição
Escolha aleatoriamente uma palavra da lista predefinida e prepare as variáveis que controlam o estado do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente da lista `words` usando `random`.
- Inicializar as letras já tentadas e o número de tentativas incorretas permitidas.

### 🛠️ Loop Principal e Progresso

#### Descrição
Implemente o loop que recebe palpites de letras do jogador e exibe o progresso atual da palavra.

#### Requisitos
O programa concluído deve:

- Aceitar um palpite de letra por vez via `input()`.
- Mostrar o progresso atual no formato `_ _ _`, revelando as letras já acertadas.
- Exemplo de saída para a palavra `python` após o palpite `p`:
  ```
  Progresso: p _ _ _ _ _
  ```

### 🛠️ Verificação de Palpites e Tentativas

#### Descrição
Atualize o estado do jogo a cada palpite e controle as tentativas incorretas restantes.

#### Requisitos
O programa concluído deve:

- Registrar cada letra tentada, sem contar repetições como erro.
- Descontar uma tentativa sempre que a letra não existir na palavra.
- Encerrar o jogo quando todas as letras forem reveladas ou quando as tentativas se esgotarem.

### 🛠️ Mensagens de Vitória e Derrota

#### Descrição
Ao final da partida, informe ao jogador se ele venceu ou perdeu.

#### Requisitos
O programa concluído deve:

- Exibir uma mensagem de vitória quando a palavra for adivinhada.
- Exibir uma mensagem de derrota, incluindo a palavra secreta, quando as tentativas se esgotarem.