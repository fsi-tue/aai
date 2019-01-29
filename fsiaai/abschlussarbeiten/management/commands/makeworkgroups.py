from django.core.management.base import BaseCommand
from abschlussarbeiten.models import Chair


class Command(BaseCommand):
    help = 'Trägt die Lehrstühle / Arbeitsgruppen in die Datenbank ein.'

    def handle(self, *args, **options):
        chairs = {
            'nicht zugeordnet': 'N/A',
            'Computational Systems Biology of Infection': 'Dräger',
            'Big Data Visual Analytics in den Lebenswissenschaften': 'Krone',
            'Algorithmen der Bioinformatik': 'Huson',
            'Integrative Transkriptomik': 'Nieselt',
            'Angewandte Bioinformatik': 'Kohlbacher',
            'Methoden der Medizininformatik': 'Pfeifer',
            'Learning-based Computer Vision/Autonomouns Vision': 'Geiger',
            'Theorie des maschinellen Lernens': 'Luxburg',
            'Methoden des maschinellen Lernens': 'Hein',
            'Maschinelles Lernen': 'Hennig',
            'Kognitive Systeme': 'Zell',
            'Eingebettete Systeme': 'Bringmann',
            'Programmiersprachen und Softwaretechnik': 'Ostermann',
            'Datenbanksysteme': 'Grust',
            'Technische Informatik': 'Rosenstiel',
            'Symbolisches Rechnen': 'Küchlin',
            'Informationsdienste': 'Walter',
            'Kommunikationsnetze': 'Menth',
            'Mathematische Strukturen in der Informatik': 'Dorn',
            'Selbstorganisation und Optimalität in Neuronalen Netzwerken': 'Levina',
            'Algorithmik': 'Kaufmann',
            'Logik und Sprachtheorie': 'Schroeder-Heister',
            'Theoretische Informatik': 'Lange',
            'Kognitive Modellierung': 'Butz',
            'Sensory and Sensorimotor Systems': 'Li',
            'Experimentelle Kognitionswissenschaft': 'Franz',
            'Medieninformatik/Visual Computing': 'Schilling',
            'Perception Engineering': 'Kasneci',
            'Neuronale Informationsverarbeitung': 'Wichmann',
            'Computergrafik': 'Lensch',
        }
        for key, value in chairs.items():
            Chair(name=key, head=value).save()
        print('Lehrstühle geschrieben.')
