import streamlit as st

st.set_page_config(layout='wide', page_title='Radar Regions', page_icon='https://p1.hiclipart.com/preview/994/283/642/rainmeter-tabbed-dock-grey-and-yellow-lightning-icon-png-clipart.jpg')

placeholder1 = st.empty()
placeholder2 = st.empty()
st.sidebar.title('Select Region')

region = st.sidebar.selectbox('OK1',
                              ('Europe', 'Northern Europe', 'Eastern Europe', 'South UK', 'Iberian Peninsula', 'France', 'Germany/Netherlands', 'Italy', 'Aegean Sea', 'Moscow'))

if st.sidebar.checkbox('Europe'):
    if st.sidebar.button('Europe'):
        placeholder1.title("Europe")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=55.9984,22.4121,4&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Northern Europe'):
        placeholder1.title("Northern Europe")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=56.8189,-344.2236,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Eastern Europe'):
        placeholder1.title("Eastern Europe")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=52.8492,-330.293,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('South UK'):
        placeholder1.title("South UK")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=51.6947,0.4614,8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Iberian Peninsula'):
        placeholder1.title("Iberian Peninsula")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=39.9729,-4.1748,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('France'):
        placeholder1.title("France")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=48.3526,2.4939,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Germany/Netherlands'):
        placeholder1.title("Germany/Netherlands")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=50.8025,10.1514,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Italy'):
        placeholder1.title("Italy")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=43.5127,11.5906,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Aegean Sea'):
        placeholder1.title("Aegean Sea")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=38.604,25.0378,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Moscow'):
        placeholder1.title("Moscow")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=55.2948,37.2437,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)

if st.sidebar.checkbox('Oceania'):
    if st.sidebar.button('Australia'):
        placeholder1.title("Australia")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=-25.9778,132.627,5&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Southwest Australia'):
        placeholder1.title("Southweast Australia")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=-32.7041,147.7441,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('New Zealand'):
        placeholder1.title("New Zealand")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=-40.8221,173.0347,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)

if st.sidebar.checkbox('North America'):
    if st.sidebar.button('CONUS'):
        placeholder1.title("CONUS")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=38.9765,-98.877,5&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Pacific Northwest'):
        placeholder1.title("Pacific Northwest")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=48.0524,-120.3333,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Southwest US'):
        placeholder1.title("Southwest US")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=35.3487,-116.1694,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Northeast US'):
        placeholder1.title("Northeast US")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=42.7026,-76.5747,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('North-Central US'):
        placeholder1.title("North-Central US")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=41.9554,-87.1765,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Alaska'):
        placeholder1.title("Alaska")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=63.4456,-150.7104,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)

if st.sidebar.checkbox('Northeast Asia'):
    if st.sidebar.button('Northeast Asia'):
        placeholder1.title("Northeast Asia")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=42.0982,-239.9854,5&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Northeast China'):
        placeholder1.title("Northeast China")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=46.453,-233.2397,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Korea'):
        placeholder1.title("Korea")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=37.1516,-232.4707,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('East-Central China'):
        placeholder1.title("East-Central China")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=37.6577,-245.4895,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
if st.sidebar.checkbox('Southeast Asia'):
    if st.sidebar.button('Southeast China'):
        placeholder1.title("Southeast China")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=28.5363,-247.6538,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Taiwan'):
        placeholder1.title("Taiwan")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=23.5489,-238.9142,8&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Hong Kong/Hainan Island'):
        placeholder1.title("Hong Kong/Hainan Island")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=21.361,-248.0164,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Indochina'):
        placeholder1.title("Indochina")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=13.0902,-255.1135,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
if st.sidebar.checkbox('Indonesia'):
    if st.sidebar.button('Indonesia'):
        placeholder1.title("Indonesia")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=-2.8004,-242.4683,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Malaysia'):
        placeholder1.title("Malaysia")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=3.5134,-252.4878,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Borneo'):
        placeholder1.title("Borneo")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=0.0549,-245.9399,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Java'):
        placeholder1.title("Java")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=-7.0082,-249.5435,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
if st.sidebar.checkbox('India'):
    if st.sidebar.button('India'):
        placeholder1.title("India")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=19.932,-281.2061,5&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=1&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Sri Lanka'):
        placeholder1.title("Sri Lanka")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=8.9068,-280.6458,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Northeast India'):
        placeholder1.title("Northeast India")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=23.6747,-270.8899,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('Nortwest India'):
        placeholder1.title("Northwest India")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=29.8692,-284.8865,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
if st.sidebar.checkbox('Arabian Peninsula'):
    if st.sidebar.button('Arabian Peninsula'):
        placeholder1.title("Arabian Peninsula")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=23.0797,-313.0225,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
if st.sidebar.checkbox('Japan'):
    if st.sidebar.button('Japan'):
        placeholder1.title("Japan")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=38.0654,-222.0557,6&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('North Japan'):
        placeholder1.title("North Japan")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=41.9513,-219.375,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
    if st.sidebar.button('South Japan'):
        placeholder1.title("South Japan")
        placeholder2.markdown('<iframe src="https://www.rainviewer.com/map.html?loc=34.2163,-224.6155,7&oFa=1&oC=1&oU=1&oCS=1&oF=1&oAP=0&rmt=1&c=5&o=49&lm=0&th=1&sm=0&sn=1" width="100%" frameborder="0" style="border:0;height:88vh;" allowfullscreen></iframe>', unsafe_allow_html=True)
