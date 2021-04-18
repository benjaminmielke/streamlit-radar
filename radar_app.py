import streamlit as st
import requests
import bs4 as bs

st.set_page_config(layout='wide', page_title='Radar Regions', page_icon='https://p1.hiclipart.com/preview/994/283/642/rainmeter-tabbed-dock-grey-and-yellow-lightning-icon-png-clipart.jpg')


@st.cache
def create_dct(lst_icao):
    '''

    '''
    dct = {}
    for a in range(0, len(lst_icao)):
        url1 = f'http://www.gcmap.com/airport/{lst_icao[a]}'
        soup = bs.BeautifulSoup(requests.get(url1).text, 'html.parser')

        city = soup.find('span', {'class': 'locality'}).text
        #region = soup.find('span', {'class': 'region'}).text
        country = soup.find('span', {'class': 'country-name'}).text
        lat = soup.findAll('abbr', {'class': 'latitude'})[0]['title']
        lon = soup.findAll('abbr', {'class': 'longitude'})[0]['title']
        elev = soup.findAll('td', {'colspan': '2'})[9].text

        dct[f'{lst_icao[a]}'] = {'City': f'{city}', 'Country': f'{country}', 'Lat': f'{lat}', 'Lon': f'{lon}', 'Elevation': f'{elev}'}

    return dct


def icao_button(icao_key, dct):
    '''
    '''

    ph_title.title(f'{icao_key} - {(dct.get(icao_key)).get("City")}, {(dct.get(icao_key)).get("Country")}')
    ph_subtitle.markdown(f'Coordinates: {(dct.get(icao_key)).get("Lat")}, {(dct.get(icao_key)).get("Lon")}')
    ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct.get(icao_key)).get("Lat")},{(dct.get(icao_key)).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=0&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    ph_iframe2.markdown(f'<iframe src="https://map.blitzortung.org/#7/{(dct.get(icao_key)).get("Lat")}/{(dct.get(icao_key)).get("Lon")}" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)


def lightning_button(icao_key, dct):
    '''
    '''
    ph_iframe.markdown(f'<iframe src="https://map.blitzortung.org/#2/16.64/19.07" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)



# Lists of operation desk responsible ICAOs
lst_ok1 = ['CYVR', 'CYYZ', 'EDDF', 'EGLL', 'EHAM', 'EKCH', 'EPWA', 'ESSA', 'KJFK', 'KLAX', 'KORD', 'KSEA', 'KSFO', 'LEMD', 'LFPG', 'LGAV', 'LIMC', 'LIRF', 'LKPR', 'LOWW', 'LSZH', 'NZAA', 'OMDB', 'PAFA', 'PGSN', 'PGUM', 'UMMS', 'YMML', 'YSSY', 'PANC', 'PASY', 'UUEE']
lst_ok2 = ['RCKH', 'RCTP', 'RKJJ', 'RKJK', 'RKJY', 'RKNY', 'RKPC', 'RKPK', 'RKPU', 'RKSI', 'RKSS', 'RKTH', 'RKTN', 'RKTU', 'ZBAA', 'ZBAD', 'ZBDT', 'ZBHH', 'ZBOW', 'ZBSJ', 'ZBUL', 'ZBXH', 'ZBXZ', 'ZBYN', 'ZHCC', 'ZHES', 'ZHHH', 'ZHLY', 'ZHSN', 'ZHYC', 'ZLDL', 'ZLGM', 'ZLGY', 'ZLIC', 'ZLLL', 'ZLTS', 'ZLXY', 'ZLYL', 'ZLYS', 'ZMUB', 'ZSAM', 'ZSCG', 'ZSCN', 'ZSFZ', 'ZSHC', 'ZSJG', 'ZSJN', 'ZSNB', 'ZSNJ', 'ZSOF', 'ZSPD', 'ZSQD', 'ZSSS', 'ZSTX', 'ZSWH', 'ZSWY', 'ZSYT', 'ZWKL', 'ZWKM', 'ZWWW']
lst_ok3 = ['VCBI', 'VDPP', 'VDSR', 'VECC', 'VHHH', 'VIDP', 'VLVT', 'VMMC', 'VNKT', 'VRMM', 'VTBS', 'VTCT', 'VTSG', 'VTSM', 'VTSP', 'VVDN', 'VVNB', 'VVTS', 'VYMD', 'VYYY', 'ZGDY', 'ZGGG', 'ZGHA', 'ZGHZ', 'ZGNN', 'ZGOW', 'ZGSD', 'ZGSZ', 'ZJHK', 'ZPDQ', 'ZPJH', 'ZPMS', 'ZPPP', 'ZUBD', 'ZUBJ', 'ZUBZ', 'ZUCK', 'ZUDC', 'ZUDX', 'ZUGU', 'ZUGY', 'ZUHY', 'ZUJZ', 'ZULB', 'ZULS', 'ZULZ', 'ZUMT', 'ZUMY', 'ZUNZ', 'ZUPS', 'ZUTR', 'ZUUU', 'ZUWX', 'ZUXC', 'ZUYB', 'ZUYI', 'ZUZH', 'ZUZY']
lst_ok4 = ['OPIS', 'OPKC', 'WADD', 'WAHI', 'WARR', 'WIII', 'WIOO', 'WMKK', 'WSSS', 'ZYCC', 'ZYDD', 'ZYDQ', 'ZYHB', 'ZYJM', 'ZYJS', 'ZYQQ', 'ZYTL', 'ZYTN', 'ZYTX', 'ZYYJ']
lst_sjn = ['RJAA', 'RJAF', 'RJAH', 'RJAW', 'RJBB', 'RJBE', 'RJCB', 'RJCC', 'RJCH', 'RJCK', 'RJCM', 'RJDB', 'RJEC', 'RJFF', 'RJFK', 'RJFM', 'RJFO', 'RJFS', 'RJFT', 'RJFU', 'RJGG', 'RJKA', 'RJNA', 'RJNK', 'RJNS', 'RJNT', 'RJOA', 'RJOB', 'RJOC', 'RJOM', 'RJOO', 'RJOt', 'RJSA', 'RJSC', 'RJSI', 'RJSK', 'RJSM', 'RJSN', 'RJSS', 'RJTT', 'ROAH', 'ROIG']

# Build the dictionaries
dct_ok1 = create_dct(lst_ok1)
dct_ok2 = create_dct(lst_ok2)
dct_ok3 = create_dct(lst_ok3)
dct_ok4 = create_dct(lst_ok4)
dct_sjn = create_dct(lst_sjn)

# Build the app

st.markdown("""
<style>
body {
    color: #000;
    background-color: #e8f4ff;
}
</style>
    """, unsafe_allow_html=True)


ph_title = st.empty()
ph_subtitle = st.empty()
ph_iframe = st.empty()
ph_iframe2 = st.empty()


ph_title.title('World')
ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=16.0458,-338.7305,3&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
ph_iframe2.markdown(f'<iframe src="https://map.blitzortung.org/#2/16.64/19.07" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)

# if cols_body[1].button('Radar'):
#     ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=16.0458,-338.7305,3&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)



# cols_data[0].button('Radar')
# cols_data[1].button('Lightning')
# cols_data[2].button('Satellite')

st.sidebar.title('Select Region 地域選択')
region = st.sidebar.selectbox('',
                              ('------------------------------------>>', 'OK1', 'OK2', 'OK3', 'OK4', 'SJN'))
st.markdown(
    """
<style>
.css-1aumxhk {
background-color: #ededed;
background-image: none;
color: #000000
}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------OK1-----------------------------------------------
if region == 'OK1':
    cols = st.sidebar.beta_columns(3)
    cols_data = st.sidebar.beta_columns(3)
    if cols[0].button(f'Europe'):
        ph_title.title(f'Europe')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=49.0523,-338.6865,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="3" style="border:2;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'CONUS'):
        ph_title.title(f'CONUS')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=39.113,-455.7129,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'Oceania'):
        ph_title.title(f'Oceania')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=-28.5942,-575.1563,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok1)-1:
        cols = st.sidebar.beta_columns(3)
        cols_data = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok1.keys())[i]}'):
                icao_button(lst_ok1[i], dct_ok1)
            # if cols_data[0].button('Lightning'):
            #     lightning_button(lst_ok1[i], dct_ok1)
            if cols[1].button(f'{list(dct_ok1.keys())[i+1]}'):
                icao_button(lst_ok1[i+1], dct_ok1)
            if cols[2].button(f'{list(dct_ok1.keys())[i+2]}'):
                icao_button(lst_ok1[i+2], dct_ok1)
        except IndexError:
            pass
        i = i+3

# ----------------------------OK2------------------------------------------------
if region == 'OK2':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Korea'):
        ph_title.title(f'Korea')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=36.7521,-233.1189,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'N China'):
        ph_title.title(f'NE China')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=42.7228,-239.4141,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'E China'):
        ph_title.title(f'E China')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=35.6662,-246.6431,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok2)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok2.keys())[i]}'):
                icao_button(lst_ok2[i], dct_ok2)
            if cols[1].button(f'{list(dct_ok2.keys())[i+1]}'):
                icao_button(lst_ok2[i+1], dct_ok2)
            if cols[2].button(f'{list(dct_ok2.keys())[i+2]}'):
                icao_button(lst_ok2[i+2], dct_ok2)
        except IndexError:
            pass
        i = i+3

# ----------------------------OK3------------------------------------------------
if region == 'OK3':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Indochina'):
        ph_title.title(f'Indochina')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=13.5018,-255.2563,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'S China'):
        ph_title.title(f'SE China')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=22.761,-250.5212,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'India'):
        ph_title.title(f'India')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=24.3971,-277.2949,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok3)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok3.keys())[i]}'):
                icao_button(lst_ok3[i], dct_ok3)
            if cols[1].button(f'{list(dct_ok3.keys())[i+1]}'):
                icao_button(lst_ok3[i+1], dct_ok3)
            if cols[2].button(f'{list(dct_ok3.keys())[i+2]}'):
                icao_button(lst_ok3[i+2], dct_ok3)
        except IndexError:
            pass
        i = i+3

# ----------------------------OK4------------------------------------------------
if region == 'OK4':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Java'):
        ph_title.title(f'Java')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=-7.6729,-248.2471,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'Malaysia'):
        ph_title.title(f'Malaysia')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=1.1755,-251.543,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'Russia'):
        ph_title.title(f'W Russia')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=58.3672,-314.3848,5&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_ok4)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_ok4.keys())[i]}'):
                icao_button(lst_ok4[i], dct_ok4)
            if cols[1].button(f'{list(dct_ok4.keys())[i+1]}'):
                icao_button(lst_ok4[i+1], dct_ok4)
            if cols[2].button(f'{list(dct_ok4.keys())[i+2]}'):
                icao_button(lst_ok4[i+3], dct_ok4)
        except IndexError:
            pass
        i = i+3


# ----------------------------SJN------------------------------------------------
if region == 'SJN':
    cols = st.sidebar.beta_columns(3)
    if cols[0].button(f'Japan'):
        ph_title.title(f'Japan')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=38.5911,-221.9019,6&oFa=1&oC=0&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=0&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[1].button(f'N Japan'):
        ph_title.title('North Japan')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=34.4567,-224.2749,7&oFa=1&oC=0&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=0&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if cols[2].button(f'S Japan'):
        ph_title.title(f'South Japan')
        ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc=41.2984,-217.8699,7&oFa=1&oC=0&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=0&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    i = 0
    while i <= len(dct_sjn)-1:
        cols = st.sidebar.beta_columns(3)
        try:
            if cols[0].button(f'{list(dct_sjn.keys())[i]}'):
                icao_button(lst_sjn[i], dct_sjn)
            if cols[1].button(f'{list(dct_sjn.keys())[i+1]}'):
                icao_button(lst_sjn[i+1], dct_sjn)
            if cols[2].button(f'{list(dct_sjn.keys())[i+2]}'):
                icao_button(lst_sjn[i+2], dct_sjn)
        except IndexError:
            pass
        i = i+3
