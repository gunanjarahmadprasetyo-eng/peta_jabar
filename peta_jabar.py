import streamlit as st 
import networkx as nx 
import matplotlib.pyplot as plt
import random 
st.title("Peta Koneksi AntarKota Di Jawa Barat")
cities = ["Bandung", "Bogor", "Depok", "Bekasi", "Cirebon", "Tasikmalaya", "Sukabumi", "Cimahi", "Banjar"]
#Membuat Graph kosong
G = nx.Graph()
G.add_nodes_from(cities)
#Tambahkan sisi antar semua kota dengan jarak acak (dalam km)
edges = []
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        jarak = random.randint(80, 250)
        edges.append((cities[i], cities[j], jarak))
G.add_weighted_edges_from(edges)
#Tata letak node
pos = nx.spring_layout(G, seed=42)
#Gambar Graph
fig, ax = plt.subplots(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, ax=ax)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
st.pyplot(fig)
#fitur pilih kota asal
st.header("Lihat Semua Rute Dari kota Asal")
start_city = st.selectbox("Pilih kota asal:", cities)
st.write(f"### Rute dari {start_city}:")
for city in cities:
    if city != start_city:
        try:
            distance = nx.shortest_path_length(G, start_city, city, weight='weight')
            path = nx.shortest_path(G, start_city, city, weight='weight')
            st.write(f"🛣️{start_city} ➜ {city}: {distance} km (rute: {path})")
        except:
            st.write(f"⚠️ Tidak ada jalur dari {start_city} ke {city}")