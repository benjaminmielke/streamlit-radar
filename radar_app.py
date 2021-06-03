import streamlit as st
import requests
import bs4 as bs
import webbrowser
import pandas as pd

# Build the app
st.set_page_config(layout='wide', page_title='Radar Regions', page_icon='https://p1.hiclipart.com/preview/994/283/642/rainmeter-tabbed-dock-grey-and-yellow-lightning-icon-png-clipart.jpg')

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
ph_subtitle2 = st.empty()
ph_iframe = st.empty()
ph_iframe2 = st.empty()

st.sidebar.title('Select Region 地域選択')
region = st.sidebar.selectbox('',
                              ('------------------------------------>>', 'JGP', 'OK1', 'OK2', 'OK3', 'OK4', 'SG1', 'SG2', 'SG3', 'SG4', 'SGD', 'SJD', 'SJN'))
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


@st.cache
def create_dct(lst_icao):
    '''

    '''
    dct = {}
    for a in range(0, len(lst_icao)):
        url1 = f'http://www.gcmap.com/airport/{lst_icao[a]}'
        soup = bs.BeautifulSoup(requests.get(url1).text, 'html.parser')

        try:
            city = soup.find('span', {'class': 'locality'}).text
            #region = soup.find('span', {'class': 'region'}).text
            country = soup.find('span', {'class': 'country-name'}).text
            lat = soup.findAll('abbr', {'class': 'latitude'})[0]['title']
            lon = soup.findAll('abbr', {'class': 'longitude'})[0]['title']
            elev = soup.findAll('td', {'colspan': '2'})[9].text
            try:
                tz = soup.findAll('abbr', {'class': 'tz'})[0]['title']
            except IndexError:
                pass
        except AttributeError:
            pass
        except IndexError:
            pass
       

        try:
            dct[f'{lst_icao[a]}'] = {'City': city, 'Country': country, 'Lat': round(float(lat), 2), 'Lon': round(float(lon), 2), 'Elevation': elev, 'Timezone': f'UTC{tz}'}
        except UnboundLocalError:
            pass

    return dct


@st.cache
def connect_gs():
    '''
    '''
    # Import Master list
    df_master_list = pd.read_csv('Duty_Regions_Master_List.csv')

    dct = {}
    dct['jgp'] = [x for x in df_master_list['JGP'] if str(x) != 'nan']
    dct['ok1'] = [x for x in df_master_list['OK1'] if str(x) != 'nan']
    dct['ok2'] = [x for x in df_master_list['OK2'] if str(x) != 'nan']
    dct['ok3'] = [x for x in df_master_list['OK3'] if str(x) != 'nan']
    dct['ok4'] = [x for x in df_master_list['OK4'] if str(x) != 'nan']
    dct['sg1'] = [x for x in df_master_list['SG1'] if str(x) != 'nan']
    dct['sg2'] = [x for x in df_master_list['SG2'] if str(x) != 'nan']
    dct['sg3'] = [x for x in df_master_list['SG3'] if str(x) != 'nan']
    dct['sg4'] = [x for x in df_master_list['SG4'] if str(x) != 'nan']
    dct['sgd'] = [x for x in df_master_list['SGD'] if str(x) != 'nan']
    dct['sja'] = [x for x in df_master_list['SJA'] if str(x) != 'nan']
    dct['sjd'] = [x for x in df_master_list['SJD'] if str(x) != 'nan']
    dct['sjn'] = [x for x in df_master_list['SJN'] if str(x) != 'nan']

    return dct


def radar_button(icao_key, dct):
    '''
    '''
    ph_title.title(f'{icao_key} - {(dct.get(icao_key)).get("City")}, {(dct.get(icao_key)).get("Country")}')
    ph_subtitle.markdown(f'''**Coordinates:** {(dct.get(icao_key)).get("Lat")}, {(dct.get(icao_key)).get("Lon")}  **Timezone:** {(dct.get(icao_key)).get("Timezone")}''')
    ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={(dct.get(icao_key)).get("Lat")},{(dct.get(icao_key)).get("Lon")},8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=0&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)


def lightning_button(icao_key, dct):
    '''
    '''
    ph_title.title(f'{icao_key} - {(dct.get(icao_key)).get("City")}, {(dct.get(icao_key)).get("Country")}')
    ph_subtitle.markdown(f'**Coordinates:** {(dct.get(icao_key)).get("Lat")}, {(dct.get(icao_key)).get("Lon")}  **Timezone:** {(dct.get(icao_key)).get("Timezone")}')
    ph_iframe.markdown(f'<iframe src="https://www.google.com/maps/embed/v1/view?key=AIzaSyAyhBpjJa4e_NoIMjUau11Q1UbsEZK2nzQ&center={(dct.get(icao_key)).get("Lat")},{(dct.get(icao_key)).get("Lon")}&maptype=satellite&zoom=7" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)


def satellite_button(icao_key, dct):
    '''
    '''
    ph_title.title(f'{icao_key} - {(dct.get(icao_key)).get("City")}, {(dct.get(icao_key)).get("Country")}')
    ph_subtitle.markdown(f'**Coordinates:** {(dct.get(icao_key)).get("Lat")}, {(dct.get(icao_key)).get("Lon")}  **Timezone:** {(dct.get(icao_key)).get("Timezone")}')
    # ph_iframe.markdown(f'<iframe src="https://www.tsohost.com/assets/uploads/blog/under-construction-pages-1-image-library.jpg" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    url = 'https://rammb-slider.cira.colostate.edu/?sat=himawari&sec=full_disk&x=10576&y=7952&z=1&angle=0&im=6&ts=3&st=0&et=0&speed=130&motion=loop&maps%5Bborders%5D=white&maps%5Bairports%5D=pink&lat=0&p%5B0%5D=geocolor&p%5B1%5D=band_13&opacity%5B0%5D=1&opacity%5B1%5D=0.15&pause=0&slider=-1&hide_controls=0&mouse_draw=0&follow_feature=0&follow_hide=0&s=rammb-slider&draw_color=FFD700&draw_width=6'
    webbrowser.open_new_tab(url)


def region_lightning(coords, zoom):
    '''
    '''
    ph_iframe2.markdown(f'<iframe src="https://map.blitzortung.org/index.php?MapStyle=3#{zoom}/{coords}" width="100%" frameborder="0" style="border:0;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)


def region_radar(coords, zoom):
    '''
    '''
    ph_iframe.markdown(f'<iframe src="https://www.rainviewer.com/map.html?loc={coords},{zoom}&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=0&sm=0&sn=1" width="100%" frameborder="3" style="border:2;height:80vh;" allowfullscreen></iframe>', unsafe_allow_html=True)


def create_scroll_item(region, duty, dct, lst):
    '''
    '''
    if region == duty:
        i = 0
        while i <= len(dct)-1:
            cols = st.sidebar.beta_columns([.5,.75,1,1])
            cols[0].markdown(f'**{list(dct.keys())[i]}**')
            if cols[1].button('Radar', key=i+10000):
                radar_button(lst[i], dct)
            if cols[2].button(f'Satellite', key=i+10002):
                satellite_button(lst[i], dct)
            if cols[3].button(f'Map', key=i+10001):
                lightning_button(lst[i], dct)
            i = i+1


dct_duty = connect_gs()

# Build duty lists
lst_jgp = dct_duty.get('jgp')
lst_ok1 = dct_duty.get('ok1')
lst_ok2 = dct_duty.get('ok2')
lst_ok3 = dct_duty.get('ok3')
lst_ok4 = dct_duty.get('ok4')
lst_sg1 = dct_duty.get('sg1')
lst_sg2 = dct_duty.get('sg2')
lst_sg3 = dct_duty.get('sg3')
lst_sg4 = dct_duty.get('sg4')
lst_sgd = dct_duty.get('sgd')
lst_sja = dct_duty.get('sja')
lst_sjd = dct_duty.get('sjd')
lst_sjn = dct_duty.get('sjn')

# Build the dictionaries
dct_jgp = create_dct(lst_jgp)
dct_ok1 = create_dct(lst_ok1)
dct_ok2 = create_dct(lst_ok2)
dct_ok3 = create_dct(lst_ok3)
dct_ok4 = create_dct(lst_ok4)
dct_sg1 = create_dct(lst_sg1)
dct_sg2 = create_dct(lst_sg2)
dct_sg3 = create_dct(lst_sg3)
dct_sg4 = create_dct(lst_sg4)
dct_sgd = create_dct(lst_sgd)
# dct_sja = create_dct(lst_sja)
dct_sjd = create_dct(lst_sjd)
dct_sjn = create_dct(lst_sjn)
#
# import numpy as np
# st.markdown(lst_sgd)
# st.markdown(list(dct_sgd.keys()))
# st.markdown(np.setdiff1d(lst_sgd, list(dct_sgd.keys())))
# st.markdown('-----')
# st.markdown(lst_ok2)
# st.markdown(list(dct_ok2.keys()))
# st.markdown(np.setdiff1d(list(dct_ok2.keys()), lst_ok2))
# st.markdown('-----')
# st.markdown(lst_sg4)
# st.markdown(list(dct_sg4.keys()))
# st.markdown(np.setdiff1d(lst_sg4, list(dct_sg4.keys())))
# st.markdown('-----')
# st.markdown(lst_sg1)
# st.markdown(list(dct_sg1.keys()))
# st.markdown(np.setdiff1d(lst_sg1, list(dct_sg1.keys())))

# Create sidebar scroll options
create_scroll_item(region, 'JGP', dct_jgp, lst_jgp)
create_scroll_item(region, 'OK1', dct_ok1, lst_ok1)
create_scroll_item(region, 'OK2', dct_ok2, lst_ok2)
create_scroll_item(region, 'OK3', dct_ok3, lst_ok3)
create_scroll_item(region, 'OK4', dct_ok4, lst_ok4)
create_scroll_item(region, 'SG1', dct_sg1, lst_sg1)
create_scroll_item(region, 'SG2', dct_sg2, lst_sg2)
create_scroll_item(region, 'SG3', dct_sg3, lst_sg3)
create_scroll_item(region, 'SG4', dct_sg4, lst_sg4)
create_scroll_item(region, 'SGD', dct_sgd, lst_sgd)
create_scroll_item(region, 'SJD', dct_sjd, lst_sjd)
create_scroll_item(region, 'SJN', dct_sjn, lst_sjn)
