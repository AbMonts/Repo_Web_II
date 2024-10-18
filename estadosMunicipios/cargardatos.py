import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estadosMunicipios.settings')
django.setup()

from ubicaciones.models import Estado, Municipio

# Lista de estados y municipios
estados_municipios = {
    "Aguascalientes": ["Aguascalientes", "Asientos", "Calvillo", "Cosío", "Jesús María", "Pabellón de Arteaga", "Rincón de Romos", "San José de Gracia", "Tepezalá", "El Llano"],
    "Baja California": ["Ensenada", "Mexicali", "Tecate", "Tijuana", "Playas de Rosarito"],
    "Baja California Sur": ["Comondú", "La Paz", "Loreto", "Los Cabos", "Mulegé"],
    "Campeche": ["Calkiní", "Campeche", "Candelaria", "Carmen", "Champotón", "Hecelchakán", "Hopelchén", "Palizada", "Tenabo", "Escárcega", "Calakmul"],
    "Chiapas": ["Tuxtla Gutiérrez", "San Cristóbal de las Casas", "Tapachula", "Comitán", "Arriaga", "Berriozábal", "Cintalapa", "Ocosingo", "Palenque", "Pijijiapan"],
    "Chihuahua": ["Chihuahua", "Ciudad Juárez", "Cuauhtémoc", "Delicias", "Hidalgo del Parral", "Nuevo Casas Grandes"],
    "Ciudad de México": ["Álvaro Obregón", "Azcapotzalco", "Benito Juárez", "Coyoacán", "Cuajimalpa", "Cuauhtémoc", "Gustavo A. Madero", "Iztacalco", "Iztapalapa", "Magdalena Contreras"],
    "Coahuila": ["Saltillo", "Torreón", "Monclova", "Acuña", "Piedras Negras", "Sabinas", "San Pedro", "Múzquiz", "Ramos Arizpe"],
    "Colima": ["Colima", "Manzanillo", "Tecomán", "Villa de Álvarez", "Armería", "Comala", "Coquimatlán", "Cuauhtémoc", "Ixtlahuacán", "Minatitlán"],
    "Durango": ["Durango", "Gómez Palacio", "Lerdo", "Canatlán", "Cuencamé", "El Salto", "Mapimí", "Nombre de Dios", "Santiago Papasquiaro", "Tlahualilo"],
    "Guanajuato": ["León", "Irapuato", "Celaya", "Guanajuato", "Salamanca", "Silao", "San Miguel de Allende", "Dolores Hidalgo", "Acámbaro", "San Luis de la Paz"],
    "Guerrero": ["Acapulco", "Chilpancingo", "Iguala", "Taxco", "Zihuatanejo", "Coyuca de Benítez", "Ayutla de los Libres", "Tixtla", "Tecpan de Galeana", "Ometepec"],
    "Hidalgo": ["Pachuca", "Tulancingo", "Tizayuca", "Tula de Allende", "Huejutla de Reyes", "Ixmiquilpan", "Zimapán", "Actopan", "Apan", "Mixquiahuala"],
    "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque", "Tonalá", "Puerto Vallarta", "Lagos de Moreno", "Tepatitlán", "Ciudad Guzmán", "El Salto", "Tala"],
    "Estado de México": ["Toluca", "Ecatepec", "Nezahualcóyotl", "Naucalpan", "Tlalnepantla", "Chimalhuacán", "Cuautitlán Izcalli", "Tultitlán", "Atizapán", "Valle de Chalco"],
    "Michoacán": ["Morelia", "Uruapan", "Zamora", "Lázaro Cárdenas", "Apatzingán", "Pátzcuaro", "Zitácuaro", "Los Reyes", "Sahuayo", "Tacámbaro"],
    "Morelos": ["Cuernavaca", "Cuautla", "Jiutepec", "Temixco", "Yautepec", "Zacatepec", "Tepoztlán", "Tlayacapan", "Tetecala", "Xochitepec"],
    "Nayarit": ["Tepic", "Bahía de Banderas", "Compostela", "Ixtlán del Río", "Santiago Ixcuintla", "Acaponeta", "Huajicori", "San Blas", "Rosamorada", "Tecuala"],
    "Nuevo León": ["Monterrey", "San Nicolás de los Garza", "Guadalupe", "Apodaca", "General Escobedo", "Santa Catarina", "San Pedro Garza García", "Linares", "Montemorelos", "Santiago"],
    "Oaxaca": ["Oaxaca de Juárez", "Salina Cruz", "Juchitán", "Tuxtepec", "Huatulco", "Miahuatlán", "Pochutla", "Tlaxiaco", "San Juan Bautista", "Huajuapan"],
    "Puebla": ["Puebla", "Tehuacán", "San Martín Texmelucan", "Atlixco", "Cholula", "Izúcar de Matamoros", "Zacatlán", "Amozoc", "Ajalpan", "Huauchinango"],
    "Querétaro": ["Querétaro", "San Juan del Río", "El Marqués", "Corregidora", "Tequisquiapan", "Pedro Escobedo", "Amealco", "Pinal de Amoles", "Jalpan de Serra"],
    "Quintana Roo": ["Cancún", "Playa del Carmen", "Cozumel", "Tulum", "Isla Mujeres", "Chetumal", "Felipe Carrillo Puerto", "Bacalar", "José María Morelos", "Lázaro Cárdenas"],
    "San Luis Potosí": ["San Luis Potosí", "Soledad de Graciano Sánchez", "Ciudad Valles", "Matehuala", "Rioverde", "Tamazunchale", "Cerritos", "Cárdenas", "Villa de Reyes"],
    "Sinaloa": ["Culiacán", "Mazatlán", "Los Mochis", "Guasave", "Navolato", "El Rosario", "Escuinapa", "Mocorito", "Angostura", "Cosalá"],
    "Sonora": ["Hermosillo", "Ciudad Obregón", "Nogales", "Guaymas", "Navojoa", "Caborca", "Agua Prieta", "Puerto Peñasco", "San Luis Río Colorado", "Cananea"],
    "Tabasco": ["Villahermosa", "Cárdenas", "Comalcalco", "Macuspana", "Centla", "Tenosique", "Paraíso", "Balancán", "Jalpa de Méndez", "Nacajuca"],
    "Tamaulipas": ["Reynosa", "Matamoros", "Nuevo Laredo", "Ciudad Victoria", "Tampico", "Altamira", "Madero", "Río Bravo", "Valle Hermoso", "San Fernando"],
    "Tlaxcala": ["Tlaxcala", "Apizaco", "Chiautempan", "Huamantla", "Zacatelco", "San Pablo del Monte", "Santa Cruz Tlaxcala", "Calpulalpan", "Contla", "Ixtacuixtla"],
    "Veracruz": ["Xalapa", "Veracruz", "Coatzacoalcos", "Minatitlán", "Córdoba", "Orizaba", "Tuxpan", "Poza Rica", "Cosamaloapan", "Martínez de la Torre"],
    "Yucatán": ["Mérida", "Progreso", "Valladolid", "Tizimín", "Izamal", "Motul", "Maxcanú", "Kanasín", "Umán", "Tekax"],
    "Zacatecas": ["Zacatecas", "Fresnillo", "Jerez", "Guadalupe", "Sombrerete", "Valparaíso", "Río Grande", "Ojocaliente", "Loreto", "Villa de Cos"]
}

# Insercioon de datos
for estado_nombre, municipios in estados_municipios.items():
    estado, created = Estado.objects.get_or_create(nombre=estado_nombre)
    
    for municipio_nombre in municipios:
        Municipio.objects.get_or_create(nombre=municipio_nombre, estado=estado)

print("Datos de estados y municipios, insertados.")
