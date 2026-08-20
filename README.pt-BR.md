# Biblioteca de Casos DWSIM

[English](README.md) | **Português**

Uma coleção comunitária de casos de processos industriais reais modelados no [DWSIM](https://dwsim.org): destilação de cru, hidrotratamento, processamento de gás, sistemas de separação e reação, e muito mais. Cada caso documenta o processo, as escolhas termodinâmicas, as dicas de ajuste e convergência e, quando permitido, uma comparação com dados de planta ou de software comercial e o próprio arquivo de fluxograma do DWSIM.

O objetivo é simples: encurtar a curva de aprendizado de novos usuários e mostrar o que o DWSIM faz em problemas industriais, usando exemplos contribuídos por engenheiros que de fato operam esses processos.

## O que entra aqui

- Casos de processo com contexto suficiente para que outro engenheiro os reproduza.
- As escolhas de pacote termodinâmico e o raciocínio por trás delas.
- Notas práticas de ajuste e convergência (estimativas iniciais, parâmetros do solver, o que observar).
- Opcional: o arquivo de fluxograma do DWSIM (`.dwxmz`).
- Opcional: uma comparação dos resultados do DWSIM com dados de planta ou de outro simulador, **somente quando você tem permissão para publicar essa comparação** (veja [Confidencialidade e licenciamento](#confidencialidade-e-licenciamento)).

## O que não entra aqui

- Dados de planta confidenciais ou proprietários que você não tem o direito de publicar.
- Comparações de benchmark que a licença de uma ferramenta comercial proíbe publicar.
- Dados pessoais de qualquer tipo.
- Dúvidas de suporte. Use o [DWSIM Discussions](https://github.com/DanWBR/dwsim10/discussions) para isso.

## Navegar pelos casos

| Categoria | Pasta | Exemplos |
|---|---|---|
| Destilação de cru e a vácuo | [`cases/crude-distillation`](cases/crude-distillation) | torre atmosférica, torre de vácuo |
| Conversão de refino | [`cases/refining-conversion`](cases/refining-conversion) | FCC, reforma, coqueamento, alquilação |
| Hidrotratamento e hidrocraqueamento | [`cases/hydrotreating`](cases/hydrotreating) | HDS de diesel, hidrotratamento de nafta |
| Processamento de gás | [`cases/gas-processing`](cases/gas-processing) | desidratação, adoçamento com amina, recuperação de LGN |
| Captura e uso de carbono | [`cases/carbon-capture`](cases/carbon-capture) | captura de CO2 com amina, transporte e armazenamento |
| Processos de separação | [`cases/separation-processes`](cases/separation-processes) | destilação, absorção, extração |
| Sistemas de reação | [`cases/reaction-systems`](cases/reaction-systems) | reatores, cinética, equilíbrio |
| Bioprocessos | [`cases/bioprocesses`](cases/bioprocesses) | digestão anaeróbia, fermentação, biogás |
| Eletrólitos e sistemas aquosos | [`cases/electrolytes-and-aqueous`](cases/electrolytes-and-aqueous) | água ácida, gás ácido, salmouras, água do mar |
| Energia limpa | [`cases/clean-energy`](cases/clean-energy) | células a combustível, eletrolisadores, hidrogênio |
| Escoamento de fluidos e tubulação | [`cases/fluid-flow-and-piping`](cases/fluid-flow-and-piping) | redes de tubulação, hidráulica, alívio |
| Integração energética e utilidades | [`cases/heat-integration-utilities`](cases/heat-integration-utilities) | redes de trocadores, fornos, chillers, vapor |
| Outros processos | [`cases/other`](cases/other) | qualquer coisa que não se encaixe acima |

Cada caso é uma pasta com um `README.md` construído a partir do [modelo de caso](templates/CASE_TEMPLATE.md), mais os arquivos que ele precisar.

### Casos publicados

| Caso | Categoria | Destaques |
|---|---|---|
| [Controle de ponto de orvalho de gás natural (JT auto-refrigerado)](cases/gas-processing/natural-gas-dew-point-control) | gas-processing | trocador gás-gás + válvula JT fechados com reciclo; recuperação de LGN; C5 no gás de venda cai pela metade |
| [Ciclo de refrigeração a propano (malha fechada)](cases/heat-integration-utilities/propane-refrigeration-cycle) | heat-integration-utilities | primeira lei fecha < 0,01 %; COP 2,62 |
| [Planta de hidrogênio por reforma a vapor de metano](cases/reaction-systems/steam-methane-reforming-h2) | reaction-systems | dois reatores de Gibbs (reformador + shift); 89 % de conversão de CH4; balanço de carbono exato |
| [Síntese de amônia, passe único](cases/reaction-systems/ammonia-synthesis-single-pass) | reaction-systems | limitada pelo equilíbrio a 200 bar / 700 K; balanços atômicos H/N exatos |
| [Síntese de metanol a partir de gás de síntese](cases/reaction-systems/methanol-synthesis-syngas) | reaction-systems | reator de Gibbs + destilação; destilado com 99,8 mol% de MeOH |
| [Destilaria de etanol](cases/separation-processes/ethanol-distillery) | separation-processes | fermentação → degaseificação → coluna de 25 estágios; destilado abaixo do azeótropo |
| [Destilação benzeno/tolueno com preaquecimento](cases/separation-processes/benzene-toluene-distillation) | separation-processes | preaquecedor especificado por UA; 99,99 % no topo / 99,98 % no fundo |
| [Biogás para a rede](cases/bioprocesses/biogas-to-grid) | bioprocesses | digestor anaeróbio + upgrader de amina; caminho do H2S verificado de ponta a ponta |
| [Turbina hidrelétrica com recuperação de calor](cases/clean-energy/hydroelectric-heat-recovery) | clean-energy | 20,8 kW = ṁ·g·h·η exato |
| [Hidrogênio verde: solar + eletrólise](cases/clean-energy/green-hydrogen-solar-electrolysis) | clean-energy | produção de H2 na lei de Faraday; ~48 kWh/kg |

Esses dez casos são gerados e verificados continuamente por testes automatizados no repositório do DWSIM (`tests/DWSIM.FluentAPI.Tests/Samples`): cada fluxograma é construído pela fluent API, resolvido, checado quanto à consistência física, salvo e depois recarregado e re-resolvido a partir do arquivo salvo.

## Contribuir com um caso

Dois jeitos, escolha o que for mais confortável:

1. **Formulário web (sem git).** Abra uma issue de [Envio de caso](../../issues/new?template=case-submission-pt.yml) e preencha os campos. Um mantenedor transforma em uma pasta de caso.
2. **Pull request.** Copie o [`templates/CASE_TEMPLATE.md`](templates/CASE_TEMPLATE.md) para a pasta da categoria certa, preencha, adicione seus arquivos e abra um PR.

Leia o [CONTRIBUTING.pt-BR.md](CONTRIBUTING.pt-BR.md) antes. Ele cobre o checklist de confidencialidade, os campos do modelo, a nomeação e como os casos são revisados.

## Verificado vs comunidade

- Casos de **comunidade** são publicados como enviados. São úteis, mas não foram checados de forma independente.
- Casos **verificados** foram reproduzidos por um mantenedor ou por um segundo contribuidor: o fluxograma abre, resolve e bate com os resultados relatados. Casos verificados ganham um selo e aparecem primeiro em cada categoria.

Os critérios de verificação estão em [VERIFICATION.pt-BR.md](VERIFICATION.pt-BR.md).

## Confidencialidade e licenciamento

Isto importa, por favor leia antes de enviar.

- **Publique só o que você tem permissão de publicar.** Dado de planta real costuma ser confidencial. Se não puder compartilhar valores absolutos, compartilhe a forma do problema: vazões normalizadas, erros relativos, tendências. Anonimize nomes de correntes, de sites e qualquer detalhe identificável.
- **Comparações com software comercial.** Algumas licenças de simulador restringem a publicação de comparações de benchmark. Verifique sua licença antes de publicar números de Aspen, HYSYS, PRO/II ou similares. Na dúvida, descreva o acordo de forma qualitativa em vez de publicar a saída bruta do concorrente.
- **Licença do que você envia.** Os textos e figuras dos casos são publicados sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Os arquivos de fluxograma do DWSIM que você anexar são compartilhados para outros abrirem e aprenderem. Ao enviar, você confirma que tem o direito de publicar o material e concorda com estes termos. Veja [LICENSE.pt-BR.md](LICENSE.pt-BR.md).

## Relação com o FOSSEE

O [projeto de fluxogramas DWSIM do FOSSEE](https://dwsim.fossee.in/) já hospeda um grande conjunto de fluxogramas contribuídos por usuários, com relatórios, e é um ótimo lugar para olhar e contribuir. Esta biblioteca é complementar: foca em casos industriais com notas de ajuste e, quando possível, comparações com dados reais ou comerciais. Se o seu caso se encaixa melhor no FOSSEE, contribua lá também.

## Aviso

Os casos aqui são fornecidos como estão pelos seus contribuidores, para fins educacionais e de referência. Não são entregas de engenharia validadas. Não os use para decisões de projeto, segurança ou operação sem verificação independente.
