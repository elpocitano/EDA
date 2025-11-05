# /EDA/TDA_ArbolBBusqueda.py 
"""TAD Árbol Binario de Búsqueda (ABB):
Es un Árbol Binario que impone una *Propiedad de Orden* sobre sus nodos. 
Esto permitiria operaciones eficientes, siendo O(logn) en el caso ideal,
On si se degenera en una lista (si insertamos las claves ordenadas)
Fuente: EDA 2025, Diapos de la catedra unidad 04
Proporciona:
    Objeto de datos:
Elemento,   Característica,         Propósito
Nodo,       Clave (Ordinal),        Almacena el dato y la estructura. La clave define la posición.
            Puntero Izquierdo, 
            Puntero Derecho.   

Raíz,       Único puntero inicial   Punto de entrada a la estructura. 
            de la clase ArbolABB.

Algunas Operaciones fundamentales

Autor: elpocitano@gmail.com
"""

from typing import Any, Optional, List, Tuple

# ----------------------------------------------------------------------
# NODO ABB (Para el arbol binario de busqueda)
# Se usa 'Any' para la clave ordinal
# ----------------------------------------------------------------------
class NodoABB:
    _clave: Any 
    _izq: Optional['NodoABB']
    _der: Optional['NodoABB']

    def __init__(self, clave: Any):
        self._clave = clave
        self._izq = None  
        self._der = None  

    # getters 
    def getClave(self)-> Any:
        return self._clave
    def getIzq(self)-> Optional['NodoABB']:
        return self._izq
    def getDer(self)-> Optional['NodoABB']:
        return self._der
    def getGrado(self)-> int:
        grado_nodo = 0
        if self.getIzq() and self.getDer():
            grado_nodo = 2
        elif self.getIzq() or self.getDer():
            grado_nodo = 1 
        return grado_nodo
    
    # setters 
    def setClave(self, clave: Any):
        self._clave = clave
    def setIzq(self, nodo_menor: Optional['NodoABB']):
        self._izq = nodo_menor
    def setDer(self, nodo_mayor: Optional['NodoABB']):
        self._der = nodo_mayor
     

# ----------------------------------------------------------------------
# TAD ÁRBOL BINARIO DE BÚSQUEDA (ABB)
# ----------------------------------------------------------------------
class ArbolABB:
    _raiz: 'NodoABB'
    
    # --- Operación Canónica: CREAR(A) ---
    def __init__(self):
      self._raiz = None 
    
    # --- Operación Canónica: VACIO(A) ---
    def Vacio(self) -> bool:
        return self._raiz is None
    
    # ------------------------------------------------------------------
    # --- Operación Canónica: INSERTAR (Interfaz Pública) ---
    # ------------------------------------------------------------------
    def Insertar(self, clave) -> None:
        self._raiz = self._insertarRecursivo(self._raiz, clave)
        
    # Función auxiliar para la inserción recursiva.
    # Busca el extremo de la rama que le corresponde a la clave, apilando los nodos (referencias)
    # Al llegar al caso base, el extremo del arbol, instancia un nodo y lo retorna
    # Al desapilar, primero conecta el nuevo nodo, y luego retorna todo el recorrido hasta el primero
    # El primero nodo es el que vuelve al metodo publico y se asigna a la raiz, reconstruyendo el arbol 
    def _insertarRecursivo(self, nodo_actual, clave) -> 'NodoABB':
        
        # Auxiliar que almacenará el nodo que iremos apilando y luego los retornaremos en orden ascendente
        nodo_a_retornar: 'NodoABB'= nodo_actual
        
        # 01 Caso base: Llegamos al extremo de la rama, se instancia el nodo con la nueva clave y se retornara
        if nodo_actual is None:
            nodo_a_retornar = NodoABB(clave) 
        
        # 02 Caso general: Aun no llegamos al extremo, seguimos el recorrido respetando propiedad de orden
        else:
            # Si la clave a insertar es menor
            if clave < nodo_actual.getClave():
                # Reasignamos el puntero izquierdo con el resultado recursivo
                # El puntero interno debe ser _izq
                nodo_actual._izq = self._insertarRecursivo(nodo_actual._izq, clave)
            
            # Si la clave a insertar es mayor
            elif clave > nodo_actual.getClave():
                # Reasignamos el puntero derecho con el resultado recursivo
                # El puntero interno debe ser _der
                nodo_actual._der = self._insertarRecursivo(nodo_actual._der, clave)
                
            # Si la clave ya existe en el arbol
            else: 
                # La clave existe, no se hace nada o se actualiza el valor asociado.
                # En este TAD simplificado, no modificamos la estructura.
                pass 
        
        # Al desapilar todo, retornamos el nodo inicial que apilamos, el nodo raiz
        return nodo_a_retornar

    # ------------------------------------------------------------------
    # --- Operación Recorrer y processar INORDEN ---
    # ------------------------------------------------------------------
    def MostrarInorden(self) -> List[Any]:
        resultado: List[int] = []
        self._inOrdenRecursivo(self._raiz, resultado)
        print(" ".join(map(str, resultado)))
        return resultado

    def _inOrdenRecursivo(self, nodo_actual, resultado: List[Any]) -> None:
        if nodo_actual:
            self._inOrdenRecursivo(nodo_actual.getIzq(), resultado)
            resultado.append(nodo_actual.getClave())
            self._inOrdenRecursivo(nodo_actual.getDer(), resultado)
        
    
    # ------------------------------------------------------------------
    # --- Operación Recorrer y preocesar PREORDEN ---
    # ------------------------------------------------------------------
    def MostrarPreorden(self)-> None:
        self._preOrdenRecursivo(self._raiz)
    
    def _preOrdenRecursivo(self, nodo_actual)-> None:
        if nodo_actual:
            # Procesamos la raiz primero
            print(f"{nodo_actual.getClave()}", end=" ")
            
            # Apilamos todos los nodos de la izquierda (menores)
            self._preOrdenRecursivo(nodo_actual.getIzq())
            
            # Apilamos todos los nodos de la derecha (mayores)
            self._preOrdenRecursivo(nodo_actual.getDer())

    # ------------------------------------------------------------------
    # --- Operación Recorrer y preocesar POSTORDEN ---
    # ------------------------------------------------------------------
    def MostrarPostorden(self)-> None:
        self._postOrdenRecursivo(self._raiz)
    
    def _postOrdenRecursivo(self, nodo_actual)-> None:
        if nodo_actual:
            # Apilamos todos los nodos de la izquierda (menores)
            self._postOrdenRecursivo(nodo_actual.getIzq())
            
            # Apilamos todos los nodos de la derecha
            self._postOrdenRecursivo(nodo_actual.getDer())
            
            # Procesamos la raiz
            print(f"{nodo_actual.getClave()}", end=" ")


    # ------------------------------------------------------------------
    # --- Operación BUSCAR(A,X) - Metodo publico
    #     # Reporta datos asociados a clave X, else Error
    # ------------------------------------------------------------------
    def Buscar(self, clave) -> Optional['NodoABB']:
        nodo_encontrado = self._buscarRecursivo(self._raiz, clave)
        return nodo_encontrado
    
    # ------------------------------------------------------------------
    # --- Función auxiliar recursiva 
    # ------------------------------------------------------------------
    def _buscarRecursivo(self, nodo_actual, clave) -> 'NodoABB':
        
        resultado: 'NodoABB' = None
        
        # 1. Caso Base 01: Se llegó al extremo (o el árbol está vacío)
        if not nodo_actual:
            resultado = None
            
        # 2. Caso Base 02: Clave encontrada
        elif nodo_actual.getClave() == clave:
            resultado = nodo_actual
            
        # 3. Caso General: Buscar a la izquierda
        elif clave < nodo_actual.getClave():
            resultado = self._buscarRecursivo(nodo_actual.getIzq(), clave)
            
        # 4. Caso General: Buscar a la derecha
        else:
            resultado = self._buscarRecursivo(nodo_actual.getDer(), clave)
            
        return resultado 
    
    # ------------------------------------------------------------------
    # --- Operación Suprimir (Arbol.pdf)                             ---
    # ------------------------------------------------------------------
        
    def Suprimir(self, clave) -> None:
        self._raiz = self._suprimirRecursivo(self._raiz, clave)
        

    def _suprimirRecursivo(self, nodo_actual, clave) -> 'NodoABB':
        # Caso Base: Llego al extremo de la rama (None), detiene apilamiento
        if nodo_actual is None:
            return None
        
    # 2. Caso general implicito o recursivo, Búsqueda y Recorrido
        if clave < nodo_actual.getClave():
            # Recursión a la izquierda y se apila el puntero
            nodo_actual._izq = self._suprimirRecursivo(nodo_actual._izq, clave)
        elif clave > nodo_actual.getClave():
            # Recursión a la derecha y se apila el puntero
            nodo_actual._der = self._suprimirRecursivo(nodo_actual._der, clave)
            
        # 3. Caso Base: Se encontró el nodo a eliminar (==)
        else:
            pass
            # Aquí se implementa la lógica de eliminación, que depende del grado del nodo:
            # A) 0 hijos: Retorna None
            # B) 1 hijo: Retorna el único hijo
            # C) 2 hijos: Lógica de reemplazo por el sucesor o predecesor inorden.
            # ...
            
            # Después de la lógica de eliminación, la función retorna el nuevo puntero del subárbol
            # (ej. el puntero al único hijo o al nodo sucesor).
            # En Python, si la función retorna el nodo_actual sin modificar, simplemente pasa al return final.

        # 4. Propagación: Si no se eliminó este nodo, se retorna su puntero
        
        return nodo_actual  
    
    # ------------------------------------------------------------------
    # --- Operación Contar nodos con grado 1 (un solo descendiente directo)                             ---
    # ------------------------------------------------------------------


    def ContarNodosGradoUnomutable(self) -> None: 
        contador: List[int] = [0]  
        self._contarGradoUnoRecursivoMutable(self._raiz, contador)
        print("Cantidad de nodos con un descendiente directo:", contador[0])
    
    def _contarGradoUnoRecursivoMutable(self, nodo_actual, contador) -> None:
        # caso base: cuando las ramas llegan al extremo, None
        if not nodo_actual:
            return 
        
        # caso general o recursivo, recorrido post orden comun
        # apilamos izq, der y procesamos raiz (acumulamos el contador nodos g1)
        self._contarGradoUnoRecursivoMutable(nodo_actual.getIzq(), contador)
        self._contarGradoUnoRecursivoMutable(nodo_actual.getDer(), contador)

        if nodo_actual.getGrado() == 1:
            contador[0] += 1
        
        # Retorno a la invocacion incial
        return


# Contador de nodos grado 1
# metodo publico que actua como interfaz, solo se invoca
    def ContarNodoG1(self)-> int:
        contador: int
        total_nodos: int = self._ContarNodosG1Recursivo(self._raiz, contador = 0) 
        print("Total nodos grado 1: ", total_nodos)
        return total_nodos

    def _ContarNodosG1Recursivo(self, nodo_actual, contador: int = 0)-> int:
        # caso base, llego al fin de la rama
        # Corta esa recursion y retorna el contador
        if nodo_actual is None:
            return contador
        
        # procesamos el nodo actual
        if nodo_actual.getGrado() == 1:
            contador += 1
        
        # caso general, recorremos izq si existe y derecha y acumulamos el retorno
        contador: int = self._ContarNodosG1Recursivo(nodo_actual.getIzq(), contador)
        contador: int = self._ContarNodosG1Recursivo(nodo_actual.getDer(), contador)
        
        # Caso base final, al terminar el desapilado de ambas ramas y el conteo
        # retorna el contador a la invocacion principal
        return contador 

# ----------------------------------------------------------------------
# PRUEBAS DEL MÓDULO (MAIN)
# ----------------------------------------------------------------------
if __name__ == '__main__':
    
    print("--- INICIO DE PRUEBAS DEL TAD ÁRBOL BINARIO DE BÚSQUEDA (ABB) ---")
    
    # 1. PRUEBA DE CREACIÓN Y VACÍO
    arbol = ArbolABB()
    print("\n[TEST 1] Creación del Árbol:")
    print(f"¿El árbol está vacío? {arbol.Vacio()} (Esperado: True)")
    
    # 2. PRUEBA DE INSERCIÓN Y ABB PROPIEDAD
    claves_a_insertar = [50, 30, 70, 20, 40, 60, 80, 50, 20, 10, 110, 90, 110, 120, 55, 35, 85] 
    print("\n[TEST 2] Insertando claves:", claves_a_insertar)
    
    for clave in claves_a_insertar:
        arbol.Insertar(clave)
        
    print(f"¿El árbol está vacío después de insertar? {arbol.Vacio()} (Esperado: False)")
    
    # 3. PRUEBA DE VERIFICACIÓN (INORDEN)
    # Un recorrido Inorden debe mostrar las claves ordenadas.
    claves_obtenidas = arbol.MostrarInorden()
    claves_esperadas = sorted(list(set(claves_a_insertar))) # Elimina duplicados y ordena
    
    print("\n[TEST 3] Recorrido Inorden (Verificación de la Propiedad de Orden):")
    print(f"Claves insertadas (ordenadas): {claves_obtenidas}")
    
    assert claves_obtenidas == claves_esperadas, "ERROR: Las claves Inorden no coinciden con las claves esperadas."
    print("Resultado: ✅ OK. La estructura ABB se mantiene.")
    
    # 4. PRUEBA DE CASOS LÍMITE (ÁRBOL DEGENERADO)
    arbol_deg = ArbolABB()
    claves_ordenadas = [10, 20, 30, 40, 50, 60, 70]
    print("\n[TEST 4] Insertando claves ordenadas (Árbol Degenerado):", claves_ordenadas)
    
    for clave in claves_ordenadas:
        arbol_deg.Insertar(clave)
        
    claves_deg_obtenidas = arbol_deg.MostrarInorden()
    print(f"Claves obtenidas (Inorden): {claves_deg_obtenidas}")
    
    assert claves_deg_obtenidas == claves_ordenadas, "ERROR: Falló la inserción en árbol degenerado."
    print("Resultado: ✅ OK. La inserción funciona correctamente.")

    # 5. PRUEBA DE VACÍO DESPUÉS DE INSERCIÓN/VERIFICACIÓN
    arbol_vacio = ArbolABB()
    arbol_vacio.Insertar(1)
    assert not arbol_vacio.Vacio(), "ERROR: Vacio() retornó True después de insertar."
    print("\n[TEST 5] Vacio() funciona correctamente tras inserción.")
    
        # ------------------------------------------------------------------
    # [TEST 6] Operación BUSCAR(clave)
    # ------------------------------------------------------------------
    print("\n[TEST 6] Búsqueda de claves en el árbol:")

    # Caso 1: Clave existente
    clave_existente = 40
    nodo_encontrado = arbol.Buscar(clave_existente)
    print(f"Buscando clave {clave_existente} → Resultado:", 
          "Encontrada ✅" if nodo_encontrado else "No encontrada ❌")
    assert nodo_encontrado is not None, "ERROR: La clave existente no fue encontrada."

    # Caso 2: Clave inexistente
    clave_inexistente = 999
    nodo_no_encontrado = arbol.Buscar(clave_inexistente)
    print(f"Buscando clave {clave_inexistente} → Resultado:", 
          "Encontrada ❌ (Incorrecto)" if nodo_no_encontrado else "No encontrada ✅")
    assert nodo_no_encontrado is None, "ERROR: Se encontró una clave inexistente."

    print("Resultado: ✅ OK. La búsqueda funciona correctamente.")


    # ------------------------------------------------------------------
    # [TEST 7] Contar nodos con un solo descendiente directo (grado 1)
    # ------------------------------------------------------------------
    print("\n[TEST 7] Conteo de nodos con grado 1:")
    
    # Usamos el método con contador inmutable
    total_g1 = arbol.ContarNodoG1()
    print(f"Total de nodos con grado 1 (un solo descendiente): {total_g1}")

    # Usamos el método alternativo (mutable)
    print("\nVerificación con método mutable:")
    arbol.ContarNodosGradoUnomutable()

    # Verificamos que ambos den el mismo resultado
    contador_verificacion = [0]
    arbol._contarGradoUnoRecursivoMutable(arbol._raiz, contador_verificacion)
    assert contador_verificacion[0] == total_g1, \
        "ERROR: Los métodos mutable e inmutable devolvieron diferentes resultados."

    print("Resultado: ✅ OK. Los contadores coinciden correctamente.")

    
    print("\n--- PRUEBAS DEL TAD ABB FINALIZADAS EXITOSAMENTE ---")
