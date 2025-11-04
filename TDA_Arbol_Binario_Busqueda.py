"""
Tipo de Datos Abstracto Arbol Binario de Busqueda
autor: elpocitano@gmail.com
"""

class NodoB:
  # Objeto de datos Nodo
    _clave: int # Atributo que define la estructura ordinal del arbol
    _izq: 'NodoB'
    _der: 'NodoB'
    def __init__(self, clave: int) -> None:
        self._clave = clave
        self._izq = None
        self._der = None

  # Getters
    def getClave(self) -> int:
        """Retorna la clave (ordinal) del nodo."""
        return self._clave
    def getIzq(self) -> 'NodoB':
        """Retorna el hijo izquierdo."""
        return self._izq
    def getDer(self) -> 'NodoB':
        """Retorna el hijo derecho."""
        return self._der
    def getGrado(self)-> int:
        grado: int = 0
        if self.getIzq() and self.getDer():
			grado = 2
		elif self.getIzq() or self.getDer():
			grado = 1
		return grado

	# setters
	def setClave(self, nueva_clave: int) -> None:
        """Asigna un nuevo valor al nodo."""
        self._clave = nueva_clave

    def izq(self, nodo: 'NodoB') -> None:
        """Asigna el hijo izquierdo."""
        self._izq = nodo

    def der(self, nodo: 'NodoB') -> None:
        """Asigna el hijo derecho."""
        self._der = nodo

class ArbolBBusqueda:
	# Objeto de datos TDA arbol binario de busqueda
	_raiz: 'NodoB'
	def __init__(self):
		self._raiz = None

	def getRaiz(self)->'NodoB':
		return self._raiz

	def EstaVacio(self)-> bool:
		return self._raiz is None


	
