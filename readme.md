<img src="https://media.discordapp.net/attachments/1191142569845989407/1191148524184797405/elysian_banner.jpg?ex=65a46282&is=6591ed82&hm=02e26829204164e982e62f587dbd4d849ae78a13fff4bbf6eb33aa876f266ab4&=&format=webp&width=1080&height=390">

## Pré-requisitos

Antes de começar, siga estas etapas:

1. **Crie um Bot no Discord Developer Portal**: Acesse o [Discord Developer Portal](https://discord.com/developers/applications) e crie um novo bot. Lembre-se de salvar o Token gerado.

2. **Ative as Intents**: No Discord Developer Portal, na seção "Bot", ative as Intents necessárias para que o bot funcione corretamente.

3. **Convide o Bot**: Use o link de convite gerado no portal para convidar o bot para o seu servidor Discord.

## Configuração do Ambiente
Siga estas etapas para configurar o ambiente e executar o bot:

1. **Baixe esse repositório**: clone ou baixe o repositório da seguinte forma:

<img src="https://media.discordapp.net/attachments/1191142569845989407/1191142942094667806/image.png?ex=65a45d4f&is=6591e84f&hm=b5d280bdf5cf325e9de0af88faaf3c36efa6e6176b40349e779ad11b62eac1ca&=&format=webp&quality=lossless">

2. **Instale o Python**: Se você ainda não tiver o Python instalado, você pode fazê-lo com o seguinte comando (se estiver usando o Termux em um celular):
   
   ```bash
   pkg install python3
   ```
caso não esteja usando o termux acesse __[python](https://www.python.org/)__ para instalar.

3. **Instale as Dependências**:
   Abra o terminal e navegue até a pasta do projeto. Use o seguinte comando para instalar as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

   Isso instalará as bibliotecas py-cord, python-dotenv.

4. **Configure o Token do Bot**:
   na raiz do projeto terá um arquivo com o nome `example.env` basta renomear para `.env` e Adicionar o token do seu bot nesse arquivo:

   ```
   TOKEN=seu_token_aqui
   ```

5. **Configurações Adicionais**:
   Na pasta "settings", você encontrará um arquivo chamado `config.py`. Nele, você pode configurar o prefixo do bot em `PREFIX`. o bot também suporta comandos de barra (slash commands).

## Executando o Bot

Agora, você está pronto para executar o bot. No terminal, execute o seguinte comando:

```bash
python main.py
```

fazendo isso o bot estará online em seu servidor e pronto para responder aos comandos.

Divirta-se usando a base da elysian em seu servidor! Se você tiver alguma dúvida ou precisar de assistência adicional, sinta-se à vontade para perguntar no [servidor](https://discord.gg/Mbj3bmRPKk)

<a href="https://discord.gg/Mbj3bmRPKk"><img src="https://img.shields.io/discord/1065760715442495559?label=Gold3nUniversus&logo=discord&style=for-the-badge">
</a>

CREDITOS:

- icones: polvolunarck
- desenvolvedores: Gold3nMoon
- emojis: reddeadredemptiom3