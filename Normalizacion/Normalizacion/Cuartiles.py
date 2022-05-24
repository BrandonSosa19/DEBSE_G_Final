import math

def Outliers(datos = []):

    """
        posQ1 = (1*(N+1))/4
        posQ2 = (2*(N+1))/4
        posQ3 = (3*(N+1))/4
    """

    for i in range(len(datos[0])-1):  # Por cada Columna

        N = len(datos)
        posQ = [ (x*(N+1))/4 for x in range(1,4,1)]  

        #Ordenar los datos
        datos.sort(key= lambda x:x[0])
        
        p_decQ1, p_entQ1 = math.modf(posQ[0]) #Primer Cuartil
        p_decQ2, p_entQ2 = math.modf(posQ[1])
        p_decQ3, p_entQ3 = math.modf(posQ[2])

        p_entQ1 = int(p_entQ1)
        p_entQ2 = int(p_entQ2)
        p_entQ3 = int(p_entQ3)

        Q1 = datos[p_entQ1-1][i]+p_decQ1*(datos[p_entQ1][i]-datos[p_entQ1-1][i])
        Q2 = datos[p_entQ2-1][i]+p_decQ2*(datos[p_entQ2][i]-datos[p_entQ2-1][i])
        Q3 = datos[p_entQ3-1][i]+p_decQ3*(datos[p_entQ3][i]-datos[p_entQ3-1][i])

        print("Q1-Position: ", posQ[0], " Q1 Value: ", Q1)
        print("Q1-Position: ", posQ[1], " Q2 Value: ", Q1)
        print("Q3-Position: ", posQ[2], " Q3 Value: ", Q3)

        """
            Qi = valor[posQi] + posQi * ( valor[posQi + 1]) - valor[posQi]
                    Entero   Decimal         entera              entera
        """
        IQRange = Q3-Q1
        print("IQR: ", IQRange)


        """
        se considera un valor atípico el que se encuentra 1.5 veces 
        esa distancia de uno de esos cuartiles (atípico leve) o a 
        3 veces esa distancia (atípico extremo).
        """
        whiskers = 1.5
        #whiskers = 3.0 

        lower_limit = Q1 - whiskers * IQRange
        upper_limit = Q3 + whiskers * IQRange
        print("LOWER LIMIT: ", lower_limit, " UPPER LIMIT: ", upper_limit)

        
        # Eliminar valores atípicos/Outliers

        auxiliar = []
        for value in datos:
            if value[i] < lower_limit or value[i] > upper_limit:
                print("outlier found: ",  value)
            else:
                auxiliar.append(value)            
        dataset = auxiliar.copy()
        print()
 