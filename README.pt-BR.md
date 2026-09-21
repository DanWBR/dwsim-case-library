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
| Treinamento de operadores | [`cases/operator-training`](cases/operator-training) | plantas dinâmicas com alarmes, intertravamentos, telas de operador e cenários pontuados para o Simulador de Treinamento de Operadores |
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
| [Coluna benzeno/tolueno em dinâmica](cases/separation-processes/benzene-toluene-column-dynamics) | separation-processes | hidráulica dos pratos do dimensionamento de internos; controle de nível e pressão num degrau de 10 % na alimentação por uma hora |
| [Partida da coluna benzeno/tolueno](cases/separation-processes/benzene-toluene-column-startup) | separation-processes | de uma coluna vazia e fria a 1 atm ao estado estacionário de projeto em duas horas: enchimento, rampa do refervedor, pressurização, refluxo, malhas de nível em automático |
| [Parada da coluna benzeno/tolueno](cases/separation-processes/benzene-toluene-column-shutdown) | separation-processes | corte da alimentação, rampa do refervedor a zero sob refluxo total, tambor e fundo drenados pelos controladores de nível |
| [Biogás para a rede](cases/bioprocesses/biogas-to-grid) | bioprocesses | digestor anaeróbio + upgrader de amina; caminho do H2S verificado de ponta a ponta |
| [Turbina hidrelétrica com recuperação de calor](cases/clean-energy/hydroelectric-heat-recovery) | clean-energy | 20,8 kW = ṁ·g·h·η exato |
| [Hidrogênio verde: solar + eletrólise](cases/clean-energy/green-hydrogen-solar-electrolysis) | clean-energy | produção de H2 na lei de Faraday; ~48 kWh/kg |
| [Separador gás-líquido: a planta do curso de OTS](cases/operator-training/gas-liquid-separator-ots) | operator-training | malhas de pressão e nível; válvula de alimentação falha aberta em 01:00, H em 02:40, HH em 03:20, trip em 03:25; exercício pontuado, intertravamento e duas telas de operador |
| [Trem de separação em dois estágios com pacote de cenários](cases/operator-training/two-stage-separation-ots) | operator-training | separadores de 30 bar e 8 bar, controlador de nível lendo um transmissor; sete cenários incl. blow-by de gás, com os tempos de alarme medidos; dois relatórios de exemplo |
| [Resfriador de descarga de compressor com vaso de knock-out e pacote de cenários](cases/operator-training/compressor-aftercooler-ots) | operator-training | malha de temperatura no duty de resfriamento; falta de água de resfriamento, transmissores congelado e com deriva, válvula de nível travada, falha de ar; passo de 2 s |
| [Bomba de água de resfriamento com inversor de frequência](cases/fluid-flow-and-piping/pump-variable-frequency-drive) | fluid-flow-and-piping | curvas medidas a 1450 e 1750 rpm, lidas e interpoladas a 1600 rpm: 62,8 m, 69,7 % |
| [Bomba dosadora sob controle de vazão (dinâmico)](cases/fluid-flow-and-piping/dosing-pump-flow-control-dynamics) | fluid-flow-and-piping | bomba de deslocamento positivo em malha de vazão: degrau de 1,894 para 2,6 kg/s, 240 para 329,4 rpm |
| [Anel de combate a incêndio de uma planta de GLP](cases/fluid-flow-and-piping/fire-water-ring-network) | fluid-flow-and-piping | rede de tubulação: anel de 6" e 4", as quatro condições da NBR 15186 e um incêndio aberto por eventos em dinâmica |
| [Compressor booster de gás combustível sobre seu mapa de desempenho](cases/gas-processing/compressor-performance-map) | gas-processing | mapa de altura e rendimento a 8000 / 10000 / 12000 rpm, interpolado a 11000 rpm; 44,0 kW |
| [Turboexpansor de letdown sobre seu mapa de potência medido](cases/gas-processing/turboexpander-performance-map) | gas-processing | mapa de potência a 14000 / 18000 / 22000 rpm; 255,9 kW a 20000 rpm, gás saindo a 255 K |

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
