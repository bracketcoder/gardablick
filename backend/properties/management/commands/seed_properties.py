import shutil
from pathlib import Path
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.conf import settings

from properties.models import Property, PropertyImage


FRONTEND_PUBLIC = Path(settings.BASE_DIR).parent / "forntend" / "public"

LISTING_IMAGES = FRONTEND_PUBLIC / "images" / "listing-images"
DETAIL_IMAGES = FRONTEND_PUBLIC / "details"

PROPERTIES_DATA = [
    {
        "title": {
            "it": "Villa singola con parco privato e vista sul golfo di Salò.",
            "en": "Detached villa with private park and view over the Gulf of Salò.",
            "de": "Einfamilienhaus mit privatem Park und Blick auf den Golf von Salò.",
        },
        "location": "Salò",
        "price": Decimal("3150000"),
        "ref": "RF: 00152",
        "area": Decimal("643"),
        "bedrooms": 9,
        "bathrooms": 9,
        "main_image_src": "Villa singola con parco privato e vista sul golfo di Salò.png",
        "description": {
            "it": "In una zona tranquilla e riservata, a pochi minuti dal centro di Salò e dal lago, proponiamo una villa singola recente e in condizioni impeccabili. La proprietà offre spazi interni ed esterni generosi, alta efficienza energetica e un elevato comfort abitativo.\n\nÈ dotata di impianto fotovoltaico con batteria di accumulo, per un reale risparmio energetico e una gestione sostenibile dell'abitazione.",
            "en": "In a quiet and private area, just minutes from the centre of Salò and the lake, we offer a recent detached villa in impeccable condition. The property features generous indoor and outdoor spaces, high energy efficiency and elevated living comfort.\n\nIt is equipped with a photovoltaic system with storage battery, for real energy savings and sustainable home management.",
            "de": "In einer ruhigen und privaten Gegend, nur wenige Minuten vom Zentrum von Salò und dem See entfernt, bieten wir eine kürzlich erbaute freistehende Villa in einwandfreiem Zustand. Die Immobilie bietet großzügige Innen- und Außenbereiche, hohe Energieeffizienz und gehobenen Wohnkomfort.\n\nSie ist mit einer Photovoltaikanlage mit Speicherbatterie ausgestattet, für echte Energieeinsparungen und nachhaltiges Wohnmanagement.",
        },
        "commercial_area": Decimal("252"),
        "net_area": Decimal("200"),
        "total_rooms": 12,
        "energy_class": "A",
        "condominium_fees": None,
        "composition": {
            "it": ["Soggiorno ampio e luminoso", "Cucina separata e abitabile", "Nove camere da letto", "Nove bagni moderni", "Portico coperto ideale per vivere l'esterno", "Giardino privato con parco", "Garage triplo"],
            "en": ["Spacious and bright living room", "Separate eat-in kitchen", "Nine bedrooms", "Nine modern bathrooms", "Covered porch ideal for outdoor living", "Private garden with park", "Triple garage"],
            "de": ["Geräumiges und helles Wohnzimmer", "Separate Wohnküche", "Neun Schlafzimmer", "Neun moderne Badezimmer", "Überdachte Veranda ideal für das Leben im Freien", "Privatgarten mit Park", "Dreifachgarage"],
        },
        "composition_note": {
            "it": "La villa è stata costruita con materiali di qualità e integra soluzioni moderne.",
            "en": "The villa was built with quality materials and integrates modern solutions.",
            "de": "Die Villa wurde mit hochwertigen Materialien gebaut und integriert moderne Lösungen.",
        },
        "location_note": {
            "it": "Posizione: vista sul golfo di Salò, vicino ai servizi.",
            "en": "Location: view over the Gulf of Salò, close to amenities.",
            "de": "Lage: Blick auf den Golf von Salò, in der Nähe von Einrichtungen.",
        },
        "latitude": Decimal("45.6064000"),
        "longitude": Decimal("10.5264000"),
    },
    {
        "title": {
            "it": "Bilocale ristrutturato con portico, giardino e vista lago.",
            "en": "Renovated two-room apartment with porch, garden and lake view.",
            "de": "Renovierte Zweizimmerwohnung mit Veranda, Garten und Seeblick.",
        },
        "location": "Polpenazze del Garda",
        "price": Decimal("185000"),
        "ref": "RF: 00153",
        "area": Decimal("55"),
        "bedrooms": 1,
        "bathrooms": 1,
        "main_image_src": "Bilocale ristrutturato con portico, giardino e vista lago.png",
        "description": {
            "it": "Bilocale completamente ristrutturato con finiture di pregio, situato in posizione panoramica con vista lago. Dotato di portico e giardino privato, ideale per chi cerca una soluzione abitativa o come investimento.",
            "en": "Completely renovated two-room apartment with premium finishes, located in a panoramic position with lake view. Equipped with porch and private garden, ideal for those seeking a living solution or as an investment.",
            "de": "Komplett renovierte Zweizimmerwohnung mit hochwertiger Ausstattung, in Panoramalage mit Seeblick. Ausgestattet mit Veranda und privatem Garten, ideal als Wohnlösung oder Investition.",
        },
        "commercial_area": Decimal("65"),
        "net_area": Decimal("50"),
        "total_rooms": 3,
        "energy_class": "C",
        "condominium_fees": Decimal("80"),
        "composition": {
            "it": ["Soggiorno con angolo cottura", "Camera da letto matrimoniale", "Bagno con doccia", "Portico coperto", "Giardino privato"],
            "en": ["Living room with kitchenette", "Double bedroom", "Bathroom with shower", "Covered porch", "Private garden"],
            "de": ["Wohnzimmer mit Kochnische", "Doppelschlafzimmer", "Badezimmer mit Dusche", "Überdachte Veranda", "Privatgarten"],
        },
        "composition_note": {
            "it": "Ristrutturato con materiali di qualità.",
            "en": "Renovated with quality materials.",
            "de": "Renoviert mit hochwertigen Materialien.",
        },
        "location_note": {
            "it": "Posizione panoramica con vista lago a Polpenazze del Garda.",
            "en": "Panoramic position with lake view in Polpenazze del Garda.",
            "de": "Panoramalage mit Seeblick in Polpenazze del Garda.",
        },
        "latitude": Decimal("45.5520000"),
        "longitude": Decimal("10.5100000"),
    },
    {
        "title": {
            "it": "Trilocale con totale vista lago.",
            "en": "Three-room apartment with full lake view.",
            "de": "Dreizimmerwohnung mit vollem Seeblick.",
        },
        "location": "Gargnano",
        "price": Decimal("280000"),
        "ref": "RF: 00154",
        "area": Decimal("66"),
        "bedrooms": 2,
        "bathrooms": 1,
        "main_image_src": "Trilocale con totale vista lago.png",
        "description": {
            "it": "Trilocale con vista lago mozzafiato a Gargnano. Posizione unica con accesso diretto al lungolago. Luminoso e ben disposto, perfetto come residenza o casa vacanza.",
            "en": "Three-room apartment with breathtaking lake view in Gargnano. Unique position with direct access to the lakefront. Bright and well laid out, perfect as a residence or holiday home.",
            "de": "Dreizimmerwohnung mit atemberaubendem Seeblick in Gargnano. Einzigartige Lage mit direktem Zugang zur Seepromenade. Hell und gut aufgeteilt, perfekt als Wohnsitz oder Ferienhaus.",
        },
        "commercial_area": Decimal("75"),
        "net_area": Decimal("60"),
        "total_rooms": 4,
        "energy_class": "D",
        "condominium_fees": Decimal("120"),
        "composition": {
            "it": ["Soggiorno luminoso con vista lago", "Cucina abitabile", "Due camere da letto", "Bagno con vasca", "Balcone panoramico"],
            "en": ["Bright living room with lake view", "Eat-in kitchen", "Two bedrooms", "Bathroom with bathtub", "Panoramic balcony"],
            "de": ["Helles Wohnzimmer mit Seeblick", "Wohnküche", "Zwei Schlafzimmer", "Badezimmer mit Badewanne", "Panoramabalkon"],
        },
        "composition_note": {
            "it": "Appartamento luminoso con vista totale sul lago.",
            "en": "Bright apartment with full lake view.",
            "de": "Helle Wohnung mit vollem Seeblick.",
        },
        "location_note": {
            "it": "Posizione unica a Gargnano, direttamente sul lago.",
            "en": "Unique position in Gargnano, directly on the lake.",
            "de": "Einzigartige Lage in Gargnano, direkt am See.",
        },
        "latitude": Decimal("45.6900000"),
        "longitude": Decimal("10.6600000"),
    },
    {
        "title": {
            "it": "Villa moderna con giardino e piscina privata.",
            "en": "Modern villa with garden and private pool.",
            "de": "Moderne Villa mit Garten und privatem Pool.",
        },
        "location": "Desenzano del Garda",
        "price": Decimal("450000"),
        "ref": "RF: 00155",
        "area": Decimal("180"),
        "bedrooms": 4,
        "bathrooms": 3,
        "main_image_src": "Villa singola con parco privato e vista sul golfo di Salò.png",
        "description": {
            "it": "Villa moderna di recente costruzione con ampi spazi, giardino curato e piscina privata. Situata in zona residenziale tranquilla a pochi minuti dal centro di Desenzano.",
            "en": "Recently built modern villa with spacious rooms, manicured garden and private pool. Located in a quiet residential area just minutes from the centre of Desenzano.",
            "de": "Kürzlich erbaute moderne Villa mit großzügigen Räumen, gepflegtem Garten und privatem Pool. In einer ruhigen Wohngegend nur wenige Minuten vom Zentrum von Desenzano.",
        },
        "commercial_area": Decimal("210"),
        "net_area": Decimal("165"),
        "total_rooms": 8,
        "energy_class": "B",
        "condominium_fees": None,
        "composition": {
            "it": ["Ampio soggiorno con camino", "Cucina moderna open space", "Quattro camere da letto", "Tre bagni", "Piscina privata", "Giardino curato", "Garage doppio"],
            "en": ["Spacious living room with fireplace", "Modern open-plan kitchen", "Four bedrooms", "Three bathrooms", "Private pool", "Manicured garden", "Double garage"],
            "de": ["Geräumiges Wohnzimmer mit Kamin", "Moderne offene Küche", "Vier Schlafzimmer", "Drei Badezimmer", "Privatpool", "Gepflegter Garten", "Doppelgarage"],
        },
        "composition_note": {
            "it": "Costruzione recente con materiali di alta qualità.",
            "en": "Recent construction with high quality materials.",
            "de": "Neubaue mit hochwertigen Materialien.",
        },
        "location_note": {
            "it": "Zona residenziale tranquilla a Desenzano del Garda.",
            "en": "Quiet residential area in Desenzano del Garda.",
            "de": "Ruhige Wohngegend in Desenzano del Garda.",
        },
        "latitude": Decimal("45.4700000"),
        "longitude": Decimal("10.5400000"),
    },
    {
        "title": {
            "it": "Attico panoramico con terrazza vista lago.",
            "en": "Panoramic penthouse with lake-view terrace.",
            "de": "Panorama-Penthouse mit Seeterrasse.",
        },
        "location": "Salò",
        "price": Decimal("520000"),
        "ref": "RF: 00156",
        "area": Decimal("120"),
        "bedrooms": 3,
        "bathrooms": 2,
        "main_image_src": "Bilocale ristrutturato con portico, giardino e vista lago.png",
        "description": {
            "it": "Attico di pregio con ampia terrazza panoramica e vista lago impareggiabile. Finiture di lusso e posizione centrale a Salò.",
            "en": "Premium penthouse with large panoramic terrace and unparalleled lake view. Luxury finishes and central position in Salò.",
            "de": "Hochwertiges Penthouse mit großer Panoramaterrasse und unvergleichlichem Seeblick. Luxuriöse Ausstattung und zentrale Lage in Salò.",
        },
        "commercial_area": Decimal("140"),
        "net_area": Decimal("110"),
        "total_rooms": 6,
        "energy_class": "B",
        "condominium_fees": Decimal("200"),
        "composition": {
            "it": ["Soggiorno con accesso terrazza", "Cucina separata", "Tre camere da letto", "Due bagni", "Terrazza panoramica 40m²"],
            "en": ["Living room with terrace access", "Separate kitchen", "Three bedrooms", "Two bathrooms", "Panoramic terrace 40m²"],
            "de": ["Wohnzimmer mit Terrassenzugang", "Separate Küche", "Drei Schlafzimmer", "Zwei Badezimmer", "Panoramaterrasse 40m²"],
        },
        "composition_note": {
            "it": "Finiture di lusso e ampia terrazza panoramica.",
            "en": "Luxury finishes and large panoramic terrace.",
            "de": "Luxuriöse Ausstattung und große Panoramaterrasse.",
        },
        "location_note": {
            "it": "Posizione centrale a Salò con vista lago.",
            "en": "Central position in Salò with lake view.",
            "de": "Zentrale Lage in Salò mit Seeblick.",
        },
        "latitude": Decimal("45.6080000"),
        "longitude": Decimal("10.5230000"),
    },
    {
        "title": {
            "it": "Rustico ristrutturato con uliveto.",
            "en": "Renovated farmhouse with olive grove.",
            "de": "Renoviertes Bauernhaus mit Olivenhain.",
        },
        "location": "Gardone Riviera",
        "price": Decimal("395000"),
        "ref": "RF: 00157",
        "area": Decimal("150"),
        "bedrooms": 3,
        "bathrooms": 2,
        "main_image_src": "Trilocale con totale vista lago.png",
        "description": {
            "it": "Caratteristico rustico completamente ristrutturato, circondato da un uliveto secolare. Posizione collinare con vista lago e privacy totale.",
            "en": "Characteristic farmhouse completely renovated, surrounded by a centuries-old olive grove. Hillside position with lake view and total privacy.",
            "de": "Charakteristisches, komplett renoviertes Bauernhaus, umgeben von einem jahrhundertealten Olivenhain. Hanglage mit Seeblick und absoluter Privatsphäre.",
        },
        "commercial_area": Decimal("170"),
        "net_area": Decimal("140"),
        "total_rooms": 7,
        "energy_class": "E",
        "condominium_fees": None,
        "composition": {
            "it": ["Soggiorno con travi a vista", "Cucina in muratura", "Tre camere da letto", "Due bagni", "Cantina", "Uliveto con 50 piante"],
            "en": ["Living room with exposed beams", "Stone-built kitchen", "Three bedrooms", "Two bathrooms", "Cellar", "Olive grove with 50 trees"],
            "de": ["Wohnzimmer mit Sichtbalken", "Gemauerte Küche", "Drei Schlafzimmer", "Zwei Badezimmer", "Keller", "Olivenhain mit 50 Bäumen"],
        },
        "composition_note": {
            "it": "Rustico ristrutturato mantenendo il fascino originale.",
            "en": "Farmhouse renovated maintaining the original charm.",
            "de": "Bauernhaus renoviert unter Beibehaltung des ursprünglichen Charmes.",
        },
        "location_note": {
            "it": "Posizione collinare a Gardone Riviera.",
            "en": "Hillside position in Gardone Riviera.",
            "de": "Hanglage in Gardone Riviera.",
        },
        "latitude": Decimal("45.6200000"),
        "longitude": Decimal("10.5600000"),
    },
    {
        "title": {
            "it": "Appartamento vista lago con posto barca.",
            "en": "Lake-view apartment with boat berth.",
            "de": "Seeblick-Wohnung mit Bootsplatz.",
        },
        "location": "Toscolano Maderno",
        "price": Decimal("320000"),
        "ref": "RF: 00158",
        "area": Decimal("85"),
        "bedrooms": 2,
        "bathrooms": 1,
        "main_image_src": "Villa singola con parco privato e vista sul golfo di Salò.png",
        "description": {
            "it": "Appartamento fronte lago con posto barca privato. Recentemente ristrutturato con finiture moderne. Accesso diretto alla spiaggia.",
            "en": "Lakefront apartment with private boat berth. Recently renovated with modern finishes. Direct beach access.",
            "de": "Wohnung am See mit privatem Bootsplatz. Kürzlich renoviert mit modernen Ausstattungen. Direkter Strandzugang.",
        },
        "commercial_area": Decimal("95"),
        "net_area": Decimal("78"),
        "total_rooms": 4,
        "energy_class": "C",
        "condominium_fees": Decimal("150"),
        "composition": {
            "it": ["Soggiorno con vista lago", "Cucina attrezzata", "Due camere da letto", "Bagno moderno", "Posto barca privato"],
            "en": ["Living room with lake view", "Equipped kitchen", "Two bedrooms", "Modern bathroom", "Private boat berth"],
            "de": ["Wohnzimmer mit Seeblick", "Ausgestattete Küche", "Zwei Schlafzimmer", "Modernes Badezimmer", "Privater Bootsplatz"],
        },
        "composition_note": {
            "it": "Ristrutturato con finiture moderne e accesso al lago.",
            "en": "Renovated with modern finishes and lake access.",
            "de": "Renoviert mit modernen Ausstattungen und Seezugang.",
        },
        "location_note": {
            "it": "Fronte lago a Toscolano Maderno con posto barca.",
            "en": "Lakefront in Toscolano Maderno with boat berth.",
            "de": "Am See in Toscolano Maderno mit Bootsplatz.",
        },
        "latitude": Decimal("45.6400000"),
        "longitude": Decimal("10.6100000"),
    },
    {
        "title": {
            "it": "Bilocale in centro storico ristrutturato.",
            "en": "Renovated two-room apartment in the historic centre.",
            "de": "Renovierte Zweizimmerwohnung im historischen Zentrum.",
        },
        "location": "Limone sul Garda",
        "price": Decimal("210000"),
        "ref": "RF: 00159",
        "area": Decimal("50"),
        "bedrooms": 1,
        "bathrooms": 1,
        "main_image_src": "Bilocale ristrutturato con portico, giardino e vista lago.png",
        "description": {
            "it": "Grazioso bilocale nel cuore del centro storico di Limone sul Garda. Completamente ristrutturato, ideale come casa vacanza o investimento turistico.",
            "en": "Charming two-room apartment in the heart of Limone sul Garda's historic centre. Completely renovated, ideal as a holiday home or tourist investment.",
            "de": "Charmante Zweizimmerwohnung im Herzen des historischen Zentrums von Limone sul Garda. Komplett renoviert, ideal als Ferienhaus oder touristische Investition.",
        },
        "commercial_area": Decimal("58"),
        "net_area": Decimal("45"),
        "total_rooms": 3,
        "energy_class": "D",
        "condominium_fees": Decimal("60"),
        "composition": {
            "it": ["Soggiorno con angolo cottura", "Camera matrimoniale", "Bagno con doccia", "Piccolo balcone"],
            "en": ["Living room with kitchenette", "Double bedroom", "Bathroom with shower", "Small balcony"],
            "de": ["Wohnzimmer mit Kochnische", "Doppelschlafzimmer", "Badezimmer mit Dusche", "Kleiner Balkon"],
        },
        "composition_note": {
            "it": "Completamente ristrutturato con gusto.",
            "en": "Completely renovated with taste.",
            "de": "Komplett geschmackvoll renoviert.",
        },
        "location_note": {
            "it": "Centro storico di Limone sul Garda.",
            "en": "Historic centre of Limone sul Garda.",
            "de": "Historisches Zentrum von Limone sul Garda.",
        },
        "latitude": Decimal("45.8100000"),
        "longitude": Decimal("10.7900000"),
    },
    {
        "title": {
            "it": "Villa con parco e dependance.",
            "en": "Villa with park and guest house.",
            "de": "Villa mit Park und Gästehaus.",
        },
        "location": "Manerba del Garda",
        "price": Decimal("680000"),
        "ref": "RF: 00160",
        "area": Decimal("250"),
        "bedrooms": 5,
        "bathrooms": 3,
        "main_image_src": "Trilocale con totale vista lago.png",
        "description": {
            "it": "Splendida villa con ampio parco e dependance per ospiti. Posizione dominante con vista panoramica sul lago. Perfetta per chi cerca spazio e privacy.",
            "en": "Splendid villa with large park and guest house. Commanding position with panoramic lake view. Perfect for those seeking space and privacy.",
            "de": "Prächtige Villa mit großem Park und Gästehaus. Beherrschende Lage mit Panorama-Seeblick. Perfekt für alle, die Platz und Privatsphäre suchen.",
        },
        "commercial_area": Decimal("300"),
        "net_area": Decimal("230"),
        "total_rooms": 10,
        "energy_class": "C",
        "condominium_fees": None,
        "composition": {
            "it": ["Grande soggiorno con camino", "Cucina professionale", "Cinque camere da letto", "Tre bagni", "Dependance con bilocale", "Parco con alberi secolari", "Garage triplo"],
            "en": ["Large living room with fireplace", "Professional kitchen", "Five bedrooms", "Three bathrooms", "Guest house with two rooms", "Park with centuries-old trees", "Triple garage"],
            "de": ["Großes Wohnzimmer mit Kamin", "Profiküche", "Fünf Schlafzimmer", "Drei Badezimmer", "Gästehaus mit Zweizimmerwohnung", "Park mit jahrhundertealten Bäumen", "Dreifachgarage"],
        },
        "composition_note": {
            "it": "Villa con dependance e ampio parco.",
            "en": "Villa with guest house and large park.",
            "de": "Villa mit Gästehaus und großem Park.",
        },
        "location_note": {
            "it": "Posizione dominante a Manerba del Garda.",
            "en": "Commanding position in Manerba del Garda.",
            "de": "Beherrschende Lage in Manerba del Garda.",
        },
        "latitude": Decimal("45.5500000"),
        "longitude": Decimal("10.5500000"),
    },
]

GALLERY_IMAGES = [
    "48d79c40b8b09555f45a9ed8039f4c1d79754a57.png",
    "5b99a64531940d19c1eaf4ac66ee06c57ce10421.png",
    "73fe6d1d203863c121fa00d82bcc072e4f1f2ee4.png",
    "7525eac7c2433a580f8604bbdd5676ef5da4d445.png",
]


class Command(BaseCommand):
    help = "Seed the database with sample property data"

    def handle(self, *args, **options):
        if Property.objects.exists():
            self.stdout.write(self.style.WARNING("Properties already exist. Skipping seed."))
            return

        media_main = settings.MEDIA_ROOT / "properties" / "main"
        media_gallery = settings.MEDIA_ROOT / "properties" / "gallery"
        media_main.mkdir(parents=True, exist_ok=True)
        media_gallery.mkdir(parents=True, exist_ok=True)

        for i, data in enumerate(PROPERTIES_DATA):
            src_image = LISTING_IMAGES / data["main_image_src"]
            if src_image.exists():
                dest_name = f"property_{i+1}{src_image.suffix}"
                dest_path = media_main / dest_name
                shutil.copy2(src_image, dest_path)
                image_field = f"properties/main/{dest_name}"
            else:
                self.stdout.write(self.style.WARNING(f"Image not found: {src_image}"))
                continue

            prop = Property.objects.create(
                title=data["title"],
                location=data["location"],
                price=data["price"],
                ref=data["ref"],
                area=data["area"],
                commercial_area=data.get("commercial_area"),
                net_area=data.get("net_area"),
                bedrooms=data["bedrooms"],
                bathrooms=data["bathrooms"],
                total_rooms=data.get("total_rooms"),
                energy_class=data.get("energy_class", ""),
                condominium_fees=data.get("condominium_fees"),
                description=data.get("description", {"it": "", "en": "", "de": ""}),
                composition=data.get("composition", {"it": [], "en": [], "de": []}),
                composition_note=data.get("composition_note", {"it": "", "en": "", "de": ""}),
                location_note=data.get("location_note", {"it": "", "en": "", "de": ""}),
                main_image=image_field,
                latitude=data.get("latitude"),
                longitude=data.get("longitude"),
            )

            if i == 0:
                for order, gallery_img in enumerate(GALLERY_IMAGES):
                    src_gallery = DETAIL_IMAGES / gallery_img
                    if src_gallery.exists():
                        dest_gallery = media_gallery / gallery_img
                        shutil.copy2(src_gallery, dest_gallery)
                        PropertyImage.objects.create(
                            property=prop,
                            image=f"properties/gallery/{gallery_img}",
                            order=order,
                        )

            title_it = data["title"].get("it", "")[:50]
            self.stdout.write(f"  Created: {prop.ref} - {title_it}")

        self.stdout.write(self.style.SUCCESS(f"Seeded {Property.objects.count()} properties."))
