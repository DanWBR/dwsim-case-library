# Contribuir com um caso

[English](CONTRIBUTING.md) | **Português**

Obrigado por compartilhar seu trabalho. Um bom caso aqui pode poupar dias de outro engenheiro. Este guia mantém os envios consistentes e, tão importante quanto, seguros para publicar.

## Antes de começar: o checklist de confidencialidade

Passe por isto antes de escrever qualquer coisa. Se não puder marcar todos os itens, anonimize o caso ou não o envie.

- [ ] Tenho o direito de publicar esta descrição de processo e estes dados.
- [ ] Nenhum dado de planta confidencial está incluído, ou ele foi normalizado/anonimizado de modo que nada proprietário seja exposto.
- [ ] Qualquer comparação com um simulador comercial é permitida pela licença desse simulador.
- [ ] Nomes de site, nomes de empresa e dados pessoais foram removidos.
- [ ] Sou o autor do fluxograma DWSIM que estou anexando, ou tenho permissão para compartilhá-lo.

Na dúvida, compartilhe a forma do problema em vez dos números brutos: vazões normalizadas, erros relativos e tendências ainda tornam o caso útil sem expor nada.

## O que faz um bom caso

- Uma descrição de processo clara que outro engenheiro consiga seguir.
- O pacote termodinâmico e o motivo da escolha (não só "usei Peng-Robinson").
- Condições operacionais suficientes para reproduzir o resultado.
- Notas honestas de ajuste e convergência, inclusive o que não funcionou.
- Opcional, mas valioso: o arquivo `.dwxmz` e uma comparação com dados de planta ou comerciais.

Um caso curto e bem documentado vale mais que um grande e sem explicação.

## Dois jeitos de enviar

### Formulário web (sem git)

Abra uma issue de **Envio de caso** a partir dos [modelos de issue](../../issues/new/choose) e preencha os campos. Um mantenedor vai transformar em uma pasta de caso e dar o crédito. Este é o caminho mais fácil se você não usa git.

Para anexar o fluxograma: o GitHub não aceita um `.dwxmz` cru na caixa de arrastar e soltar, mas um `.dwxmz` já é um zip, então renomeie para `.zip` (ou compacte) e arraste. Isso só vale para o formulário; um pull request pode commitar o `.dwxmz` direto.

### Pull request

1. Copie `templates/CASE_TEMPLATE.md` para a categoria certa dentro de `cases/`.
2. Renomeie a pasta usando a convenção abaixo.
3. Preencha o modelo. Apague os comentários de orientação.
4. Adicione os arquivos (fluxograma, figuras) na mesma pasta.
5. Abra um pull request.

## Nomeação de pastas e arquivos

- Uma pasta por caso, dentro da categoria correspondente: `cases/<categoria>/<nome-do-caso>/`.
- Nome da pasta do caso: minúsculas, palavras separadas por hífen, descritivo. Exemplo: `atmospheric-crude-unit-40kbpd`.
- O texto é sempre `README.md` dentro dessa pasta.
- Arquivo de fluxograma: `<nome-do-caso>.dwxmz`.
- Figuras: coloque na pasta do caso e referencie com links relativos. Mantenha as imagens em tamanho razoável.

```
cases/
  crude-distillation/
    atmospheric-crude-unit-40kbpd/
      README.md
      atmospheric-crude-unit-40kbpd.dwxmz
      column-profile.png
```

## Categorias

Escolha a mais próxima. Se nada se encaixar, use `other` e sugira uma nova categoria no seu envio.

- `crude-distillation` - destilação atmosférica e a vácuo de petróleo cru.
- `refining-conversion` - craqueamento catalítico, reforma, hidrocraqueamento, coqueamento, alquilação, isomerização.
- `hydrotreating` - hidrotratamento e hidrocraqueamento.
- `gas-processing` - desidratação, adoçamento, recuperação de LGN, GNL.
- `carbon-capture` - captura de CO2, absorção com amina, transporte e armazenamento de CO2.
- `separation-processes` - destilação, absorção, extração, flash, membranas.
- `reaction-systems` - reatores, cinética, equilíbrio, conversão.
- `bioprocesses` - digestão anaeróbia (ADM1), fermentação, biogás, algas, tratamento de efluentes.
- `electrolytes-and-aqueous` - água ácida, gás ácido, salmouras, água do mar, sistemas eletrolíticos.
- `clean-energy` - células a combustível, eletrolisadores, produção de hidrogênio, power-to-X.
- `fluid-flow-and-piping` - trechos de tubulação, redes de tubulação, hidráulica, alívio de pressão, dispositivos de restrição.
- `heat-integration-utilities` - redes de trocadores de calor, fornos, chillers, sistemas de vapor e utilidades.
- `other` - qualquer outra coisa.

## Licenciamento e consentimento

Ao enviar, você concorda que:

- O texto e as figuras do seu caso são publicados sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), para outros reusarem com atribuição.
- Qualquer arquivo de fluxograma DWSIM que você anexar pode ser baixado e aberto por outros para aprendizado.
- Você tem o direito de publicar tudo no envio.

Veja [LICENSE.md](LICENSE.md) para o texto completo.

## Revisão e verificação

1. Um mantenedor confere o envio quanto à completude e ao checklist de confidencialidade.
2. Ele é publicado como caso de **comunidade**.
3. Se um mantenedor ou um segundo contribuidor o reproduzir (o fluxograma abre, resolve e bate com os resultados relatados), ele é promovido a **verificado** e ganha o selo.

Você pode ajudar verificando o caso de outra pessoa: abra o fluxograma, execute e comente na issue ou no PR do caso com o que encontrou.

## Estilo

- Inglês é preferível para a biblioteca continuar útil no mundo todo, mas textos em português ou bilíngues são bem-vindos. Informe o idioma no campo **Language** do caso, e se você escrever em outra língua, um resumo curto em inglês no topo ajuda outros a encontrar o caso. Uma versão em segundo idioma também pode ser adicionada como arquivo extra (por exemplo `README.pt-BR.md` dentro da pasta do caso).
- Use unidades SI e informe o sistema de unidades se você fugir disso.
- Prefira linguagem simples e específica. "A carga do refervedor teve que subir cerca de 8% acima do valor de projeto para bater a especificação de fundo" é mais útil que "foi difícil convergir".
