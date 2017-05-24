%include('head.tpl')

	<h1>Resultados de la búsqueda</h1>
    %for n,m in zip (lista2,lista1):
        <p>
            <a href="{{m[1]}}"><img src="{{m[0]}}"></a> 
        </p>
        <p>
            <a href="https://www.flickr.com/photos/{{n}}">Propietario</a> 
        </p>
    % end
%include('footer.tpl')
