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

import json
from datetime import datetime
from paciente import Paciente
from turno import Turno

class Clinica:
    def __init__(self, razon_social):
        self.razon_social = razon_social
        self.pacientes = []
        self.turnos = []
        self.especialidades = {}
        self.obras_sociales = {}
        self.recaudacion = 0.0
        self.hay_pacientes_sin_atencion = False
        self.cargar_config()
        self.cargar_pacientes()

    def cargar_config(self):
        with open('configs.json') as config_json:
            config = json.load(config_json)
        self.especialidades = config["especialidades"]
        self.obras_sociales = config["obras_sociales"]


    def cargar_pacientes(self):
            with open("pacientes.csv", mode='r') as file:
                lineas = file.readlines()
                for linea in lineas[1:]:
                    columnas = linea.strip().split(',')
                    id = int(columnas[0])
                    nombre = columnas[1]
                    apellido = columnas[2]
                    dni = columnas[3]
                    edad = int(columnas[4])
                    obra_social = columnas[5]
                    paciente = Paciente(id, nombre, apellido, dni, edad, obra_social)
                    self.pacientes.append(paciente)

    def agregar_paciente(self, nombre, apellido, dni, edad, obra_social):
            dni_existe = False
            for paciente in self.pacientes:
                if paciente.dni == dni:
                    dni_existe = True
                    break
            
            if dni_existe:
                 print("Error: Ya existe un paciente con este DNI")
            else :    
                nuevo_id = len(self.pacientes) + 1
                nuevo_paciente = Paciente(nuevo_id, nombre, apellido, dni, edad, obra_social)
                self.pacientes.append(nuevo_paciente)
                print(f"Paciente {nombre} {apellido} registrado con éxito.") 

    def asignar_turno(self, id_paciente, especialidad, monto_base):
        resultado = list(filter(lambda paciente: paciente.id == id_paciente,self.pacientes))
        if not resultado:
            if id_paciente not in self.pacientes:
                print("Error: El paciente no existe en el sistema.")
                return
        if especialidad not in self.especialidades:
            print("Error: Especialidad no válida.")
            return
        obra_social = self.pacientes[id_paciente].obra_social
        obra_social_descuento = self.obras_sociales.get(obra_social, 1.0)
        nuevo_id = len(self.turnos) + 1
        nuevo_turno = Turno(nuevo_id, id_paciente, especialidad, monto_base, obra_social_descuento)
        self.turnos.append(nuevo_turno)
        print(f"Turno asignado con éxito al paciente {id_paciente} para {especialidad}.")