
# 모든코인 상승장? 하락장?
> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.


|Key Name|Description|
|------|---|
|opeing_price|최근 24시간 내 시작 거래금액|
|closing_price|최근 24시간 내 마지막 거래금액|
|min_price|최근 24시간 내 최저 거래금액|
|max_price|최근 24시간 내 최고 거래금액|


```python
import requests
import pprint
url = "https://api.bithumb.com/public/ticker/all"
data = requests.get(url).json()['data']
pprint.pprint(data)
```

    {'ABT': {'24H_fluctate': '6',
             '24H_fluctate_rate': '2.04',
             'average_price': '301.5452',
             'buy_price': '298',
             'closing_price': '300',
             'max_price': '318',
             'min_price': '284',
             'opening_price': '294',
             'sell_price': '300',
             'units_traded': '1573092.88581994',
             'volume_1day': '1573092.88581994',
             'volume_7day': '10457421.661381080946111547'},
     'ADA': {'24H_fluctate': '3.4',
             '24H_fluctate_rate': '3.63',
             'average_price': '96.0375',
             'buy_price': '96.1',
             'closing_price': '96.9',
             'max_price': '103',
             'min_price': '91.3',
             'opening_price': '93.5',
             'sell_price': '96.7',
             'units_traded': '6520407.8417137',
             'volume_1day': '6520407.8417137',
             'volume_7day': '63783938.8751128'},
     'AE': {'24H_fluctate': '1',
            '24H_fluctate_rate': '0.19',
            'average_price': '533.6007',
            'buy_price': '522',
            'closing_price': '522',
            'max_price': '570',
            'min_price': '505',
            'opening_price': '521',
            'sell_price': '525',
            'units_traded': '438498.30798956',
            'volume_1day': '438498.30798956',
            'volume_7day': '2528006.191261433528959624'},
     'AMO': {'24H_fluctate': '-0.01',
             '24H_fluctate_rate': '-1.53',
             'average_price': '0.6409',
             'buy_price': '0.63',
             'closing_price': '0.64',
             'max_price': '0.66',
             'min_price': '0.61',
             'opening_price': '0.65',
             'sell_price': '0.64',
             'units_traded': '327093612.77887477',
             'volume_1day': '327093612.77887477',
             'volume_7day': '3305617842.482424469475093072'},
     'ANKR': {'24H_fluctate': '0.3',
              '24H_fluctate_rate': '2.85',
              'average_price': '10.5452',
              'buy_price': '10.6',
              'closing_price': '10.8',
              'max_price': '11',
              'min_price': '10.1',
              'opening_price': '10.5',
              'sell_price': '10.8',
              'units_traded': '92739257.18100425',
              'volume_1day': '92739257.18100425',
              'volume_7day': '683916743.537400687930143084'},
     'APIS': {'24H_fluctate': '0.17',
              '24H_fluctate_rate': '10.24',
              'average_price': '1.7339',
              'buy_price': '1.75',
              'closing_price': '1.83',
              'max_price': '1.9',
              'min_price': '1.66',
              'opening_price': '1.66',
              'sell_price': '1.83',
              'units_traded': '65039823.95299579',
              'volume_1day': '65039823.95299579',
              'volume_7day': '300755658.896510022513315604'},
     'ARN': {'24H_fluctate': '12',
             '24H_fluctate_rate': '2.29',
             'average_price': '546.1745',
             'buy_price': '526',
             'closing_price': '536',
             'max_price': '586',
             'min_price': '516',
             'opening_price': '524',
             'sell_price': '536',
             'units_traded': '285220.40802498',
             'volume_1day': '285220.40802498',
             'volume_7day': '1681584.9049294'},
     'AUTO': {'24H_fluctate': '-0.03',
              '24H_fluctate_rate': '-1.80',
              'average_price': '1.6686',
              'buy_price': '1.63',
              'closing_price': '1.63',
              'max_price': '1.73',
              'min_price': '1.62',
              'opening_price': '1.66',
              'sell_price': '1.67',
              'units_traded': '27156140.32465438',
              'volume_1day': '27156140.32465438',
              'volume_7day': '314263817.308813603262875436'},
     'BAT': {'24H_fluctate': '0',
             '24H_fluctate_rate': '0.00',
             'average_price': '291.4758',
             'buy_price': '276',
             'closing_price': '282',
             'max_price': '305',
             'min_price': '276',
             'opening_price': '282',
             'sell_price': '280',
             'units_traded': '570666.87572239',
             'volume_1day': '570666.87572239',
             'volume_7day': '8683750.730817355292766026'},
     'BCD': {'24H_fluctate': '332',
             '24H_fluctate_rate': '17.55',
             'average_price': '2178.989',
             'buy_price': '2187',
             'closing_price': '2223',
             'max_price': '2367',
             'min_price': '1872',
             'opening_price': '1891',
             'sell_price': '2220',
             'units_traded': '832026.57852728',
             'volume_1day': '832026.57852728',
             'volume_7day': '1594255.99282278'},
     'BCH': {'24H_fluctate': '31200',
             '24H_fluctate_rate': '9.11',
             'average_price': '368672.1922',
             'buy_price': '372200',
             'closing_price': '373500',
             'max_price': '393600',
             'min_price': '338000',
             'opening_price': '342300',
             'sell_price': '373000',
             'units_traded': '38333.6372498',
             'volume_1day': '38333.6372498',
             'volume_7day': '215764.2077531'},
     'BHP': {'24H_fluctate': '6',
             '24H_fluctate_rate': '0.34',
             'average_price': '1766.0594',
             'buy_price': '1734',
             'closing_price': '1740',
             'max_price': '1871',
             'min_price': '1680',
             'opening_price': '1734',
             'sell_price': '1736',
             'units_traded': '708297.75468545',
             'volume_1day': '708297.75468545',
             'volume_7day': '1456472.02053679'},
     'BSV': {'24H_fluctate': '12300',
             '24H_fluctate_rate': '8.68',
             'average_price': '150968.5415',
             'buy_price': '154100',
             'closing_price': '154000',
             'max_price': '163600',
             'min_price': '138400',
             'opening_price': '141700',
             'sell_price': '154600',
             'units_traded': '77104.59332257',
             'volume_1day': '77104.59332257',
             'volume_7day': '297027.19538424'},
     'BTC': {'24H_fluctate': '608000',
             '24H_fluctate_rate': '4.95',
             'average_price': '12761076.6713',
             'buy_price': '12868000',
             'closing_price': '12868000',
             'max_price': '13451000',
             'min_price': '12110000',
             'opening_price': '12260000',
             'sell_price': '12869000',
             'units_traded': '12434.159896',
             'volume_1day': '12434.159896',
             'volume_7day': '90002.84789265'},
     'BTG': {'24H_fluctate': '1100',
             '24H_fluctate_rate': '3.92',
             'average_price': '29515.501',
             'buy_price': '29160',
             'closing_price': '29150',
             'max_price': '30800',
             'min_price': '27800',
             'opening_price': '28050',
             'sell_price': '29320',
             'units_traded': '23508.53470297',
             'volume_1day': '23508.53470297',
             'volume_7day': '240128.36575974'},
     'BTT': {'24H_fluctate': '0.03',
             '24H_fluctate_rate': '2.23',
             'average_price': '1.3616',
             'buy_price': '1.36',
             'closing_price': '1.37',
             'max_price': '1.53',
             'min_price': '1.21',
             'opening_price': '1.34',
             'sell_price': '1.37',
             'units_traded': '362446384.17570319',
             'volume_1day': '362446384.17570319',
             'volume_7day': '1521571836.38589899'},
     'BZNT': {'24H_fluctate': '0.3',
              '24H_fluctate_rate': '1.34',
              'average_price': '22.7511',
              'buy_price': '22.6',
              'closing_price': '22.6',
              'max_price': '23.4',
              'min_price': '22',
              'opening_price': '22.3',
              'sell_price': '22.8',
              'units_traded': '4303530.66816213',
              'volume_1day': '4303530.66816213',
              'volume_7day': '88414336.078611064867138655'},
     'CMT': {'24H_fluctate': '1',
             '24H_fluctate_rate': '1.59',
             'average_price': '63.7834',
             'buy_price': '63.5',
             'closing_price': '63.8',
             'max_price': '67.7',
             'min_price': '60.6',
             'opening_price': '62.8',
             'sell_price': '63.7',
             'units_traded': '11593914.15065267',
             'volume_1day': '11593914.15065267',
             'volume_7day': '321663693.622124548568758734'},
     'CON': {'24H_fluctate': '0.3',
             '24H_fluctate_rate': '2.17',
             'average_price': '14.0621',
             'buy_price': '14',
             'closing_price': '14.1',
             'max_price': '14.5',
             'min_price': '13.7',
             'opening_price': '13.8',
             'sell_price': '14.1',
             'units_traded': '142203116.61831457',
             'volume_1day': '142203116.61831457',
             'volume_7day': '1188620142.098098126919498287'},
     'CTXC': {'24H_fluctate': '9',
              '24H_fluctate_rate': '1.86',
              'average_price': '498.4561',
              'buy_price': '492',
              'closing_price': '492',
              'max_price': '514',
              'min_price': '480',
              'opening_price': '483',
              'sell_price': '495',
              'units_traded': '388793.73722177',
              'volume_1day': '388793.73722177',
              'volume_7day': '8879336.594546649042605382'},
     'DAC': {'24H_fluctate': '0',
             '24H_fluctate_rate': '0.17',
             'average_price': '5.8001',
             'buy_price': '5.65',
             'closing_price': '5.71',
             'max_price': '6.04',
             'min_price': '5.53',
             'opening_price': '5.7',
             'sell_price': '5.71',
             'units_traded': '25410342.36820895',
             'volume_1day': '25410342.36820895',
             'volume_7day': '815960101.689098645147710247'},
     'DACC': {'24H_fluctate': '0.01',
              '24H_fluctate_rate': '6.25',
              'average_price': '0.1647',
              'buy_price': '0.16',
              'closing_price': '0.17',
              'max_price': '0.17',
              'min_price': '0.15',
              'opening_price': '0.16',
              'sell_price': '0.17',
              'units_traded': '403089352.24839411',
              'volume_1day': '403089352.24839411',
              'volume_7day': '2766889854.52124614'},
     'DASH': {'24H_fluctate': '9900',
              '24H_fluctate_rate': '6.44',
              'average_price': '159789.4947',
              'buy_price': '163300',
              'closing_price': '163400',
              'max_price': '170000',
              'min_price': '149100',
              'opening_price': '153500',
              'sell_price': '163500',
              'units_traded': '1040203.59706835',
              'volume_1day': '1040203.59706835',
              'volume_7day': '11266722.90049985'},
     'ELF': {'24H_fluctate': '8',
             '24H_fluctate_rate': '5.09',
             'average_price': '161.4948',
             'buy_price': '162',
             'closing_price': '165',
             'max_price': '170',
             'min_price': '154',
             'opening_price': '157',
             'sell_price': '165',
             'units_traded': '1089895.22880696',
             'volume_1day': '1089895.22880696',
             'volume_7day': '10592604.264624397487223412'},
     'ENJ': {'24H_fluctate': '-2',
             '24H_fluctate_rate': '-1.65',
             'average_price': '120.1553',
             'buy_price': '118',
             'closing_price': '119',
             'max_price': '126',
             'min_price': '115',
             'opening_price': '121',
             'sell_price': '119',
             'units_traded': '15869662.65508712',
             'volume_1day': '15869662.65508712',
             'volume_7day': '69340593.706997812374310654'},
     'EOS': {'24H_fluctate': '0',
             '24H_fluctate_rate': '0.00',
             'average_price': '5185.0973',
             'buy_price': '5110',
             'closing_price': '5120',
             'max_price': '5345',
             'min_price': '4973',
             'opening_price': '5120',
             'sell_price': '5120',
             'units_traded': '2148498.12391653',
             'volume_1day': '2148498.12391653',
             'volume_7day': '17628925.67139707'},
     'ETC': {'24H_fluctate': '325',
             '24H_fluctate_rate': '4.93',
             'average_price': '6771.7669',
             'buy_price': '6875',
             'closing_price': '6905',
             'max_price': '7105',
             'min_price': '6430',
             'opening_price': '6580',
             'sell_price': '6905',
             'units_traded': '111028.95458467',
             'volume_1day': '111028.95458467',
             'volume_7day': '804130.248156791870193793'},
     'ETH': {'24H_fluctate': '7100',
             '24H_fluctate_rate': '2.66',
             'average_price': '275259.5966',
             'buy_price': '272700',
             'closing_price': '273500',
             'max_price': '284900',
             'min_price': '262900',
             'opening_price': '266400',
             'sell_price': '273400',
             'units_traded': '112490.48786265',
             'volume_1day': '112490.48786265',
             'volume_7day': '610589.705887078849461332'},
     'ETHOS': {'24H_fluctate': '4',
               '24H_fluctate_rate': '2.66',
               'average_price': '152.2278',
               'buy_price': '151',
               'closing_price': '154',
               'max_price': '160',
               'min_price': '144',
               'opening_price': '150',
               'sell_price': '153',
               'units_traded': '2835560.69848567',
               'volume_1day': '2835560.69848567',
               'volume_7day': '45223318.30223607'},
     'ETZ': {'24H_fluctate': '10',
             '24H_fluctate_rate': '3.46',
             'average_price': '302.8588',
             'buy_price': '298',
             'closing_price': '299',
             'max_price': '318',
             'min_price': '286',
             'opening_price': '289',
             'sell_price': '299',
             'units_traded': '1225279.5309824',
             'volume_1day': '1225279.5309824',
             'volume_7day': '18466682.651887551552491321'},
     'GNT': {'24H_fluctate': '2',
             '24H_fluctate_rate': '2.71',
             'average_price': '76.1292',
             'buy_price': '75.8',
             'closing_price': '75.8',
             'max_price': '80',
             'min_price': '73.3',
             'opening_price': '73.8',
             'sell_price': '77.9',
             'units_traded': '509642.63444313',
             'volume_1day': '509642.63444313',
             'volume_7day': '5937652.545275536012054078'},
     'GTO': {'24H_fluctate': '0.4',
             '24H_fluctate_rate': '1.46',
             'average_price': '27.7067',
             'buy_price': '27.6',
             'closing_price': '27.7',
             'max_price': '29.5',
             'min_price': '26.3',
             'opening_price': '27.3',
             'sell_price': '27.7',
             'units_traded': '2922210.57227256',
             'volume_1day': '2922210.57227256',
             'volume_7day': '27888346.41323324'},
     'GXC': {'24H_fluctate': '119',
             '24H_fluctate_rate': '6.46',
             'average_price': '1918.9114',
             'buy_price': '1907',
             'closing_price': '1959',
             'max_price': '2055',
             'min_price': '1761',
             'opening_price': '1840',
             'sell_price': '1959',
             'units_traded': '135252.69833304',
             'volume_1day': '135252.69833304',
             'volume_7day': '1669696.95963179'},
     'HC': {'24H_fluctate': '96',
            '24H_fluctate_rate': '2.42',
            'average_price': '4183.4887',
            'buy_price': '4051',
            'closing_price': '4053',
            'max_price': '4500',
            'min_price': '3835',
            'opening_price': '3957',
            'sell_price': '4059',
            'units_traded': '316198.3504668',
            'volume_1day': '316198.3504668',
            'volume_7day': '4509909.35918372'},
     'HDAC': {'24H_fluctate': '-0.3',
              '24H_fluctate_rate': '-0.98',
              'average_price': '30.5916',
              'buy_price': '30.3',
              'closing_price': '30.2',
              'max_price': '32.5',
              'min_price': '28.8',
              'opening_price': '30.5',
              'sell_price': '30.7',
              'units_traded': '2876303.9598944',
              'volume_1day': '2876303.9598944',
              'volume_7day': '34721684.23004786'},
     'HYC': {'24H_fluctate': '0.02',
             '24H_fluctate_rate': '0.30',
             'average_price': '10.008',
             'buy_price': '9.88',
             'closing_price': '9.91',
             'max_price': '10.4',
             'min_price': '9.73',
             'opening_price': '9.88',
             'sell_price': '9.91',
             'units_traded': '61420863.92570955',
             'volume_1day': '61420863.92570955',
             'volume_7day': '1413869520.371760941'},
     'ICX': {'24H_fluctate': '2',
             '24H_fluctate_rate': '0.58',
             'average_price': '343.1201',
             'buy_price': '341',
             'closing_price': '341',
             'max_price': '357',
             'min_price': '332',
             'opening_price': '339',
             'sell_price': '346',
             'units_traded': '372349.11308365',
             'volume_1day': '372349.11308365',
             'volume_7day': '3714817.41305403393693958'},
     'INS': {'24H_fluctate': '3',
             '24H_fluctate_rate': '0.67',
             'average_price': '455.3885',
             'buy_price': '445',
             'closing_price': '446',
             'max_price': '488',
             'min_price': '426',
             'opening_price': '443',
             'sell_price': '446',
             'units_traded': '333363.02240741',
             'volume_1day': '333363.02240741',
             'volume_7day': '8542772.4102807144'},
     'IOST': {'24H_fluctate': '0.6',
              '24H_fluctate_rate': '5.21',
              'average_price': '11.9695',
              'buy_price': '11.9',
              'closing_price': '12.1',
              'max_price': '13',
              'min_price': '11',
              'opening_price': '11.5',
              'sell_price': '12.1',
              'units_traded': '4374745.13162112',
              'volume_1day': '4374745.13162112',
              'volume_7day': '39880331.797591936210584287'},
     'ITC': {'24H_fluctate': '2',
             '24H_fluctate_rate': '0.57',
             'average_price': '355.6175',
             'buy_price': '346',
             'closing_price': '349',
             'max_price': '375',
             'min_price': '323',
             'opening_price': '347',
             'sell_price': '348',
             'units_traded': '1496686.59698889',
             'volume_1day': '1496686.59698889',
             'volume_7day': '22389445.097999064799285311'},
     'KNC': {'24H_fluctate': '10',
             '24H_fluctate_rate': '4.60',
             'average_price': '224.2995',
             'buy_price': '224',
             'closing_price': '227',
             'max_price': '247',
             'min_price': '213',
             'opening_price': '217',
             'sell_price': '226',
             'units_traded': '603304.07595415',
             'volume_1day': '603304.07595415',
             'volume_7day': '5465619.01439698425300172'},
     'LBA': {'24H_fluctate': '-0.8',
             '24H_fluctate_rate': '-2.58',
             'average_price': '31.1657',
             'buy_price': '30.1',
             'closing_price': '30.2',
             'max_price': '32.3',
             'min_price': '30.2',
             'opening_price': '31',
             'sell_price': '30.2',
             'units_traded': '9095348.87089058',
             'volume_1day': '9095348.87089058',
             'volume_7day': '96667635.33813059765145354'},
     'LINK': {'24H_fluctate': '10',
              '24H_fluctate_rate': '0.21',
              'average_price': '4676.3821',
              'buy_price': '4562',
              'closing_price': '4588',
              'max_price': '4940',
              'min_price': '4434',
              'opening_price': '4578',
              'sell_price': '4583',
              'units_traded': '356976.44063995',
              'volume_1day': '356976.44063995',
              'volume_7day': '5133129.714514809153537911'},
     'LOOM': {'24H_fluctate': '6.1',
              '24H_fluctate_rate': '7.39',
              'average_price': '87.2111',
              'buy_price': '88.6',
              'closing_price': '88.6',
              'max_price': '91.5',
              'min_price': '81.9',
              'opening_price': '82.5',
              'sell_price': '90.5',
              'units_traded': '475680.87968112',
              'volume_1day': '475680.87968112',
              'volume_7day': '4427647.153480573999395522'},
     'LRC': {'24H_fluctate': '0',
             '24H_fluctate_rate': '0.00',
             'average_price': '73.2002',
             'buy_price': '71.3',
             'closing_price': '71.2',
             'max_price': '80.8',
             'min_price': '70.1',
             'opening_price': '71.2',
             'sell_price': '73.9',
             'units_traded': '581064.17988488',
             'volume_1day': '581064.17988488',
             'volume_7day': '5610021.087529428809595789'},
     'LTC': {'24H_fluctate': '1200',
             '24H_fluctate_rate': '1.12',
             'average_price': '108565.9376',
             'buy_price': '107000',
             'closing_price': '107400',
             'max_price': '112200',
             'min_price': '103500',
             'opening_price': '106200',
             'sell_price': '107400',
             'units_traded': '21740.191698',
             'volume_1day': '21740.191698',
             'volume_7day': '175816.59769662'},
     'MCO': {'24H_fluctate': '35',
             '24H_fluctate_rate': '0.57',
             'average_price': '6058.7761',
             'buy_price': '6020',
             'closing_price': '6105',
             'max_price': '6300',
             'min_price': '5790',
             'opening_price': '6070',
             'sell_price': '6085',
             'units_traded': '44030.41554906',
             'volume_1day': '44030.41554906',
             'volume_7day': '256235.30326217'},
     'MITH': {'24H_fluctate': '0.3',
              '24H_fluctate_rate': '0.62',
              'average_price': '47.0548',
              'buy_price': '47.5',
              'closing_price': '48.1',
              'max_price': '49.4',
              'min_price': '45.4',
              'opening_price': '47.8',
              'sell_price': '48.1',
              'units_traded': '3192484.60997159',
              'volume_1day': '3192484.60997159',
              'volume_7day': '15599479.569708808527223843'},
     'MIX': {'24H_fluctate': '-0.7',
             '24H_fluctate_rate': '-1.04',
             'average_price': '67.1719',
             'buy_price': '66.5',
             'closing_price': '66.6',
             'max_price': '69.6',
             'min_price': '64.3',
             'opening_price': '67.3',
             'sell_price': '67',
             'units_traded': '2813600.91355097',
             'volume_1day': '2813600.91355097',
             'volume_7day': '40539489.010999805620073668'},
     'MTL': {'24H_fluctate': '136',
             '24H_fluctate_rate': '6.96',
             'average_price': '2070.9794',
             'buy_price': '2092',
             'closing_price': '2090',
             'max_price': '2313',
             'min_price': '1877',
             'opening_price': '1954',
             'sell_price': '2110',
             'units_traded': '138507.06332698',
             'volume_1day': '138507.06332698',
             'volume_7day': '638040.09100034'},
     'NPXS': {'24H_fluctate': '0.03',
              '24H_fluctate_rate': '4.05',
              'average_price': '0.775',
              'buy_price': '0.76',
              'closing_price': '0.77',
              'max_price': '0.82',
              'min_price': '0.71',
              'opening_price': '0.74',
              'sell_price': '0.77',
              'units_traded': '530201963.4406872',
              'volume_1day': '530201963.4406872',
              'volume_7day': '3212915068.192432208350640193'},
     'OCN': {'24H_fluctate': '0.06',
             '24H_fluctate_rate': '1.90',
             'average_price': '3.2509',
             'buy_price': '3.22',
             'closing_price': '3.21',
             'max_price': '3.46',
             'min_price': '3.09',
             'opening_price': '3.15',
             'sell_price': '3.27',
             'units_traded': '13036119.88647508',
             'volume_1day': '13036119.88647508',
             'volume_7day': '150471486.591734292031302212'},
     'OMG': {'24H_fluctate': '2',
             '24H_fluctate_rate': '0.10',
             'average_price': '1879.1051',
             'buy_price': '1845',
             'closing_price': '1845',
             'max_price': '1960',
             'min_price': '1774',
             'opening_price': '1843',
             'sell_price': '1853',
             'units_traded': '545075.38676232',
             'volume_1day': '545075.38676232',
             'volume_7day': '3232636.919083838164636937'},
     'ORBS': {'24H_fluctate': '-0.09',
              '24H_fluctate_rate': '-0.33',
              'average_price': '29.7349',
              'buy_price': '29.5',
              'closing_price': '29.6',
              'max_price': '31',
              'min_price': '28.6',
              'opening_price': '29.7',
              'sell_price': '29.6',
              'units_traded': '14430480.75467003',
              'volume_1day': '14430480.75467003',
              'volume_7day': '127336873.810361028319004324'},
     'PAY': {'24H_fluctate': '13',
             '24H_fluctate_rate': '4.94',
             'average_price': '271.0409',
             'buy_price': '276',
             'closing_price': '276',
             'max_price': '290',
             'min_price': '255',
             'opening_price': '263',
             'sell_price': '277',
             'units_traded': '215080.53693513',
             'volume_1day': '215080.53693513',
             'volume_7day': '3346408.22121745684417128'},
     'PIVX': {'24H_fluctate': '255',
              '24H_fluctate_rate': '14.63',
              'average_price': '1975.5066',
              'buy_price': '1931',
              'closing_price': '1997',
              'max_price': '2228',
              'min_price': '1692',
              'opening_price': '1742',
              'sell_price': '1997',
              'units_traded': '78273.62484005',
              'volume_1day': '78273.62484005',
              'volume_7day': '678025.92376624'},
     'PLY': {'24H_fluctate': '0.2',
             '24H_fluctate_rate': '1.49',
             'average_price': '13.726',
             'buy_price': '13.6',
             'closing_price': '13.6',
             'max_price': '14.4',
             'min_price': '13.1',
             'opening_price': '13.4',
             'sell_price': '13.8',
             'units_traded': '39229694.64895893',
             'volume_1day': '39229694.64895893',
             'volume_7day': '308892552.493790235'},
     'POLY': {'24H_fluctate': '6.4',
              '24H_fluctate_rate': '9.96',
              'average_price': '75.2969',
              'buy_price': '70.6',
              'closing_price': '70.6',
              'max_price': '88',
              'min_price': '62.1',
              'opening_price': '64.2',
              'sell_price': '71',
              'units_traded': '16954677.48876957',
              'volume_1day': '16954677.48876957',
              'volume_7day': '40392614.84739352174938958'},
     'POWR': {'24H_fluctate': '0.59',
              '24H_fluctate_rate': '0.60',
              'average_price': '97.9513',
              'buy_price': '97.4',
              'closing_price': '99',
              'max_price': '103',
              'min_price': '92',
              'opening_price': '98.4',
              'sell_price': '99.1',
              'units_traded': '901481.11027166',
              'volume_1day': '901481.11027166',
              'volume_7day': '7567503.35504943'},
     'PPT': {'24H_fluctate': '26',
             '24H_fluctate_rate': '0.76',
             'average_price': '3438.1562',
             'buy_price': '3415',
             'closing_price': '3417',
             'max_price': '3646',
             'min_price': '3169',
             'opening_price': '3391',
             'sell_price': '3447',
             'units_traded': '128559.87162431',
             'volume_1day': '128559.87162431',
             'volume_7day': '1894594.7212553'},
     'PST': {'24H_fluctate': '15',
             '24H_fluctate_rate': '11.45',
             'average_price': '145.0628',
             'buy_price': '147',
             'closing_price': '146',
             'max_price': '157',
             'min_price': '126',
             'opening_price': '131',
             'sell_price': '148',
             'units_traded': '5158718.77842081',
             'volume_1day': '5158718.77842081',
             'volume_7day': '21393943.696764452474168705'},
     'QTUM': {'24H_fluctate': '135',
              '24H_fluctate_rate': '3.58',
              'average_price': '3929.9731',
              'buy_price': '3901',
              'closing_price': '3901',
              'max_price': '4152',
              'min_price': '3691',
              'opening_price': '3766',
              'sell_price': '3911',
              'units_traded': '455587.31840091',
              'volume_1day': '455587.31840091',
              'volume_7day': '3662592.16320776'},
     'RDN': {'24H_fluctate': '69',
             '24H_fluctate_rate': '7.36',
             'average_price': '993.9623',
             'buy_price': '995',
             'closing_price': '1006',
             'max_price': '1116',
             'min_price': '861',
             'opening_price': '937',
             'sell_price': '1006',
             'units_traded': '353299.84651671',
             'volume_1day': '353299.84651671',
             'volume_7day': '1985078.380822857785250504'},
     'REP': {'24H_fluctate': '1500',
             '24H_fluctate_rate': '8.24',
             'average_price': '20597.776',
             'buy_price': '19620',
             'closing_price': '19700',
             'max_price': '24700',
             'min_price': '18030',
             'opening_price': '18200',
             'sell_price': '19690',
             'units_traded': '61060.09375455',
             'volume_1day': '61060.09375455',
             'volume_7day': '186632.862267004532677142'},
     'RNT': {'24H_fluctate': '-0.7',
             '24H_fluctate_rate': '-1.63',
             'average_price': '41.7804',
             'buy_price': '41.8',
             'closing_price': '42.1',
             'max_price': '43.9',
             'min_price': '40.5',
             'opening_price': '42.8',
             'sell_price': '42.1',
             'units_traded': '2178317.78833142',
             'volume_1day': '2178317.78833142',
             'volume_7day': '29868823.313498959215133828'},
     'ROM': {'24H_fluctate': '0.01',
             '24H_fluctate_rate': '25.00',
             'average_price': '0.0447',
             'buy_price': '0.04',
             'closing_price': '0.05',
             'max_price': '0.05',
             'min_price': '0.04',
             'opening_price': '0.04',
             'sell_price': '0.05',
             'units_traded': '1192859012.39808',
             'volume_1day': '1192859012.39808',
             'volume_7day': '19388130956.612640000000000003'},
     'SALT': {'24H_fluctate': '2',
              '24H_fluctate_rate': '0.95',
              'average_price': '212.156',
              'buy_price': '205',
              'closing_price': '211',
              'max_price': '228',
              'min_price': '203',
              'opening_price': '209',
              'sell_price': '211',
              'units_traded': '420098.25884619',
              'volume_1day': '420098.25884619',
              'volume_7day': '2723803.57035264'},
     'SNT': {'24H_fluctate': '0.9',
             '24H_fluctate_rate': '3.75',
             'average_price': '24.7877',
             'buy_price': '24.9',
             'closing_price': '24.9',
             'max_price': '26.1',
             'min_price': '23.7',
             'opening_price': '24',
             'sell_price': '25.1',
             'units_traded': '4846972.1610606',
             'volume_1day': '4846972.1610606',
             'volume_7day': '52986411.83796821656894206'},
     'STEEM': {'24H_fluctate': '3',
               '24H_fluctate_rate': '0.77',
               'average_price': '396.229',
               'buy_price': '388',
               'closing_price': '392',
               'max_price': '412',
               'min_price': '375',
               'opening_price': '389',
               'sell_price': '392',
               'units_traded': '603890.16420702',
               'volume_1day': '603890.16420702',
               'volume_7day': '12069056.74096723'},
     'STRAT': {'24H_fluctate': '88',
               '24H_fluctate_rate': '6.35',
               'average_price': '1481.5773',
               'buy_price': '1472',
               'closing_price': '1473',
               'max_price': '1600',
               'min_price': '1351',
               'opening_price': '1385',
               'sell_price': '1474',
               'units_traded': '253052.1478581',
               'volume_1day': '253052.1478581',
               'volume_7day': '1708174.34160385'},
     'THETA': {'24H_fluctate': '2',
               '24H_fluctate_rate': '1.78',
               'average_price': '114.7004',
               'buy_price': '114',
               'closing_price': '114',
               'max_price': '122',
               'min_price': '110',
               'opening_price': '112',
               'sell_price': '115',
               'units_traded': '708601.31826316',
               'volume_1day': '708601.31826316',
               'volume_7day': '6043668.710096666985828777'},
     'TMTG': {'24H_fluctate': '0.04',
              '24H_fluctate_rate': '1.86',
              'average_price': '2.1827',
              'buy_price': '2.16',
              'closing_price': '2.19',
              'max_price': '2.27',
              'min_price': '2.07',
              'opening_price': '2.15',
              'sell_price': '2.19',
              'units_traded': '48143681.73084638',
              'volume_1day': '48143681.73084638',
              'volume_7day': '283304937.835342867958841878'},
     'TRUE': {'24H_fluctate': '14',
              '24H_fluctate_rate': '2.66',
              'average_price': '553.4947',
              'buy_price': '539',
              'closing_price': '539',
              'max_price': '598',
              'min_price': '515',
              'opening_price': '525',
              'sell_price': '540',
              'units_traded': '573586.49081174',
              'volume_1day': '573586.49081174',
              'volume_7day': '4526428.474098785681782811'},
     'TRX': {'24H_fluctate': '-0.6',
             '24H_fluctate_rate': '-2.04',
             'average_price': '29.3737',
             'buy_price': '28.6',
             'closing_price': '28.7',
             'max_price': '30.3',
             'min_price': '28.4',
             'opening_price': '29.3',
             'sell_price': '28.7',
             'units_traded': '71805825.70775352',
             'volume_1day': '71805825.70775352',
             'volume_7day': '571726052.32302103'},
     'VALOR': {'24H_fluctate': '75',
               '24H_fluctate_rate': '3.06',
               'average_price': '2558.0933',
               'buy_price': '2520',
               'closing_price': '2520',
               'max_price': '2696',
               'min_price': '2403',
               'opening_price': '2445',
               'sell_price': '2573',
               'units_traded': '104380.52444095',
               'volume_1day': '104380.52444095',
               'volume_7day': '1144979.578867059660038435'},
     'VET': {'24H_fluctate': '0.3',
             '24H_fluctate_rate': '4.14',
             'average_price': '7.4273',
             'buy_price': '7.51',
             'closing_price': '7.53',
             'max_price': '7.78',
             'min_price': '7.19',
             'opening_price': '7.23',
             'sell_price': '7.6',
             'units_traded': '14275922.83097113',
             'volume_1day': '14275922.83097113',
             'volume_7day': '138100467.508215197939690796'},
     'WAVES': {'24H_fluctate': '490',
               '24H_fluctate_rate': '22.90',
               'average_price': '2735.6698',
               'buy_price': '2613',
               'closing_price': '2629',
               'max_price': '3250',
               'min_price': '2075',
               'opening_price': '2139',
               'sell_price': '2630',
               'units_traded': '810015.66034027',
               'volume_1day': '810015.66034027',
               'volume_7day': '1407174.05416476'},
     'WAX': {'24H_fluctate': '3.2',
             '24H_fluctate_rate': '5.07',
             'average_price': '64.3618',
             'buy_price': '65.6',
             'closing_price': '66.2',
             'max_price': '70',
             'min_price': '61.9',
             'opening_price': '63',
             'sell_price': '66.2',
             'units_traded': '1870865.10659123',
             'volume_1day': '1870865.10659123',
             'volume_7day': '17542664.34149504'},
     'WET': {'24H_fluctate': '0',
             '24H_fluctate_rate': '0.00',
             'average_price': '15.2704',
             'buy_price': '15',
             'closing_price': '15.1',
             'max_price': '15.8',
             'min_price': '14.8',
             'opening_price': '15.1',
             'sell_price': '15.1',
             'units_traded': '11667296.31374334',
             'volume_1day': '11667296.31374334',
             'volume_7day': '132503912.331412025431120464'},
     'WTC': {'24H_fluctate': '39',
             '24H_fluctate_rate': '1.51',
             'average_price': '2754.479',
             'buy_price': '2604',
             'closing_price': '2608',
             'max_price': '3105',
             'min_price': '2548',
             'opening_price': '2569',
             'sell_price': '2636',
             'units_traded': '230697.95851654',
             'volume_1day': '230697.95851654',
             'volume_7day': '5304718.173220448284851752'},
     'XEM': {'24H_fluctate': '3.1',
             '24H_fluctate_rate': '3.16',
             'average_price': '98.5543',
             'buy_price': '98.4',
             'closing_price': '101',
             'max_price': '104',
             'min_price': '92.7',
             'opening_price': '97.9',
             'sell_price': '101',
             'units_traded': '1093509.99266868',
             'volume_1day': '1093509.99266868',
             'volume_7day': '12199783.33032243'},
     'XLM': {'24H_fluctate': '1',
             '24H_fluctate_rate': '0.89',
             'average_price': '112.3355',
             'buy_price': '112',
             'closing_price': '113',
             'max_price': '117',
             'min_price': '107',
             'opening_price': '112',
             'sell_price': '114',
             'units_traded': '2688510.79163372',
             'volume_1day': '2688510.79163372',
             'volume_7day': '23204333.76321197'},
     'XMR': {'24H_fluctate': '3300',
             '24H_fluctate_rate': '3.36',
             'average_price': '97141.0455',
             'buy_price': '100800',
             'closing_price': '101300',
             'max_price': '107700',
             'min_price': '90300',
             'opening_price': '98000',
             'sell_price': '101500',
             'units_traded': '3966362.84322706',
             'volume_1day': '3966362.84322706',
             'volume_7day': '17506172.048910047431'},
     'XRP': {'24H_fluctate': '0',
             '24H_fluctate_rate': '0.00',
             'average_price': '378.9932',
             'buy_price': '375',
             'closing_price': '376',
             'max_price': '391',
             'min_price': '369',
             'opening_price': '376',
             'sell_price': '376',
             'units_traded': '85478922.35040967',
             'volume_1day': '85478922.35040967',
             'volume_7day': '649110466.19331539'},
     'XVG': {'24H_fluctate': '0.1',
             '24H_fluctate_rate': '0.67',
             'average_price': '14.7085',
             'buy_price': '14.7',
             'closing_price': '15',
             'max_price': '15.7',
             'min_price': '13.9',
             'opening_price': '14.9',
             'sell_price': '15',
             'units_traded': '1718658.81202629',
             'volume_1day': '1718658.81202629',
             'volume_7day': '21725142.38678206'},
     'ZEC': {'24H_fluctate': '2700',
             '24H_fluctate_rate': '2.61',
             'average_price': '105140.0614',
             'buy_price': '105900',
             'closing_price': '106000',
             'max_price': '113300',
             'min_price': '96200',
             'opening_price': '103300',
             'sell_price': '106400',
             'units_traded': '2095.22264529',
             'volume_1day': '2095.22264529',
             'volume_7day': '15711.75840851'},
     'ZIL': {'24H_fluctate': '0.8',
             '24H_fluctate_rate': '4.90',
             'average_price': '16.9617',
             'buy_price': '17',
             'closing_price': '17.1',
             'max_price': '17.5',
             'min_price': '16.3',
             'opening_price': '16.3',
             'sell_price': '17.1',
             'units_traded': '7239620.44215369',
             'volume_1day': '7239620.44215369',
             'volume_7day': '61776527.250081790174'},
     'ZRX': {'24H_fluctate': '42',
             '24H_fluctate_rate': '16.09',
             'average_price': '304.1947',
             'buy_price': '303',
             'closing_price': '303',
             'max_price': '328',
             'min_price': '256',
             'opening_price': '261',
             'sell_price': '305',
             'units_traded': '1591059.56589439',
             'volume_1day': '1591059.56589439',
             'volume_7day': '4534754.471622466409196126'},
     'date': '1563251746896'}
    


```python
for key in data:
    if key != 'date':
        price = float(data[key]['opening_price']) + float(data[key]['max_price']) - float(data[key]['min_price'])
        print(f'{key}는 상승장') if price > float(data[key]['max_price']) else print(f'{key}는 하락장')
```

    BTC는 상승장
    ETH는 상승장
    DASH는 상승장
    LTC는 상승장
    ETC는 상승장
    XRP는 상승장
    BCH는 상승장
    XMR는 상승장
    ZEC는 상승장
    QTUM는 상승장
    BTG는 상승장
    EOS는 상승장
    ICX는 상승장
    VET는 상승장
    TRX는 상승장
    ELF는 상승장
    MITH는 상승장
    MCO는 상승장
    OMG는 상승장
    KNC는 상승장
    GNT는 상승장
    ZIL는 하락장
    ETHOS는 상승장
    PAY는 상승장
    WAX는 상승장
    POWR는 상승장
    LRC는 상승장
    GTO는 상승장
    STEEM는 상승장
    STRAT는 상승장
    ZRX는 상승장
    REP는 상승장
    AE는 상승장
    XEM는 상승장
    SNT는 상승장
    ADA는 상승장
    PPT는 상승장
    CTXC는 상승장
    CMT는 상승장
    THETA는 상승장
    WTC는 상승장
    ITC는 상승장
    TRUE는 상승장
    ABT는 상승장
    RNT는 상승장
    PLY는 상승장
    WAVES는 상승장
    LINK는 상승장
    ENJ는 상승장
    PST는 상승장
    SALT는 상승장
    RDN는 상승장
    LOOM는 상승장
    PIVX는 상승장
    INS는 상승장
    BCD는 상승장
    BZNT는 상승장
    XLM는 상승장
    OCN는 상승장
    BSV는 상승장
    TMTG는 상승장
    BAT는 상승장
    WET는 상승장
    XVG는 상승장
    IOST는 상승장
    POLY는 상승장
    HC는 상승장
    ROM는 하락장
    AMO는 상승장
    ETZ는 상승장
    ARN는 상승장
    APIS는 하락장
    MTL는 상승장
    DACC는 상승장
    DAC는 상승장
    BHP는 상승장
    BTT는 상승장
    HDAC는 상승장
    NPXS는 상승장
    AUTO는 상승장
    GXC는 상승장
    ORBS는 상승장
    VALOR는 상승장
    CON는 상승장
    ANKR는 상승장
    MIX는 상승장
    HYC는 상승장
    LBA는 상승장
    


```python
for coin, coin_data in data.items():
    if type(coin_data) == type(dict()):
        if float(coin_data['opening_price']) - float(coin_data['min_price']) > 0:
            print('상승장')
        else:
            print('하락장')
```

    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    하락장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    하락장
    상승장
    상승장
    상승장
    하락장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    

# 평균점수
> 다음 딕셔너리에서 평균 점수를 출력하라



```python
student = {'python':80, 'algorithm':78, 'django':95, 'flask':80}
print(f'student의 평균점수 : {sum(student.values()) / len(student)}')
```

    student의 평균점수 : 83.25
    


```python
count = 0
total_score = 0
for score in student.values():
    total_score += score
    count += 1
print(total_score/count)
```

    83.25
    

# 혈액형
> 학생들의 혈액형(A,B,O,AB)에 대한 데이터가 리스트에 들어있다. 각 혈액형이 몇명인지 딕셔너리를 만들어 출력하라


```python
blood = ['A','A','B','O','A','B','A','AB','AB','O','A','O','AB','O']
blood_dict = {'A': blood.count('A'), 'B': blood.count('B'), 'O': blood.count('O'), 'AB': blood.count('AB')}
print(blood_dict)
```

    {'A': 5, 'B': 2, 'O': 4, 'AB': 3}
    


```python
a = 0
b = 0
o = 0
ab = 0
for blood_type in blood:
    if blood_type == 'A':
        a += 1
    elif blood_type == 'B':
        b += 1
    elif blood_type == 'AB':
        ab += 1
    elif blood_type == 'O':
        o += 1
print({'A': a, 'B': b, 'O': o, 'AB': ab})
```

    {'A': 5, 'B': 2, 'O': 4, 'AB': 3}
    


```python
# 2번째 방법
blood_dict = {}

# (반복)하나씩 꺼내서 확인한다.
for blood_type in blood:
    # 지금 나온적이 없으면, 키와 value 1로 만든다.
    if blood_type not in blood_dict.keys():
        blood_dict[blood_type] = 1
    else:
        blood_dict[blood_type] += 1
print(blood_dict)
```

    {'A': 5, 'B': 2, 'O': 4, 'AB': 3}
    


```python
{blood_type: blood.count(blood_type) for blood_type in set(blood)}
```




    {'AB': 3, 'O': 4, 'B': 2, 'A': 5}



# UBD
> movies는 영화제목이 key로 누적관객수가 value인 딕셔너리이다. 
>
> 자전차왕 엄복동의 누적관객수는 172212명이고 172212명을 1UBD라고 할때 80UBD를 넘지 못하는 영화를 출력하라.


```python
movies = {
    "7번방의선물":12811206,
    "괴물":13019740,
    "국제시장":14257115,
    "극한직업":16261018,
    "도둑들":12983330,
    "명량":17613682,
    "베테랑":13414009,
    "신과함께-죄와벌":14410754,
    "아바타":13624328,
    "어벤져스:엔드게임":13901423,
}
for key, value in movies.items():
    print(key) if value < 80 * 172212 else None
```

    7번방의선물
    괴물
    도둑들
    베테랑
    아바타
    


```python
print(list(key for key, value in movies.items() if value < 80 * 172212))
```

    ['7번방의선물', '괴물', '도둑들', '베테랑', '아바타']
    


```python
for movie, count in movies.items():
    if count / 172212 < 80:
        print(movie)
```

    7번방의선물
    괴물
    도둑들
    베테랑
    아바타
    
