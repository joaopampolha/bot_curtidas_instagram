import configparser
import string

class PropertiesReader:

    geckoDriver = None
    paginaInicial = None
    paginaTags = None
    paginaFoto = None
    usuario = None
    senha = None
    totalLikes = None
    paginaPerfil = None
    executaCurtir = None
    hashTag = None

    def __init__(self):
        _config = configparser.RawConfigParser()
        _config.read('ConfigFile.properties')

        self.geckoDriver = _config.get('Inicializacao', 'geckoDriver')
        self.paginaInicial = _config.get('Inicializacao', 'paginaInicial')
        self.paginaTags = _config.get('Inicializacao', 'paginaTags')
        self.paginaFoto = _config.get('Inicializacao', 'paginaFoto')
        self.usuario = _config.get('Inicializacao', 'usuario')
        self.senha = _config.get('Inicializacao', 'senha')
        self.totalLikes =  int(_config.get('Inicializacao', 'totalLikes'))
        self.paginaPerfil = _config.get('Inicializacao', 'paginaPerfil')
        self.executaCurtir = _config.get('Inicializacao', 'executaCurtir')
        self.executaCurtir = self.executaCurtir.lower()
        self.hashTag = _config.get('Inicializacao', 'hashTag')