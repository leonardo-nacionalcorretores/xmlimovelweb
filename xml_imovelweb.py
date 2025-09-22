import requests
import xml.etree.ElementTree as ET

# Baixa o XML original
url = "https://universal-ftp2.s3.us-west-2.amazonaws.com/iw/nacionalcorretores-imovelweb-8039-ambos.xml"
response = requests.get(url)
response.raise_for_status()

# Lê o XML
tree = ET.ElementTree(ET.fromstring(response.content))
root = tree.getroot()

# Percorre todos os imóveis
for imovel in root.findall(".//Imovel"):
    tipo = imovel.find("TipoImovel")
    if tipo is not None and tipo.text:
        tipo.text = tipo.text.split(" ")[0]  # só a primeira palavra

# Salva em arquivo
tree.write("saida.xml", encoding="utf-8", xml_declaration=True)
