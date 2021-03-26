import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(layout='wide', page_title='Radar Regions', page_icon='https://p1.hiclipart.com/preview/994/283/642/rainmeter-tabbed-dock-grey-and-yellow-lightning-icon-png-clipart.jpg')


@st.cache
def create_dct(lst_icao):
    '''

    '''
    dct = {}
    for a in range(0, len(lst_icao)):
        url1 = f'http://www.gcmap.com/airport/{lst_icao[a]}'
        soup = BeautifulSoup(requests.get(url1).text, 'lxml')

        city = soup.find('span', {'class': 'locality'}).text
        #region = soup.find('span', {'class': 'region'}).text
        country = soup.find('span', {'class': 'country-name'}).text
        lat = soup.findAll('abbr', {'class': 'latitude'})[0]['title']
        lon = soup.findAll('abbr', {'class': 'longitude'})[0]['title']
        elev = soup.findAll('td', {'colspan': '2'})[9].text

        dct[f'{lst_icao[a]}'] = {'City': f'{city}', 'Country': f'{country}', 'Lat': f'{lat}', 'Lon': f'{lon}', 'Elevation': f'{elev}'}

    return dct


# Lists of operation desk responsible ICAOs
lst_ok1 = ['EDDF', 'EGLL', 'EHAM', 'EKCH', 'EPWA', 'ESSA', 'KJFK', 'KLAX', 'KORD', 'KSEA', 'KSFO', 'LEMD', 'LFPG', 'LGAV', 'LIMC', 'LIRF', 'LKPR', 'LOWW', 'LSZH', 'NZAA', 'OMDB', 'PAFA', 'UMMS', 'YMML', 'YSSY', 'PANC', 'PASY', 'UUEE']
lst_ok2 = ['RCKH', 'RCTP', 'RKJJ', 'RKJK', 'RKJY', 'RKNY', 'RKPC', 'RKPK', 'RKPU', 'RKSI', 'RKSS', 'RKTH', 'RKTN', 'RKTU', 'ZBAA', 'ZBAD', 'ZBDT', 'ZBHH', 'ZBOW', 'ZBSJ', 'ZBUL', 'ZBXH', 'ZBXZ', 'ZBYN', 'ZHCC', 'ZHES', 'ZHHH', 'ZHLY', 'ZHSN', 'ZHYC', 'ZLDL', 'ZLGM', 'ZLGY', 'ZLIC', 'ZLLL', 'ZLTS', 'ZLXY', 'ZLYL', 'ZLYS', 'ZMUB', 'ZSAM', 'ZSCG', 'ZSCN', 'ZSFZ', 'ZSHC', 'ZSJG', 'ZSJN', 'ZSNB', 'ZSNJ', 'ZSOF', 'ZSPD', 'ZSQD', 'ZSSS', 'ZSTX', 'ZSWH', 'ZSWY', 'ZSYT', 'ZWKL', 'ZWKM', 'ZWWW']
lst_ok3 = ['VCBI', 'VDPP', 'VDSR', 'VECC', 'VHHH', 'VIDP', 'VLVT', 'VMMC', 'VNKT', 'VRMM', 'VTBS', 'VTCT', 'VTSG', 'VTSM', 'VTSP', 'VVDN', 'VVNB', 'VVTS', 'VYMD', 'VYYY', 'ZGGG', 'ZGHA', 'ZGHZ', 'ZGNN', 'ZGOW', 'ZGSZ', 'ZJHK', 'ZPDQ', 'ZPJH', 'ZPMS', 'ZPPP', 'ZUBD', 'ZUBJ', 'ZUBZ', 'ZUCK', 'ZUDC', 'ZUDX', 'ZUGU', 'ZUGY', 'ZUHY', 'ZUJZ', 'ZULB', 'ZULS', 'ZULZ', 'ZUMT', 'ZUMY', 'ZUNZ', 'ZUPS', 'ZUTR', 'ZUUU', 'ZUWX', 'ZUXC', 'ZUYB', 'ZUYI', 'ZUZH', 'ZUZY', ]
lst_ok4 = ['OPIS', 'OPKC', 'WADD', 'WAHI', 'WARR', 'WIII', 'WIOO', 'WMKK', 'WSSS', 'ZYCC', 'ZYDD', 'ZYDQ', 'ZYHB', 'ZYJM', 'ZYJS', 'ZYQQ', 'ZYTL', 'ZYTN', 'ZYTX', 'ZYYJ']

# Build the dictionaries
dct_ok1 = create_dct(lst_ok1)
dct_ok2 = create_dct(lst_ok2)
dct_ok3 = create_dct(lst_ok3)
dct_ok4 = create_dct(lst_ok4)

# Build the app
placeholder1 = st.empty()
placeholder3 = st.empty()
placeholder4 = st.empty()
placeholder2 = st.empty()

placeholder1.title('World')
placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=26.8241,-351.7383,3&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
st.sidebar.title('Select Region')
region = st.sidebar.selectbox('',
                              ('------------------------------------>>', 'OK1', 'OK2', 'OK3', 'OK4'))

# ----------------------------OK1-----------------------------------------------
if region == 'OK1':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Europe'):
        placeholder1.title(f'Europe')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=49.0523,-338.6865,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'CONUS'):
        placeholder1.title(f'CONUS')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=39.113,-455.7129,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'Oceania'):
        placeholder1.title(f'Oceania')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=-28.5942,-575.1563,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok1)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok1.keys())[i]}'):
                placeholder1.title(f'{lst_ok1[i]} - {(dct_ok1.get(lst_ok1[i])).get("City")}, {(dct_ok1.get(lst_ok1[i])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok1.get(lst_ok1[i])).get("Lat")}, {(dct_ok1.get(lst_ok1[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok1.get(lst_ok1[i])).get("Lat")},{(dct_ok1.get(lst_ok1[i])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[1].button(f'{list(dct_ok1.keys())[i+1]}'):
                placeholder1.title(f'{lst_ok1[i]} - {(dct_ok1.get(lst_ok1[i+1])).get("City")}, {(dct_ok1.get(lst_ok1[i+1])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok1.get(lst_ok1[i])).get("Lat")}, {(dct_ok1.get(lst_ok1[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok1.get(lst_ok1[i+1])).get("Lat")},{(dct_ok1.get(lst_ok1[i+1])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[2].button(f'{list(dct_ok1.keys())[i+2]}'):
                placeholder1.title(f'{lst_ok1[i]} - {(dct_ok1.get(lst_ok1[i+2])).get("City")}, {(dct_ok1.get(lst_ok1[i+2])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok1.get(lst_ok1[i])).get("Lat")}, {(dct_ok1.get(lst_ok1[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok1.get(lst_ok1[i+2])).get("Lat")},{(dct_ok1.get(lst_ok1[i+2])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
        except IndexError:
            pass
        i = i+3

# ----------------------------OK2------------------------------------------------
if region == 'OK2':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Korea'):
        placeholder1.title(f'Korea')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=36.7521,-233.1189,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'N China'):
        placeholder1.title(f'NE China')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=42.7228,-239.4141,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'E China'):
        placeholder1.title(f'E China')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=35.6662,-246.6431,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok2)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok2.keys())[i]}'):
                placeholder1.title(f'{lst_ok2[i]} - {(dct_ok2.get(lst_ok2[i])).get("City")}, {(dct_ok2.get(lst_ok2[i])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok2.get(lst_ok2[i])).get("Lat")}, {(dct_ok2.get(lst_ok2[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok2.get(lst_ok2[i])).get("Lat")},{(dct_ok2.get(lst_ok2[i])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[1].button(f'{list(dct_ok2.keys())[i+1]}'):
                placeholder1.title(f'{lst_ok2[i]} - {(dct_ok2.get(lst_ok2[i+1])).get("City")}, {(dct_ok2.get(lst_ok2[i+1])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok2.get(lst_ok2[i])).get("Lat")}, {(dct_ok2.get(lst_ok2[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok2.get(lst_ok2[i+1])).get("Lat")},{(dct_ok2.get(lst_ok2[i+1])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[2].button(f'{list(dct_ok2.keys())[i+2]}'):
                placeholder1.title(f'{lst_ok2[i]} - {(dct_ok2.get(lst_ok2[i+2])).get("City")}, {(dct_ok2.get(lst_ok2[i+2])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok2.get(lst_ok2[i])).get("Lat")}, {(dct_ok2.get(lst_ok2[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok2.get(lst_ok2[i+2])).get("Lat")},{(dct_ok2.get(lst_ok2[i+2])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
        except IndexError:
            pass
        i = i+3

# ----------------------------OK3------------------------------------------------
if region == 'OK3':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Indochina'):
        placeholder1.title(f'Indochina')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=13.5018,-255.2563,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'S China'):
        placeholder1.title(f'SE China')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=22.761,-250.5212,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'India'):
        placeholder1.title(f'India')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=24.3971,-277.2949,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok3)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok3.keys())[i]}'):
                placeholder1.title(f'{lst_ok3[i]} - {(dct_ok3.get(lst_ok3[i])).get("City")}, {(dct_ok3.get(lst_ok3[i])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok3.get(lst_ok3[i])).get("Lat")}, {(dct_ok3.get(lst_ok3[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok3.get(lst_ok3[i])).get("Lat")},{(dct_ok3.get(lst_ok3[i])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[1].button(f'{list(dct_ok3.keys())[i+1]}'):
                placeholder1.title(f'{lst_ok3[i]} - {(dct_ok3.get(lst_ok3[i+1])).get("City")}, {(dct_ok3.get(lst_ok3[i+1])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok3.get(lst_ok3[i])).get("Lat")}, {(dct_ok3.get(lst_ok3[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok3.get(lst_ok3[i+1])).get("Lat")},{(dct_ok3.get(lst_ok3[i+1])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[2].button(f'{list(dct_ok3.keys())[i+2]}'):
                placeholder1.title(f'{lst_ok3[i]} - {(dct_ok3.get(lst_ok3[i+2])).get("City")}, {(dct_ok3.get(lst_ok3[i+2])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok3.get(lst_ok3[i])).get("Lat")}, {(dct_ok3.get(lst_ok3[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok3.get(lst_ok3[i+2])).get("Lat")},{(dct_ok3.get(lst_ok3[i+2])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
        except IndexError:
            pass
        i = i+3

# ----------------------------OK4------------------------------------------------
if region == 'OK4':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Java'):
        placeholder1.title(f'Java')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=-7.6729,-248.2471,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'Malaysia'):
        placeholder1.title(f'Malaysia')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=1.1755,-251.543,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'Russia'):
        placeholder1.title(f'W Russia')
        placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=58.3672,-314.3848,5&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok4)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok4.keys())[i]}'):
                placeholder1.title(f'{lst_ok4[i]} - {(dct_ok4.get(lst_ok4[i])).get("City")}, {(dct_ok4.get(lst_ok4[i])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok4.get(lst_ok4[i])).get("Lat")}, {(dct_ok4.get(lst_ok4[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok4.get(lst_ok4[i])).get("Lat")},{(dct_ok4.get(lst_ok4[i])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[1].button(f'{list(dct_ok4.keys())[i+1]}'):
                placeholder1.title(f'{lst_ok4[i]} - {(dct_ok4.get(lst_ok4[i+1])).get("City")}, {(dct_ok4.get(lst_ok4[i+1])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok4.get(lst_ok4[i])).get("Lat")}, {(dct_ok4.get(lst_ok4[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok4.get(lst_ok4[i+1])).get("Lat")},{(dct_ok4.get(lst_ok4[i+1])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
            if cols[2].button(f'{list(dct_ok4.keys())[i+2]}'):
                placeholder1.title(f'{lst_ok4[i]} - {(dct_ok4.get(lst_ok4[i+2])).get("City")}, {(dct_ok4.get(lst_ok4[i+2])).get("Country")}')
                placeholder3.markdown(f'Coordinates: {(dct_ok4.get(lst_ok4[i])).get("Lat")}, {(dct_ok4.get(lst_ok4[i])).get("Lon")}')
                placeholder2.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct_ok4.get(lst_ok4[i+2])).get("Lat")},{(dct_ok4.get(lst_ok4[i+2])).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
        except IndexError:
            pass
        i = i+3
