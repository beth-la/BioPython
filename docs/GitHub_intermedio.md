# Git Hub intermedio 

*Clase 9 de agosto 2022*

## Tags 

Versiones estables:

- Obtener resultados de versiones pasadas. 

- Ejecutar programas anteriores.

- Rastreo de programas por fecha, commits.

  Etiquetar código para obtener versiones estables de los sccripts. 

  Los tags nos ayudan a identificar el estado de nuestro código.

  El etiquetado es una herramienta para el programador, usurarios, etc.

  Git tag: Estado de todo el proyecto de manera global.

  Numeración de las versiones: Los cambios se dividen en tres niveles de "importancia": mayor, menor y pequeño ajuste (3.1.1)

  ```
  git tag [tag name]
  
  git tag v0.1.0
  
  # Muestra las etiquetas generadas 
  git tag 
  
  # Para poner un mensaje a la etiqueta 
  git tag [verson] -m "mensaje"
  
  # Para obtener información sobre la etiqueta 
  # Fehca, autor
  git show [etiqueta]
  ```

  Llevar etiquetas a un repositorio remoto 

  ```
  git push origin master --tags
  
  # Para subir unicaente una etiqueta 
  git push origin master v0.1.0
  
  # Para etiquetar commits especificos 
  git tag -a [tag][commit_id] -m "mensaje"
  
  # Eliminar etiqquetas 
  git tag -d [tag]
  
  # Para eliminar la etiqueta del repositorio remoto
  git push --delete origin [tag]
  
  # Para ayuda:
  git tag -h
  ```

  # Trabajar con ramas en GitHub

```
Push origin master 
```

Se utiliza "master" ya que master es la rama principal del repositorio.

Es útil utilizar ramas en un repositorio para poder dividir y gestionar cambios al trabajar de manera colaborativa.

Son desarrollos alternos en un repositorio.

Al crear ramas, creamos una copia de nuestro repositorio, en la cual podemos realizar cambios que no se  ven reflejados en la rama master o en cualquier otra rama.

```
# Verificar cuentas ramas existen en el repositorio y en que rama nos encontramos
git branch

# Para crear ramas 
git branch [nombre]

# Movernos a otras ramas
git checkout [branch name]

# muestra los commits en cada rama
git show-branch 

# Crea y brinca hacia la rama recien creada.
git checkout -b [nombre]

# Llevar cambios de una rama a otra, dependiendo de a donde quieras llevar los cambios es en donde debes posicionarte y correr el comando:
git merge [rama] -m "mensaje" 

# Borrar ramas 
git branch -d [branch name]

# Para forzar a borrar una rama
git branch -D [branch name]

# Para subir una rama al repositorio remoto 
git push origin []

# Para elimirar una rama del repositorio remoto
git push origin --delete [branch name]
```

# ISSUES en GitHub

*Clase 16 de Agosto 2022*

Se crean issues en GitHub para generar nuevas tareas, dar mantenimiento al software, resolver errores, crear nuevas funcionalidades, realizar actualizaciones, etc.

Un issue permite rastrear el trabajo en GitHub. 

Los issues incluyen:

-  Título: claro y descriptivo

- Descripción

- Asignación 

- Etiquetas 

- @menciones 

  Ejemplos:

  - Enviar mensaje al desarrollador para solicitar ayuda en la resolución de un error

    

    

  