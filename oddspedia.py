import requests
from datetime import date, timedelta, datetime


hoje = str(date.today())
amanha = str(date.today() + timedelta(1))
url = f'https://oddspedia.com/api/v1/getMatchListNew?geoCode=BR&sport=futebol&popularLeaguesOnly=0&excludeSpecialStatus=0&status=all&sortBy=default&startDate={hoje}T03:00:00Z&endDate={amanha}T02:59:59Z&language=br'
print(url)
bar = requests.get(url)
bar.encoding = 'utf-8'
times = []

for x in range(0, len(bar.json()['data']['matchList'])):
    ID_pais = bar.json()['data']['matchList'][x]['category_id']
    PAIS = bar.json()['data']['categoryList'][str(ID_pais)]['name']

    CASA = bar.json()['data']['matchList'][x]['ht']
    FORA = bar.json()['data']['matchList'][x]['at']

    TEMPO = bar.json()['data']['matchList'][x]['current_time']
    ID = bar.json()['data']['matchList'][x]['league_id']
    LIGA = bar.json()['data']['leagueList'][str(ID)]['name']
    
    # PARA URI
    SLUG = bar.json()['data']['leagueList'][str(ID)]['slug']
    DATA = bar.json()['data']['matchList'][x]['md'].split()[0]    
    
    hora_string = bar.json()['data']['matchList'][x]['md'].split()[-1].split('+')[0]
    HORA = (datetime.strptime(hora_string, '%H:%M:%S') - timedelta(hours=3)).time()

    STATUS = bar.json()['data']['matchList'][x]['inplay_status']

    times.append(CASA)
    times.append(FORA)
    
    print('INDICE:', x)
    print('PAÍS:', PAIS)
    print('CASA:', CASA)
    print('FORA:', FORA)
    print('TEMPO:', TEMPO)
    print('LIGA:', LIGA)
    print('DATA:', DATA)
    print('HORA', HORA)
    print('STATUS:', STATUS)
    print()

##input()
