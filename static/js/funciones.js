function muestraModal(url, titulo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = `¿Deseas eliminar el videojuego ${titulo} ? `;
}

$("#id_estado").on('change', function (e) { 
    var token = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "post",
        url: `/usuarios/municipios/`,
        data: {'id':this.value, 'csrfmiddlewaretoken':token},
        success: function (response) {
            var html = ""
            if (response[0].hasOwnProperty('error')){
                html = `<option value="0">${response[0].error}</option>`;
            }
            else{
                $.each(response, function (llave, valor) { 
                  html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                });
            }
            $("#id_municipio").html(html)
        },
        error: function (params) {
            console.log('Error en la petición')
        }
    });
       
});