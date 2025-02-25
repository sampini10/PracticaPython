# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import library_utn as utn
from clinica import Clinica
from paciente import Paciente
from turno import Turno


def main_app():
    """
    Aplicacion principal del Segundo Parcial de Laboratorio 1
    """

    clinica = Clinica("Prueba")
    
    while True:  
        selected_option = int(input("Seleccione una opción: "))
        
        match selected_option:
            case 1: # Alta paciente
                nombre = input("Ingrese el nombre del paciente: ")
                apellido = input("Ingrese el apellido del paciente: ")
                dni = input("Ingrese el DNI del paciente: ")
                edad = int(input("Ingrese la edad del paciente: "))
                obra_social = input("Ingrese la obra social del paciente: ")
                clinica.agregar_paciente(nombre, apellido, dni, edad, obra_social)
                pass
            case 2: # Alta turno
                id_paciente = int(input("Ingrese el ID del paciente: "))
                especialidad = input("Ingrese la especialidad del turno (Odontología, Médico Clínico, Psicología, Traumatología): ")
                monto_base = float(input("Ingrese el monto base del turno: "))
                clinica.asignar_turno(id_paciente, especialidad,monto_base)
                pass
            case 3: # Ordenar turnos
                pass
            case 4: # Mostrar pacientes en espera
                pass
            case 5: # Atender pacientes
                pass
            case 5: # Cobrar atenciones
                pass
            case 7: # Cerrar caja
                pass
            case 8: # Mostrar informe
                pass
            case 9: # Salir
                break
            case _:
                utn.UTN_messenger('Opción inválida. Por favor, seleccione una opción válida.', 'Error')
        utn.clear_console()
            