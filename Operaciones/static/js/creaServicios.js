(function (){
    $(document).ready(function() {
        $('.js-example-basic-single').select2();
    });
})()

(function(){
    const btnEliminar=document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('Seguro quiere eliminar el servicio?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    })
})();

let table = new DataTable('#myTable')