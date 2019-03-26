
jQuery(document).ready(function(){

    var location = window.location.pathname;
    /*Marca cual opcion esta activa del menu en el Portal del Cliente*/
    if (location=="/dashboard/") {
        $("#menu1").addClass("active");
        $("#menu2").removeClass("active");
    }else if(location.includes("citas")){
        $("#menu1").removeClass("active");
        $("#menu2").addClass("active");
    }
    
    /*Marca cual opcion esta activa del menu del home*/
    if (location=="/contacto/") {
        $("#menu1").removeClass("current");
        $("#menu2").removeClass("current");
        $("#menu3").removeClass("current");
        $("#menu4").addClass("current");
    }else if(location=="/"){
        $("#menu1").addClass("current");
        $("#menu2").removeClass("current");
        $("#menu3").removeClass("current");
        $("#menu4").removeClass("current");
    }else if(location=="/servicios/"){
        $("#menu1").removeClass("current");
        $("#menu2").addClass("current");
        $("#menu3").removeClass("current");
        $("#menu4").removeClass("current");
    }else if(location=="/quienes-somos/"){
        $("#menu1").removeClass("current");
        $("#menu2").removeClass("current");
        $("#menu3").addClass("current");
        $("#menu4").removeClass("current");
    }

    /*Puglin para seleccionar fechas*/
    if(location == "/citas/agregar/" || location.includes("citas/editar/")){
    	var fecha_hoy = "{{fecha_hoy|safe}}"
      	$('#id_dia_agendado').datetimepicker({
        	format: "MM/DD/YYYY",
            locale: "es",
            icons: {
                time: "fas fa-clock",
                date: "fas fa-calendar",
                up: "fas fa-arrow-up",
                down: "fas fa-arrow-down",
                previous: 'fas fa-chevron-left',
                next: 'fas fa-chevron-right',
                today: 'fas fa-calendar-check',
                clear: 'fas fa-trash',
                close: 'fas fa-remove'
            },
            minDate: moment(),
        });

        /*Puglin para seleccionar Horas*/
        $('#id_hora_agendado').datetimepicker({
        	format: "HH:mm",
            locale: "es",
            icons: {
                time: "fa fa-clock",
                date: "fa fa-calendar",
                up: "fa fa-arrow-up",
                down: "fa fa-arrow-down",
                previous: 'fa fa-chevron-left',
                next: 'fa fa-chevron-right',
                today: 'fa fa-calendar-check',
                clear: 'fa fa-trash',
                close: 'fa fa-remove'
            }
        });
    }

    /*Datatables*/
    var table = $('.tabla-generica').DataTable({
        responsive: true,
        language: {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        },
    });
});