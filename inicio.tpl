%include('head.tpl')

	<h1>BUSCADOR DE FOTOS</h1>
	<form action="/busqueda" method="post">
		<label>Nombre de la foto:</label>
		<input type="text" name="foto" required/>
		<input type="submit" value="Buscar">
	</form>

%include('footer.tpl')
