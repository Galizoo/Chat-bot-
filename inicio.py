#Comandos para la creacion de nuestro repocitorio en git hub 
#git init                                   --para inicializar e repocitorio
#git status                                 --para verificar que es lo que vamos a subir /no es obligatorio solo es para revisar el estado
#git add                                    --(si solo queremos subir un archivo en especifico colocaremos el nombre) si se quiere colocar todo colocar --git add . 
#git commit -m "Se agrega un proyecto"      --sirven para subir los cambios en repocitorio
#Luego de esto nos pedira colocar nuestro usuario y correo de git
#git config --global user.email (Correo)
#git config --global user.name (Tu nombre de usuario)
#Repetimos el: git commit -m "Se agrega un proyecto" 
#Aqui solo tenemos el repocitorio en nuestro repocitorio remoto 
#git branch -M main --sirve para indicar que vamos a subir esto a nuestra rama principal 
#Copiamos la ruta especifica de --git remote al crear el repocitorio en el git hub
#git push -u origin main --indicamos que vamos hacer el push para poder hacer efectiva la sincronisacion de mi local con mi remoto  
#Luego de ello se te abrira una ventana que te pedira que confirmes el acceso de git hub y se subiran los archivos 
#Y si no pararece eso en la consola se te pedira que te logues con tu usuario y contraseña 
#Y eso es todo para poder crear y subir archivos en un repocitorio 


#Ahora para poder hacer push los colaboradores a mi repocitorio
#git clone (pegamos la url) --Clonaremos el codigo  del repocitorio
#git pull origin main --esto actualizara los datos de nuestro achivo local con ekl del main 
#git add
#git commit -m "Mensaje del commit"
#git push --si no tienes colaborador no te va a funcionar 
print ("Holas, este sera el inicio de nuestro proyecto o intento de proyecto de chat bot XD")
print("CLONANDO EL REPOSITORIO")
print("Haciendo pruebas")
print("PROBANDO")

#INSTALACION DE RAZA
#1.Conda create -n asistente python=3.6  -Primero anaconda creara un ambiente virtual que se llame asistente con la version de python
#2.Aceptamos con entrer el procedimiento 
#3.El entorno virtual ya estara creado y entraremos a el con el siguiente comando: 
#-conda activate asistente
#4.python -m pip unisntall pip           -pip es un manejador de paquetes donde se pueden actualizar, instalar e elimnar paquetes (en la documentacion de raza se sugiere que se desinstale pip de tu entorno virtual)
#5.Confirmaremos la desinstalacion de pip con enter
#6.python -m ensurepip                   -Ahora ya desinstalado volveremos a instalar pip (este comando solo trae el paquete) 
#7.python -m pip install -U pip          -Este comando lo instala dando un upgrate 
#8.Esto guiandoce desde la documentacion de rasa 
#9.pip install rasa