
$(document).ready(function(){
    console.log('cargando...');

    $("#busqueda").submit(function (e) {
        e.preventDefault();
        console.log('he presionado el boton busqueda...');

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),


            success:function (jsonData) {
                console.log(jsonData);


                jsonData.forEach(function (dato){
                    console.log(dato.nombre);
                    $("#prep").append("")
                    $("#prep").append("<b>"+dato.nombre+"</b>, "+ dato.correo+"<br>");
                });

            },
            error: function(error){
                console.log('ocurrio un error'+error);
            },
        });


    });




    })




