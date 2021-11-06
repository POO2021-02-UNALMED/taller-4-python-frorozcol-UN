

from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            if self._asignaturas:
                self._asignaturas.append(Asignatura(x))
            else:
                self._asignaturas = [Asignatura(x)]

    def agregarAlumno(self, alumno, lista=None):
        
        if(lista is not None):
            lista.append(alumno)
            if self.listadoAlumnos is None:
                self.listadoAlumnos = lista
            else:
                self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    
    def __str__(self):
        return "Grupo de estudiantes: {}".format(self._grupo)
